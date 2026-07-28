import { useEffect, useRef, useState } from "react";
import { Camera, Pencil, Save, Trash2 } from "lucide-react";
import { useAuth } from "../../contexts/AuthContext";
import { boardNames } from "../../data/academic/boards";
import { calculateProfileCompletion, getAssessmentPurpose, getHighSchoolProfile, isStreamRequired, saveHighSchoolProfile, type HighSchoolClass, type HighSchoolProfile as ProfileData, type HighSchoolStream } from "../../services/highSchoolProfileService";

const classes: HighSchoolClass[] = ["9", "10", "11", "12"];
const streams: HighSchoolStream[] = ["Science - PCM", "Science - PCB", "Science - PCMB", "Commerce with Mathematics", "Commerce without Mathematics", "Humanities / Arts"];

function HighSchoolProfile() {
  const { user } = useAuth();
  const input = useRef<HTMLInputElement>(null);
  const [edit, setEdit] = useState(false);
  const [msg, setMsg] = useState("");
  const [data, setData] = useState({ studentClass: "" as HighSchoolClass | "", board: "", currentStream: "" as HighSchoolStream | "", schoolName: "", state: "", district: "", city: "", careerGoal: "", profilePhoto: "" });
  const [saved, setSaved] = useState<ProfileData | null>(null);

  useEffect(() => {
    if (!user) return;
    const p = getHighSchoolProfile(user.id);
    if (p) {
      setSaved(p);
      setData({ studentClass: p.studentClass, board: p.board, currentStream: p.currentStream ?? "", schoolName: p.schoolName, state: p.state ?? "", district: p.district ?? "", city: p.city, careerGoal: p.careerGoal, profilePhoto: p.profilePhoto ?? "" });
    } else setEdit(true);
  }, [user]);

  if (!user) return null;
  const set = (key: keyof typeof data, value: string) => setData(current => ({ ...current, [key]: value }));
  const completion = calculateProfileCompletion(saved);
  const streamRequired = data.studentClass ? isStreamRequired(data.studentClass) : false;
  const purpose = data.studentClass ? getAssessmentPurpose(data.studentClass) : null;

  const photo = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0]; if (!file) return;
    const reader = new FileReader(); reader.onload = () => set("profilePhoto", String(reader.result || "")); reader.readAsDataURL(file);
  };

  const save = () => {
    setMsg("");
    if (!data.studentClass) return setMsg("Please select your class.");
    if (!data.board) return setMsg("Please select your board.");
    if (!data.schoolName.trim() || !data.state.trim() || !data.district.trim() || !data.city.trim()) return setMsg("Please complete school and location details.");
    if (streamRequired && !data.currentStream) return setMsg("Please select your current stream.");
    const profile = saveHighSchoolProfile({ userId: user.id, fullName: user.name, email: user.email, studentClass: data.studentClass, board: data.board, currentStream: streamRequired ? data.currentStream as HighSchoolStream : null, careerGoal: data.careerGoal.trim(), schoolName: data.schoolName.trim(), city: data.city.trim(), state: data.state.trim(), district: data.district.trim(), profilePhoto: data.profilePhoto || null });
    setSaved(profile); setEdit(false); setMsg("Profile saved successfully.");
  };

  const field = "mt-1 w-full rounded-xl border border-slate-200 px-4 py-2.5 outline-none focus:border-cyan-500 disabled:bg-slate-50 disabled:text-slate-600";
  return <div className="mx-auto max-w-5xl space-y-5">
    <div className="flex items-center justify-between gap-4"><div><h1 className="text-3xl font-bold text-slate-900">My High School Profile</h1><p className="mt-1 text-slate-600">Class, board and academic details control your High School experience.</p></div><button onClick={() => setEdit(true)} className="flex items-center gap-2 rounded-xl border bg-white px-5 py-2.5 font-semibold"><Pencil size={17}/>Edit Profile</button></div>

    <section className="rounded-2xl border border-slate-200 bg-white p-5 shadow-sm"><div className="flex items-center gap-5"><div className="relative flex h-24 w-24 shrink-0 items-center justify-center overflow-hidden rounded-full bg-cyan-50 text-3xl font-bold text-cyan-700">{data.profilePhoto ? <img src={data.profilePhoto} alt="Profile" className="h-full w-full object-cover"/> : (user.name?.[0] || "S")}<button type="button" onClick={() => input.current?.click()} className="absolute bottom-0 right-0 rounded-full border-4 border-white bg-cyan-600 p-2 text-white"><Camera size={14}/></button></div><input ref={input} type="file" accept="image/*" className="hidden" onChange={photo}/><div><h2 className="text-xl font-bold">{user.name}</h2><p className="text-slate-500">{data.studentClass ? `Class ${data.studentClass}` : "Class not selected"} · {data.board || "Board not selected"}</p><p className="mt-1 text-sm text-cyan-700">Profile completion: {completion}%</p>{data.profilePhoto && <button type="button" onClick={() => set("profilePhoto", "")} className="mt-2 flex items-center gap-1 text-sm text-red-600"><Trash2 size={14}/>Remove photo</button>}</div></div></section>

    <section className="rounded-2xl border border-slate-200 bg-white p-5 shadow-sm"><div className="grid gap-4 md:grid-cols-2">
      <Label text="Full Name"><input disabled value={user.name} className={field}/></Label><Label text="Email"><input disabled value={user.email} className={field}/></Label>
      <Label text="Class"><select disabled={!edit} value={data.studentClass} onChange={e => { set("studentClass", e.target.value); if (e.target.value === "9" || e.target.value === "10") set("currentStream", ""); }} className={field}><option value="">Select class</option>{classes.map(x => <option key={x} value={x}>Class {x}</option>)}</select></Label>
      <Label text="Board"><select disabled={!edit} value={data.board} onChange={e => set("board", e.target.value)} className={field}><option value="">Select board</option>{boardNames.map(x => <option key={x} value={x}>{x}</option>)}</select></Label>
      {streamRequired && <Label text="Current Stream"><select disabled={!edit} value={data.currentStream} onChange={e => set("currentStream", e.target.value)} className={field}><option value="">Select current stream</option>{streams.map(x => <option key={x}>{x}</option>)}</select></Label>}
      <Label text="School Name"><input disabled={!edit} value={data.schoolName} onChange={e => set("schoolName", e.target.value)} placeholder="Enter school name" className={field}/></Label>
      <Label text="State"><input disabled={!edit} value={data.state} onChange={e => set("state", e.target.value)} placeholder="Enter state" className={field}/></Label>
      <Label text="District"><input disabled={!edit} value={data.district} onChange={e => set("district", e.target.value)} placeholder="Enter district" className={field}/></Label>
      <Label text="City / Town"><input disabled={!edit} value={data.city} onChange={e => set("city", e.target.value)} placeholder="Enter city / town" className={field}/></Label>
      <Label text="Career Goal"><input disabled={!edit} value={data.careerGoal} onChange={e => set("careerGoal", e.target.value)} placeholder="Optional career goal" className={field}/></Label>
    </div>
    {purpose && <div className="mt-5 rounded-xl bg-cyan-50 p-4"><p className="text-xs font-bold uppercase tracking-wide text-cyan-700">Guidance Assessment</p><p className="mt-1 font-bold text-slate-900">{purpose.title}</p><p className="mt-1 text-sm text-slate-600">{purpose.description}</p></div>}
    {edit && <button type="button" onClick={save} className="mt-5 flex items-center gap-2 rounded-xl bg-cyan-600 px-5 py-2.5 font-semibold text-white"><Save size={17}/>Save Changes</button>}
    {msg && <p className={`mt-4 rounded-xl p-3 text-sm font-medium ${msg.includes("successfully") ? "bg-green-50 text-green-700" : "bg-amber-50 text-amber-800"}`}>{msg}</p>}
    </section>
  </div>;
}

function Label({ text, children }: { text: string; children: React.ReactNode }) { return <label className="text-sm font-semibold text-slate-700">{text}{children}</label>; }
export default HighSchoolProfile;
