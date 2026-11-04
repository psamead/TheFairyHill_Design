const { makeDoc } = require('./lib');
const I = (n) => __dirname + '/img/' + n + '.png';

// ============ 概念设计说明 _m ============
const D1 = require('./doc1.js').slice();
D1[2] = ['subtitle', '原作者：YiChun Jiang　|　整理版本 v1.1（含概念图进展）　|　2026-10'];
D1.push(
['h1', '7. 原设计参考图与概念图进展（v1.1 新增）'],
['p', '本章记录 v1.0 文档完成后，用 Midjourney 生成概念图的实际进展。参考图全部存放在 ShareWorkFolder\\MJ_ref\\。'],
['h2', '7.1 原作者设计图（总览）'],
['img', I('ORIGINAL_SHEET'), { w: 600, h: 320, cap: '原作者设计总图：两位女孩的设定、铁十字架、风景图与三张手绘关卡草图' }],
['h2', '7.2 从原图裁出的参考图（MJ_ref）'],
['imgrow', [[I('NIAMH_REF'), 'NIAMH_REF\n妮芙（原设计）'], [I('OISIN_REF'), 'OISIN_REF\n奥伊芯（原设计）'], [I('CROSS_REF'), 'CROSS_REF\n铁十字架（原设计）']], 190],
['imgrow', [[I('LANDSCAPE_REF'), 'LANDSCAPE_REF → S1'], [I('SKETCH_1'), 'SKETCH_1 → S2 古墓入口'], [I('SKETCH_2'), 'SKETCH_2 → S4 藤蔓门厅'], [I('SKETCH_3'), 'SKETCH_3 → S3 古墓石廊']], 110],
['h2', '7.3 妮芙 v2 概念图（当前定稿候选）'],
['img', I('Niamh_v2'), { w: 560, h: 380, cap: 'Niamh_v2：Niji 6 生成 + 编辑器局部重画头饰后的结果（正面 + 背面）' }],
['table', [
  ['设计说明要求', 'v2 结果', '状态'],
  ['家传旧银冠（刻纹，一颗绿石）', '凯尔特结纹银冠，中央绿色三叶草', '✔ 基本达成（三叶草代替绿石，可接受）'],
  ['短披风 + 兜帽', '及膝绿色兜帽斗篷', '◐ 有兜帽，但披风仍偏长'],
  ['胸前铁十字架', '有十字架，但为绿色玉石质感', '✘ 需改为暗铁色'],
  ['腰间小挎包', '棕色皮挎包', '✔'],
  ['裙摆到膝', '裙摆到膝', '✔'],
  ['绿色绑带短靴', '浅灰褐编织长靴', '✘ 颜色不符'],
  ['半边心形扣、红绿手绳', '未明显体现', '✘ 待补'],
  ['三视图（正/侧/背）', '只有正面和背面', '✘ 缺侧面'],
], [2.6, 2.6, 2.4]],
['h2', '7.4 从 v2 中裁出的新参考图'],
['imgrow', [[I('NIAMH_REF_v2'), 'NIAMH_REF_v2\n新版妮芙正面（后续 Character Reference 用这张）'], [I('CIRCLET_REF'), 'CIRCLET_REF\n家传银冠特写'], [I('CROSS_v2'), 'CROSS_v2\n胸前十字架（颜色待修正）']], 190],
['note', '两张特写放大自约 80–180 像素的小区域，清晰度有限，只适合作造型参考。正式道具设定图请用 Prompt 集 P01 / P05 单独生成高清版（特写图放 Image Prompts 格子）。'],
['h2', '7.5 下一步（概念图）'],
['n', 'nx', '修正十字架为暗铁色、靴子改绿色、补半边心形扣与手绳（编辑器逐处局部重画）。'],
['n', 'nx', '用编辑器扩展画布补侧面，完成三视图后替换 NIAMH_REF_v2。'],
['n', 'nx', '以同样流程生成奥伊芯 v2（C05），检查两人「剪影不同、饰物成对」。'],
['n', 'nx', '再进入动作表、表情表、道具、场景。'],
);


