import { useEffect, useRef, useState } from 'react';
import { Camera, CheckCircle2, MapPin, Pencil, Target, Trash2, UserRound } from 'lucide-react';
import { useAuth } from '../../contexts/AuthContext';
import { getCollegeProfile, saveCollegeProfile, type CollegeProfileData } from '../../services/collegeService';
import { deleteProfilePhoto, uploadProfilePhoto } from '../../services/canonicalProfileService';

const degrees = ['B.Tech','B.E.','BCA','B.Sc','BBA','B.Com','Diploma','MCA','M.Tech','MBA'];
const branches = ['Computer Science Engineering','Information Technology','Mechanical Engineering','Civil Engineering','Electronics and Communication Engineering','Electrical Engineering','Computer Applications','Business Administration','Commerce'];
const states = ['Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chhattisgarh','Delhi','Goa','Gujarat','Haryana','Himachal Pradesh','Jharkhand','Karnataka','Kerala','Madhya Pradesh','Maharashtra','Odisha','Punjab','Rajasthan','Tamil Nadu','Telangana','Uttar Pradesh','Uttarakhand','West Bengal'];
const roles = ['Software Developer','Data Analyst','AI Engineer','Cloud Engineer','Cybersecurity Analyst','Core Engineering Role','Management Trainee'];

const completion = (p: CollegeProfileData) => {
  const fields = [p.fullName,p.phone,p.city,p.degree,p.branch,p.semester,p.cgpa,p.targetRole,p.skills];
  return Math.round(fields.filter(v => String(v ?? '').trim()).length / fields.length * 100);
};

