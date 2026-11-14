"""Build the short human-facing Niamh v8 review from verified project records.

Run with the bundled Python runtime after reconciling any new Unity evidence.
The archived trial task and Unity result log remain the detailed sources.
"""

from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "TechnicalArt" / "妮芙动作试做与Unity试玩记录_v8.docx"
OFFLINE = ROOT / "TechArtAsset/Characters/Niamh/Motion_v8/previews/Niamh_motion_v8_still.png"
GAME = ROOT / "TechnicalArt/references/Niamh_v8_Unity_Forest_Fall.png"
BLACK = RGBColor(28, 32, 28)
MUTED = RGBColor(93, 101, 93)


def set_font(style, size, bold=False, color=BLACK):
    style.font.name = "Microsoft YaHei"
    style._element.get_or_add_rPr().rFonts.set(qn("w:eastAsia"), "Microsoft YaHei")
    style.font.size = Pt(size)
    style.font.bold = bold
    style.font.color.rgb = color


def add_text(document, text, style=None, keep=False):
    p = document.add_paragraph(style=style)
    p.add_run(text)
    p.paragraph_format.keep_with_next = keep
    return p


def add_bullet(document, label, body):
    p = document.add_paragraph(style="List Bullet")
    r = p.add_run(label)
    r.bold = True
    p.add_run(body)
    return p


def add_image(document, path, caption, width_cm=16.1):
    p = document.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.add_run().add_picture(str(path), width=Cm(width_cm))
    p.paragraph_format.space_after = Pt(3)
    p2 = document.add_paragraph(style="Caption")
    p2.add_run(caption)
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER


def add_page_number(paragraph):
    paragraph.add_run("妮芙动作试做 v8  ·  ")
    field = OxmlElement("w:fldSimple")
    field.set(qn("w:instr"), "PAGE")
    paragraph._p.append(field)


def main():
    doc = Document()
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Cm(21), Cm(29.7)
    sec.top_margin, sec.bottom_margin = Cm(2.0), Cm(1.8)
    sec.left_margin, sec.right_margin = Cm(2.4), Cm(2.4)
    sec.header_distance, sec.footer_distance = Cm(0.9), Cm(0.8)

    styles = doc.styles
    set_font(styles["Normal"], 10.5)
    styles["Normal"].paragraph_format.line_spacing = 1.28
    styles["Normal"].paragraph_format.space_after = Pt(7)
    set_font(styles["Title"], 20, True)
    styles["Title"].paragraph_format.space_after = Pt(11)
    title_ppr = styles["Title"]._element.get_or_add_pPr()
    title_border = title_ppr.find(qn("w:pBdr"))
    if title_border is not None:
        title_ppr.remove(title_border)
    for name, size, before in (("Heading 1", 13.5, 13), ("Heading 2", 11, 9)):
        set_font(styles[name], size, True)
        styles[name].paragraph_format.space_before = Pt(before)
        styles[name].paragraph_format.space_after = Pt(5)
        styles[name].paragraph_format.keep_with_next = True
    set_font(styles["Caption"], 8.5, False, MUTED)
    styles["Caption"].paragraph_format.space_after = Pt(8)
    set_font(styles["List Bullet"], 10.5)
    styles["List Bullet"].paragraph_format.left_indent = Cm(0.55)
    styles["List Bullet"].paragraph_format.first_line_indent = Cm(-0.27)
    styles["List Bullet"].paragraph_format.space_after = Pt(5)

    footer = sec.footer.paragraphs[0]
    footer.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    add_page_number(footer)
    for run in footer.runs:
        run.font.size = Pt(8)
        run.font.color.rgb = MUTED

    add_text(doc, "妮芙动作试做与 Unity 试玩记录", "Title")
    add_text(doc, "《妖精丘陵》  ·  v8  ·  2026 年 11 月 14 日")
    add_text(doc, "供项目负责人、学生、美术制作人员及后续 Agent 阅读。本文说明这轮动作做到了哪里、在游戏中验证了什么，以及继续制作时要保留的经验。", keep=True)

    doc.add_heading("当前结论", 1)
    add_text(doc, "六张由用户修订的 Photoshop 部件已接入 Unity，形成可回退的分层角色试玩版。编辑器编译通过，村庄与森林的 Play Mode 中观察到了基础运动和跳跃阶段。项目负责人试玩后反馈：‘除了些卡顿，其他基本 ok’。卡顿原因尚未测量；本轮也没有完成计划中的 22 骨骼绑定。")

    doc.add_heading("动作如何变化", 1)
    add_bullet(doc, "跳起：", "腿向后、手向前、头微抬。")
    add_bullet(doc, "下落：", "头往下看、手往后、腿往前；摆幅逐渐增大，再在落地前收回。")
    add_bullet(doc, "落地：", "脚保持接地，上半身与后发轻微下沉后恢复，不再做明显的整身压缩。")
    add_text(doc, "下图是接入 Unity 之前制作的离线姿势预览，画面上的 ‘NOT IN UNITY’ 是当时的状态标注。游戏内动作已经按实际跳跃速度重新安排。")
    add_image(doc, OFFLINE, "图 1  待机、走、跑、跳的离线姿势预览；不是游戏运行截图。")

    doc.add_heading("Unity 试玩看到了什么", 1)
    add_text(doc, "Unity 将六张 327 × 699 像素的透明部件组装为试验 Prefab，另复制并调暗一组腿和靴子作为远侧腿。七个 Animator 状态由现有玩家的速度和落地状态驱动；玩家根对象、碰撞体、输入与场景加载逻辑保留。")
    add_text(doc, "记录到的村庄动作包括待机、走、跳起、最高点、下落和落地，后来也观察到了负责人从村庄切到森林。森林中看到了同类动作与左右转向。下图展示森林 Play Mode 的下落姿势；它是单帧证据，不等于整段动作的验收。")
    add_image(doc, GAME, "图 2  Unity 森林场景 Play Mode 下落帧。来源：TheFairyHill2D/Docs/References/Niamh_Motion_v8/Unity_Trial/Forest_Live_Fall.png。")

    doc.add_heading("仍需确认", 1)
    add_bullet(doc, "画面：", "检查大幅摆臂时肩后是否露出缺画、腿靴接缝与脚底滑动；六部件无法独立弯肘、弯膝或摆动披风。")
    add_bullet(doc, "操作：", "5.6u/s 跑速、栅门开关和各处碰撞路线尚无逐项录像；不能由总体试玩反馈推断这些检查均已通过。")
    add_bullet(doc, "卡顿：", "原因未剖析。再次观察时先减少同时运行的软件和截图负担，再用 Unity Profiler 定位。")
    add_bullet(doc, "下一批动作：", "推门与举十字架尚未制作；先对照现有交互和 S2/S3 的实际场景需求，确定触发时机、手型和补画范围。")

    doc.add_heading("资料与接手", 1)
    add_text(doc, "美术源、六部件和离线预览：TechArtAsset/Characters/Niamh/Motion_v8/。Unity 结果、截图与回退：TheFairyHill2D/Docs/Niamh_Motion_v8_Unity_Handoff.md。制作经验：TechnicalArt/LESSONS_CHARACTER_ANIMATION.md。原 Unity 任务单已执行，仅供追溯；新证据应先记入 Unity 结果，再更新本文。")

    doc.save(OUTPUT)
    print(OUTPUT)


if __name__ == "__main__":
    main()