// ---- 神话出处：正文加内部链接 + 附录 ----
const REFS = require('./refs.js');
function linkify(text) {
  for (const r of REFS) for (const term of r.terms) {
    const segs = text.split(/(\[\[[^\]]+\]\])/g);
    let done = false;
    text = segs.map(sg => { if (done || sg.startsWith('[[')) return sg; const i = sg.indexOf(term); if (i < 0) return sg; done = true; return sg.slice(0, i) + '[[' + term + '|#' + r.id + ']]' + sg.slice(i + term.length); }).join('');
  }
  return text;
}
const appendixStart = D1.length;
for (let k = 0; k < D1.length; k++) {
  const it = D1[k];
  if (['p', 'b', 'note'].includes(it[0])) it[1] = linkify(it[1]);
  else if (it[0] === 'n') it[2] = linkify(it[2]);
  else if (it[0] === 'table') it[1] = it[1].map((row, ri) => ri === 0 ? row : row.map(c => linkify(c)));
}
const iDoc = D1.findIndex(x => x[0] === 'h2' && x[1].startsWith('0.2'));
D1.splice(iDoc, 0, ['note', '**v1.1 新增**：正文中蓝色下划线的神话名词可点击，跳转到文末「附录 A 神话出处与参考链接」，附录内再链接到外部资料。']);
D1.push(['h1', '附录 A　神话出处与参考链接']);
D1.push(['p', '以下为设计中引用的爱尔兰神话、民俗与考古出处。外部链接以维基百科、爱尔兰国家博物馆、大学与文化机构为主；民俗类资料多为二手整理，引用到正式文案前建议再核实。']);
for (const r of REFS) {
  D1.push(['h3bm', r.title, r.id]);
  D1.push(['p', '**游戏中的用途**：' + r.use]);
  for (const [label, url] of r.links) D1.push(['b', '[[' + label + '|' + url + ']]']);
}

