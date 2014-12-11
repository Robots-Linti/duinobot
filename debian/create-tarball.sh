#!/bin/sh

CURRENT=0
while [ $# -gt 0 ]; do
    case "$1" in
        --current)
            CURRENT=1
            ;;
    esac
    shift
done

DIR=$(readlink -f $(dirname $0))
VERSION=$(cat "$DIR/changelog"  | head -n1 | grep -oE '\(.+\)' | tr -d '()')

if [ "$CURRENT" -eq 0 ]; then
    VERSION=$(echo $VERSION | cut -d- -f1)
    git checkout "v$VERSION"
    # git reset --hard
fi

tar cvJf "$DIR/../../robot_$VERSION".orig.tar.xz --exclude=.git --exclude=.gitignore --transform="s/duinobot/robot_$VERSION/" -C "$DIR/../../" duinobot

if [ "$CURRENT" -eq 0 ]; then
    git checkout debianpkg
    # git reset --hard
fi
