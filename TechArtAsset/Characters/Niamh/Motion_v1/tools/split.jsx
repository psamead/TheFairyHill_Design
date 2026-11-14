// Photoshop 2023: non-destructive source-derived puppet trial. Coordinates in source pixels.
app.displayDialogs=DialogModes.NO;
var oldUnits=app.preferences.rulerUnits; app.preferences.rulerUnits=Units.PIXELS;
var base=File($.fileName).parent.parent;
var d=app.open(new File(base.parent.fsName+'/Niamh_side_static_v3.png'));
var original=d.activeLayer; original.name='reference_original';
var shapes=[
['hair_back',[[28,155],[150,174],[192,226],[175,325],[155,414],[118,496],[70,508],[0,453],[0,274]]],
['body',[[145,211],[227,213],[274,263],[325,359],[325,542],[52,545],[10,518],[67,345],[108,251]]],
['arm',[[211,298],[242,310],[254,342],[247,361],[258,383],[274,418],[269,432],[253,425],[241,406],[222,371],[213,344],[199,328]]],
['leg',[[159,523],[228,523],[215,581],[161,590],[150,566]]],
['boot',[[151,572],[221,572],[225,698],[145,698],[146,604]]],
['head',[[26,160],[34,101],[70,48],[130,4],[227,0],[271,20],[300,63],[319,111],[321,156],[302,181],[298,204],[279,222],[240,232],[208,228],[181,217],[177,195],[145,193],[112,186],[72,180]]]
];
for(var i=0;i<shapes.length;i++){
 var l=original.duplicate();d.activeLayer=l;l.name=shapes[i][0];
 d.selection.select(shapes[i][1]);d.selection.invert();d.selection.clear();d.selection.deselect();
 // Repaint arm's original footprint before using the torso as a moving backdrop.
 if(l.name=='body'){
  d.selection.select([[218,341],[246,341],[248,362],[259,384],[275,418],[271,435],[251,430],[238,408],[220,372]]);
  var cream=new SolidColor();cream.rgb.red=239;cream.rgb.green=227;cream.rgb.blue=209;d.selection.fill(cream);
  d.selection.deselect();
 }
 for(var j=0;j<d.layers.length;j++)d.layers[j].visible=false;
 l.visible=true;
 var opt=new ExportOptionsSaveForWeb();opt.format=SaveDocumentType.PNG;opt.PNG8=false;opt.transparency=true;
 d.exportDocument(new File(base.fsName+'/parts/'+l.name+'.png'),ExportType.SAVEFORWEB,opt);
}
for(var j=0;j<d.layers.length;j++)d.layers[j].visible=true;
original.visible=false;
var psd=new PhotoshopSaveOptions();psd.layers=true;
d.saveAs(new File(base.fsName+'/Niamh_puppet_trial_v1.psd'),psd,true,Extension.LOWERCASE);
d.close(SaveOptions.DONOTSAVECHANGES);app.preferences.rulerUnits=oldUnits;
'Exported source-aligned parts and layered PSD';