// ============ Prompt 集 _m ============
const D2 = require('./doc2.js').slice();
D2[2] = ['subtitle', '原作者：YiChun Jiang　|　配套文档：《妖精丘陵》概念设计说明 v1.1　|　2026-10（v1.1 含实测修订）'];
const i02 = D2.findIndex(x => x[0] === 'h2' && x[1].startsWith('0.2'));
D2.splice(i02 + 1, 0, ['note', '**v1.1 实测修订**：在 Midjourney **网页版**不需要填 URL——把图片拖进 Character References / Image Prompts / Style reference 格子即可，同时把 prompt 里对应的 [XXX_REF] 占位符和 --cref 删掉。详见第 6 章。']);
D2.push(
['h1', '6. 实测记录与修订 Prompt（v1.1 新增）'],
['p', '本章记录用 Midjourney 网页版实际跑 C01（妮芙三视图）时遇到的问题、解决办法和修订后的 prompt，后续生成其他角色/道具时照此流程即可。'],
['h2', '6.1 网页版参考图格子对照'],
['table', [
  ['格子', '等同参数', '用于', '注意'],
  ['Character References', '--cref', '角色图（C 系列）', '仅 V6 / Niji 6 支持；配合 --cw'],
  ['Omni Reference（V7）', '--oref', 'V7 下的角色/物件', '用 --ow（默认 100，25–50 允许改衣服）'],
  ['Image Prompts', '图片放 prompt 开头', '草图构图、道具特写', '配合 --iw（草图 0.5–0.8）'],
  ['Style reference', '--sref', '统一画风', '选定满意图后长期使用'],
], [1.8, 1.6, 1.8, 2.8]],
['h2', '6.2 遇到的问题与解决'],
['table', [
  ['报错 / 现象', '原因', '解决'],
  ['Character Reference should be a URL: [NIAMH_REF]', 'prompt 中留着占位符', '删掉 --cref [NIAMH_REF]，图拖进格子即可'],
  ['Version 7 doesn\'t support --cw', '网页版设置里的版本是 V7，覆盖了 --niji 6', '设置里切到 Niji 6；或改用 Omni Reference + --ow'],
  ['衣服总回到原设计', '参考的是旧设计图，--cw 过高', '先用 --cw 40 生成；选出新造型后改用新图做参考，再调高到 70–100'],
  ['Active selection detected...', 'Smart Select 只选中，未处理选区', '点 Erase selection 挖空后再 Submit edit'],
  ['四周透明格子 / 图被裁切', '编辑器 Aspect ratio 与原图（3:2）不符，Scale 被改', '比例选回 3:2，Scale 调到图片正好铺满；或关闭编辑器重开'],
], [2.6, 2.6, 3]],
['h2', '6.3 C01 实测结果'],
['img', I('Niamh_v2'), { w: 520, h: 350, cap: '当前选定结果 Niamh_v2（ar 3:2, niji 6, cw 40, stylize 150，编辑器重画头饰）' }],
['p', '使用的参考图（Character References）：MJ_ref\\NIAMH_REF.png；首轮参数 --cw 40。'],
['h2', '6.4 修订 Prompt'],
['h3', 'C01-R 三视图（补侧面、强化饰物）'],
['p', '用法：Character References 放 NIAMH_REF_v2.png（不要再放旧图），设置 Niji 6。'],
['prompt', 'character turnaround sheet, three full body views evenly spaced: front view, side profile view, back view, same little Irish village girl explorer Niamh, very long wavy golden blonde hair with a small side braid, big grey-green eyes, thin old silver circlet with one green stone on her head, small hand-forged dark iron cross pendant clearly visible on her chest, short waist-length forest green cape with a hood, cream linen dress to the knees with Celtic knot hem and shamrock embroidery, small brown leather satchel at the hip, left half of a silver heart-shaped belt buckle, red and green braided friendship bracelet, green lace-up ankle boots, chibi anime style, 2.5 heads tall, soft watercolor cel shading, clean thin brown lineart, pastel storybook palette, plain white background --niji 6 --ar 16:9 --s 150 --cw 70'],
['h3', 'E 系列：编辑器局部重画（每次只改一处）'],
['p', '流程：Open Editor → Smart Select 选中部位 → Erase selection → 确认画布无多余透明区（比例 3:2）→ 替换 prompt → Submit edit。prompt 只描述角色本身，不写三视图和 --ar。'],
['p', '**E01 头饰（已完成）**'],
['prompt', 'chibi girl with very long wavy golden blonde hair, wearing a thin old silver circlet with one small green stone on her head, big grey-green eyes, chibi anime style, soft watercolor cel shading, clean thin brown lineart, pastel storybook palette --niji 6'],
['p', '**E02 十字架改为暗铁色**'],
['prompt', 'small hand-forged dull dark grey iron cross pendant on a cord hanging on her chest, rough hammered metal, wrapped with thin red and green thread, not green, not jade, chibi girl, chibi anime style, soft watercolor cel shading, clean thin brown lineart --niji 6'],
['p', '**E03 兜帽短披风**'],
['prompt', 'short waist-length forest green cape with a hood resting on her shoulders, Celtic knotwork border, chibi girl with long golden hair, chibi anime style, soft watercolor cel shading --niji 6'],
['p', '**E04 绿色绑带短靴**'],
['prompt', 'green lace-up ankle boots, chibi girl legs, chibi anime style, soft watercolor cel shading, clean thin brown lineart --niji 6'],
['p', '**E05 补侧面（扩展画布）**：Aspect ratio 改为 21:9，Scale 缩小让一侧留白，再提交：'],
['prompt', 'side profile view of the same chibi girl, full body, standing, long wavy golden blonde hair, short green hooded cape, cream dress, plain white background --niji 6'],
['h3', 'P05-R 家传银冠（以特写为参考）'],
['p', '用法：CIRCLET_REF.png 拖进 **Image Prompts**（不是 Character References），--iw 约 0.6。'],
['imgrow', [[I('CIRCLET_REF'), 'CIRCLET_REF'], [I('CROSS_v2'), 'CROSS_v2（仅造型参考，颜色错误）']], 170],
['prompt', 'game item concept, an old worn family heirloom silver circlet, thin band with Celtic knotwork engraving and ogham line carvings, one small green stone shaped like a shamrock at the center, slightly tarnished, front view and three-quarter view, painterly game prop illustration, plain parchment background --v 7 --ar 3:2 --s 200'],
['h3', 'P01-R 铁十字架（修正颜色）'],
['prompt', '[CROSS_REF] game item concept of a small hand-forged dull dark grey iron cross pendant made from two old horseshoe nails, hammer marks and light rust, NOT green, NOT jade, crossing bound with red and green wool thread, stamped shamrock on a small round iron center, hanging red and green braided tassel, humble handmade charm, painterly game prop illustration, plain parchment background --v 7 --ar 2:3 --iw 0.5 --s 200'],
['h2', '6.5 参考图文件清单（ShareWorkFolder\\MJ_ref）'],
['table', [
  ['文件', '来源', '用途 / 放入格子'],
  ['NIAMH_REF.png', '原设计总图裁切', 'C01 首轮 · Character References'],
  ['NIAMH_REF_v2.png', 'Niamh_v2 裁切', 'C01-R / C02 / C03 / C04 · Character References（--cw 70–100）'],
  ['Niamh_v2.png', 'MJ 生成 + 编辑', 'C01 当前结果（正/背）'],
  ['OISIN_REF.png', '原设计总图裁切', 'C05 / C06 · Character References（--cw 40 起）'],
  ['CROSS_REF.png', '原设计总图裁切', 'P01 · Image Prompts'],
  ['CROSS_v2.png', 'Niamh_v2 裁切', '造型参考（颜色需修正）'],
  ['CIRCLET_REF.png', 'Niamh_v2 裁切', 'P05 · Image Prompts'],
  ['LANDSCAPE_REF.png', '原设计总图裁切', 'S01 · Image Prompts（--iw 0.5）'],
  ['SKETCH_1/2/3.png', '原作者手绘草图', 'S02 / S04 / S03 · Image Prompts（--iw 0.5–0.8）'],
], [2, 2, 4]],
);


