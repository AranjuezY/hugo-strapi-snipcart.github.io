#!/usr/bin/env sh

if [ -f .env ]; then
  export $(grep -v '^#' .env | xargs)
fi

hugo --config hugo.production.toml -D --ignoreCache
