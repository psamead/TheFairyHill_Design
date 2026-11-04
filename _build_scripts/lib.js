const fs = require('fs');
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, Table, TableRow, TableCell,
  WidthType, ShadingType, BorderStyle, AlignmentType, LevelFormat, PageBreak,
  Footer, PageNumber, TableOfContents, ImageRun, InternalHyperlink, ExternalHyperlink, Bookmark
} = require('docx');
const sizeOf = (p) => { const b = fs.readFileSync(p); return { w: b.readUInt32BE(16), h: b.readUInt32BE(20), b }; };
function img(p, maxW, maxH) { const { w, h, b } = sizeOf(p); let k = Math.min(maxW / w, (maxH || 99999) / h); return new ImageRun({ type: 'png', data: b, transformation: { width: Math.round(w * k), height: Math.round(h * k) } }); }

const CN = 'Microsoft YaHei';
const MONO = 'Consolas';
const GREEN = '2F5D3A';
const W = 9026; // A4 content width with 1" margins (11906-2*1440)

function runs(text, opts = {}) {
  // supports **bold** inline
  const parts = String(text).split(/(\*\*[^*]+\*\*|\[\[[^\]]+\]\])/g).filter(Boolean);
  return parts.map(p => {
    if (p.startsWith('[[')) {
      const [label, target] = p.slice(2, -2).split('|');
      const r = new TextRun({ text: label, style: 'Hyperlink', color: '1F5FA8', underline: {}, size: opts.size });
      return target.startsWith('#') ? new InternalHyperlink({ anchor: target.slice(1), children: [r] }) : new ExternalHyperlink({ link: target, children: [r] });
    }
    const b = p.startsWith('**') && p.endsWith('**');
    return new TextRun({
      text: b ? p.slice(2, -2) : p,
      bold: b || opts.bold,
      color: opts.color,
      size: opts.size,
      italics: opts.italics,
      font: opts.font ? { ascii: opts.font, hAnsi: opts.font, eastAsia: CN } : undefined,
    });
  });
}

function cell(text, width, header, shade) {
  const lines = Array.isArray(text) ? text : String(text).split('\n');
  return new TableCell({
    width: { size: width, type: WidthType.DXA },
    shading: header ? { type: ShadingType.CLEAR, fill: GREEN, color: 'auto' }
      : shade ? { type: ShadingType.CLEAR, fill: 'F1F5EF', color: 'auto' } : undefined,
    margins: { top: 60, bottom: 60, left: 100, right: 100 },
    children: lines.map(l => new Paragraph({
      spacing: { after: 40, line: 276 },
      children: runs(l, { size: 18, bold: header, color: header ? 'FFFFFF' : undefined }),
    })),
  });
}

function table(rows, ratios) {
  const n = rows[0].length;
  ratios = ratios || Array(n).fill(1);
  const tot = ratios.reduce((a, b) => a + b, 0);
  const widths = ratios.map(r => Math.floor(W * r / tot));
  widths[n - 1] += W - widths.reduce((a, b) => a + b, 0);
  return new Table({
    width: { size: W, type: WidthType.DXA },
    columnWidths: widths,
    rows: rows.map((r, i) => new TableRow({
      tableHeader: i === 0,
      children: r.map((c, j) => cell(c, widths[j], i === 0, i > 0 && i % 2 === 0)),
    })),
  });
}

