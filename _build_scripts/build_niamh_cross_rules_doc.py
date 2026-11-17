from pathlib import Path
from docx import Document
from docx.shared import Cm,Pt,RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.enum.text import WD_ALIGN_PARAGRAPH
from PIL import Image,ImageDraw
ROOT=Path(__file__).resolve().parent.parent
ASSET=ROOT/'TechArtAsset/Characters/Niamh/Cross_Actions'
OUT=ROOT/'TechnicalArt/妮芙十字架双动作使用规则与制作交接_v1.docx'
doc=Document();sec=doc.sections[0]
sec.page_width=Cm(21);sec.page_height=Cm(29.7)
sec.top_margin=sec.bottom_margin=Cm(2);sec.left_margin=sec.right_margin=Cm(2.1)
for name,size,color in [('Normal',10.5,'26352B'),('Title',23,'2F5D3A'),('Heading 1',16,'2F5D3A'),('Heading 2',13,'3E7B4E'),('Caption',9,'657169')]:
 s=doc.styles[name];s.font.name='Microsoft YaHei';s.font.size=Pt(size);s.font.color.rgb=RGBColor.from_string(color)
 rf=s.element.get_or_add_rPr().get_or_add_rFonts()
 for a in ['ascii','hAnsi','eastAsia','cs']:rf.set(qn('w:'+a),'Microsoft YaHei')
 for a in ['asciiTheme','hAnsiTheme','eastAsiaTheme','cstheme']:rf.attrib.pop(qn('w:'+a),None)
 s.paragraph_format.space_after=Pt(6)
 s.paragraph_format.line_spacing=Pt(17)
 if name not in ['Normal','Caption']:s.font.bold=True
for s in doc.styles:
 for border in list(s.element.iter(qn('w:pBdr'))):border.getparent().remove(border)
def para(t,style=None):return doc.add_paragraph(t,style)
def table(headers,rows,widths):
 t=doc.add_table(rows=1,cols=len(headers));t.autofit=False
 for c,h,w in zip(t.rows[0].cells,headers,widths):c.text=h;c.width=Cm(w)
 rep=OxmlElement('w:tblHeader');t.rows[0]._tr.get_or_add_trPr().append(rep)
 for row in rows:
  cells=t.add_row().cells
  for c,v,w in zip(cells,row,widths):c.text=v;c.width=Cm(w)
 for i,row in enumerate(t.rows):
  trpr=row._tr.get_or_add_trPr();trpr.append(OxmlElement('w:cantSplit'))
  for c in row.cells:
   pr=c._tc.get_or_add_tcPr();sh=OxmlElement('w:shd');sh.set(qn('w:fill'),'2F5D3A' if i==0 else ('FFFFFF' if i%2 else 'EFF3EE'));pr.append(sh)
   borders=OxmlElement('w:tcBorders')
   for e in ['top','left','bottom','right']:
    z=OxmlElement('w:'+e);z.set(qn('w:val'),'single');z.set(qn('w:sz'),'4');z.set(qn('w:color'),'8C9B8D');borders.append(z)
   pr.append(borders);m=OxmlElement('w:tcMar')
   for e in ['top','bottom','left','right']:
    z=OxmlElement('w:'+e);z.set(qn('w:w'),'80');z.set(qn('w:type'),'dxa');m.append(z)
   pr.append(m)
   for p in c.paragraphs:
    p.paragraph_format.line_spacing=Pt(16);p.paragraph_format.space_after=Pt(2)
    for r in p.runs:
     r.font.size=Pt(10)
     if i==0:r.bold=True;r.font.color.rgb=RGBColor(255,255,255)
 return t
title=para('妮芙十字架双动作使用规则','Title');title.alignment=WD_ALIGN_PARAGRAPH.CENTER
p=para('制作交接 v1  |  2026年11月17日  |  负责人、美术、设计与开发协作者');p.alignment=WD_ALIGN_PARAGRAPH.CENTER
para('本次确定采用两个用户绘制的动作，不再制作第三个动作。第一个服务关卡内的局部事件，第二个服务剧情触发的大范围释放。两张静帧已整理图层、统一画幅和前襟花纹，连续动画、光束特效及游戏接入仍需后续制作与验收。')
para('1. 两个动作的使用范围','Heading 1')
table(['动作','适用场景','表现原则'],[
 ['01 胸前局部使用','关卡内对付小怪、小障碍物及小剧情互动。','用胸前持十字架姿势表达局部使用；攻击、驱散或互动的具体判定另按场景设计。'],
 ['02 举起剧情释放','剧情触发的大光线、湮灭大型障碍物等关键事件。','由剧情事件组织举起、光束与目标反馈；不默认为随时可用的普通大范围攻击。']],[3,6.4,7.4])