// ---- v1.2：奥伊芯 v2 ----
{
  const i75 = D1.findIndex(x => x[0] === 'h2' && x[1].startsWith('7.5'));
  D1.splice(i75, 0,
    ['h2', '7.5 奥伊芯 v2 概念图（v1.2 新增，当前定稿候选）'],
    ['img', I('Oisin_v2'), { w: 560, h: 330, cap: 'Oisin_v2：Niji 6，Character Reference = OISIN_REF，--cw 40，--no green cape, blonde hair，经一次 Vary (Subtle)' }],
    ['table', [
      ['设计说明要求', 'v2 结果', '状态'],
      ['主色玫瑰红 + 奶白，与妮芙拉开', '红色披肩 + 奶白长裙；背面红色为主、中间一条绿色', '✔'],
      ['短卷红发', '短卷红发', '✔'],
      ['花冠（第一阶段不宜过大）', '玫瑰 + 雏菊 + 三叶草小花冠', '✔ 适合第一阶段'],
      ['长袖 / 圆裙摆', '泡泡长袖、圆裙摆', '✔'],
      ['右半边心形扣', '中间视图腰间有银色心形扣（完整心形，非半边）', '◐ 有心形扣；「半边」在第四章合一时再表现'],
      ['红绿手绳', '腰带为红色编绳，手腕未见', '✘ 待补（可选）'],
      ['腰间旧铁钉', '未出现（其他候选图被画成钥匙或刀具）', '✘ 文字注明即可'],
      ['浅色绑带靴', '浅棕绑带短靴', '✔'],
      ['三视图', '3/4 正面 + 正面 + 背面，缺真正侧面', '✘ 待用扩展画布补'],
    ], [2.4, 3, 2.4]],
    ['imgrow', [[I('OISIN_REF_v2'), 'OISIN_REF_v2\n新版正面（带心形扣）'], [I('HEART_BUCKLE_REF'), 'HEART_BUCKLE_REF\n心形扣特写'], [I('OISIN_BACK_v2'), 'OISIN_BACK_v2\n背面']], 190],
    ['h3', '两人对照（视觉距离 + 饰物联系）'],
    ['imgrow', [[I('NIAMH_REF_v2'), '妮芙 v2：金发长直 · 绿斗篷 · 银冠 · 铁十字架'], [I('OISIN_REF_v2'), '奥伊芯 v2：红发短卷 · 红披肩 · 花冠 · 心形扣']], 230],
    ['p', '剪影与主色已明显区分；共同元素为凯尔特结纹裙边、三叶草纹样。两人的心形扣 / 十字架 / 手绳仍需在后续图中统一（妮芙尚缺心形扣，两人都缺手绳）。'],
  );
  const iNext = D1.findIndex(x => x[0] === 'h2' && x[1].startsWith('7.5 下一步'));
  D1[iNext] = ['h2', '7.6 下一步（概念图）'];
  D1.splice(iNext + 1, 4,
    ['n', 'nx', '妮芙：十字架改暗铁色、靴子改绿色、补左半边心形扣（编辑器逐处局部重画），补侧面。'],
    ['n', 'nx', '奥伊芯：补侧面；可选补红绿手绳。'],
    ['n', 'nx', '两人统一「半心扣」造型：以 HEART_BUCKLE_REF 为基准，做成可左右拼合的一对。'],
    ['n', 'nx', '奥伊芯同化三阶段（C06）：以 OISIN_REF_v2 为第一阶段。'],
    ['n', 'nx', '进入动作表、表情表、道具、场景。'],
  );
  D1[2] = ['subtitle', '原作者：YiChun Jiang　|　整理版本 v1.2（含概念图进展）　|　2026-10'];

  const i65 = D2.findIndex(x => x[0] === 'h2' && x[1].startsWith('6.5'));
  D2.splice(i65, 0,
    ['h2', '6.5 C05 奥伊芯实测（v1.2 新增）'],
    ['p', '**设置**：Version = Niji 6；Character References 只放 OISIN_REF.png；Style reference 留空（放原图会把绿披风配色带回来）；Aspect ratio 与 prompt 一致（16:9）。'],
    ['h3', 'C05-R 三视图（实际使用）'],
    ['prompt', 'character turnaround sheet, three full body views evenly spaced: front view, side profile view, back view, cheerful curious little Irish girl Oisin, short fluffy curly auburn red hair, big warm brown eyes, crown of red white and blush pink roses with wildflowers, cream dress with wide long bell sleeves and rounded fuller skirt, rose red shawl with Celtic knot trim and moss green lining, right half of a silver heart-shaped shamrock belt buckle, red and green braided friendship bracelet on left wrist, a few old iron nails tied at her waist with string, light tan lace-up cloth boots, chibi anime style, 2.5 heads tall, soft watercolor cel shading, clean thin brown lineart, pastel storybook palette, plain white background --niji 6 --ar 16:9 --s 150 --cw 40 --no green cape, blonde hair'],
    ['p', '**结果**：首轮四张主色均为玫瑰红，与妮芙拉开成功；选中一张后做 Vary (Subtle)，得到 Oisin_v2。'],
    ['img', I('Oisin_v2'), { w: 520, h: 300, cap: 'Oisin_v2（定稿候选）' }],
    ['h3', '经验'],
    ['b', '用 --no green cape 并且 Style reference 留空，才能把原设计的绿披风「甩掉」。'],
    ['b', 'iron nails 常被画成钥匙或刀具：改写为 three small bent rusty nails tied in a bundle with string，或干脆不在图中表现。'],
    ['b', '花冠在部分候选中过大——可留作同化第二阶段参考；第一阶段选花冠小的。'],
    ['b', '「右半边心形扣」通常被画成完整心形，可接受；半心造型改在道具设定图中单独画。'],
    ['h3', 'E06 奥伊芯补侧面（扩展画布）'],
    ['prompt', 'side profile view of the same chibi girl with short curly auburn red hair and small rose crown, full body, standing, rose red shawl, cream dress with long bell sleeves, light tan boots, plain white background --niji 6'],
    ['h3', 'P04-R 半心扣（以 HEART_BUCKLE_REF 为 Image Prompt）'],
    ['prompt', 'game item concept, a silver heart-shaped belt buckle with Celtic knot and shamrock engraving, split vertically into a left half and a right half with a zigzag edge, shown apart and then joined into one glowing heart, painterly game prop illustration, plain parchment background --v 7 --ar 3:2 --iw 0.5 --s 200'],
  );
  const iFiles = D2.findIndex(x => x[0] === 'h2' && x[1].startsWith('6.5 参考图文件清单'));
  D2[iFiles] = ['h2', '6.6 参考图文件清单（ShareWorkFolder\\MJ_ref）'];
  const tbl = D2[iFiles + 1];
  tbl[1].push(['Oisin_v2.png', 'MJ 生成（Vary Subtle）', 'C05 当前结果'], ['OISIN_REF_v2.png', 'Oisin_v2 裁切（中间正面）', 'C06 / 奥伊芯后续图 · Character References（--cw 70–100）'], ['OISIN_BACK_v2.png', 'Oisin_v2 裁切', '背面参考'], ['HEART_BUCKLE_REF.png', 'Oisin_v2 裁切', 'P04 · Image Prompts']);
}

