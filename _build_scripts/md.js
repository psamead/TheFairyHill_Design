module.exports = function toMd(C, header) {
  const out = header ? [header, ''] : []; let n = 0;
  const ln = s => String(s).replace(/\[\[([^|\]]+)\|([^\]]+)\]\]/g, (m, l, u) => u.startsWith('#') ? l : `[${l}](${u})`);
  const esc = s => ln(s).replace(/\|/g, '\\|').replace(/\n/g, '<br>');
  for (const [t, a, b] of C) {
    if (t !== 'n') n = 0;
    if (t === 'title') out.push('# ' + a, '');
    else if (t === 'subtitle') out.push('> ' + a, '');
    else if (t === 'h1') out.push('', '## ' + a, '');
    else if (t === 'h2') out.push('', '### ' + a, '');
    else if (t === 'h3') out.push('', '#### ' + a, '');
    else if (t === 'p') out.push(ln(a), '');
    else if (t === 'note') out.push('> ' + ln(a), '');
    else if (t === 'b') out.push('- ' + ln(a));
    else if (t === 'n') out.push((++n) + '. ' + ln(b));
    else if (t === 'prompt') out.push('', '```text', a, '```', '');
    else if (t === 'table') out.push('', '| ' + a[0].map(esc).join(' | ') + ' |', '|' + a[0].map(() => '---').join('|') + '|', ...a.slice(1).map(r => '| ' + r.map(esc).join(' | ') + ' |'), '');
  }
  return out.join('\n').replace(/\n{3,}/g, '\n\n') + '\n';
};
