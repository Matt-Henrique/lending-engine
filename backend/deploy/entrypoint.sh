#!/usr/bin/env bash
set -e

# Simple wait-for-postgres using nc or fallback loop
: "${DATABASE_URL:=}"
# parse host: attempt to extract host and port from DATABASE_URL if possible
# fallback host 'db' port 5432
DB_HOST="db"
DB_PORT="5432"

if command -v python >/dev/null 2>&1; then
  python - <<PYCODE
import os, urllib.parse
url=os.environ.get("DATABASE_URL","")
if url:
    try:
        parsed=urllib.parse.urlparse(url)
        host=parsed.hostname or os.environ.get("DB_HOST")
        port=str(parsed.port or os.environ.get("DB_PORT") or 5432)
        print(f"__PARSED_DB__{host}__{port}")
    except Exception:
        pass
PYCODE
fi

# pick up parse result if printed
PARSED=$(python - <<PYCODE
import os, urllib.parse, sys
url=os.environ.get("DATABASE_URL","")
if url:
    try:
        p=urllib.parse.urlparse(url)
        print(f"{p.hostname or ''}::{p.port or 5432}")
    except:
        print("::")
else:
    print("::")
PYCODE
)

if [ -n "$PARSED" ]; then
  HOST="$(echo "$PARSED" | cut -d: -f1)"
  PORT="$(echo "$PARSED" | cut -d: -f3)"
  if [ -n "$HOST" ]; then DB_HOST="$HOST"; fi
  if [ -n "$PORT" ]; then DB_PORT="$PORT"; fi
fi

echo "Waiting for database $DB_HOST:$DB_PORT..."

# wait for port to be open (nc -z)
RETRY=0
until nc -z "$DB_HOST" "$DB_PORT"; do
  RETRY=$((RETRY+1))
  if [ $RETRY -gt 60 ]; then
    echo "Timeout waiting for DB at $DB_HOST:$DB_PORT"
    exit 1
  fi
  sleep 1
done

echo "Database is up — applying migrations and collecting static files."

# apply migrations
python manage.py migrate --noinput

# collect static
python manage.py collectstatic --noinput

# you can add creation of superuser here if desired (conditionally)

# exec the CMD
exec "$@"