// ---- 附录 B：图片资产总览（Word，给人看） ----
{
  const A = require('./assets.js');
  const gallery = (title) => {
    const out = [['h1', title], ['p', '所有设计用图、Midjourney 生成图与裁切参考图的总览，按「原设计 → 生成 → 裁切」的顺序排列。文件都在 ShareWorkFolder\\MJ_ref\\；机器可读版本见 MJ_ref\\ASSETS.md（供 Codex 读取和后续追踪）。'],
      ['table', [['文件', '类别 / 对象', '版本', '状态'], ...A.map(a => [a.file, a.cat + ' · ' + a.obj, a.ver, a.status])], [2.4, 2.2, 0.7, 2.9]]];
    for (const a of A) {
      out.push(['h3', a.file]);
      out.push(['img', I(a.img), { w: a.img.match(/SHEET|_v2$|LANDSCAPE|SKETCH/) && !a.img.includes('REF') ? 480 : 240, h: 260 }]);
      out.push(['table', [['项目', '内容'], ['类别 / 对象', a.cat + ' · ' + a.obj + '（' + a.ver + '）'], ['来源', a.src], ['生成 / 裁切方式', a.how], ['用途', a.use], ['状态', a.status]], [1.6, 6]]);
    }
    return out;
  };
  D1.push(...gallery('附录 B　图片资产总览'));
  D2.push(...gallery('7. 图片资产总览（v1.2 新增）'));
}

