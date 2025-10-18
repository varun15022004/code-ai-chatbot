# AI Furniture Recommendation Platform - Server Startup Script
Write-Host "🚀 Starting AI Furniture Recommendation Platform..." -ForegroundColor Green
Write-Host "=" * 60 -ForegroundColor Cyan

# Navigate to project root
Set-Location "D:\aarushi project final"

# Start Backend Server
Write-Host "🖥️  Starting Backend Server (Python FastAPI)..." -ForegroundColor Yellow
Start-Job -Name "BackendServer" -ScriptBlock {
    Set-Location "D:\aarushi project final\backend"
    Write-Host "Loading Python environment and starting server..." -ForegroundColor Green
    python main_server.py
} | Out-Null

# Wait a moment for backend to initialize
Start-Sleep -Seconds 3

# Start Frontend Server  
Write-Host "🌐 Starting Frontend Server (React)..." -ForegroundColor Yellow
Start-Job -Name "FrontendServer" -ScriptBlock {
    Set-Location "D:\aarushi project final\frontend"
    Write-Host "Starting React development server..." -ForegroundColor Green
    npm start
} | Out-Null

# Wait for servers to start
Write-Host "⏳ Waiting for servers to initialize..." -ForegroundColor Cyan
Start-Sleep -Seconds 8

# Check server status
Write-Host "`n📊 Server Status:" -ForegroundColor Green
Write-Host "=" * 30

# Check Backend
try {
    $backendHealth = Invoke-RestMethod -Uri "http://localhost:8001/health" -TimeoutSec 5
    Write-Host "✅ Backend Server: RUNNING" -ForegroundColor Green
    Write-Host "   📍 URL: http://localhost:8001" -ForegroundColor White
    Write-Host "   📄 API Docs: http://localhost:8001/docs" -ForegroundColor White
    Write-Host "   📊 Dataset: $($backendHealth.dataset_size) products loaded" -ForegroundColor White
    Write-Host "   🤖 Gemini AI: ACTIVE" -ForegroundColor White
}
catch {
    Write-Host "❌ Backend Server: ERROR" -ForegroundColor Red
    Write-Host "   Please check the backend logs below." -ForegroundColor Yellow
}

# Check Frontend (port check since it's HTML)
try {
    $frontendTest = Test-NetConnection -ComputerName "localhost" -Port 3000 -WarningAction SilentlyContinue
    if ($frontendTest.TcpTestSucceeded) {
        Write-Host "✅ Frontend Server: RUNNING" -ForegroundColor Green
        Write-Host "   📍 URL: http://localhost:3000" -ForegroundColor White
        Write-Host "   📱 Analytics: http://localhost:3000/analytics" -ForegroundColor White
    } else {
        Write-Host "❌ Frontend Server: ERROR" -ForegroundColor Red
    }
}
catch {
    Write-Host "❌ Frontend Server: ERROR" -ForegroundColor Red
}

Write-Host "`n🎯 Quick Start Guide:" -ForegroundColor Cyan
Write-Host "1. 🏠 Main App: http://localhost:3000" -ForegroundColor White
Write-Host "2. 📊 Analytics: http://localhost:3000/analytics" -ForegroundColor White
Write-Host "3. 🔧 API Docs: http://localhost:8001/docs" -ForegroundColor White
Write-Host "4. Try saying hello or hi to test Gemini AI!" -ForegroundColor White

Write-Host "`n📋 Active Jobs:" -ForegroundColor Cyan
Get-Job | Format-Table -AutoSize

Write-Host "`n🔍 To monitor logs, use:" -ForegroundColor Yellow
Write-Host "   Receive-Job -Name BackendServer -Keep" -ForegroundColor Gray
Write-Host "   Receive-Job -Name FrontendServer -Keep" -ForegroundColor Gray

Write-Host "`n⏹️  To stop servers, use:" -ForegroundColor Yellow
Write-Host "   Get-Job | Stop-Job; Get-Job | Remove-Job" -ForegroundColor Gray

Write-Host "`n🎉 Both servers are now running! Happy furniture hunting!" -ForegroundColor Green