export default function CollegeProfile() {
  const { user } = useAuth();
  const id = String(user?.id || 'guest');
  const input = useRef<HTMLInputElement>(null);
  const [data,setData] = useState<CollegeProfileData>(() => getCollegeProfile(id));
  const [edit,setEdit] = useState(false);
  const [msg,setMsg] = useState('');
  const [saving,setSaving] = useState(false);

  const load = () => {
    const p = getCollegeProfile(id);
    setData({...p, fullName:p.fullName || user?.name || '', email:p.email || user?.email || ''});
  };
  useEffect(() => { load(); }, [id,user?.name,user?.email]);

  const set = (k:keyof CollegeProfileData,v:string) => setData(x=>({...x,[k]:v}));

  const save = async () => {
    setMsg('');
    if (!data.degree.trim() || !data.branch.trim() || !data.semester.trim()) {
      setMsg('Please select Degree, Branch / Specialization and Semester before saving.');
      return;
    }
    setSaving(true);
    try {
      const updated = await saveCollegeProfile(id,data);
      setData({ ...getCollegeProfile(id), photo: updated.profile_photo || undefined });
      setEdit(false);
      setMsg('College profile saved successfully.');
    } catch(e) {
      setMsg(e instanceof Error ? e.message : 'Could not save profile.');
    } finally {
      setSaving(false);
    }
  };

  const changePhoto = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file=e.target.files?.[0]; if(!file)return;
    try {
      const updated=await uploadProfilePhoto(id,file);
      setData(x=>({...x,photo:updated.profile_photo || undefined}));
      setMsg('Profile photo updated.');
    } catch(e) { setMsg(e instanceof Error ? e.message : 'Could not upload profile photo.'); }
    e.target.value='';
  };

  const removePhoto = async () => {
    try {
      const updated=await deleteProfilePhoto(id);
      setData(x=>({...x,photo:updated.profile_photo || undefined}));
      setMsg('Profile photo removed.');
    } catch(e) { setMsg(e instanceof Error ? e.message : 'Could not remove profile photo.'); }
  };

  const pct=completion(data);
  const initials=(data.fullName || user?.name || 'C').trim().charAt(0).toUpperCase();

  if(edit) return (
    <div className="mx-auto max-w-5xl space-y-5">
      <div className="flex items-center justify-between">
        <div><p className="text-sm font-semibold text-cyan-600">EDIT PROFILE</p><h1 className="text-3xl font-bold text-slate-900">College Profile</h1><p className="mt-1 text-slate-500">Update only the information used by your profile, dashboard and assessments.</p></div>
        <button onClick={()=>{setEdit(false);load();}} className="rounded-xl border bg-white px-4 py-2.5 font-semibold">Cancel</button>
      </div>
      <section className="rounded-3xl bg-white p-6 shadow-sm border border-slate-100">
        <div className="mb-6 flex items-center gap-4">
          <div className="relative h-20 w-20 overflow-hidden rounded-2xl bg-cyan-50 flex items-center justify-center text-2xl font-bold text-cyan-700">
            {data.photo ? <img src={data.photo} className="h-full w-full object-cover" alt="Profile"/> : initials}
            <button onClick={()=>input.current?.click()} className="absolute bottom-1 right-1 rounded-full bg-cyan-600 p-1.5 text-white"><Camera size={14}/></button>
          </div>
          <div><p className="font-bold text-slate-900">Profile photo</p><p className="text-sm text-slate-500">JPG, PNG or WEBP up to 5 MB.</p>{data.photo&&<button onClick={removePhoto} className="mt-1 inline-flex items-center gap-1 text-xs font-semibold text-red-600"><Trash2 size={13}/>Remove</button>}</div>
          <input ref={input} hidden type="file" accept="image/jpeg,image/png,image/webp" onChange={changePhoto}/>
        </div>
        <div className="grid gap-4 md:grid-cols-2">
          <Field label="Full Name" value={data.fullName} onChange={v=>set('fullName',v)} />
          <Field label="Email" value={data.email} disabled />
          <Field label="Phone" value={data.phone} onChange={v=>set('phone',v)} />
          <Select label="Degree" value={data.degree} options={degrees} onChange={v=>set('degree',v)} required />
          <Select label="Branch / Specialization" value={data.branch} options={branches} onChange={v=>set('branch',v)} required />
          <Select label="Semester" value={data.semester} options={Array.from({length:8},(_,i)=>String(i+1))} onChange={v=>set('semester',v)} required />
          <Field label="CGPA" value={data.cgpa} onChange={v=>set('cgpa',v)} />
          <Field label="University" value={data.university} onChange={v=>set('university',v)} />
          <Field label="College Name (optional)" value={data.college} onChange={v=>set('college',v)} />
          <Select label="State" value={data.state} options={states} onChange={v=>set('state',v)} />
          <Field label="City" value={data.city} onChange={v=>set('city',v)} />
          <Select label="Target Role" value={data.targetRole} options={roles} onChange={v=>set('targetRole',v)} />
          <Field label="Career Goal" value={data.careerGoal} onChange={v=>set('careerGoal',v)} />
          <Field label="Skills (comma separated)" value={data.skills} onChange={v=>set('skills',v)} />
          <Field label="LinkedIn (optional)" value={data.linkedin} onChange={v=>set('linkedin',v)} />
          <Field label="GitHub (optional)" value={data.github} onChange={v=>set('github',v)} />
          <Field label="Portfolio (optional)" value={data.portfolio} onChange={v=>set('portfolio',v)} />
        </div>
        {msg && <p className="mb-4 rounded-xl bg-cyan-50 p-3 text-sm font-medium text-cyan-800">{msg}</p>}
        <div className="mt-6 flex justify-end"><button type="button" disabled={saving} onClick={() => void save()} className="rounded-xl bg-cyan-600 px-6 py-3 font-semibold text-white hover:bg-cyan-700 disabled:cursor-not-allowed disabled:opacity-60">{saving ? 'Saving…' : 'Save Changes'}</button></div>
      </section>
    </div>
  );

  return (
    <div className="mx-auto max-w-5xl space-y-5 rounded-[28px] bg-slate-50 p-4 sm:p-6">
      <section className="overflow-hidden rounded-[28px] bg-white shadow-sm">
        <div className="bg-gradient-to-r from-cyan-50 via-white to-blue-50 p-6 sm:p-8">
          <div className="flex flex-wrap items-start justify-between gap-5">
            <div className="flex items-center gap-4">
              <div className="relative h-16 w-16 overflow-hidden rounded-2xl bg-cyan-600 flex items-center justify-center text-xl font-bold text-white">
                {data.photo ? <img src={data.photo} className="h-full w-full object-cover" alt="Profile"/> : initials}
              </div>
              <div><p className="text-sm font-semibold text-cyan-600">MY PROFILE</p><h1 className="mt-1 text-3xl font-bold text-slate-900">{data.fullName || 'Your Profile'}</h1><p className="mt-1 text-sm text-slate-500">Your academic and career profile</p></div>
            </div>
            <button onClick={()=>setEdit(true)} className="inline-flex items-center gap-2 rounded-xl bg-cyan-600 px-5 py-3 font-semibold text-white"><Pencil size={17}/>Edit Profile</button>
          </div>
          <div className="mt-7 rounded-2xl border border-white/80 bg-white/80 p-5">
            <div className="flex justify-between"><div><p className="font-bold text-slate-900">Profile completion</p><p className="mt-1 text-sm text-slate-500">Keep your core academic and career details up to date.</p></div><span className="text-2xl font-bold text-cyan-700">{pct}%</span></div>
            <div className="mt-4 h-2.5 overflow-hidden rounded-full bg-slate-100"><div className="h-full rounded-full bg-cyan-600" style={{width:`${pct}%`}}/></div>
          </div>
        </div>
        <div className="grid gap-px bg-slate-100 sm:grid-cols-3">
          {([['Basic Information',!!data.fullName&&!!data.phone],['Academic Information',!!data.degree&&!!data.branch&&!!data.semester],['Career Direction',!!data.targetRole||!!data.careerGoal]] as const).map(([label,ok])=><div key={label} className="bg-white p-5"><p className="text-sm font-semibold text-slate-700">{label}</p><div className="mt-2 flex items-center gap-2 text-sm font-semibold">{ok?<><CheckCircle2 size={16} className="text-emerald-500"/>Complete</>:<span className="text-slate-400">Needs attention</span>}</div></div>)}
        </div>
      </section>
      <div className="grid gap-5 lg:grid-cols-2">
        <section className="rounded-2xl bg-white p-6 shadow-sm"><div className="flex items-center gap-3"><UserRound className="text-cyan-600" size={21}/><h2 className="text-lg font-bold">Academic Profile</h2></div><div className="mt-5 grid gap-4 sm:grid-cols-2"><Info label="Degree" value={data.degree}/><Info label="Branch" value={data.branch}/><Info label="Semester" value={data.semester}/><Info label="CGPA" value={data.cgpa}/><Info label="University" value={data.university}/><Info label="College" value={data.college || 'Optional'}/></div></section>
        <section className="rounded-2xl bg-white p-6 shadow-sm"><div className="flex items-center gap-3"><Target className="text-cyan-600" size={21}/><h2 className="text-lg font-bold">Career Direction</h2></div><Info label="Target Role" value={data.targetRole}/><Info label="Career Goal" value={data.careerGoal}/><div className="mt-5"><p className="text-xs uppercase tracking-wide text-slate-400">Skills</p><p className="mt-1 font-semibold text-slate-800">{data.skills || 'Not set'}</p></div><div className="mt-5 flex items-start gap-3 rounded-xl bg-slate-50 p-4"><MapPin size={19} className="mt-0.5 text-cyan-600"/><div><p className="text-xs uppercase tracking-wide text-slate-400">Location</p><p className="mt-1 font-semibold text-slate-800">{[data.city,data.state].filter(Boolean).join(', ')||'Not set'}</p></div></div></section>
      </div>
      {msg&&<p className="rounded-xl bg-cyan-50 p-4 text-cyan-800">{msg}</p>}
    </div>
  );
}
function Field({label,value,onChange,disabled=false}:{label:string,value:string,onChange?:(v:string)=>void,disabled?:boolean}){return <label className="text-sm font-semibold text-slate-700">{label}{onChange&&label!=='Email'&&<span className="text-slate-400"> {['Phone','Degree','Branch / Specialization','Semester'].includes(label)?'*':''}</span>}<input disabled={disabled} value={value||''} onChange={e=>onChange?.(e.target.value)} className="mt-1 w-full rounded-xl border px-4 py-2.5 disabled:bg-slate-50"/></label>}
function Select({label,value,options,onChange,required=false}:{label:string,value:string,options:string[],onChange:(v:string)=>void,required?:boolean}){return <label className="text-sm font-semibold text-slate-700">{label}{required&&<span className="text-red-500"> *</span>}<select value={value||''} onChange={e=>onChange(e.target.value)} className="mt-1 w-full rounded-xl border px-4 py-2.5"><option value="">Select {label.toLowerCase()}</option>{options.map(x=><option key={x}>{x}</option>)}</select></label>}
function Info({label,value}:{label:string,value?:string}){return <div><p className="text-xs uppercase tracking-wide text-slate-400">{label}</p><p className="mt-1 font-semibold text-slate-800">{value||'Not set'}</p></div>}