// ---- v1.3：关键场景与标题（与 美术方向 文档同源）----
{
  const { K } = require('./doc_art');
  D2.push(['h1', '8. 关键场景与标题 Prompt（v1.3 新增）'],
    ['p', '与《妖精丘陵_美术方向_关键场景标题字体.docx》第 4 章同源。用于海报、横幅、开始菜单背景动图和宣传短片。通用规则：用 --no text 让 Midjourney 不写字；为标题留白；两人同框时画成小剪影，需要清楚的角色就后期合成。'],
    ['h3', 'K1 主视觉（竖版海报）· 参考 SKETCH_1 或 LANDSCAPE_REF，--iw 0.4'], ['prompt', K.K1],
    ['h3', 'K1W 主视觉（横版）'], ['prompt', K.K1W],
    ['h3', 'K2 开始菜单背景板（无角色，分层）· 参考 LANDSCAPE_REF，--iw 0.5'], ['prompt', K.K2],
    ['h3', 'K3 藤蔓门厅 · 名字交易 · 参考 SKETCH_2，--iw 0.7'], ['prompt', K.K3],
    ['h3', 'K4 古墓石廊 · 参考 SKETCH_3，--iw 0.7'], ['prompt', K.K4],
    ['h3', 'KT-R 标题 Retexture（先用 Uncial Antiqua 排好 The Fairy Hills，上传后在编辑器中 Retexture）'], ['prompt', K.KTR],
    ['h3', 'KT 标题装饰框'], ['prompt', K.KT]);
}

