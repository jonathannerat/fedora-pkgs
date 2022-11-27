#!/bin/sh

pkgdir="$1"
pkg="${pkgdir##*/}"

echo "Packaging $pkg"
version="$(git -C "$pkgdir" describe --tags | sed 's/-\([^-]*\)/.r\1/;s/-/./')"
echo "Version detected: $version"

git -C "$pkgdir" worktree add "$(pwd)/$pkg-$version" HEAD
echo "Creating temp package worktree at $(pwd)/$pkg-$version"
tar --exclude=.git/ -czf "$pkg-$version.tar.gz" "$pkg-$version"
echo "Package created: $pkg-$version.tar.gz"
echo "Deleting temp package worktree"
git -C "$pkgdir" worktree remove "$(pwd)/$pkg-$version"
