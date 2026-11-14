"""Current five-page human reading edition, derived from project records.

No historical Word or user artwork is overwritten. Render all five pages before delivery.
"""
from pathlib import Path
from docx import Document
from docx.shared import Inches, Pt, RGBColor, Cm
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
ROOT=Path(__file__).resolve().parents[1]
doc=Document()
s=doc.sections[0]
s.page_width,s.page_height=Cm(21),Cm(29.7)
s.top_margin=s.bottom_margin=Cm(1.65)
s.left_margin=s.right_margin=Cm(1.9)
s.footer_distance=Cm(.8)
for name,size in [('Normal',11),('Title',23),('Subtitle',11),('Heading 1',17),('Heading 2',12.5),('Caption',9)]:
    st=doc.styles[name]
    st.font.name='Microsoft YaHei'
    st.font.size=Pt(size)
    st.font.color.rgb=RGBColor.from_string('253629' if 'Heading' in name or name=='Title' else '222722')
    fonts=st.element.get_or_add_rPr().get_or_add_rFonts()
    fonts.set(qn('w:eastAsia'),'Microsoft YaHei')
    st.paragraph_format.space_after=Pt(7)
    st.paragraph_format.line_spacing=1.16
    if st.element.pPr is not None:
        for border in list(st.element.pPr.findall(qn('w:pBdr'))):
            st.element.pPr.remove(border)
    if name.startswith('Heading') or name=='Title':
        st.font.bold=True
        st.paragraph_format.keep_with_next=True
        st.paragraph_format.space_before=Pt(10)
def p(t,style=None):return doc.add_paragraph(t,style)
def h(t):doc.add_heading(t,2)
def page(title):doc.add_page_break();doc.add_heading(title,1)
def pic(rel,width=6.65):
    pp=doc.add_paragraph()
    pp.paragraph_format.space_after=Pt(4)
    pp.add_run().add_picture(str(ROOT/rel),width=Inches(width))
    return pp
footer=s.footer.paragraphs[0]
footer.alignment=2
r=footer.add_run('The Fairy Hills · 2026.11.14 · ')
r.font.size=Pt(8)
field=OxmlElement('w:fldSimple');field.set(qn('w:instr'),'PAGE');footer._p.append(field)
doc.core_properties.title='妖精丘陵：开场故事画与章节过渡交接 v2'
doc.core_properties.subject='开场占位试装、MJ 实测经验、Unity 接手与后续动作计划'
doc.core_properties.author='The Fairy Hills 项目协作'

p('妖精丘陵', 'Title')
p('开场故事画与章节过渡交接  v2','Subtitle')
p('2026 年 11 月 14 日  ·  负责人、学生、制作与排版人员及后续 Agent', 'Caption')
h('目前采用：先用候选图验证游戏流程')
p('负责人已把原第 4 轮右下角（U4）的双人图放大，批准临时放进 Unity，加入开场故事引入和第一章封面。正式人物画风仍待改进；批准占位不等于美术定稿。')
pic('MJ_ref/Slideshow/Opening_v1/OP01_MJ_r04_U4_upscale_candidate_v1.png')
p('占位候选 OP01 · MJ 用户放大下载，2912×1632 · 本文件按版面缩放展示', 'Caption')
h('已经确认与仍需改善')
p('背景的金色天空、蓝绿色远山、草地层次，以及两人的神态较接近目标。人物仍偏 Q、外轮廓较强；妮芙的眼睛偏绿，后续需按灰眼参考校正。服装、手部和圣物连续性仍需终稿检查。')
p('试装流程：菜单 Play → 三个故事字幕节拍 → 第一章封面 → 现有村庄。后两个节拍复用同图，专门的召唤和追跑插图留待后续制作。')

page('01  判断画风：人物与环境分别对照')
pp=p('')
pp.add_run().add_picture(str(ROOT/'MJ_ref/NIAMH_REF_v3.png'),width=Inches(2.65))
pp.add_run('    ')
pp.add_run().add_picture(str(ROOT/'MJ_ref/OISIN_REF_v3.png'),width=Inches(2.65))
p('身份和笔触参考：左为妮芙 v3，右为奥伊芯 v3；两张均为既有角色参考。','Caption')
h('人物：保留原角色的柔和手绘处理')
p('妮芙为金发、灰眼、绿披风；奥伊芯为红发、琥珀眼、玫瑰雏菊花冠和红披肩。原立绘本身有适度大头，减少 Q 感不能直接变成写实成人或改变服装。轮廓应细而柔和，避免人物像贴在画面上的硬边贴纸。')
h('故事：圣物现在由谁保管')
p('开场前妮芙已将家传铁十字交给奥伊芯。奥伊芯被召唤、经过森林时，挂绳被受控荆棘扯断；妮芙追来后捡回。因此开场画不能给妮芙加上参考立绘中的十字项链。')
pic('MJ_ref/S1_VILLAGE_KEY_03_pan_empty.png')
p('环境基准：现有黄昏村庄干净背景；夜间菜单图只辅助判断环境线条与色块。','Caption')
h('当前文件与来源')
p('1456×816 单图和 2912×1632 放大图均按 OP01、r04、U4 命名，保留原下载名和 SHA-256。详情见 MJ_ref/Slideshow/Opening_v1/generation_manifest.json。游戏使用 placeholder 子目录中的原像素副本。')

