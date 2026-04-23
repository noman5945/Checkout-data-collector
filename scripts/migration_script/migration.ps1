param(
    [string]$message
)

if (-not $message) {
    Write-Host "❌ Please provide a migration message"
    Write-Host 'Example: .\migrate.ps1 "add agent table"'
    exit 1
}

Write-Host "🚀 Generating migration..."
alembic revision --autogenerate -m "$message"

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Migration generation failed"
    exit 1
}

Write-Host "📦 Applying migration..."
alembic upgrade head

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Migration apply failed"
    exit 1
}

Write-Host "✅ Migration completed successfully!"