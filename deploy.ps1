# AI Furniture Discovery - Quick Deployment Script

param(
    [string]$BackendUrl = "",
    [switch]$BuildOnly = $false
)

Write-Host "🚀 AI Furniture Discovery Platform - Deployment Script" -ForegroundColor Green
Write-Host "===============================================" -ForegroundColor Green

if (-not $BackendUrl -and -not $BuildOnly) {
    Write-Host "❌ Please provide your backend URL or use -BuildOnly flag" -ForegroundColor Red
    Write-Host "Usage: .\deploy.ps1 -BackendUrl 'https://your-backend.onrender.com'" -ForegroundColor Yellow
    Write-Host "   or: .\deploy.ps1 -BuildOnly" -ForegroundColor Yellow
    exit 1
}

# Step 1: Build Frontend
Write-Host "📦 Building frontend for production..." -ForegroundColor Yellow
Set-Location "frontend"

if ($BackendUrl) {
    # Update environment file
    $envContent = "REACT_APP_API_URL=$BackendUrl`nREACT_APP_ENVIRONMENT=production"
    Set-Content -Path ".env.production" -Value $envContent
    Write-Host "✅ Updated .env.production with backend URL: $BackendUrl" -ForegroundColor Green
}

# Install dependencies and build
npm install
npm run build

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Frontend build completed successfully!" -ForegroundColor Green
} else {
    Write-Host "❌ Frontend build failed!" -ForegroundColor Red
    exit 1
}

# Go back to root directory
Set-Location ".."

if ($BuildOnly) {
    Write-Host "🎉 Build completed! Frontend ready for deployment." -ForegroundColor Green
    Write-Host "📁 Deploy the 'frontend/build' folder to your hosting service." -ForegroundColor Cyan
} else {
    Write-Host "🎉 Deployment preparation completed!" -ForegroundColor Green
    Write-Host "📋 Next steps:" -ForegroundColor Cyan
    Write-Host "   1. Deploy backend to Render/Railway with your repository" -ForegroundColor White
    Write-Host "   2. Deploy frontend/build folder to Vercel/Netlify" -ForegroundColor White
    Write-Host "   3. Set environment variables on both platforms" -ForegroundColor White
    Write-Host "   4. Test your deployment!" -ForegroundColor White
}

Write-Host "`n📚 See DEPLOYMENT_GUIDE.md for detailed instructions." -ForegroundColor Gray