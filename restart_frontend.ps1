# Restart Frontend Server Script

Write-Host "Stopping existing frontend server..." -ForegroundColor Yellow

# Find and stop Node.js processes on port 3000
$frontendProcess = Get-Process | Where-Object { $_.ProcessName -eq "node" } | Where-Object { 
    (Get-NetTCPConnection -OwningProcess $_.Id -ErrorAction SilentlyContinue | Where-Object { $_.LocalPort -eq 3000 }).Count -gt 0 
}

if ($frontendProcess) {
    Write-Host "Found frontend process with PID: $($frontendProcess.Id)" -ForegroundColor Red
    Stop-Process -Id $frontendProcess.Id -Force
    Start-Sleep 2
    Write-Host "Frontend process stopped." -ForegroundColor Green
} else {
    Write-Host "No frontend process found on port 3000." -ForegroundColor Yellow
}

Write-Host "Starting new frontend server..." -ForegroundColor Green

# Change to frontend directory and start the server
Set-Location "D:\aarushi project final\frontend"

# Start the frontend server in a new job
Start-Job -ScriptBlock {
    Set-Location "D:\aarushi project final\frontend"
    npm start
} -Name "FrontendServer"

# Wait a moment for server to start
Start-Sleep 5

Write-Host "Frontend server started!" -ForegroundColor Green
Write-Host "You can access it at: http://localhost:3000" -ForegroundColor Cyan
Write-Host "To view server logs, use: Get-Job -Name 'FrontendServer' | Receive-Job" -ForegroundColor Gray