const { makeDoc } = require('./lib'); const fs = require('fs'); const toMd = require('./md');
const O = process.argv[2];
const MK = require('./doc_market'), PL = require('./doc_plan'), ART = require('./doc_art').C, IM = require('./doc_impl');
Promise.all([
  makeDoc(MK, O + '/妖精丘陵_市场定位玩家画像与可行性_v2.docx'),
  makeDoc(PL, O + '/妖精丘陵_前期方案_平台类型内容策略_v2.docx'),
  makeDoc(ART, O + '/妖精丘陵_美术方向_关键场景标题字体.docx', ['nt']),
  makeDoc(IM, O + '/妖精丘陵_Demo设计与开发实施说明.docx', ['nq']),
]);
fs.writeFileSync(O + '/DEMO_IMPLEMENTATION_PLAN.md', toMd(IM.filter(x => !['break', 'toc'].includes(x[0])), '<!-- 由 妖精丘陵_Demo设计与开发实施说明.docx 同源生成；更新时两者同步。清单项用 ☐ / ☑ 标记进度。 -->'));
fs.writeFileSync(O + '/ART_DIRECTION.md', toMd(ART.filter(x => !['break', 'toc'].includes(x[0])), '<!-- 由 妖精丘陵_美术方向_关键场景标题字体.docx 同源生成。 -->'));
