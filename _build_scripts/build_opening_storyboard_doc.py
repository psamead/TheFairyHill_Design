"""Build the three-page human storyboard brief from existing reference images.

Run with the bundled Codex Python runtime. This creates a DOCX, not MJ artwork.
Review rendered pages after running. Prompts and generation records live in MJ_ref.
"""
from pathlib import Path
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.oxml.ns import qn

ROOT = Path(__file__).resolve().parent.parent
doc = Document()
s = doc.sections[0]
s.page_width, s.page_height = Inches(8.5), Inches(11)
s.top_margin = s.bottom_margin = Inches(.7)
s.left_margin = s.right_margin = Inches(.85)
for name, size in [('Normal', 11), ('Title', 20), ('Heading 1', 15), ('Heading 2', 12)]:
    st = doc.styles[name]
    st.font.name = 'Microsoft YaHei'
    st.font.size = Pt(size)
    st.font.color.rgb = RGBColor(0, 0, 0)
    st.element.get_or_add_rPr().get_or_add_rFonts().set(qn('w:eastAsia'), 'Microsoft YaHei')
    st.paragraph_format.space_after = Pt(7)
    st.paragraph_format.line_spacing = 1.18
    if name != 'Normal':
        st.font.bold = True
        st.paragraph_format.keep_with_next = True
        st.paragraph_format.space_before = Pt(10)
    ppr = st.element.pPr
    if ppr is not None:
        border = ppr.find(qn('w:pBdr'))
        if border is not None:
            ppr.remove(border)

def p(text):
    return doc.add_paragraph(text)

def h(text):
    doc.add_heading(text, 2)

def image(path, width):
    doc.add_picture(str(ROOT / path), width=Inches(width))

foot = s.footer.paragraphs[0]
foot.text = 'The Fairy Hills  |  开场制作单 v1  |  2026 年 11 月 14 日'
foot.runs[0].font.size = Pt(9)

doc.add_paragraph('妖精丘陵开场故事画制作单', 'Title')
p('2026 年 11 月 14 日  ·  供负责人 学生 美术与后续 Agent 阅读')
p('菜单 Play 后先用三张故事画交代朋友被召唤、妮芙追赶的动机，再进入村庄操作。全段约 20 秒，可逐张前进或跳过。画面必须延续现有游戏的角色与黄昏风格。')
p('当前状态：分镜与 MJ 提示词已备；浏览器连接异常，尚未提交生成，没有故事画成品。以下图片均为既有参考图。')
doc.add_heading('OP01 黄昏里的两个人', 1)
pp = doc.add_paragraph()
pp.add_run().add_picture(str(ROOT/'MJ_ref/NIAMH_REF_v3.png'), width=Inches(2.05))
pp.add_run('     ')
pp.add_run().add_picture(str(ROOT/'MJ_ref/OISIN_REF_v3.png'), width=Inches(2.05))
p('角色参考　左为妮芙　右为奥伊芯　不是本镜头成片')
h('画面与故事')
p('村庄外的草坡，两人轻松追逐。妮芙在左，奥伊芯在右，人物约占画面高度三分之一；保持立绘的大头身比、各自的发色与衣装，面部和动作轮廓清楚。')
p('妮芙此时已把十字架交给奥伊芯，因此需要去掉参考立绘中妮芙的项链。若画出十字架，只能由奥伊芯携带，挂绳为红绿缠绳。')
h('播放与字幕草稿')
p('约 6 秒，缓慢推近约 2%。下方 18% 保留安静背景供 Unity 排字幕。')
p('At dusk, the hills were still a place to play.')

doc.add_page_break()
doc.add_heading('OP02 奥伊芯听见召唤', 1)
image('MJ_ref/S1_VILLAGE_KEY_03_pan_empty.png', 6.7)
p('环境与画风参考　现有村庄干净背景　不是本镜头成片')
h('画面与故事')
p('奥伊芯在左中停下，望向右侧远处的古墓丘陵。她听见妮芙听不见的声音，神情是好奇和失神。妮芙可不入画，保持视线关系清楚。')
p('古墓只显示远处的小暗口与微弱冷光，暗示门自行打开。暂不确定门体近景结构，避免与后续 S2 实机场景冲突。不出现女王、普卡或守门者。')
h('保持游戏画风')
p('沿用暖金天空、橄榄草地、蓝绿远丘与阴影。保留明显的深色不规则线条和简化的手绘色块，不把画面变成写实电影或柔淡无轮廓的水彩。')
p('奥伊芯仍是短卷红发、玫瑰雏菊花冠、玫红披肩和奶油色钟袖。先选定 OP01 的候选，再让本镜头延续同一风格。')
h('播放与字幕草稿')
p('约 7 秒，轻推向她的视线方向。音乐可减薄；低语属于后续音频制作，本轮还没有配音。')
p('Then Oisín heard something Niamh could not.')
h('参考输入')
p('使用奥伊芯 v3 与村庄环境图。OP01 选定后可作为连续性参考；实际上传的附件、模型设置和完整提示词必须记录到生成清单。')

doc.add_page_break()
doc.add_heading('OP03 她跑向树林', 1)
image('TechnicalArt/mock/FOREST_LIGHTING_TARGET_warm.jpg', 4.7)
p('冷暖方向参考　森林灯光目标图　不是本镜头成片')
h('画面与游戏衔接')
p('奥伊芯在右前方跑向村庄外的树影，妮芙从左后方追赶。两人都朝右，左侧保留村庄的暖光，右侧树影渐冷。仍在村庄外，不提前进入古墓或森林深处。')
p('约 6 秒后淡暗，接现有 S1 村庄出生点并交还操作。真正抵达古墓的镜头留到森林之后，避免画面已经进墓、游戏却又回到村庄。')
p('Oisín ran towards the trees. Niamh followed.')
h('出图顺序与交付')
p('先生成 OP01 一组并挑选，再生成 OP02 和 OP03。全图 16∶9，不生成文字；字幕和章节标题在 Unity 独立排版。首轮检查角色、圣物归属、轮廓、颜色和下方字幕区。')
p('候选保留原始文件与 job 链接；选中后才修订并输出 1920×1080 PNG。将 OP03 与村庄实机相邻播放，检查风格落差。未通过的图不标记定稿。')
h('制作资料与后续接手')
p('完整提示词及生成记录：MJ_ref/Slideshow/Opening_v1/。目前 jobs 为空，表示尚未生成；不要把本说明中的参考图当作可接入的故事画。')
p('详细接入与依据：TechnicalArt/SLIDESHOW_OPENING_v1.md。首批完成后再做森林至古墓、第二章入口与分支结尾；想象之眼的获得与再次使用仍由玩家实际操作展示。')

out = ROOT/'TechnicalArt/妖精丘陵_开场故事画制作单_v1.docx'
doc.save(out)
print(out)
