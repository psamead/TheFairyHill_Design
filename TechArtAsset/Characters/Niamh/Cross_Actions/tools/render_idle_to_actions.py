"""Two idle-to-pose studies. Preserve the existing hold loops and source PSDs."""
from pathlib import Path
from math import sin,cos,pi,atan2,hypot
import json,subprocess,hashlib
import numpy as np
from PIL import Image,ImageDraw,ImageChops
ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'previews/idle_to_actions_v1';CACHE=OUT/'_qa'
CACHE.mkdir(parents=True,exist_ok=True)
CLI=r'C:\photocraft-0.5.0\photocraft-cli.exe'
W,H=420,699  # Working margin for the prop's arc; source PSDs stay 350 x 699.
def info(p):return json.loads(subprocess.run([CLI,'info',str(p),'--compact'],capture_output=True,text=True,check=True).stdout)
def nodes(ls):
 for l in ls:
  yield l
  yield from nodes(l.get('children',[]))
def export(p,steps,name):
 args=[CLI,'run',str(p)]
 for c,q in steps:args+=['--cmd',c,'--params',json.dumps(q)]
 dest=CACHE/(name+'.png');args+=['--out',str(dest)]
 subprocess.run(args,capture_output=True,text=True,check=True)
 image=Image.open(dest).convert('RGBA');out=blank();out.alpha_composite(image);return out
def smooth(t):
 t=max(0.,min(1.,t));return t*t*(3-2*t)
def blank():return Image.new('RGBA',(W,H))
def compose(*ims):
 out=blank()
 for im in ims:out.alpha_composite(im)
 return out
def bone(p,a,b,c,d):
 # Map the segment a-b onto c-d; p can be an N x 2 array.
 v=b-a;z=d-c;den=float(v@v)
 mat=np.array([[z[0]*v[0]+z[1]*v[1],z[0]*v[1]-z[1]*v[0]],
               [z[1]*v[0]-z[0]*v[1],z[0]*v[0]+z[1]*v[1]]])/den
 return (p-a)@mat.T+c
def skin(points,src,dst):
 a,e,w=src;da,de,dw=dst;v=w-e
 blend=np.clip(((points-e)@v)/(v@v)*1.4+.25,0,1)
 blend=blend*blend*(3-2*blend)
 p1=bone(points,a,e,da,de);p2=bone(points,e,w,de,dw)
 return p1*(1-blend[:,None])+p2*blend[:,None]
def warped(art,src,dst):
 if np.max(np.abs(src-dst))<1e-6:return art.copy()
 box=art.getbbox()
 if box is None:return blank()
 x0,y0,x1,y1=box
 xs=np.linspace(max(0,x0-2),min(W,x1+2),10)
 ys=np.linspace(max(0,y0-2),min(H,y1+2),18)
 sp=np.array([(x,y) for y in ys for x in xs]);dp=skin(sp,src,dst)
 inp=np.asarray(art,dtype=np.float32)/255.;inp[:,:,:3]*=inp[:,:,3:4]
 out=np.zeros((H,W,4),dtype=np.float32)
 def tri(ids):
  s=sp[list(ids)];q=dp[list(ids)];lo=np.floor(q.min(axis=0)).astype(int);hi=np.ceil(q.max(axis=0)).astype(int)
  lx,ly=np.maximum(lo,[0,0]);hx,hy=np.minimum(hi,[W-1,H-1])
  if hx<lx or hy<ly:return
  m=np.column_stack((q[1]-q[0],q[2]-q[0]))
  if abs(np.linalg.det(m))<1e-7:return
  yy,xx=np.mgrid[ly:hy+1,lx:hx+1];xy=np.stack((xx,yy),axis=-1)
  uv=(xy-q[0])@np.linalg.inv(m).T
  mask=(uv[:,:,0]>=-1e-5)&(uv[:,:,1]>=-1e-5)&(uv.sum(axis=2)<=1.00001)
  syx=s[0]+uv[:,:,0:1]*(s[1]-s[0])+uv[:,:,1:2]*(s[2]-s[0])
  sx=np.clip(syx[:,:,0],0,W-1);sy=np.clip(syx[:,:,1],0,H-1)
  ix=np.floor(sx).astype(int);iy=np.floor(sy).astype(int);jx=np.minimum(ix+1,W-1);jy=np.minimum(iy+1,H-1)
  fx=(sx-ix)[:,:,None];fy=(sy-iy)[:,:,None]
  val=(inp[iy,ix]*(1-fx)+inp[iy,jx]*fx)*(1-fy)+(inp[jy,ix]*(1-fx)+inp[jy,jx]*fx)*fy
  region=out[ly:hy+1,lx:hx+1];region[mask]=val[mask]
 for j in range(len(ys)-1):
  for i in range(len(xs)-1):
   a=j*len(xs)+i;b=a+1;c=a+len(xs);d=c+1
   tri((a,b,d));tri((a,d,c))
 alpha=out[:,:,3:4];out[:,:,:3]=np.divide(out[:,:,:3],alpha,out=np.zeros_like(out[:,:,:3]),where=alpha>1e-7)
 return Image.fromarray(np.clip(np.rint(out*255),0,255).astype(np.uint8))
