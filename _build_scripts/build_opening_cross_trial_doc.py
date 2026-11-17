"""Human companion to the dated shared task; preserves all earlier Word files."""
from pathlib import Path
from docx import Document
from docx.shared import Cm,Pt,RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'TechnicalArt/妖精丘陵_开场界面与举高动作试装_2026-11-18.docx'
doc=Document();sec=doc.sections[0]
sec.page_width=Cm(21);sec.page_height=Cm(29.7)
sec.top_margin=sec.bottom_margin=Cm(2);sec.left_margin=sec.right_margin=Cm(2.1)
for name,size,color in [('Normal',10.5,'26352B'),('Title',23,'2F5D3A'),('Heading 1',16,'2F5D3A'),('Heading 2',13,'3E7B4E')]:
    s=doc.styles[name];s.font.name='Microsoft YaHei';s.font.size=Pt(size);s.font.color.rgb=RGBColor.from_string(color)
    fonts=s.element.get_or_add_rPr().get_or_add_rFonts()
    for a in ['ascii','hAnsi','eastAsia','cs']:fonts.set(qn('w:'+a),'Microsoft YaHei')
    for a in ['asciiTheme','hAnsiTheme','eastAsiaTheme','cstheme']:fonts.attrib.pop(qn('w:'+a),None)
    s.paragraph_format.space_after=Pt(6);s.paragraph_format.line_spacing=Pt(18)
    if name!='Normal':s.font.bold=True
for s in doc.styles:
    for border in list(s.element.iter(qn('w:pBdr'))):border.getparent().remove(border)
def p(t,style=None):return doc.add_paragraph(t,style)
def table(headers,rows,widths):
    t=doc.add_table(rows=1,cols=len(headers));t.autofit=False
    for col,w in zip(t.columns,widths):col.width=Cm(w)
    for cell,h,w in zip(t.rows[0].cells,headers,widths):cell.text=h;cell.width=Cm(w)
    header=OxmlElement('w:tblHeader');t.rows[0]._tr.get_or_add_trPr().append(header)
    for row in rows:
        for cell,value,w in zip(t.add_row().cells,row,widths):cell.text=value;cell.width=Cm(w)
    for i,row in enumerate(t.rows):
        row._tr.get_or_add_trPr().append(OxmlElement('w:cantSplit'))
        for cell in row.cells:
            cell.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER
            pr=cell._tc.get_or_add_tcPr()
            sh=OxmlElement('w:shd');sh.set(qn('w:fill'),'2F5D3A' if i==0 else ('FFFFFF' if i%2 else 'EFF3EE'));pr.append(sh)
            borders=OxmlElement('w:tcBorders')
            for edge in ['top','left','bottom','right']:
                e=OxmlElement('w:'+edge);e.set(qn('w:val'),'single');e.set(qn('w:sz'),'4');e.set(qn('w:color'),'8C9B8D');borders.append(e)
            pr.append(borders);margin=OxmlElement('w:tcMar')
            for edge,value in [('top','80'),('bottom','80'),('left','100'),('right','100')]:
                e=OxmlElement('w:'+edge);e.set(qn('w:w'),value);e.set(qn('w:type'),'dxa');margin.append(e)
            pr.append(margin)
            for para in cell.paragraphs:
                para.paragraph_format.line_spacing=Pt(16);para.paragraph_format.space_after=Pt(2)
                for run in para.runs:
                    run.font.size=Pt(10)
                    if i==0:run.bold=True;run.font.color.rgb=RGBColor(255,255,255)
    gap=p('');gap.paragraph_format.space_after=Pt(0);gap.paragraph_format.line_spacing=Pt(5)
    return t

