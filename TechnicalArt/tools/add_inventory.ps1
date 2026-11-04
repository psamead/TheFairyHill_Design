$ErrorActionPreference='Stop'
$base='C:\Users\Administrator\Documents\MyFlie\AsArtPortfolioTeaching\Animation_yichun\ShareWorkFolder'
$docPath=Join-Path $base 'StoryDesign\妖精丘陵_概念设计说明_m_故事v2.2更新.docx'
$bak=Join-Path $base 'deprecated\妖精丘陵_概念设计说明_m_故事v2.2更新_m3.docx'
$log=Join-Path $base 'TechnicalArt\tools\_add_refs_log.txt'
Get-Process WINWORD -ErrorAction SilentlyContinue | ? { $_.MainWindowTitle -eq '' } | Stop-Process -Force; Start-Sleep 2
if(Test-Path $bak){ throw 'backup exists' }
Copy-Item $docPath $bak
$w=New-Object -ComObject Word.Application; $w.Visible=$false
try{ $d=$w.Documents.Open($docPath)
 $target=$null; foreach($p in $d.Paragraphs){ if($p.OutlineLevel -eq 1 -and $p.Range.Text.Trim().StartsWith('4.')){ $target=$p; break } }
 if(-not $target){ throw 'heading 4 not found' }
 function Before($text,$style){ $h=$target.Range; $h.InsertParagraphBefore(); $npr=$h.Paragraphs.Item(1).Range; $npr.Style=[int]$style; if($text){ $npr.InsertBefore([string]$text) }; return $npr }
 $lines=@(
  @('背包：妮芙的小挎包（2026-10-26 新增）',-4),
  @('参考《空洞骑士》的物品栏：任何时候都能打开查看，打开时游戏暂停。界面画成妮芙随身的布挎包。本作没有战斗，背包只用来查看与回忆，不做配装。',-1),
  @('为什么加：游戏里本来就有很多要拿在手上的东西（欧甘石牌、记忆碎片、铁十字、三叶草光点、四叶草），以及交易付出的代价（名字、存在值上限、被封印的能力）。背包把它们集中显示，是整合已有系统，不是新增玩法。',-1),
  @('Demo 显示内容：圣物（铁十字：断绳 / 重新系好）；欧甘石牌（已收集的字母，未收集为空槽）；记忆碎片（点开显示一句回忆，数量即「回忆」可用次数）；妮芙（名字、存在值上限、三叶草光点数）。四叶草为 Could；图鉴、地图留到第三章以后。',-1),
  @('呼应主题：交出名字后，名字布签变成空白；存在值上限降低、能力被封印也都在背包里看得见——「救朋友的每一步都在付出代价」。',-1),
  @('禁用时机：交易对话、过场动画、结尾卡、Boss 战、第五章原路返回的逃脱段、场景加载中。',-1),
  @('技术要点：只做一个跨场景的 GameState 单例，下面挂背包、剧情旗标（NarrativeFlags）和存在值；界面与数据分开；数据可序列化，以后直接接存档。详细设计与美术资产清单见共享文件夹 INVENTORY_SYSTEM_DESIGN.md。',-1)
 )
 foreach($x in $lines){ $null=Before $x[0] $x[1] }
 $d.Save(); $d.Close(); 'ok inventory' | Out-File -Encoding utf8 $log
} catch { ('ERR '+$_.Exception.Message) | Out-File -Encoding utf8 $log } finally { try{ foreach($x in @($w.Documents)){ $x.Close($false) } }catch{}; $w.Quit() }