def cross_move(art,source_grip,target_grip,angle):
 # Keep prop size rigid, independent of arm-length interpolation.
 im=art.rotate(angle,Image.Resampling.BICUBIC,center=tuple(source_grip))
 out=blank();out.alpha_composite(im,(round(target_grip[0]-source_grip[0]),round(target_grip[1]-source_grip[1])));return out
def opacity(im,v):
 im=im.copy();im.putalpha(im.getchannel('A').point(lambda a:round(a*v)));return im

chestpsd=ROOT/'current/Niamh_cross_chest_local_v1.psd'
ids={l['name']:l['id'] for l in nodes(info(chestpsd)['layers'])}
idlebase=export(chestpsd,[('layer.setProps',{'layer':ids['01_CHEST_LOCAL_current'],'visible':False})],'idle_base')
idlearm=blank();idlearm.alpha_composite(Image.open(ROOT.parent/'Motion_v8/parts/arm.png').convert('RGBA'))
idle=compose(idlebase,idlearm)
records=[]
for kind in ['chest_local','raised_story']:
 psd=ROOT/'current'/f'Niamh_cross_{kind}_v1.psd'
 meta=info(psd);ids={l['name']:l['id'] for l in nodes(meta['layers'])}
 propname='cross_chest_user_cut' if kind=='chest_local' else 'cross_raised_user_cut'
 cross=export(psd,[('layer.showOnly',{'layer':ids[propname]})],kind+'_cross')
 if kind=='chest_local':
  base=idlebase;foreground=blank()
  arm=export(psd,[('layer.showOnly',{'layer':ids['01_CHEST_LOCAL_current']}),('layer.setProps',{'layer':ids[propname],'visible':False})],kind+'_arm')
  rest=np.array([[224.,270.],[237.,340.],[258.,403.]])
  target=np.array([[230.,270.],[245.,320.],[282.,262.]])
  duration=4.;raise_end=1.45;hold_end=2.65;return_end=3.55
 else:
  hide=['cross_raised_user_cut','raised_arm_sleeve_user_cutout','front_costume_user_paint','cape_transition_user_paint']
  base=export(psd,[('layer.setProps',{'layer':ids[n],'visible':False}) for n in hide],kind+'_base')
  foreground=export(psd,[('layer.showOnly',{'layer':ids['cape_transition_user_paint']}),('layer.setProps',{'layer':ids['front_costume_user_paint'],'visible':True})],kind+'_foreground')
  arm=export(psd,[('layer.showOnly',{'layer':ids['raised_arm_sleeve_user_cutout']})],kind+'_arm')
  rest=np.array([[224.,270.],[237.,310.],[258.,403.]])
  target=np.array([[267.,260.],[307.,220.],[309.,103.]])
  duration=4.5;raise_end=1.8;hold_end=2.75;return_end=3.8
 full=export(psd,[],kind+'_full')
 # Preserve the user's exact finished artwork at the held endpoint.
 recomposed=compose(base,arm,foreground,cross)
 diff=ImageChops.difference(full,recomposed)
 if any(ext!=(0,0) for ext in diff.getextrema()):
  # Tiny overlaps from original layer ordering are restored at full extension.
  endpoint_correction=True
 else:endpoint_correction=False
 frames=[];characters=[];phases=[];FPS=20
 for i in range(round(duration*FPS)):
  t=i/FPS
  if t<.55:u=0.;label='IDLE'
  elif t<raise_end:u=smooth((t-.55)/(raise_end-.55));label='BEND TO CHEST' if kind=='chest_local' else 'LIFT ARM HIGH'
  elif t<hold_end:u=1.;label='HOLD'
  elif t<return_end:u=1-smooth((t-hold_end)/(return_end-hold_end));label='RETURN'
  else:u=0.;label='IDLE'
  dst=rest*(1-u)+target*u
  arc=sin(pi*u)
  dst[1,0]+=arc*(13 if kind=='chest_local' else 22)
  dst[2,0]+=arc*(27 if kind=='chest_local' else 35)
  if u<1e-6:char=idle.copy()
  elif u>1-1e-6:char=full.copy()
  else:
   old=warped(idlearm,rest,dst)
   new=warped(arm,target,dst)
   blend=smooth(u/.18)
   moving=Image.blend(old,new,blend)
   body=Image.blend(idlebase,base,smooth(u))
   char=compose(body,moving,opacity(foreground,smooth(u)))
   vs=target[2]-target[1];vd=dst[2]-dst[1]
   angle=-(atan2(vd[1],vd[0])-atan2(vs[1],vs[0]))*180/pi
   grip=target[2]+np.array([0.,-22.])
   moving_grip=skin(grip[None,:],target,dst)[0]
   prop=cross_move(cross,grip,moving_grip,angle)
   char.alpha_composite(opacity(prop,smooth(u/.18)))
   if endpoint_correction and u>.9:char=Image.blend(char,full,smooth((u-.9)/.1))
  frame=Image.new('RGB',(500,820),'#263141');d=ImageDraw.Draw(frame)
  d.text((24,17),'NIAMH | '+('01 IDLE > CHEST' if kind=='chest_local' else '02 IDLE > RAISED'),fill='#f1e6ca')
  d.text((24,39),'MOTION STUDY | ORIGINAL USER END POSE',fill='#acbeb2')
  d.line((30,769,470,769),fill='#829184')
  frame.paste(char,(75,70),char)
  d.text((24,790),label+' | OFFLINE / NO VFX',fill='#c7d0c4')
  frames.append(frame);characters.append(char);phases.append(label)
 samples=Image.new('RGB',(500*8,820))
 for k in range(8):samples.paste(frames[round(k*(len(frames)-1)/7)],(500*k,0))
 palette=samples.quantize(colors=256,method=Image.Quantize.MEDIANCUT)
 indexed=[f.quantize(palette=palette,dither=Image.Dither.NONE) for f in frames]
 dest=OUT/f'Niamh_idle_to_{kind}_v1.gif'
 indexed[0].save(dest,save_all=True,append_images=indexed[1:],duration=50,loop=0,disposal=1,optimize=False)
 picks=[0,round((.55+(raise_end-.55)*.3)*FPS),round((.55+(raise_end-.55)*.65)*FPS),round(raise_end*FPS)+2]
 contact=Image.new('RGB',(2000,820))
 for j,k in enumerate(picks):contact.paste(frames[k],(500*j,0))
 contact.save(CACHE/f'{kind}_contact.png')
 for j,k in enumerate(picks):characters[k].save(CACHE/f'{kind}_key_{j}.png')
 assert all(x==(0,0) for x in ImageChops.difference(characters[0],idle).getextrema())
 assert all(x==(0,0) for x in ImageChops.difference(characters[round(raise_end*FPS)+2],full).getextrema())
 for c in characters:
  assert ImageChops.difference(c.crop((0,540,W,H)),idle.crop((0,540,W,H))).getbbox() is None
 with Image.open(dest) as verify:
  ms=0
  for k in range(verify.n_frames):verify.seek(k);ms+=verify.info.get('duration',0)
  assert ms==round(duration*1000)
 records.append({'action':kind,'source_psd':str(psd.relative_to(ROOT)),'source_sha256':hashlib.sha256(psd.read_bytes()).hexdigest(),'gif':dest.name,'duration_ms':ms,'idle_endpoint_exact':True,'user_hold_endpoint_exact':True,'feet_unchanged':True,'motion':'two-segment arm mesh, separate wrist-following rigid prop, small open-to-grip blend'})
 print(dest)
(OUT/'preview_spec.json').write_text(json.dumps({'date':'2026-11-18','status':'idle-to-action cutout motion studies; not final rigged animation','old_hold_loops_preserved':True,'fps':20,'source_canvas':[350,H],'working_canvas':[W,H],'limitations':['open-hand to gripping-hand uses a brief aligned blend','garment transition uses blended user paint layers','not elbow skinning or a production rig','no beam, damage, game integration or Play Mode validation'],'clips':records},ensure_ascii=False,indent=2),encoding='utf-8')
