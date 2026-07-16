import { Award, BadgeCheck, BookOpen, CheckCircle2, Compass, Medal, Star, Target } from "lucide-react";
import { useAuth } from "../../contexts/AuthContext";
import { calculateWorkspaceStats } from "../../services/highSchoolWorkspaceService";
import { getUserAssessmentResults } from "../../data/assessment/assessmentService";
import { getHighSchoolProfile, calculateProfileCompletion } from "../../services/highSchoolProfileService";
function Achievements(){const {user}=useAuth();if(!user)return null;const w=calculateWorkspaceStats(user.id);const analyses=getUserAssessmentResults(user.id);const profile=getHighSchoolProfile(user.id);const avg=analyses.length?Math.round(analyses.reduce((s,a)=>s+a.percentage,0)/analyses.length):0;
 const badges=[
  {title:"Profile Ready",description:"Complete your academic profile.",icon:BadgeCheck,unlocked:calculateProfileCompletion(profile)===100},
  {title:"Assessment Starter",description:"Complete your first assessment.",icon:Star,unlocked:analyses.length>=1},
  {title:"Assessment Finisher",description:"Complete all five assessments.",icon:Medal,unlocked:analyses.length>=5},
  {title:"Strong Performer",description:"Reach 70% average assessment performance.",icon:Award,unlocked:avg>=70},
  {title:"Goal Keeper",description:"Complete all of today's goals.",icon:Target,unlocked:w.goals.length>0&&w.completedGoals===w.goals.length},
  {title:"Assignment Finisher",description:"Complete at least five assignments.",icon:CheckCircle2,unlocked:w.completedAssignments>=5},
  {title:"Career Explorer",description:"Explore at least three career pathways.",icon:Compass,unlocked:w.careers.length>=3},
  {title:"Roadmap Progress",description:"Complete three roadmap milestones.",icon:BookOpen,unlocked:w.roadmap.length>=3},
 ] as const;const unlocked=badges.filter(b=>b.unlocked).length;const level=unlocked>=7?"Gold":unlocked>=4?"Silver":unlocked>=1?"Bronze":"Starter";
 return <div className="mx-auto max-w-5xl space-y-5"><div><h1 className="text-3xl font-bold">Achievements</h1><p className="mt-1 text-slate-600">Badges unlock only from your actual activity in TalentSphere.</p></div><section className="rounded-2xl bg-gradient-to-r from-cyan-600 to-blue-600 p-6 text-white"><div className="grid gap-4 sm:grid-cols-3"><Stat label="Unlocked Badges" value={`${unlocked} / ${badges.length}`}/><Stat label="Current Level" value={level}/><Stat label="Assessment Average" value={`${avg}%`}/></div></section><div className="grid gap-4 md:grid-cols-2">{badges.map(b=><div key={b.title} className={`rounded-2xl border bg-white p-5 ${!b.unlocked?"opacity-60":""}`}><div className="flex items-start gap-4"><div className="iconbox"><b.icon size={22}/></div><div><h2 className="text-lg font-bold">{b.title}</h2><p className="mt-1 text-sm text-slate-600">{b.description}</p><span className={`mt-3 inline-block rounded-full px-3 py-1 text-xs font-semibold ${b.unlocked?"bg-green-100 text-green-700":"bg-slate-100 text-slate-500"}`}>{b.unlocked?"Unlocked":"Locked"}</span></div></div></div>)}</div></div>}
function Stat({label,value}:{label:string;value:string}){return <div><p className="text-cyan-100">{label}</p><h3 className="mt-1 text-3xl font-bold">{value}</h3></div>}
export default Achievements;