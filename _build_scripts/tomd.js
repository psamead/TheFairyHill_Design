const Module=require('module');const orig=Module.prototype.require;
let C;Module.prototype.require=function(p){if(p==='./lib')return{makeDoc:(c)=>{C=c}};return orig.apply(this,arguments)};
require('./doc3.js');
const out=[];let n=0;
const esc=s=>String(s).replace(/\|/g,'\\|').replace(/\n/g,'<br>');
for(const [t,a,b] of C){
 if(t==='title')out.push('# '+a,'');
 else if(t==='subtitle')out.push('> '+a,'');
 else if(t==='h1')out.push('## '+a,'');
 else if(t==='h2')out.push('### '+a,'');
 else if(t==='p'||t==='note')out.push(a,'');
 else if(t==='b')out.push('- '+a);
 else if(t==='table'){out.push('','| '+a[0].map(esc).join(' | ')+' |','|'+a[0].map(()=>'---').join('|')+'|',...a.slice(1).map(r=>'| '+r.map(esc).join(' | ')+' |'),'');}
}
require('fs').writeFileSync(process.argv[2],out.join('\n').replace(/\n{3,}/g,'\n\n'));
