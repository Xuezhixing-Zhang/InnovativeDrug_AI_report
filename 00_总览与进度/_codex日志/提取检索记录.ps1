# 用法: powershell -File 提取检索记录.ps1 <module_log.jsonl>
# 从 codex JSONL 日志提取「已执行查询式」与「已访问网站」，输出可粘进 检索记录_已检索关键词与网站.md
param([Parameter(Mandatory=$true)][string]$Log)
$raw = [System.IO.File]::ReadAllText($Log)
$bt  = [char]96
$apos = [char]39
$trim = [char[]]@('.', ',', ';', $apos, '}', ']')

Write-Output "### 已执行查询式"
$qs = New-Object System.Collections.Generic.List[string]
foreach ($m in [regex]::Matches($raw, '"query":"((?:[^"\\]|\\.)*)"')) {
  $q = $m.Groups[1].Value
  if ($q -and $q.Length -gt 1) { $qs.Add($q) }
}
foreach ($q in ($qs | Sort-Object -Unique)) { Write-Output ("- " + $bt + $q + $bt) }

Write-Output ""
Write-Output "### 已访问关键网站/页面"
$noise = 'googletagmanager|chatgpt|schema\.org|w3\.org|gmpg|fonts\.|gstatic|/wp-|\.css|\.woff|search\?q='
$urls = New-Object System.Collections.Generic.List[string]
foreach ($m in [regex]::Matches($raw, 'https?://[^\s"\\)\]]+')) {
  $u = $m.Groups[0].Value.TrimEnd($trim)
  if ($u.Contains('$')) { continue }
  if ($u -match $noise) { continue }
  $urls.Add($u)
}
foreach ($u in ($urls | Sort-Object -Unique)) { Write-Output ("- " + $u) }

Write-Output ""
Write-Output "### URL 主机汇总"
$hosts = $urls | ForEach-Object { try { ([System.Uri]$_).Host } catch { } }
foreach ($h in ($hosts | Where-Object { $_ } | Sort-Object -Unique)) { Write-Output ("- " + $h) }
