# Windows fallback: the packaged renderer was attempted and cannot find soffice.
# Convert only this generated document using a dedicated hidden Word instance.
param([string]$QaDir)
$ErrorActionPreference = 'Stop'
$root = Split-Path $PSScriptRoot -Parent
$source = Join-Path $root 'TechnicalArt\妖精丘陵_开场故事画与章节过渡交接_v2.docx'
New-Item -ItemType Directory -Path $QaDir -Force | Out-Null
$pdfPath = Join-Path $QaDir 'opening_handoff_v2.pdf'
$wordApp = $null
$ownedDoc = $null
try {
    $wordApp = New-Object -ComObject Word.Application
    $wordApp.Visible = $false
    $wordApp.DisplayAlerts = 0
    $ownedDoc = $wordApp.Documents.Open($source, $false, $true, $false)
    $ownedDoc.Repaginate()
    $pageCount = $ownedDoc.ComputeStatistics(2)
    $ownedDoc.ExportAsFixedFormat($pdfPath, 17)
    Write-Output "Word rendered pages: $pageCount"
} finally {
    if ($null -ne $ownedDoc) { $ownedDoc.Close(0) }
    if ($null -ne $wordApp) { $wordApp.Quit(0) }
}
& pdftoppm -png -r 110 $pdfPath (Join-Path $QaDir 'page')
if ($LASTEXITCODE -ne 0) { throw 'PDF rasterization failed' }
Write-Output $QaDir