// ---- 故事 v2 ----
{
  const STORY = require('./story.js')(true).map(it => { const x = it.slice(); if (['p','b','note'].includes(x[0])) x[1] = linkify(x[1]); return x; });
  const NOTE = (t) => ['note', '**故事 v2 更新**：' + t + '（详见第 8 章）'];
  const after = (pred, item) => { const i = D1.findIndex(pred); if (i < 0) throw new Error('nf'); D1.splice(i + 1, 0, item); };
  after(x => x[0] === 'h2' && x[1].startsWith('1.4'), NOTE('达南神族退居之后，还有一段「欧甘契约法典」的大背景：守门贵族 Ogma 与人类第一代媒介立约分隔两界，签约后在回去见女王的路上被普卡之首诱杀，契约在千年间慢慢失效。'));
  after(x => x[0] === 'h2' && x[1].startsWith('1.5'), NOTE('第四、五章与结局已改写：真正的大 Boss 是假扮守门贵族的普卡之首；真结局为「重订契约」。下表为 v1 版本'));
  after(x => x[0] === 'h3' && x[1].startsWith('守门贵族'), NOTE('玩家在第二章见到的守门贵族是普卡之首假扮的；原贵族 Ogma 是契约签署者，千年前已被杀害。「看不清脸」是伪装的破绽'));
  after(x => x[0] === 'h3' && x[1].startsWith('女妖'), NOTE('女妖为千年前被害的 Ogma 哀哭，安抚她后得知真正的贵族早已死去'));
  after(x => x[0] === 'h3' && x[1].startsWith('普卡'), NOTE('普卡群是普卡之首（真正的大 Boss）的爪牙和眼线，四处收集名字'));
  after(x => x[0] === 'h2' && x[1].startsWith('2.6'), NOTE('荆棘女王不再是最终 Boss：她的目标是两界互不侵犯；Ogma 没能回来禀告，所以她不知道契约细节；第四章仍有与她的 Boss 战，她从妮芙使用铁的方式（Ogma 亲传）认出真相而停手；真结局中她代替 Ogma 签约。最终 Boss 改为普卡之首'));
  const iA = D1.findIndex(x => x[0] === 'h1' && x[1].startsWith('附录 A'));
  D1.splice(iA, 0, ...STORY);
  D1[2] = ['subtitle', '原作者：YiChun Jiang　|　整理版本 v1.4（含故事 v2.1）　|　2026-10'];
}

Promise.all([
  makeDoc(D1, process.argv[2] + '/妖精丘陵_概念设计说明_m.docx', ['np', 'nq', 'nx', 'ns']),
  makeDoc(D2, process.argv[2] + '/妖精丘陵_Midjourney_Prompt集_m.docx', ['n1']),
]);
