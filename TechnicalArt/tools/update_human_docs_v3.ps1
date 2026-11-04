$ErrorActionPreference='Stop'
$base='C:\Users\Administrator\Documents\MyFlie\AsArtPortfolioTeaching\Animation_yichun\ShareWorkFolder'
$log=Join-Path $base 'TechnicalArt\tools\_human_docs_log.txt'
$out=@()
Get-Process WINWORD -ErrorAction SilentlyContinue | ? { $_.MainWindowTitle -eq '' } | Stop-Process -Force; Start-Sleep 2
$w=New-Object -ComObject Word.Application; $w.Visible=$false
function Backup($src,$bakName){ $b=Join-Path $base ('deprecated\'+$bakName); if(Test-Path $b){ throw "backup exists $bakName" }; Copy-Item $src $b }
function AppendLines($d,$lines){
 foreach($x in $lines){
  $d.Content.InsertParagraphAfter(); $lp=$d.Paragraphs.Last; if($x[1] -ne 99){ $lp.Range.Style=[int]$x[1] }
  if($x[1] -eq 99){ $lp.Range.Style=-1; $rr=$d.Paragraphs.Last.Range; $rr.Collapse(1); $pic=$d.InlineShapes.AddPicture([string]$x[0],$false,$true,$rr); $mw=$w.CentimetersToPoints(15); if($pic.Width -gt $mw){ $s=$mw/$pic.Width; $pic.Width=$mw; $pic.Height=$pic.Height*$s } }
  else { $lp.Range.InsertBefore([string]$x[0]) }
 }
}
function BeforeHeading($d,$startsWith,$level,$lines){
 $target=$null; foreach($p in $d.Paragraphs){ if($p.OutlineLevel -eq $level -and $p.Range.Text.Trim().StartsWith($startsWith)){ $target=$p; break } }
 if(-not $target){ throw "heading not found: $startsWith" }
 foreach($x in $lines){ $h=$target.Range; $h.InsertParagraphBefore(); $npr=$h.Paragraphs.Item(1).Range
  if($x[1] -eq 99){ $npr.Style=-1; $rr=$h.Paragraphs.Item(1).Range; $rr.Collapse(1); $pic=$d.InlineShapes.AddPicture([string]$x[0],$false,$true,$rr); $mw=$w.CentimetersToPoints(15); if($pic.Width -gt $mw){ $s=$mw/$pic.Width; $pic.Width=$mw; $pic.Height=$pic.Height*$s } }
  else { $npr.Style=[int]$x[1]; $npr.InsertBefore([string]$x[0]) } }
}
try{
 Backup (Join-Path $base 'StoryDesign\妖精丘陵_Demo设计与开发实施说明.docx') '妖精丘陵_Demo设计与开发实施说明_m.docx'; $out+='demo backup ok'
 # 2 美术方向
 $p2=Join-Path $base 'TechnicalArt\妖精丘陵_美术方向_关键场景标题字体.docx'; # backup _m already made in previous run
 $d=$w.Documents.Open($p2)
 AppendLines $d @(
  @('进度更新（2026-10-26）',-2),
  @('标题：石刻标题牌',-3),
  @('原计划用 Midjourney Retexture 做艺术字，MJ 做不出准确文字，改用 Google Nano Banana 生成「新石器时代古墓镶边石」风格的石刻标题牌：灰色花岗岩、苔藓、三曲枝螺旋与结绳纹，Uncial 字体刻字，字槽内有暖金光。花纹只用螺旋与结绳，不用凯尔特十字（十字架是剧情道具，且属于后来的年代）。',-1),
  @('两行版透明底存于 MJ_ref/TileArtFont_wip.psd，用于海报与开始菜单；单行横版备用。字体文件在 TechnicalArt/fonts/（Uncial Antiqua、Fondamento）。',-1),
  @((Join-Path $base 'TechArtAsset\Poster\TITLE_PLAQUE_nb.png'),99),
  @('海报 v1',-3),
  @('TechArtAsset/Poster/POSTER_v1.png：古墓夜景向上扩出星空，两人背影站在小路上望向门洞；妮芙身前冷蓝光（铁十字）、奥伊芯身前暖金光，两人之间冷暖交汇；顶部石刻标题牌。',-1),
  @((Join-Path $base 'TechArtAsset\Poster\POSTER_v1.png'),99),
  @('开始菜单',-3),
  @('左上标题牌、左侧纵向压暗、按钮左对齐、三曲枝选中图标；Unity 中已可运行，背景音乐已接入。',-1),
  @('风格决定',-3),
  @('原作者新稿 L7/66 只作参考：单张精细，但放在一起会互相争抢、缺主次层次。画面风格沿用现有的两位女主 v3、开始菜单与海报；做到对应场景时按需简化借用。',-1)
 )
 $d.Save(); $d.Close(); $out+='artdir ok'
 # 3 概念设计说明
 $p3=Join-Path $base 'StoryDesign\妖精丘陵_概念设计说明_m_故事v2.2更新.docx'; Backup $p3 '妖精丘陵_概念设计说明_m_故事v2.2更新_m4.docx'
 $d=$w.Documents.Open($p3)
 BeforeHeading $d '7.' 1 @(
  @('6.4 音乐与音效（2026-10-26 新增）',-3),
  @('原设计没有音频。音乐基调：爱尔兰民间传说式的安静好奇、温暖、带一点忧伤，不恐怖、不史诗；乐器以凯尔特竖琴、低音哨笛、弦乐铺底和很淡的无词合唱为主，鼓尽量少；只做器乐。',-1),
  @('做法：用 Google Lyria 3 Pro 生成，再处理成无缝循环。开始菜单 BGM 已完成。Demo 还需要：第一章森林、古墓内部；完整版另需 Boss 与结局。流程与提示词见 TechnicalArt/AUDIO_PIPELINE.md。',-1)
 )
 BeforeHeading $d '8.' 1 @(
  @('7.7 两位主角 v3 定稿（2026-10）',-3),
  @('妮芙 v3：暗铁十字 + 红绿缠线流苏、左半心扣、红绿手绳、绿色绑带中筒靴。四视图（正面 / 朝右侧面 / 朝左侧面 / 背面），朝右侧面为骨骼动画拆件基准。',-1),
  @((Join-Path $base 'MJ_ref\Niamh_v3_turnaround.png'),99),
  @('奥伊芯 v3：去掉铁钉与铁钥匙；原来的大灰心换成右半心扣（与妮芙的左半心扣合成一颗心）；加红绿手绳。四视图（正面 / 3/4 侧 / 朝右侧面 / 背面）。已知差异：侧面披肩画成长围巾，比正面长，拆件以侧面为准。',-1),
  @((Join-Path $base 'MJ_ref\Oisin_v3_turnaround.png'),99)
 )
 $d.Save(); $d.Close(); $out+='concept ok'
} catch { $out+=('ERR '+$_.Exception.Message+' @ '+$_.InvocationInfo.ScriptLineNumber) } finally { try{ foreach($x in @($w.Documents)){ $x.Close($false) } }catch{}; $w.Quit(); $out | Out-File -Encoding utf8 $log }
