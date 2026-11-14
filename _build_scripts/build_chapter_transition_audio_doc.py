"""Build the human-readable v1 transition and movement-audio brief.

Use the bundled Codex document Python runtime, then render and inspect pages.
"""

from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT
from docx.shared import Inches, Pt, RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn


ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "TechnicalArt" / "妖精丘陵_章节过渡与妮芙动作声音设计_v1.docx"

doc = Document()
sec = doc.sections[0]
sec.page_width = Inches(8.5)
sec.page_height = Inches(11)
sec.top_margin = Inches(0.77)
sec.bottom_margin = Inches(0.72)
sec.left_margin = Inches(0.85)
sec.right_margin = Inches(0.85)

styles = doc.styles
normal = styles["Normal"]
normal.font.name = "Microsoft YaHei"
normal.font.size = Pt(10.5)
normal.font.color.rgb = RGBColor(29, 35, 31)
normal.paragraph_format.line_spacing = 1.28
normal.paragraph_format.space_after = Pt(7)

for name, size, before, after in (("Title", 19, 0, 12), ("Heading 1", 14, 15, 6), ("Heading 2", 11.5, 10, 4)):
    s = styles[name]
    s.font.name = "Microsoft YaHei"
    s.font.size = Pt(size)
    s.font.bold = True
    s.font.color.rgb = RGBColor(0, 0, 0)
    s.paragraph_format.space_before = Pt(before)
    s.paragraph_format.space_after = Pt(after)
    s.paragraph_format.keep_with_next = True

# Word's built-in Title style can carry a colored bottom border in its XML.
title_ppr = styles["Title"]._element.pPr
if title_ppr is not None:
    border = title_ppr.find(qn("w:pBdr"))
    if border is not None:
        title_ppr.remove(border)


def para(text="", bold_lead=None, style=None):
    p = doc.add_paragraph(style=style)
    if bold_lead and text.startswith(bold_lead):
        p.add_run(bold_lead).bold = True
        p.add_run(text[len(bold_lead):])
    else:
        p.add_run(text)
    return p


def bullet(text):
    p = doc.add_paragraph(style="List Bullet")
    p.add_run(text)
    p.paragraph_format.space_after = Pt(4)
    return p


doc.add_paragraph("妖精丘陵章节过渡与妮芙动作声音设计", style="Title")
para("2026 年 11 月 14 日  ·  设计方案 v1  ·  供项目负责人、制作人员、学生与后续 Agent 阅读")
para("这份说明规划章节与地点过渡，以及妮芙移动、跳跃和不同地面的声音。村庄与森林已经能玩，妮芙 v8 动作在这两处试玩基本可用。Demo 按现行计划完成第一、二章 S1–S4 和结尾卡；重点展示妮芙获得想象之眼、切换现实与幻象视野、再次使用它推动剧情和人物互动。下述过渡和声音尚未接入 Unity。")

doc.add_heading("先做什么", 1)
bullet("先把村庄到森林做成短淡出、换场与地点提示，保持同一章的探索连贯。")
bullet("石廊后进入第二章时展示章节标题与短叙事画；开场和结尾保留必要镜头。")
bullet("先用 Python 离线合成动作声音试听稿，再在 Unity 中按动作与接触材质播放；听过游戏音乐下的效果后才定稿。")

doc.add_heading("章节和地点不是同一种提示", 1)
para("第一章《误入》覆盖黄昏村庄、森林小径、古墓入口和古墓石廊。玩家从村庄走进森林时，只需短暂遮画、音乐与环境声的衔接，并在进入后显示 Forest Path 这样的地点字样。地点字样不挡操作，约两秒消失。森林走向古墓时，用低语、门声和冷色光逐渐建立不安；古墓石廊的关门事件留在实时画面内。")
para("石廊门打开、玩家进入藤蔓门厅，才是第二章《规则》的边界。建议短暂黑场，显示 CHAPTER II 和 THE RULES，再用一到两张画面引出文字、名字和门的规则。守门者真身仍应保密。想象之眼在 S3 获得并首次切换，在后续主线再次使用，例如进入 S4 时看见与对话有关的线索。它与十字架的瞬时脉冲分开。")
para("S4 名字交易后，Demo 结尾卡使用与接受或拒绝相应的短句，并明确第三章尚未开放。")