page('02  本轮 MJ 经验：看结果，也保留边界')
h('1  上传成功与引用成功是两件事')
p('网页上传曾停在加载，负责人改用 Discord 上传并生成。提示词写“参考角色”不等于实际附上图；聊天里已有附件，也不能证明新任务自动引用。每轮保存真实请求、角色与风格参考用途。未核实的模型、种子或 job ID 明确留待核查。')
h('2  改比例时，人物身份容易一起改变')
p('强调更小头眼、更长四肢的一组明显偏离原角色。人物的年龄感、五官和衣服都变了；此结果不采用。可能与提示词重心、参考图和模型解释有关，本轮没有隔离根因。下一次每批只检验一个目标。')
h('3  微变没有弹出提示词编辑框')
p('负责人两次点击 Vary (Subtle) 后直接生成，未能追加“更细、更浅的暖棕色轮廓”。新图仍偏 Q、线条重。因此不能记成“新提示词已测试无效”，也不能继续保证点击一定出现编辑框。以后先验证可编辑入口，再生成。')
h('4  两人区域重绘：风格转向写实背影')
p('两人完整选区配新提示词，生成了写实感更强的背影，角色身份、比例与朝向偏离。这不是可用的原图线条修正。整人物遮罩允许大范围重建，文字“保留原姿势”未形成可靠约束。')
h('5  单人区域重绘：妮芙消失')
p('只选完整妮芙后，四个结果都将她替换为草地或花，原因未查清。此失败保留作参考，整人物重绘不作为稳定的修线方法。本轮先用最接近的候选做游戏试玩，Photoshop 修线尚未执行。')
h('过程可以追溯')
p('原四轮 WebP 拼图、后续选区/提示词/结果截图、两条实际输入的失败提示词都保留在 MJ_ref/Slideshow/Opening_v1/。截图仅为过程证据，不能直接作为游戏资产。可迁移经验统一收在 STORYBOARD_KNOWLEDGE_BASE.md。')

page('03  Unity 首版：故事引入与第一章封面')
h('开场三节拍，图片与文字分开配置')
p('OP01 · 约 6 秒：两位朋友在黄昏玩耍。')
p('At dusk, the hills were still a place to play.','Subtitle')
p('OP02 · 约 7 秒：奥伊芯听见妮芙听不见的召唤。')
p('Then Oisín heard something Niamh could not.','Subtitle')
p('OP03 · 约 6 秒：奥伊芯跑向树林，妮芙跟随。')
p('Oisín ran towards the trees. Niamh followed.','Subtitle')
p('本轮三节拍共用 OP01，仅由字幕传达后两个事件。正式 OP02/03 仍按原分镜补画；此时没有已完成的召唤、追跑专图。')
h('第一章封面，约 2 秒')
p('CHAPTER I  /  THE THRESHOLD','Subtitle')
p('标题沿用既有工作文案，可在配置中替换。临时背景沿用 OP01，在 Unity 叠加压暗和文字，不把字烘焙到图上。封面后进入现有村庄出生点。村庄到森林属于同章换场，不显示第二章标题。')
h('交互与排版验收')
p('支持 Next / Skip 和键盘前进；跳过故事仍经过第一章封面，再进入相同初始状态。切换期间锁输入，结束释放，避免按键穿透造成跳跃；重复点击只触发一次加载。保持图片比例，字幕和按钮不遮脸、不重叠。检查 1920×1080 与 1280×720。')
h('借鉴守灯人的实现经验')
p('借鉴数据驱动故事页、双图淡入、字幕独立定位与结束回调。检查推镜跳页无突跳、Time Scale 为 1、BGM 不重复、Core 和 AudioListener 不叠加。完成试玩后只留 MainMenu，便于下一次打开。')

page('04  接手、运行反馈与下一次工作')
h('另一台电脑上的制作任务')
p('素材、序列配置、散列清单及任务单通过共享网络预放进 Unity。制作端先检查工程已有输入，缺少才按精确路径向维护者索取，不默认从 GitHub 下载美术。共享源只复制、保持原件。')
p('本机可复制文件，但 SSH 连接超时，WinRM 受当前认证配置限制；应用列表没有可直接发送的远程 Codex 对话。因此任务包准备好不代表远程 Agent 已启动。派发结果以 unity_drop 的 dispatch_status.json 为准。')
h('需要 Unity 制作端交回什么')
p('正常播放、逐页前进、跳过、第一章封面和进入村庄的实际运行截图；小分辨率字幕/按钮截图；代码与配置位置、编译结果、已知问题和回退方法。动作声音任务先核对是否已做，未做则按已批准的任务单分批接入，另留听感检查记录。')
p('素材就绪、已复制、已派发、已接入、已编译、Play Mode 已观察、用户认可，分别记录。目前没有实机验收结果，提交或文档存在都不能代替运行证据。')
h('下次新对话先查反馈，再做动作')
p('从根目录 STORYBOARD_RESUME.md 开始，读取 Unity 的 Opening_Chapter1_Placeholder_Unity_Handoff.md 与 Niamh_Surface_Audio_Unity_Handoff.md，检查截图、提交和实际工程。反馈存在缺陷时先修。')
p('然后继续 Niamh：基于用户修订的 _m PSD、Motion_v8 六部件与现有 Unity 角色，先做栅门伸手/推门，再做举十字架与红障碍湮灭配合。先检查手型、肩部遮挡和真实交互时机，离线 GIF 审查后另写 Unity 接入任务。')
h('正式 Demo 的范围继续保留')
p('第一、二章 S1–S4 与结尾卡；想象之眼是 Must：获得后能切换现实与幻象，并在后续主线再次使用、推动人物互动。不要按旧动作表推迟至第三章。')
p('资料入口：本册为旧概念说明附录 B、Prompt 集第 7 章和开场 v1 制作单的当前补充。原件保留；来源、完整失败提示词、过程截图和资产路径按知识库继续追溯。','Caption')

out=ROOT/'TechnicalArt/妖精丘陵_开场故事画与章节过渡交接_v2.docx'
doc.save(out)
print(out)
