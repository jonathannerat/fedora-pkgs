#!/bin/sh

# USAGE: git-tar-dist.sh REPODIR
# Generate a tar.gz for a git repository following the format: $name-$version.tar.gz
# where $name is the name of the directory, and $version is given by git-describe(1).

fail() {
    >&2 echo "$@"
    exit 1
}

pkgdir="$1"
[ -d "$pkgdir" ] || fail "Not a directory: $pkgdir"
git -C status >/dev/null || fail "Not a git repository: $pkgdir"

pkg="$(basename "$pkgdir")"

echo "Packaging $pkg"
# Format git-describe(1) in a version allowed by fedora pkgs
version="$(git -C "$pkgdir" describe --tags | sed 's/-\([^-]*\)/.r\1/;s/-/./')"
echo "Version detected: $version"

# "Copy" the directory using worktree to a folder with name "$pkg-$version"
# so the built tar.gz has that folder as root, which is needed for fedpkg to build
git -C "$pkgdir" worktree add "$(pwd)/$pkg-$version" HEAD
echo "Creating temp package worktree at $(pwd)/$pkg-$version"
tar --exclude=.git/ -czf "$pkg-$version.tar.gz" "$pkg-$version"
echo "Package created: $pkg-$version.tar.gz"
echo "Deleting temp package worktree"
git -C "$pkgdir" worktree remove "$(pwd)/$pkg-$version"
