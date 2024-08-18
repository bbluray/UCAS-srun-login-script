# 设置执行策略
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted -Force

# 检查并创建事件源（如果不存在）
$source = "UCAS-Login"
if ([System.Diagnostics.EventLog]::SourceExists($source) -eq $false) {
    New-EventLog -LogName Application -Source $source
}

# 获取用户 newton 的家目录
$userHome = [System.Environment]::GetFolderPath("UserProfile")
$scriptPath = Join-Path -Path $userHome -ChildPath "bin\auto_login\run.py"

# 克隆 Git 仓库
$repoUrl = "https://github.com/LittleNewton/UCAS-srun-login-script.git"
$localPath = Join-Path -Path $userHome -ChildPath "bin\auto_login"
git clone $repoUrl $localPath

# 创建任务的命令
$scriptBlock = {
    $output = & python $scriptPath
    # 写入到Windows事件日志
    Write-EventLog -LogName Application -Source "UCAS-Login" -EventId 1001 -EntryType Information -Message "UCAS-Login Output: $output"
}

# 创建新的定时任务
$action = New-ScheduledTaskAction -Execute "PowerShell.exe" -Argument "-NoProfile -WindowStyle Hidden -Command $scriptBlock"
$trigger = New-ScheduledTaskTrigger -AtStartup -Once -RepetitionInterval (New-TimeSpan -Minutes 1)
$principal = New-ScheduledTaskPrincipal -UserId "$env:USERNAME" -LogonType S4U -RunLevel Highest

# 注册任务
Register-ScheduledTask -Action $action -Trigger $trigger -Principal $principal -TaskName "ucas-login" -Description "UCAS 校园网自动登录"