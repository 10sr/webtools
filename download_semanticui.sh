#!/bin/bash
set -eux
set -o pipefail

FOMANTIC_UI_VERSION=2.8.2

tarball=Fomantic-UI-CSS-$FOMANTIC_UI_VERSION.tar.gz
static_dir=.smanticui_static

# https://github.com/fomantic/Fomantic-UI-CSS
# Fomantic-UI は Semantic-UI への Merge を目指す community fork なので、
# パスなどは semanticui のものをそのまま使う
# （ファイル名なども semanticui.js のままになっている）
wget https://github.com/fomantic/Fomantic-UI-CSS/archive/$FOMANTIC_UI_VERSION.tar.gz \
     -O $tarball

tar -vxf $tarball
rm -rfv $static_dir/semanticui/
mkdir -p $static_dir
cp -rv Fomantic-UI-CSS-$FOMANTIC_UI_VERSION/ $static_dir/semanticui/
rm -rfv $tarball
