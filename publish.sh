#!/usr/bin/env bash
#
# publish.sh: release sphinx-2009scape-theme.
#
#   1. run the test suite
#   2. build sdist + wheel and upload them to PyPI
#   3. tag the release
#   4. create a GitHub release for the tag, with the distributions attached
#   5. build the demo docs and push them to the gh-pages branch
#
# Usage:
#   ./publish.sh [--pypi-only | --docs-only] [--test-pypi] [--skip-tests]
#                [--no-tag] [--no-release] [--dry-run] [--yes]

set -Eeuo pipefail

# configuration

readonly EXPECTED_REPO="arsalan-anwari/2009scape-sphinx-theme"
readonly PKG_NAME="sphinx-2009scape-theme"
readonly DOCS_BRANCH="gh-pages"
readonly DOCS_SRC="docs"
readonly DOCS_BUILD="docs/_build/html"
readonly PAGES_URL="https://arsalan-anwari.github.io/2009scape-sphinx-theme/"

REPO_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "$REPO_ROOT"

DO_PYPI=1
DO_DOCS=1
RUN_TESTS=1
DO_TAG=1
DO_RELEASE=1
DRY_RUN=0
ASSUME_YES=0
TWINE_REPO=()

# output

if [[ -t 1 ]]; then
    C_RESET=$'\033[0m'; C_BOLD=$'\033[1m'; C_DIM=$'\033[2m'
    C_RED=$'\033[31m'; C_GREEN=$'\033[32m'; C_YELLOW=$'\033[33m'
else
    C_RESET=""; C_BOLD=""; C_DIM=""; C_RED=""; C_GREEN=""; C_YELLOW=""
fi

step() { printf '\n%s==>%s %s%s%s\n' "$C_GREEN" "$C_RESET" "$C_BOLD" "$*" "$C_RESET"; }
info() { printf '    %s\n' "$*"; }
warn() { printf '%swarning:%s %s\n' "$C_YELLOW" "$C_RESET" "$*" >&2; }
die()  { printf '%serror:%s %s\n' "$C_RED" "$C_RESET" "$*" >&2; exit 1; }

# Echo a command, then run it (or just echo it under --dry-run).
run() {
    printf '    %s$ %s%s\n' "$C_DIM" "$*" "$C_RESET"
    (( DRY_RUN )) && return 0
    "$@"
}

confirm() {
    (( ASSUME_YES )) && return 0
    local reply
    read -r -p "    $1 [y/N] " reply
    [[ "$reply" =~ ^[Yy]$ ]]
}

# arguments

while (( $# )); do
    case "$1" in
        --pypi-only)  DO_DOCS=0 ;;
        --docs-only)  DO_PYPI=0; DO_TAG=0; DO_RELEASE=0 ;;
        --test-pypi)  TWINE_REPO=(--repository testpypi); DO_TAG=0; DO_RELEASE=0 ;;
        --skip-tests) RUN_TESTS=0 ;;
        --no-tag)     DO_TAG=0; DO_RELEASE=0 ;;
        --no-release) DO_RELEASE=0 ;;
        --dry-run)    DRY_RUN=1 ;;
        -y|--yes)     ASSUME_YES=1 ;;
        -h|--help)    awk 'NR>1 && /^#/ {sub(/^# ?/, ""); print; next} NR>1 {exit}' \
                          "${BASH_SOURCE[0]}"; exit 0 ;;
        *)            die "unknown option: $1 (try --help)" ;;
    esac
    shift
done

(( DO_PYPI || DO_DOCS )) || die "nothing to do"

# sanity checking

need() { command -v "$1" >/dev/null 2>&1 || die "required command not found: $1"; }

step "Checking environment"

need git
need python3
git rev-parse --git-dir >/dev/null 2>&1 || die "not a git repository: $REPO_ROOT"

# Pin to this repository. Accept both SSH and HTTPS spellings of the remote.
origin_url="$(git remote get-url origin 2>/dev/null || true)"
[[ -n "$origin_url" ]] || die "no 'origin' remote configured"
origin_slug="${origin_url#*github.com}"
origin_slug="${origin_slug#[:/]}"
origin_slug="${origin_slug%.git}"
[[ "$origin_slug" == "$EXPECTED_REPO" ]] \
    || die "origin is '$origin_slug', expected '$EXPECTED_REPO' — refusing to publish"
