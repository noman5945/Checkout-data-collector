#!/bin/bash

# Usage: ./migrate.sh "message"

MESSAGE=$1

if [ -z "$MESSAGE" ]; then
  echo "❌ Please provide a migration message"
  echo "Example: ./migrate.sh 'add agent table'"
  exit 1
fi

echo "🚀 Generating migration..."
alembic revision --autogenerate -m "$MESSAGE"

if [ $? -ne 0 ]; then
  echo "❌ Migration generation failed"
  exit 1
fi

echo "📦 Applying migration..."
alembic upgrade head

if [ $? -ne 0 ]; then
  echo "❌ Migration apply failed"
  exit 1
fi

echo "✅ Migration completed successfully!"