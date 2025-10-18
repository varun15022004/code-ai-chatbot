# Simple Server Startup Script
Write-Host "Starting AI Furniture Recommendation Platform..." -ForegroundColor Green

# Start Backend Server
Write-Host "Starting Backend Server..." -ForegroundColor Yellow
Start-Job -Name "BackendServer" -ScriptBlock {
    Set-Location "D:\aarushi project final\backend"
    python main_server.py
} | Out-Null

# Wait for backend to start
Start-Sleep -Seconds 5

# Start Frontend Server  
Write-Host "Starting Frontend Server..." -ForegroundColor Yellow
Start-Job -Name "FrontendServer" -ScriptBlock {
    Set-Location "D:\aarushi project final\frontend"
    npm start
} | Out-Null

# Wait for both to initialize
Write-Host "Waiting for servers to start..." -ForegroundColor Cyan
Start-Sleep -Seconds 8

# Check status
Write-Host "Server Status:" -ForegroundColor Green

try {
    $health = Invoke-RestMethod -Uri "http://localhost:8001/health" -TimeoutSec 5
    Write-Host "Backend: RUNNING (Dataset: $($health.dataset_size) products)" -ForegroundColor Green
}
catch {
    Write-Host "Backend: ERROR" -ForegroundColor Red
}

try {
    $frontend = Test-NetConnection -ComputerName "localhost" -Port 3000 -WarningAction SilentlyContinue
    if ($frontend.TcpTestSucceeded) {
        Write-Host "Frontend: RUNNING" -ForegroundColor Green
    } else {
        Write-Host "Frontend: ERROR" -ForegroundColor Red
    }
}
catch {
    Write-Host "Frontend: ERROR" -ForegroundColor Red
}

Write-Host ""
Write-Host "URLs:" -ForegroundColor Cyan
Write-Host "Main App: http://localhost:3000" -ForegroundColor White
Write-Host "API Docs: http://localhost:8001/docs" -ForegroundColor White
Write-Host "Analytics: http://localhost:3000/analytics" -ForegroundColor White

Write-Host ""
Write-Host "Active Jobs:" -ForegroundColor Cyan
Get-Job

Write-Host ""
Write-Host "To stop servers: Get-Job | Stop-Job; Get-Job | Remove-Job" -ForegroundColor Yellow
Write-Host "Both servers are now running!" -ForegroundColor Green