function build(items) {
  const out = [];
  for (const it of items) {
    const [t, a, b] = it;
    if (t === 'title') out.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 1800, after: 300 }, children: runs(a, { size: 48, bold: true, color: GREEN }) }));
    else if (t === 'subtitle') out.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 160 }, children: runs(a, { size: 24, color: '555555' }) }));
    else if (t === 'h1') out.push(new Paragraph({ heading: HeadingLevel.HEADING_1, pageBreakBefore: b !== false, children: runs(a) }));
    else if (t === 'h2') out.push(new Paragraph({ heading: HeadingLevel.HEADING_2, children: runs(a) }));
    else if (t === 'h3bm') out.push(new Paragraph({ heading: HeadingLevel.HEADING_3, children: [new Bookmark({ id: b, children: [new TextRun(a)] })] }));
    else if (t === 'h3') out.push(new Paragraph({ heading: HeadingLevel.HEADING_3, children: runs(a) }));
    else if (t === 'p') out.push(new Paragraph({ spacing: { after: 120, line: 320 }, children: runs(a) }));
    else if (t === 'note') out.push(new Paragraph({ spacing: { after: 120, line: 300 }, shading: { type: ShadingType.CLEAR, fill: 'FFF6E0', color: 'auto' }, border: { left: { style: BorderStyle.SINGLE, size: 18, color: 'D9A23A', space: 6 } }, children: runs(a, { size: 20 }) }));
    else if (t === 'b') out.push(new Paragraph({ numbering: { reference: 'bul', level: b || 0 }, spacing: { after: 60, line: 300 }, children: runs(a) }));
    else if (t === 'n') out.push(new Paragraph({ numbering: { reference: a, level: 0 }, spacing: { after: 60, line: 300 }, children: runs(b) }));
    else if (t === 'table') { out.push(table(a, b)); out.push(new Paragraph({ spacing: { after: 120 }, children: [] })); }
    else if (t === 'prompt') out.push(new Paragraph({
      spacing: { before: 60, after: 160, line: 276 },
      shading: { type: ShadingType.CLEAR, fill: 'F3F3F3', color: 'auto' },
      border: { left: { style: BorderStyle.SINGLE, size: 18, color: GREEN, space: 6 } },
      children: runs(a, { font: MONO, size: 18 }),
    }));
    else if (t === 'img') { out.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 120 }, children: [img(a, b.w || 560, b.h || 420)] })); if (b.cap) out.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 200 }, children: runs(b.cap, { size: 18, color: '666666' }) })); }
    else if (t === 'imgrow') {
      const n = a.length; const cw = Math.floor(W / n);
      out.push(new Table({ width: { size: W, type: WidthType.DXA }, columnWidths: Array(n).fill(cw), borders: { top: { style: BorderStyle.NONE }, bottom: { style: BorderStyle.NONE }, left: { style: BorderStyle.NONE }, right: { style: BorderStyle.NONE }, insideHorizontal: { style: BorderStyle.NONE }, insideVertical: { style: BorderStyle.NONE } },
        rows: [new TableRow({ children: a.map(([p, cap]) => new TableCell({ width: { size: cw, type: WidthType.DXA }, children: [
          new Paragraph({ alignment: AlignmentType.CENTER, children: [img(p, Math.floor(600 / n) - 10, b || 200)] }),
          ...cap.split('\n').map(l => new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 60 }, children: runs(l, { size: 16, color: '666666' }) }))] })) })] }));
      out.push(new Paragraph({ spacing: { after: 120 }, children: [] }));
    }
    else if (t === 'toc') out.push(new TableOfContents('目录', { hyperlink: true, headingStyleRange: '1-2' }));
    else if (t === 'break') out.push(new Paragraph({ children: [new PageBreak()] }));
    else throw new Error('unknown ' + t);
  }
  return out;
}

function makeDoc(items, file, numberedRefs = []) {
  const numCfg = [{ reference: 'bul', levels: [
    { level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 420, hanging: 260 } } } },
    { level: 1, format: LevelFormat.BULLET, text: '–', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 840, hanging: 260 } } } },
  ] }];
  for (const r of numberedRefs) numCfg.push({ reference: r, levels: [{ level: 0, format: LevelFormat.DECIMAL, text: '%1.', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 420, hanging: 300 } } } }] });
  const doc = new Document({
    features: { updateFields: true },
    styles: {
      default: { document: { run: { font: { ascii: 'Calibri', hAnsi: 'Calibri', eastAsia: CN }, size: 21 } } },
      paragraphStyles: [
        { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { size: 34, bold: true, color: GREEN, font: { ascii: 'Calibri', eastAsia: CN } }, paragraph: { spacing: { before: 240, after: 200 }, outlineLevel: 0, border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: GREEN, space: 4 } } } },
        { id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { size: 27, bold: true, color: '3E7B4E', font: { ascii: 'Calibri', eastAsia: CN } }, paragraph: { spacing: { before: 280, after: 140 }, outlineLevel: 1 } },
        { id: 'Heading3', name: 'Heading 3', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { size: 23, bold: true, color: '7A5A1E', font: { ascii: 'Calibri', eastAsia: CN } }, paragraph: { spacing: { before: 200, after: 100 }, outlineLevel: 2 } },
      ],
    },
    numbering: { config: numCfg },
    sections: [{
      properties: { page: { size: { width: 11906, height: 16838 }, margin: { top: 1440, bottom: 1440, left: 1440, right: 1440 } } },
      footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ children: [PageNumber.CURRENT], size: 18, color: '888888' })] })] }) },
      children: build(items),
    }],
  });
  return Packer.toBuffer(doc).then(buf => { fs.writeFileSync(file, buf); console.log('wrote', file); });
}

module.exports = { makeDoc };
