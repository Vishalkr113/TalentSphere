import { useEffect, useMemo, useState, type ReactNode } from 'react';
import { Award, BarChart3, BriefcaseBusiness, FileText, Target, UserRound } from 'lucide-react';
import { useAuth } from '../../contexts/AuthContext';
import { getAssessmentHistory, type AssessmentHistoryItem } from '../../services/dashboardService';
import { getProfessionalProfile, professionalStats } from '../../services/professionalService';

const PROFESSIONAL_TYPES = new Set(['professional_skill', 'professional_common', 'professional_technical', 'professional_dsa', 'professional_situational']);

export default function ProfessionalFinalCareerReport() {
  const { user } = useAuth();
  const [attempts, setAttempts] = useState<AssessmentHistoryItem[]>([]);

  useEffect(() => {
    if (!user) return;
    void getAssessmentHistory().then((r) => setAttempts(r.attempts.filter((x) => x.status === 'completed' && PROFESSIONAL_TYPES.has(x.assessment_type)))).catch(() => setAttempts([]));
  }, [user]);

  const profile = useMemo(() => user ? getProfessionalProfile(user.id, user.name || '', user.email || '') : null, [user]);
  const stats = useMemo(() => user ? professionalStats(user.id, user.name || '', user.email || '') : null, [user]);
  const assessment = attempts.length ? Math.round(attempts.reduce((s, x) => s + x.percentage, 0) / attempts.length) : 0;
  const profileScore = stats?.profile ?? 0;
  const resumeScore = stats?.resume ?? 0;
  const interviewScore = stats?.interview ?? 0;
  const careerScore = stats?.career ?? 0;
  const overall = Math.round(profileScore * .25 + assessment * .30 + resumeScore * .15 + interviewScore * .15 + careerScore * .15);

  if (!user || !profile) return null;

  return (
    <div className="space-y-5">
      <div>
        <p className="text-sm font-semibold text-cyan-600">FINAL CAREER REPORT</p>
        <h1 className="mt-1 text-2xl font-bold text-slate-900">Professional Career Readiness Report</h1>
        <p className="mt-1 text-sm text-slate-500">A consolidated view of saved profile data and completed professional activity.</p>
      </div>

      <section className="rounded-2xl bg-gradient-to-r from-cyan-600 to-blue-700 p-6 text-white shadow-sm">
        <p className="text-sm text-cyan-100">Overall career readiness</p>
        <div className="mt-1 flex items-end gap-3"><span className="text-5xl font-bold">{overall}%</span><span className="pb-2 text-sm text-cyan-100">evidence-based</span></div>
        <div className="mt-4 grid gap-2 sm:grid-cols-4">
          <Mini label="Profile" value={`${profileScore}%`} />
          <Mini label="Assessment" value={`${assessment}%`} />
          <Mini label="Resume" value={`${resumeScore}%`} />
          <Mini label="Interview" value={`${interviewScore}%`} />
        </div>
      </section>

      <section className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
        <Info icon={<UserRound size={18} />} title="Professional profile" value={profile.fullName || 'Not set'} detail={profile.designation || 'Role not set'} />
        <Info icon={<BriefcaseBusiness size={18} />} title="Current context" value={profile.company || 'Company not set'} detail={profile.industry || 'Domain not set'} />
        <Info icon={<Target size={18} />} title="Target direction" value={profile.targetRole || 'Target role not set'} detail={profile.careerGoal || 'Career goal not set'} />
      </section>

      <section className="rounded-2xl border bg-white p-5 shadow-sm">
        <h2 className="text-lg font-bold">Evidence summary</h2>
        <div className="mt-3 grid gap-3 md:grid-cols-3">
          <Evidence icon={<BarChart3 size={18} />} label="Submitted assessments" value={String(attempts.length)} />
          <Evidence icon={<FileText size={18} />} label="Resume evidence" value={`${resumeScore}%`} />
          <Evidence icon={<Award size={18} />} label="Career readiness" value={`${careerScore}%`} />
        </div>
        <p className="mt-4 text-sm text-slate-500">The report does not invent missing evidence. Scores increase only when the corresponding profile information or activity is actually recorded.</p>
      </section>
    </div>
  );
}

function Mini({ label, value }: { label: string; value: string }) { return <div className="rounded-lg bg-white/10 px-3 py-2"><p className="text-xs text-cyan-100">{label}</p><p className="font-bold">{value}</p></div>; }
function Info({ icon, title, value, detail }: { icon: ReactNode; title: string; value: string; detail: string }) { return <div className="rounded-2xl border bg-white p-4 shadow-sm"><div className="flex items-center gap-2 text-cyan-600">{icon}<span className="text-sm font-semibold">{title}</span></div><p className="mt-2 font-bold text-slate-900">{value}</p><p className="mt-1 text-sm text-slate-500">{detail}</p></div>; }
function Evidence({ icon, label, value }: { icon: ReactNode; label: string; value: string }) { return <div className="rounded-xl bg-slate-50 p-4"><div className="flex items-center gap-2 text-slate-500">{icon}<span className="text-xs">{label}</span></div><p className="mt-2 text-xl font-bold text-slate-900">{value}</p></div>; }
