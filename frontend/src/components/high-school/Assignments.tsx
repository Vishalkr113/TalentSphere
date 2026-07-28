import { useEffect, useState } from "react";
import { CalendarDays, ClipboardList, Pencil, Plus, Trash2, X } from "lucide-react";
import { useAuth } from "../../contexts/AuthContext";
import { getAssignments, saveAssignments, type Assignment, type AssignmentStatus } from "../../services/highSchoolWorkspaceService";

const empty={subject:"",title:"",dueDate:"",status:"Pending" as AssignmentStatus,notes:""};
function Assignments(){
 const {user}=useAuth(); const [items,setItems]=useState<Assignment[]>([]); const [form,setForm]=useState(empty); const [editing,setEditing]=useState<string|null>(null); const [open,setOpen]=useState(false);
 useEffect(()=>{if(user)setItems(getAssignments(user.id))},[user]);
 const persist=(next:Assignment[])=>{if(!user)return;setItems(next);saveAssignments(user.id,next)};
 const submit=(e:React.FormEvent)=>{e.preventDefault();if(!form.subject.trim()||!form.title.trim()||!form.dueDate)return;
  const next=editing?items.map(i=>i.id===editing?{...i,...form}:i):[...items,{id:crypto.randomUUID(),...form}];persist(next);setForm(empty);setEditing(null);setOpen(false)};
 const edit=(i:Assignment)=>{setForm({subject:i.subject,title:i.title,dueDate:i.dueDate,status:i.status,notes:i.notes});setEditing(i.id);setOpen(true)};
 const status=(i:Assignment,s:AssignmentStatus)=>persist(items.map(x=>x.id===i.id?{...x,status:s}:x));
 return <div className="mx-auto max-w-5xl space-y-5">
  <Header title="Assignments" text="Add, edit, track and complete your real school assignments." action={()=>{setForm(empty);setEditing(null);setOpen(true)}} />
  {open&&<form onSubmit={submit} className="grid gap-3 rounded-2xl border bg-white p-5 shadow-sm md:grid-cols-2">
   <input className="field" placeholder="Subject" value={form.subject} onChange={e=>setForm({...form,subject:e.target.value})}/>
   <input className="field" placeholder="Assignment title" value={form.title} onChange={e=>setForm({...form,title:e.target.value})}/>
   <input className="field" type="date" value={form.dueDate} onChange={e=>setForm({...form,dueDate:e.target.value})}/>
   <select className="field" value={form.status} onChange={e=>setForm({...form,status:e.target.value as AssignmentStatus})}><option>Pending</option><option>In Progress</option><option>Completed</option></select>
   <textarea className="field md:col-span-2" placeholder="Notes / instructions" value={form.notes} onChange={e=>setForm({...form,notes:e.target.value})}/>
   <div className="flex gap-2 md:col-span-2"><button className="primary">{editing?"Update":"Save"} Assignment</button><button type="button" className="secondary" onClick={()=>setOpen(false)}><X size={17}/>Cancel</button></div>
  </form>}
  {!items.length?<Empty icon={<ClipboardList size={28}/>} text="No assignments yet. Add your first school assignment."/>:
  <div className="space-y-3">{items.sort((a,b)=>a.dueDate.localeCompare(b.dueDate)).map(i=><div key={i.id} className="rounded-2xl border bg-white p-5 shadow-sm">
   <div className="flex flex-col gap-4 lg:flex-row lg:items-center lg:justify-between"><div><p className="text-sm font-semibold text-cyan-600">{i.subject}</p><h2 className="text-xl font-bold text-slate-900">{i.title}</h2><p className="mt-1 text-sm text-slate-500">{i.notes||"No notes added"}</p></div>
   <div className="flex flex-wrap items-center gap-2"><span className="flex items-center gap-2 rounded-lg bg-slate-100 px-3 py-2 text-sm"><CalendarDays size={16}/>{i.dueDate}</span>
   <select className="field !w-auto" value={i.status} onChange={e=>status(i,e.target.value as AssignmentStatus)}><option>Pending</option><option>In Progress</option><option>Completed</option></select>
   <button className="iconbtn" onClick={()=>edit(i)}><Pencil size={17}/></button><button className="iconbtn text-red-600" onClick={()=>persist(items.filter(x=>x.id!==i.id))}><Trash2 size={17}/></button></div></div>
  </div>)}</div>}
 </div>
}
function Header({title,text,action}:{title:string;text:string;action:()=>void}){return <div className="flex flex-col justify-between gap-3 sm:flex-row sm:items-end"><div><h1 className="text-3xl font-bold text-slate-900">{title}</h1><p className="mt-1 text-slate-600">{text}</p></div><button onClick={action} className="primary"><Plus size={17}/>Add Assignment</button></div>}
function Empty({icon,text}:{icon:React.ReactNode;text:string}){return <div className="rounded-2xl border border-dashed bg-white p-10 text-center text-slate-500"><div className="mx-auto mb-3 flex h-12 w-12 items-center justify-center rounded-xl bg-cyan-50 text-cyan-600">{icon}</div>{text}</div>}
export default Assignments;