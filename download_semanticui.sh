#!/bin/bash
set -eux
set -o pipefail

SEMANTIC_UI_VERSION=2.4.1

tarball=Semantic-UI-CSS-$SEMANTIC_UI_VERSION.tar.gz

# https://github.com/Semantic-Org/Semantic-UI-CSS
wget https://github.com/Semantic-Org/Semantic-UI-CSS/archive/$SEMANTIC_UI_VERSION.tar.gz \
     -O $tarball

tar -vxf $tarball
rm -rfv static/semanticui/
mkdir -p static
cp -rv Semantic-UI-CSS-$SEMANTIC_UI_VERSION/ static/semanticui/
