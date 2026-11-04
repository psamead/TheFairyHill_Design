$ErrorActionPreference='Stop'
$base='C:\Users\Administrator\Documents\MyFlie\AsArtPortfolioTeaching\Animation_yichun\ShareWorkFolder'
$docPath=Join-Path $base 'StoryDesign\妖精丘陵_概念设计说明_m_故事v2.2更新.docx'
$log=Join-Path $base 'TechnicalArt\tools\_add_refs_log.txt'
$w=New-Object -ComObject Word.Application; $w.Visible=$false
try{ $d=$w.Documents.Open($docPath); $n=0
 $f=$d.Content; $f.Find.ClearFormatting(); if($f.Find.Execute('可借用的地方')){ $t=$f.Tables.Item(1); $t.Range.Style=-1; $t.Range.Rows.Item(1).Range.Font.Bold=$true; $n=1 }
 $d.Save(); $d.Close(); "fixed $n" | Out-File -Encoding utf8 $log
} catch { ("ERR "+$_.Exception.Message) | Out-File -Encoding utf8 $log } finally { $w.Quit() }
