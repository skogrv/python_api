#!/bin/sh
set -e
wait-for-it -s db:5432 -t 10
exec "$@"
