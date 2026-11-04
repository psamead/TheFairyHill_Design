const { makeDoc } = require('./lib'); const O = process.argv[2];
makeDoc(require('./doc_ta.js'), O + '/妖精丘陵_技术美术方案_手绘高清与骨骼动画.docx', ['nt','nr']);
