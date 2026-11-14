// Export only from a duplicate. Never rerun the original polygon split on user artwork.
app.displayDialogs=DialogModes.NO;
var root=File($.fileName).parent.parent;
var source=app.open(new File(root.fsName+'/Niamh_user_revision_source.psd'));
var d=source.duplicate('Niamh_user_export_temporary');
var names=['hair_back','body','arm','leg','boot','head'];
var opt=new ExportOptionsSaveForWeb();opt.format=SaveDocumentType.PNG;opt.PNG8=false;opt.transparency=true;
for(var i=0;i<names.length;i++){
 for(var j=0;j<d.layers.length;j++)d.layers[j].visible=false;
 d.layers.getByName(names[i]).visible=true;
 if(names[i]=='body'){
  d.activeLayer=d.layers.getByName('body');
  d.selection.select([[218,341],[248,341],[251,363],[263,385],[279,419],[274,436],[250,432],[235,408],[216,372]]);
  d.selection.feather(1);
  var cream=new SolidColor();cream.rgb.red=239;cream.rgb.green=227;cream.rgb.blue=209;
  d.selection.fill(cream);d.selection.deselect();
 }
 d.exportDocument(new File(root.fsName+'/parts/'+names[i]+'.png'),ExportType.SAVEFORWEB,opt);
}
for(var j=0;j<d.layers.length;j++)d.layers[j].visible=d.layers[j].name!='reference_original';
d.exportDocument(new File(root.fsName+'/previews/parts_without_reference.png'),ExportType.SAVEFORWEB,opt);
d.close(SaveOptions.DONOTSAVECHANGES);source.close(SaveOptions.DONOTSAVECHANGES);
'Exported user layers from duplicate; original remains untouched';