info "repository: $origin_slug"

# A dirty tree means the artefacts would not match any commit.
if [[ -n "$(git status --porcelain --untracked-files=no)" ]]; then
    git status --short --untracked-files=no >&2
    die "working tree has uncommitted changes — commit or stash them first"
fi

branch="$(git rev-parse --abbrev-ref HEAD)"
[[ "$branch" == "main" ]] || warn "publishing from branch '$branch', not 'main'"

VERSION="$(python3 - <<'PY'
import pathlib, sys
try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib
data = tomllib.loads(pathlib.Path("pyproject.toml").read_text(encoding="utf-8"))
print(data["project"]["version"])
PY
)"
[[ -n "$VERSION" ]] || die "could not read version from pyproject.toml"
readonly VERSION
readonly TAG="v$VERSION"
info "version:    $VERSION"
(( DRY_RUN )) && warn "dry run — no commands will actually execute"

# plan

step "Plan"
(( RUN_TESTS )) && info "• run pytest"
(( DO_PYPI ))   && info "• build and upload $PKG_NAME $VERSION to ${TWINE_REPO[*]:-PyPI}"
(( DO_TAG ))    && info "• tag $TAG and push it to origin"
(( DO_RELEASE )) && info "• create GitHub release $TAG"
(( DO_DOCS ))   && info "• build docs and force-push them to origin/$DOCS_BRANCH"
confirm "Proceed?" || die "aborted"

# tests

if (( RUN_TESTS )); then
    step "Running tests"
    run python3 -m pytest -q
fi

# PyPI

