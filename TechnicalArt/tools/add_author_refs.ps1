$ErrorActionPreference='Stop'
$base='C:\Users\Administrator\Documents\MyFlie\AsArtPortfolioTeaching\Animation_yichun\ShareWorkFolder'
$docPath=Join-Path $base 'StoryDesign\妖精丘陵_概念设计说明_m_故事v2.2更新.docx'
$bak=Join-Path $base 'deprecated\妖精丘陵_概念设计说明_m_故事v2.2更新_m2.docx'
$img=Join-Path $base 'MJ_ref\AUTHOR_L7_66'
$log=Join-Path $base 'TechnicalArt\tools\_add_refs_log.txt'
if(Test-Path $bak){ throw "backup exists: $bak" }
Copy-Item $docPath $bak
$items=@(
 @('S01_VILLAGE_REF.png','S1 黄昏村庄','稍作改动可用（Demo）','村庄布局、远处山丘上的古墓'),
 @('S02_TOMB_ENTRANCE_REF.png','S2 古墓入口','稍作改动可用（Demo）','三曲枝刻石、门洞构图'),
 @('S03_TOMB_CORRIDOR_REF.png','S3 古墓石廊','稍作改动可用（Demo）','青绿妖火火把；墙上两个小女孩涂鸦可作奥伊芯留下的记忆碎片'),
 @('S04_VINE_HALL_REF.png','S4 藤蔓门厅','稍作改动可用（Demo）','石门与兜帽假 Ogma 的站位'),
 @('PUCA_REF_1.png','普卡','参考细节（Demo）','黑羽毛团与金色眼睛；第二章结尾卡「光晕下的金色眼睛」可借用'),
 @('CROSS_AUTHOR_REF.png','妮芙家传十字','参考细节（Demo）','三叶草圆章、红绿缠绳细节；做道具图标时参考，不替换 v3 立绘'),
 @('S05_STONE_CIRCLE_REF.png','S5 雾中巨石阵（表世界）','以后可能用到（第三章）','灰雾色调'),
 @('S05_STONE_CIRCLE_OTHERWORLD_REF.png','S5 雾中巨石阵（里世界）','以后可能用到（第三章）','与表世界版对照的青绿色调'),
 @('S06_WITHERED_FOREST_REF.png','S6 枯萎森林','以后可能用到（第三章）','石子摆成的箭头和圆圈：追踪足迹的线索'),
 @('PUCA_FORMS_REF.png','普卡变身','以后可能用到（第三章）','兔、山羊、马、乌鸦四种形态与切换过程'),
 @('THORN_QUEEN_REF.png','荆棘女王','以后可能用到（第四章）','三视图、荆棘冠与配色'),
 @('S09_THORN_QUEEN_COURT_REF.png','S9 荆棘女王之庭','以后可能用到（第四章）','奥伊芯在女王怀中沉睡的构图'),
 @('S10_HOMECOMING_DAWN_REF.png','S10 归途 · 黎明','以后可能用到（第五章 / 宣传）','两人牵手跑出古墓'),
 @('K03_KEYART_REF.png','宣传主视觉构图','以后可能用到（宣传）','多角色主视觉排布；女妖尚未修改')
)
$w=New-Object -ComObject Word.Application; $w.Visible=$false
try{
 $d=$w.Documents.Open($docPath)
 # find 附录 A heading
 $target=$null; foreach($p in $d.Paragraphs){ if($p.OutlineLevel -eq 1 -and $p.Range.Text.Trim().StartsWith('附录 A')){ $target=$p; break } }
 if(-not $target){ throw 'appendix A not found' }
 $r=$target.Range; $r.Collapse(1)
 function Add-Para($rng,$text,$style){ $rng.InsertParagraphBefore(); $pr=$rng.Paragraphs(1).Range; $pr.Text=$text; $pr.Style=$style; $rng.SetRange($pr.End,$pr.End); return $rng }
 $intro=@(
  @('8.11 原作者新稿 L7/66：参考图（2026-10-26 新增）',-3),
  @('原作者新增了 9 张场景、普卡、荆棘女王、十字架和一张主视觉构图。副本放在 MJ_ref/AUTHOR_L7_66/，原图在 L7/66/，不改动。图片见附录 B 末尾。',-1),
  @('风格说明：这批图单张都很精细，但放在一起会互相争抢，缺少主次和前后层次，与本作现有的游戏画面风格（两位女主 v3、开始菜单、海报）不同，因此不直接作为游戏画面。游戏风格沿用现有；体量仍按 Demo 计划（第一章 S1–S3 + 第二章 S4）。',-1),
  @('用法：这批图说明相关内容已经考虑过。做到对应场景或角色时按需借用其中的构图、道具和造型，降低细节密度、拉开前后景明暗，改成本作风格；不是全部重做。每张图按可用程度标记为三类：',-1),
  @('• 稍作改动可用（Demo）：S1、S2、S3、S4',-1),
  @('• 参考细节（Demo）：普卡的金色眼睛、十字架细节',-1),
  @('• 以后可能用到：S5、S6、S9、S10、普卡变身、荆棘女王、宣传主视觉构图',-1)
 )
 foreach($x in $intro){ $r=Add-Para $r $x[0] $x[1] }
 # table
 $r.InsertParagraphBefore(); $tr=$r.Paragraphs(1).Range
 $t=$d.Tables.Add($tr,$items.Count+1,4); $t.Borders.Enable=$true
 $hd=@('文件','对应','标记','可借用的地方'); for($c=1;$c -le 4;$c++){ $t.Cell(1,$c).Range.Text=$hd[$c-1]; $t.Cell(1,$c).Range.Font.Bold=$true }
 for($i=0;$i -lt $items.Count;$i++){ for($c=1;$c -le 4;$c++){ $t.Cell($i+2,$c).Range.Text=$items[$i][$c-1] } }
 # appendix B pictures at end
 $e=$d.Content; $e.Collapse(0)
 $e.InsertParagraphAfter(); $e=$d.Content; $e.Collapse(0)
 $p=$d.Paragraphs($d.Paragraphs.Count).Range; $p.Text='原作者新稿 L7/66（参考，风格与游戏不同）'; $p.Style=-4
 foreach($it in $items){
  $d.Content.InsertParagraphAfter(); $p=$d.Paragraphs($d.Paragraphs.Count).Range; $p.Text=$it[0]; $p.Style=-4
  $d.Content.InsertParagraphAfter(); $p=$d.Paragraphs($d.Paragraphs.Count).Range; $p.Style=-1
  $pic=$d.InlineShapes.AddPicture((Join-Path $img $it[0]),$false,$true,$p)
  $maxW=$w.CentimetersToPoints(15); if($pic.Width -gt $maxW){ $s=$maxW/$pic.Width; $pic.Width=$maxW; $pic.Height=$pic.Height*$s }
  $d.Content.InsertParagraphAfter(); $p=$d.Paragraphs($d.Paragraphs.Count).Range; $p.Text=("对应："+$it[1]+"｜"+$it[2]+"｜"+$it[3]+"。与本作游戏风格不同，只作参考。"); $p.Style=-1
 }
 $d.Save(); $n=$d.InlineShapes.Count; $d.Close()
 "ok shapes=$n" | Out-File -Encoding utf8 $log
} catch { ("ERR "+$_.Exception.Message) | Out-File -Encoding utf8 $log; throw } finally { $w.Quit() }
