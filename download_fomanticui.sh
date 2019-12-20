#!/bin/bash
set -eux
set -o pipefail

FOMANTIC_UI_VERSION=2.8.2

tarball=Fomantic-UI-CSS-$FOMANTIC_UI_VERSION.tar.gz
static_dir=.fomanticui_static

# https://github.com/fomantic/Fomantic-UI-CSS
wget https://github.com/fomantic/Fomantic-UI-CSS/archive/$FOMANTIC_UI_VERSION.tar.gz \
     -O $tarball

tar -vxf $tarball
rm -rfv $static_dir/fomanticui/
mkdir -p $static_dir
cp -rv Fomantic-UI-CSS-$FOMANTIC_UI_VERSION/ $static_dir/fomanticui/
rm -rfv $tarball
