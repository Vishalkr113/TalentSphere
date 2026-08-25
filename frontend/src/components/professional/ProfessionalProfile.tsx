import { useEffect, useRef, useState } from 'react';
import { Camera, CheckCircle2, MapPin, Pencil, Target, Trash2, UserRound } from 'lucide-react';
import { useAuth } from '../../contexts/AuthContext';
import { getProfessionalProfile, saveProfessionalProfile, type ProfessionalProfile as P } from '../../services/professionalService';
import { deleteProfilePhoto, getCanonicalProfile, uploadProfilePhoto } from '../../services/canonicalProfileService';

const industries=['Software & IT','Finance & Banking','Healthcare','Education','Manufacturing','Consulting','Retail & E-commerce','Telecommunications','Other'];
const experience=['0-1 years','1-3 years','3-5 years','5-8 years','8+ years'];
const roles=['Software Developer','Data Analyst','AI Engineer','Cloud Engineer','Cybersecurity Analyst','Product Manager','Project Manager','Engineering Lead','Other'];

export default function ProfessionalProfile(){
 const {user}=useAuth(); const id=String(user?.id||'guest'); const input=useRef<HTMLInputElement>(null);
 const [form,setForm]=useState<P>(()=>getProfessionalProfile(id,user?.name||'',user?.email||'')); const [edit,setEdit]=useState(false); const [msg,setMsg]=useState(''); const [saving,setSaving]=useState(false);
 const load=()=>setForm(getProfessionalProfile(id,user?.name||'',user?.email||''));
 useEffect(()=>load(),[id,user?.name,user?.email]);
 const set=(k:keyof P,v:string)=>setForm(x=>({...x,[k]:v}));
 const save=async()=>{
  setMsg('');
  if(!form.phone.trim()||!form.company.trim()||!form.designation.trim()||!form.experience.trim()||!form.industry.trim()||!form.targetRole.trim()){setMsg('Please complete the required professional fields before saving.');return;}
  setSaving(true);
  try{
   await saveProfessionalProfile(id,form);
   setForm(getProfessionalProfile(id,user?.name||'',user?.email||''));
   setEdit(false);
   setMsg('Professional profile saved successfully.');
  }catch(e){setMsg(e instanceof Error?e.message:'Could not save profile.')}
  finally{setSaving(false);}
 };
 const photo= getCanonicalProfile(id)?.profile_photo || null;
 const upload=async(e:React.ChangeEvent<HTMLInputElement>)=>{const f=e.target.files?.[0];if(!f)return;try{await uploadProfilePhoto(id,f);setMsg('Profile photo updated.');}catch(e){setMsg(e instanceof Error?e.message:'Could not upload profile photo.')}e.target.value='';};
 const remove=async()=>{try{await deleteProfilePhoto(id);setMsg('Profile photo removed.');}catch(e){setMsg(e instanceof Error?e.message:'Could not remove profile photo.')}};
 const pct=Math.round([form.fullName,form.phone,form.company,form.designation,form.experience,form.industry,form.skills,form.targetRole].filter(Boolean).length/8*100);
 const initial=(form.fullName||user?.name||'P').trim().charAt(0).toUpperCase();
 if(edit)return <div className="mx-auto max-w-5xl space-y-5">
   <div className="flex items-center justify-between"><div><p className="text-sm font-semibold text-cyan-600">EDIT PROFILE</p><h1 className="text-3xl font-bold text-slate-900">Professional Profile</h1><p className="mt-1 text-slate-500">Keep your professional context current for assessments and career guidance.</p></div><button onClick={()=>{setEdit(false);load()}} className="rounded-xl border bg-white px-4 py-2.5 font-semibold">Cancel</button></div>
   <section className="rounded-3xl border border-slate-100 bg-white p-6 shadow-sm">
    <div className="mb-6 flex items-center gap-4"><div className="relative h-20 w-20 overflow-hidden rounded-2xl bg-cyan-50 flex items-center justify-center text-2xl font-bold text-cyan-700">{photo?<img src={photo} className="h-full w-full object-cover" alt="Profile"/>:initial}<button onClick={()=>input.current?.click()} className="absolute bottom-1 right-1 rounded-full bg-cyan-600 p-1.5 text-white"><Camera size={14}/></button></div><div><p className="font-bold">Profile photo</p><p className="text-sm text-slate-500">JPG, PNG or WEBP up to 5 MB.</p>{photo&&<button onClick={remove} className="mt-1 inline-flex items-center gap-1 text-xs font-semibold text-red-600"><Trash2 size={13}/>Remove</button>}</div><input ref={input} hidden type="file" accept="image/jpeg,image/png,image/webp" onChange={upload}/></div>
    <div className="grid gap-4 md:grid-cols-2">
      <Field label="Full Name" value={form.fullName} onChange={v=>set('fullName',v)}/><Field label="Email" value={form.email} disabled/>
      <Field label="Phone" value={form.phone} onChange={v=>set('phone',v)} required/>
      <Field label="Current Company" value={form.company} onChange={v=>set('company',v)} required/>
      <Field label="Current Role / Designation" value={form.designation} onChange={v=>set('designation',v)} required/>
      <Select label="Experience Level" value={form.experience} options={experience} onChange={v=>set('experience',v)} required/>
      <Select label="Professional Domain" value={form.industry} options={industries} onChange={v=>set('industry',v)} required/>
      <Field label="Years of Experience" value={form.yearsOfExperience} onChange={v=>set('yearsOfExperience',v)}/>
      <Field label="Skills (comma separated)" value={form.skills} onChange={v=>set('skills',v)} required/>
      <Select label="Target Role" value={form.targetRole} options={roles} onChange={v=>set('targetRole',v)} required/>
      <Field label="Career Goal" value={form.careerGoal} onChange={v=>set('careerGoal',v)}/>
      <Field label="Expected Salary" value={form.expectedSalary} onChange={v=>set('expectedSalary',v)}/>
      <Field label="City" value={form.city} onChange={v=>set('city',v)}/><Field label="State" value={form.state} onChange={v=>set('state',v)}/>
      <Field label="LinkedIn (optional)" value={form.linkedin} onChange={v=>set('linkedin',v)}/><Field label="GitHub (optional)" value={form.github} onChange={v=>set('github',v)}/><Field label="Portfolio (optional)" value={form.portfolio} onChange={v=>set('portfolio',v)}/>
    </div>
    {msg&&<p className="mb-4 rounded-xl bg-cyan-50 p-3 text-sm font-medium text-cyan-800">{msg}</p>}<div className="mt-6 flex justify-end"><button type="button" disabled={saving} onClick={()=>void save()} className="rounded-xl bg-cyan-600 px-6 py-3 font-semibold text-white disabled:cursor-not-allowed disabled:opacity-60">{saving?'Saving…':'Save Changes'}</button></div>
   </section>
 </div>;
 return <div className="mx-auto max-w-5xl space-y-5 rounded-[28px] bg-slate-50 p-4 sm:p-6">
   <section className="overflow-hidden rounded-[28px] bg-white shadow-sm">
    <div className="bg-gradient-to-r from-cyan-50 via-white to-blue-50 p-6 sm:p-8"><div className="flex flex-wrap items-start justify-between gap-5"><div className="flex items-center gap-4"><div className="h-16 w-16 overflow-hidden rounded-2xl bg-cyan-600 flex items-center justify-center text-xl font-bold text-white">{photo?<img src={photo} className="h-full w-full object-cover" alt="Profile"/>:initial}</div><div><p className="text-sm font-semibold text-cyan-600">MY PROFILE</p><h1 className="mt-1 text-3xl font-bold text-slate-900">{form.fullName||'Your Profile'}</h1><p className="mt-1 text-sm text-slate-500">{form.designation||'Working Professional'}{form.industry?` · ${form.industry}`:''}</p></div></div><button onClick={()=>setEdit(true)} className="inline-flex items-center gap-2 rounded-xl bg-cyan-600 px-5 py-3 font-semibold text-white"><Pencil size={17}/>Edit Profile</button></div>
    <div className="mt-7 rounded-2xl border border-white/80 bg-white/80 p-5"><div className="flex justify-between"><div><p className="font-bold">Profile completion</p><p className="mt-1 text-sm text-slate-500">Keep your professional essentials current.</p></div><span className="text-2xl font-bold text-cyan-700">{pct}%</span></div><div className="mt-4 h-2.5 overflow-hidden rounded-full bg-slate-100"><div className="h-full rounded-full bg-cyan-600" style={{width:`${pct}%`}}/></div></div></div>
    <div className="grid gap-px bg-slate-100 sm:grid-cols-3">{([['Basic Information',!!form.fullName&&!!form.phone],['Professional Information',!!form.company&&!!form.designation&&!!form.experience&&!!form.industry],['Career Direction',!!form.targetRole||!!form.careerGoal]] as const).map(([label,ok])=><div key={label} className="bg-white p-5"><p className="text-sm font-semibold text-slate-700">{label}</p><div className="mt-2 flex items-center gap-2 text-sm font-semibold">{ok?<><CheckCircle2 size={16} className="text-emerald-500"/>Complete</>:<span className="text-slate-400">Needs attention</span>}</div></div>)}</div>
   </section>
   <div className="grid gap-5 lg:grid-cols-2">
    <section className="rounded-2xl bg-white p-6 shadow-sm"><div className="flex items-center gap-3"><UserRound className="text-cyan-600" size={21}/><h2 className="text-lg font-bold">Professional Profile</h2></div><div className="mt-5 grid gap-4 sm:grid-cols-2"><Info label="Company" value={form.company}/><Info label="Role" value={form.designation}/><Info label="Experience" value={form.experience}/><Info label="Domain" value={form.industry}/><Info label="Skills" value={form.skills}/><Info label="Expected Salary" value={form.expectedSalary}/></div></section>
    <section className="rounded-2xl bg-white p-6 shadow-sm"><div className="flex items-center gap-3"><Target className="text-cyan-600" size={21}/><h2 className="text-lg font-bold">Career Direction</h2></div><Info label="Target Role" value={form.targetRole}/><Info label="Career Goal" value={form.careerGoal}/><div className="mt-5 flex items-start gap-3 rounded-xl bg-slate-50 p-4"><MapPin size={19} className="mt-0.5 text-cyan-600"/><div><p className="text-xs uppercase tracking-wide text-slate-400">Location</p><p className="mt-1 font-semibold text-slate-800">{[form.city,form.state].filter(Boolean).join(', ')||'Not set'}</p></div></div></section>
   </div>
   {msg&&<p className="rounded-xl bg-cyan-50 p-4 text-cyan-800">{msg}</p>}
 </div>;
}
function Field({label,value,onChange,disabled=false,required=false}:{label:string,value:string,onChange?:(v:string)=>void,disabled?:boolean,required?:boolean}){return <label className="text-sm font-semibold text-slate-700">{label}{required&&<span className="text-red-500"> *</span>}<input disabled={disabled} value={value||''} onChange={e=>onChange?.(e.target.value)} className="mt-1 w-full rounded-xl border px-4 py-2.5 disabled:bg-slate-50"/></label>}
function Select({label,value,options,onChange,required=false}:{label:string,value:string,options:string[],onChange:(v:string)=>void,required?:boolean}){return <label className="text-sm font-semibold text-slate-700">{label}{required&&<span className="text-red-500"> *</span>}<select value={value||''} onChange={e=>onChange(e.target.value)} className="mt-1 w-full rounded-xl border px-4 py-2.5"><option value="">Select {label.toLowerCase()}</option>{options.map(x=><option key={x}>{x}</option>)}</select></label>}
function Info({label,value}:{label:string,value?:string}){return <div><p className="text-xs uppercase tracking-wide text-slate-400">{label}</p><p className="mt-1 font-semibold text-slate-800">{value||'Not set'}</p></div>}
