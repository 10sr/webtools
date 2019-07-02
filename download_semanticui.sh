#!/bin/bash
set -eux
set -o pipefail

SEMANTIC_UI_VERSION=2.4.1

tarball=Semantic-UI-CSS-$SEMANTIC_UI_VERSION.tar.gz
static_dir=static

# https://github.com/Semantic-Org/Semantic-UI-CSS
wget https://github.com/Semantic-Org/Semantic-UI-CSS/archive/$SEMANTIC_UI_VERSION.tar.gz \
     -O $tarball

tar -vxf $tarball
rm -rfv $static_dir/semanticui/
mkdir -p $static_dir
cp -rv Semantic-UI-CSS-$SEMANTIC_UI_VERSION/ $static_dir/semanticui/
