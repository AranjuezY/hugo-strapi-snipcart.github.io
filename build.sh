#!/usr/bin/env sh

if [ -f .env ]; then
  export $(grep -v '^#' .env | xargs)
fi

hugo server -D --ignoreCache
