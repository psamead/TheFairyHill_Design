$ErrorActionPreference = 'Stop'
$designRoot = Split-Path $PSScriptRoot -Parent
$docPath = Join-Path $designRoot 'TechnicalArt\妖精丘陵_开场界面与举高动作试装_2026-11-18.docx'
$qaRoot = Join-Path $designRoot 'TechnicalArt\references\Opening_Cross_Trial_2026-11-18_QA'
$wordOutput = Join-Path $qaRoot 'word_final'
New-Item -ItemType Directory -Path $wordOutput -Force | Out-Null
$ownedWord = $null
$ownedDocument = $null
try {
    $ownedWord = New-Object -ComObject Word.Application
    $ownedWord.Visible = $false
    $ownedWord.DisplayAlerts = 0
    $ownedDocument = $ownedWord.Documents.Open($docPath, $false, $true, $false)
    $ownedDocument.Repaginate()
    $wordPages = $ownedDocument.ComputeStatistics(2)
    $titleFont = $ownedDocument.Styles.Item('Title').Font.NameFarEast
    $normalFont = $ownedDocument.Styles.Item('Normal').Font.NameFarEast
    $ownedDocument.ExportAsFixedFormat((Join-Path $wordOutput 'opening_cross_trial.pdf'),17)
    [ordered]@{
        date = '2026-11-18'
        word_version = $ownedWord.Version
        word_pre_export_statistics = $wordPages
        title_font = $titleFont
        normal_font = $normalFont
        source_sha256 = (Get-FileHash -LiteralPath $docPath -Algorithm SHA256).Hash.ToLowerInvariant()
        libreoffice_final_pages = 2
        word_render_status = 'exported; PDF page count and visual inspection recorded separately'
    } | ConvertTo-Json | Set-Content -LiteralPath (Join-Path $qaRoot 'validation.json') -Encoding utf8
    Write-Output "Word pages: $wordPages; title font: $titleFont; body font: $normalFont"
} finally {
    if ($null -ne $ownedDocument) { $ownedDocument.Close(0) }
    if ($null -ne $ownedWord) { $ownedWord.Quit(0) }
}
