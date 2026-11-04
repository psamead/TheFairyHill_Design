$ErrorActionPreference='Stop'
$base='C:\Users\Administrator\Documents\MyFlie\AsArtPortfolioTeaching\Animation_yichun\ShareWorkFolder'
$doc=Join-Path $base 'StoryDesign\妖精丘陵_概念设计说明_m_故事v2.2更新.docx'
$out=Join-Path $base 'TechnicalArt\tools\_headings.txt'
$w=New-Object -ComObject Word.Application; $w.Visible=$false
try{ $d=$w.Documents.Open($doc,$false,$true)
 $lines=@()
 foreach($p in $d.Paragraphs){ $lvl=$p.OutlineLevel; if($lvl -le 3){ $lines+=("L$lvl | "+$p.Style.NameLocal+" | "+$p.Range.Text.Trim()) } }
 $lines+=("PAGES "+$d.ComputeStatistics(2)); $lines+=("SHAPES "+$d.InlineShapes.Count)
 $lines | Out-File -Encoding utf8 $out; $d.Close($false) } finally { $w.Quit() }