# Both drawings use the same origin and scale in this comparison.
panel=Image.new('RGB',(740,740),'#263141')
for x,n in [(15,'chest_local'),(375,'raised_story')]:
 im=Image.open(ASSET/'current'/f'Niamh_cross_{n}_v1.png').convert('RGBA');panel.paste(im,(x,18),im)
panelpath=ASSET/'evidence/two_action_comparison.png';panel.save(panelpath)
p=doc.add_paragraph();p.alignment=WD_ALIGN_PARAGRAPH.CENTER;p.paragraph_format.line_spacing=1;p.paragraph_format.keep_with_next=True;p.add_run().add_picture(str(panelpath),width=Cm(12.1))
p=para('左：胸前局部使用。右：举起剧情释放。均为用户修订静帧；图中尚无大光线特效。','Caption');p.alignment=WD_ALIGN_PARAGRAPH.CENTER
doc.add_page_break()
para('2. 设计与制作原则','Heading 1')
para('按事件规模选择动作，而不是将两张图视为三个高度阶段中尚缺一张。不再安排第三个独立动作。后续是否需要插值、局部补画或过渡帧，应由这两稿的运动测试决定。不得从静帧自行推导伤害、射程、冷却、消耗、操作按键或解锁规则。')
para('这次登记的是动作的使用范围，不自动将完整战斗系统加入当前 Demo 制作范围。剧情光束的具体触发事件、目标清单和时序，留给对应场景的独立实施任务。')
table(['环节','操作与检查要求'],[
 ['参考与剪贴','先生成完整人物参考，再取需要的手臂和袖口，接回原人物。保留脸、头发、披风、领口、系带与纹样，检查朝向和两条肩肘腕连接。'],
 ['用户手绘衔接','剪贴与补画分层保存。沿原画高光、阴影、褶皱和外轮廓衔接；羽化不能代替衣装结构补画。'],
 ['现有游戏道具','使用游戏十字架素材，调整大小与方向，再用蒙版或栅格副本裁切握柄遮挡；智能对象保留备用。'],
 ['图层与画幅','当前动作、原人物、隐藏参考备用分别分组。统一 350×699，左上原点不变；人物未缩放或平移，脚底基线保持一致。'],
 ['预览与交付','分别确认静帧、连续运动、特效及游戏运行。旧粗 GIF 早于第二稿，有姿势跳变，不能作为当前两个动作的验收依据。']],[3.3,13.5])
para('3. 当前文件与状态','Heading 1')
para('当前资产根目录：TechArtAsset/Characters/Niamh/Cross_Actions/。PSD 文件名按用途命名，不再使用胸前文件名表示第二个举起动作。')
table(['分类','位置与内容'],[
 ['当前稿 current','Niamh_cross_chest_local_v1.psd 与 Niamh_cross_raised_story_v1.psd；各有同名透明 PNG。'],
 ['用户源稿 sources/user','保留胸前稿、举起稿及早期袖口衔接稿，按用途重命名；源文件内容和原始画布保留。'],
 ['历史与追踪','archive 保存旧 PSD 试验和粗 GIF；file_manifest.json 记录原路径、新路径、源稿 SHA256 和像素校验。']],[3.3,13.5])
para('第一稿由 327×699 右侧补透明区至 350×699；第二稿由 450×699 裁去右侧 100 像素全透明留白。图层及裁切通过像素核查；前襟新增花纹已从举起稿同步到胸前稿与基础角色，像素变化局限于补片，轮廓透明度保持。Unity 身体与静态备用 PNG 已复制更新，运行画面待检查。白边未确认完全消除。')
para('Agent 入口：STORYBOARD_RESUME.md → Cross_Actions/README.md → TechnicalArt/NIAMH_ANIM_LIST_DEMO.md。制作方法详见 TechnicalArt/LESSONS_CHARACTER_ANIMATION.md，机器可读规则见资产目录 action_usage_rules.json。')
footer=sec.footer.paragraphs[0];footer.alignment=WD_ALIGN_PARAGRAPH.RIGHT
fld=OxmlElement('w:fldSimple');fld.set(qn('w:instr'),'PAGE');footer._p.append(fld)
doc.save(OUT);print(OUT)
