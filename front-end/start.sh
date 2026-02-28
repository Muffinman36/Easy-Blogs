#!/bin/sh
node /app/.output/server/index.mjs &
nginx -g 'daemon off;'