doc.add_heading("从守灯人借用的经验", 1)
para("《守灯人》的分镜把每张图片或视频、字幕、时长和缓慢推拉存为数据；播放时交叉淡入，可逐张前进或跳过整段。人物脚步由行走动画接地时刻触发，跳跃与落地由状态变化触发。这些是已实现的参照。妖精丘陵的篇幅更长，因此还需单独记录章号、章节标题与地点名，让故事段落只出现在真正的章节边界。")

doc.add_heading("什么时候补 MJ 图片", 1)
para("候选镜头有两人玩耍、古墓自行打开与追赶、石廊后的藤蔓与守门者、结尾远景。S2 至 S4 目前只有灰盒，先用现有场景截图排时长与字幕样稿。相关场景画面确定后，再生成正式图，并在 Unity 画幅里比对颜色、笔触、人物衣装、墓门与光源。字幕保持独立文字层；想象之眼的实际切换操作留在可玩画面。")

doc.add_heading("妮芙动作声音", 1)
para("每次鞋底真正落地才播放一次脚步。步行与跑步用不同的触发速度和轻重，但声音的材质由脚下的碰撞物决定。跳跃在真实起跳时发声；落地依据下落速度分轻重，避免站稳时重复响。三到四个脚步变体轮换，避免连续两次一模一样。")

for lead, desc in (
    ("土地", "松散土粒与闷响，作为村庄路径的基础音色。"),
    ("草地", "保留轻土感，再加短草叶擦声；森林与村庄草地可共用基础音色。"),
    ("石头", "鞋底碰击与少量石粒，适用于石墙顶部和后续石路。"),
    ("木箱", "有轻微空腔感的木响；当前两处可玩场景尚未找到木箱，先留作后续物件。"),
    ("草垛", "顶部脚步是压实干草；从边缘擦过时另叠干草摩擦声。先核实草垛碰撞体是否允许穿行。"),
):
    para(f"{lead}　{desc}", bold_lead=lead)

doc.add_heading("怎样放进现有 Unity 工程", 1)
para("声音组件应附在常驻的妮芙角色上，不改变已通过试玩的运动参数。现有控制器已经检测地面接触，但只保留了“是否着地”；制作端可以沿用同一次碰撞检测，把有效的脚下碰撞体提供给音频系统。给地面、石墙和未来木箱明确的声音材质数据，并同步写入布局或场景生成数据，避免重建场景时丢失。草垛擦声可由独立的接近区域触发。")
para("先验收村庄的土地、草、石墙和草垛，再验收森林的草与地沟。木箱等出现真实可踩物件时再测试。门、拾取十字架、荆棘墙湮灭各用原来的事件音效，不混进脚步系统。")

doc.add_heading("试听稿与交付状态", 1)
para("Python 试听稿包含五种材质的三次脚步、两次起跳、轻重落地各两次和两次干草擦声。每条是 44.1 kHz 单声道 WAV 母带，另有 OGG 供 Unity 试装。脚本和固定随机种子保存在 TechnicalArt/tools/make_niamh_motion_sfx_v1.py；试听拼盘在 TechArtAsset/Audio/SFX/Niamh_Motion_v1/。这些声音尚待项目负责人试听，也尚未放入 Unity。")
para("视觉和声音分别分小批交给 Unity 端：先完成现有村庄与森林的动作声音，再做同章换场；S2、S3、S4 美术推进后制作第二章故事画面。每一批都应记录实际文件、编译、Play Mode、人工观看或试听结果。共享网络优先传素材，设计仓库作为只读源。")

footer = sec.footer.paragraphs[0]
footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
footer.add_run("妖精丘陵  ·  设计方案 v1  ·  ")
fld = OxmlElement("w:fldSimple")
fld.set(qn("w:instr"), "PAGE")
footer._p.append(fld)

doc.save(OUT)
print(OUT)