title=p('开场界面与举高动作试装','Title');title.alignment=WD_ALIGN_PARAGRAPH.CENTER
p('妖精丘陵  2026年11月18日  负责人及制作协作者').alignment=WD_ALIGN_PARAGRAPH.CENTER
p('当前结论：界面与动作代码已放入实际工程，离线 C# 类型检查通过。实机检查任务已写入共享目录；网络电脑 Codex 尚未启动，Editor 导入、Play Mode 和用户画面认可待检查。')
p('负责人休息期间已授权先推送当前源码、美术和发展记录等大文件；后续收到实机回报，再同步运行结论。')
p('1 界面与按键阅读','Heading 1')
table(['项目','本轮试装要求'],[
    ['故事画','参考守灯人的全屏阅读方式，保持比例铺满。字幕叠在下方渐暗区域，去掉原分隔线和页码；现有图片仍是占位稿。'],
    ['字幕与导航','三段字幕及6／7／6秒时长保留。Next／Skip放右上，按键提示放右下。保留章节卡、切关遮罩、输入释放和防重复推进。'],
    ['按键下划线','开场的Space、Enter、Esc，操作栏的A、D、方向键、Shift、Space，以及交互E、Q等按键名称下加线；普通词不加线。'],
    ['制作约束','沿用原字体，不改共享字体图集。每张故事画可调字幕区域以避开人脸；大、小尺寸均需实机检查。']],[3.1,13.7])
p('2 举高十字架与红障碍','Heading 1')
table(['项目','当前接法及边界'],[
    ['姿势与触发','采用B：原v8直接切到用户画的举高姿势，事件结束恢复，无胸前中间停留。有铁十字架且在原范围内对受控红墙按Q。'],
    ['保持与反馈','持势覆盖原0.3秒红光与1.6秒消解，暂时停止水平／跳跃输入；物理和碰撞继续。沿用原光效和火花，本轮没有新增大光束。'],
    ['源稿与对齐','两张用户动作、旧GIF与PSD保留。举高图350×699，脚底对齐基础327×699角色；切姿势不能横移或缩放。']],[3.1,13.7])
p('胸前动作仍服务小怪、小障碍和小剧情；举高动作服务大型剧情事件。本轮接入已有终段事件，不扩展完整战斗系统，不从GIF节奏推导冷却或伤害。')

heading=p('3 双方记录中可复用的经验','Heading 1');heading.paragraph_format.page_break_before=True
table(['来源','本轮如何采用'],[
    ['妖精丘陵','保留人物身份、原衣装与道具；使用用户绘画切换姿势，避免重新生成整个人物。静帧、预览、接入和运行分开验收。'],
    ['守灯人','在已有可玩路线内改善表现，用故事画承载更广叙事；参考画面和字幕的关系，不复制夜间色调或扩大关卡。'],
    ['交接经验','实现、编译、运行和用户认可分别记录。任务单可读不等于Agent已启动；构建或启动成功也不等于玩家路线通过。']],[3.1,13.7])
p('4 当前证据与待检查内容','Heading 1')
table(['阶段','状态与证据'],[
    ['已实施','实际工程7份脚本及举高资源已放置，来源／目标散列核对。4个既有用户场景、字体和入口文件保持原字节。'],
    ['离线检查','基线22份、试装23份Gameplay源码，引用285个实际工程程序集，类型检查通过；保留原有3项序列化字段警告。'],
    ['实机待验','Editor导入与编译；1920与1280字幕／按键线；Next／Skip与按住键；红墙前Q举高、朝向、脚底、握持、恢复、重复触发和无目标提示。'],
    ['完成后','网络端回报Handoff、截图与结果，设计端更新相关文档，再按负责人授权git push。验收尚未通过时必须保留真实状态。']],[3.1,13.7])
p('5 从共享任务单接续','Heading 1')
p('任务单只保留在我们这边的共享设计目录，由网络电脑Codex直接读取，无需复制一份任务文件到对方工程。素材仍按交接规则复制，实际运行报告保存在Unity工程Docs目录。')
p('当前任务：共享目录CommandForAgentToInitialRun中的2026年11月18日Opening Immersive Cross Raise任务单。完整路径、启动文字、代码散列与验证日志见对应TechnicalArt试装说明和unity_drop文件夹。')
p('实机反馈：Unity工程Docs中的Opening_Immersive_Cross_Raise_Unity_Handoff.md；截图与结果存对应References目录的Unity_Trial文件夹。')
footer=sec.footer.paragraphs[0];footer.alignment=WD_ALIGN_PARAGRAPH.RIGHT
fld=OxmlElement('w:fldSimple');fld.set(qn('w:instr'),'PAGE');footer._p.append(fld)
doc.save(OUT);print(OUT)