if (( DO_PYPI )); then
    step "Building distributions"
    python3 -c 'import build' 2>/dev/null || die "missing 'build' — pip install build"
    need twine

    if (( DO_TAG )) && git rev-parse -q --verify "refs/tags/$TAG" >/dev/null; then
        die "tag $TAG already exists — bump the version in pyproject.toml"
    fi

    run rm -rf dist
    run python3 -m build

    step "Checking distributions"
    if (( DRY_RUN )); then
        printf '    %s$ twine check dist/*%s\n' "$C_DIM" "$C_RESET"
    else
        check_out=""
        if ! check_out="$(twine check dist/* 2>&1)"; then
            printf '%s\n' "$check_out"

            squashed="$(printf '%s' "$check_out" | tr -s '[:space:]' ' ')"
            if [[ "$squashed" == *"not a valid metadata version"* ]]; then
                warn "this is a stale local 'packaging', not a bad distribution"
                info "fix with: pip install --upgrade 'packaging>=25.1' twine"
                confirm "Upload anyway?" || die "aborted"
            else
                die "twine check failed"
            fi
        else
            printf '%s\n' "$check_out"
        fi
    fi

    step "Uploading to ${TWINE_REPO[*]:-PyPI}"
    confirm "Upload $PKG_NAME $VERSION? This cannot be undone." || die "aborted"
    run twine upload "${TWINE_REPO[@]}" dist/*
fi

# tag

if (( DO_TAG )); then
    step "Tagging $TAG"
    run git tag -a "$TAG" -m "$PKG_NAME $VERSION"
    run git push origin "$TAG"
fi

# GitHub release

if (( DO_RELEASE )); then
    step "Creating GitHub release $TAG"

    # Ship the same artefacts that went to PyPI, when we built them.
    assets=()
    if (( DO_PYPI )); then
        shopt -s nullglob
        assets=(dist/*)
        shopt -u nullglob
    fi

    release_url="https://github.com/$EXPECTED_REPO/releases/tag/$TAG"

    if ! command -v gh >/dev/null 2>&1; then
        warn "gh CLI not found — create the release manually:"
        info "https://github.com/$EXPECTED_REPO/releases/new?tag=$TAG"
    elif ! gh auth status >/dev/null 2>&1; then
        warn "gh is not authenticated — run 'gh auth login', then:"
        info "gh release create $TAG dist/* --title '$PKG_NAME $VERSION' --generate-notes"
    elif (( ! DRY_RUN )) && gh release view "$TAG" >/dev/null 2>&1; then
        info "release $TAG already exists — skipping"
        info "$release_url"
    else
        run gh release create "$TAG" ${assets[@]+"${assets[@]}"} \
            --title "$PKG_NAME $VERSION" --generate-notes
        (( DRY_RUN )) || info "$release_url"
    fi
fi

# gh-pages

if (( DO_DOCS )); then
    step "Building documentation"
    need make
    run make -C "$DOCS_SRC" html

    if (( ! DRY_RUN )); then
        [[ -f "$DOCS_BUILD/index.html" ]] \
            || die "$DOCS_BUILD/index.html missing — the docs build produced nothing"
    fi

    step "Deploying to origin/$DOCS_BRANCH"

    worktree="$(mktemp -d -t 2009scape-pages-XXXXXX)"
    cleanup() {
        git worktree remove --force "$worktree" >/dev/null 2>&1 || true
        rm -rf "$worktree"
    }
    trap cleanup EXIT

    if (( DRY_RUN )); then
        info "(dry run) would sync $DOCS_BUILD into a $DOCS_BRANCH worktree and push"
    else
        git fetch --quiet origin "$DOCS_BRANCH" 2>/dev/null || true

        if git rev-parse -q --verify "refs/remotes/origin/$DOCS_BRANCH" >/dev/null; then
            info "reusing existing origin/$DOCS_BRANCH"
            git worktree add --force -B "$DOCS_BRANCH" "$worktree" \
                "origin/$DOCS_BRANCH" >/dev/null
        else
            info "creating orphan branch $DOCS_BRANCH"
            git worktree add --force --detach "$worktree" >/dev/null
            git -C "$worktree" checkout --orphan "$DOCS_BRANCH" >/dev/null 2>&1
            git -C "$worktree" rm -rqf . >/dev/null 2>&1 || true
        fi

        find "$worktree" -mindepth 1 -maxdepth 1 ! -name '.git' -exec rm -rf {} +
        cp -a "$DOCS_BUILD/." "$worktree/"

        touch "$worktree/.nojekyll"

        git -C "$worktree" add --all
        if git -C "$worktree" diff --cached --quiet; then
            info "documentation is already up to date — nothing to push"
        else
            git -C "$worktree" commit --quiet \
                -m "docs: deploy $VERSION ($(git rev-parse --short HEAD))"
            git -C "$worktree" push --force origin "$DOCS_BRANCH"
            info "pushed $(git -C "$worktree" rev-parse --short HEAD) to origin/$DOCS_BRANCH"
        fi
    fi

    cleanup
    trap - EXIT

    step "Enabling GitHub Pages"
    if (( DRY_RUN )); then
        info "(dry run) would ensure Pages serves $DOCS_BRANCH / (root)"
    elif ! command -v gh >/dev/null 2>&1; then
        warn "gh CLI not found — enable Pages manually, once:"
        info "Settings → Pages → Deploy from branch → $DOCS_BRANCH / (root)"
    elif ! gh auth status >/dev/null 2>&1; then
        warn "gh is not authenticated — enable Pages manually, once:"
        info "Settings → Pages → Deploy from branch → $DOCS_BRANCH / (root)"
    elif gh api "repos/$EXPECTED_REPO/pages" >/dev/null 2>&1; then
        info "already enabled"
    else
        if gh api -X POST "repos/$EXPECTED_REPO/pages" \
              -f "source[branch]=$DOCS_BRANCH" -f "source[path]=/" >/dev/null 2>&1; then
            info "enabled: serving $DOCS_BRANCH / (root)"
        else
            warn "could not enable Pages automatically (token may lack admin rights)"
            info "Settings → Pages → Deploy from branch → $DOCS_BRANCH / (root)"
        fi
    fi
    info "first build takes a minute or two to go live"
fi

step "Done"
(( DO_PYPI ))    && info "https://pypi.org/project/$PKG_NAME/$VERSION/"
(( DO_RELEASE )) && info "https://github.com/$EXPECTED_REPO/releases/tag/$TAG"
(( DO_DOCS ))    && info "$PAGES_URL"
exit 0
