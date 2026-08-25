import { getCanonicalProfile, updateCanonicalProfile } from './canonicalProfileService';

export type ProfessionalProfile = {
    fullName: string;
    email: string;
    company: string;
    designation: string;
    experience: string;
    yearsOfExperience: string;
    industry: string;
    skills: string;
    phone: string;
    city: string;
    state: string;
    linkedin: string;
    github: string;
    portfolio: string;
    expectedSalary: string;
    careerGoal: string;
    targetRole: string;
};

export type ProfessionalEvidence = {
    assessmentScores: number[];
    interviewScores: number[];
    certifications: string[];
    learningCompleted: string[];
    applications: { company: string; role: string; status: string }[];
    resumeText: string;
};

export const emptyProfessionalProfile = (name = '', email = ''): ProfessionalProfile => ({
    fullName: name, email, company: '', designation: '', experience: '', yearsOfExperience: '', industry: '', skills: '', phone: '', city: '', state: '', linkedin: '', github: '', portfolio: '', expectedSalary: '', careerGoal: '', targetRole: '',
});

export function getProfessionalProfile(id: string, name = '', email = ''): ProfessionalProfile {
    const p = getCanonicalProfile(id);
    if (!p) return emptyProfessionalProfile(name, email);
    return {
        fullName: p.full_name || name,
        email: p.email || email,
        company: p.company_name ?? '',
        designation: p.job_title ?? '',
        experience: p.experience_level ?? '',
        yearsOfExperience: p.years_of_experience == null ? '' : String(p.years_of_experience),
        industry: p.professional_domain ?? '',
        skills: p.skills.join(', '),
        phone: p.phone ?? '',
        city: p.city ?? '',
        state: p.state ?? '',
        linkedin: p.linkedin_url ?? '',
        github: p.github_url ?? '',
        portfolio: p.portfolio_url ?? '',
        expectedSalary: p.expected_salary ?? '',
        careerGoal: p.career_goal ?? '',
        targetRole: p.target_role ?? '',
    };
}

export function saveProfessionalProfile(id: string, v: ProfessionalProfile) {
    return updateCanonicalProfile(id, {
        company_name: v.company,
        job_title: v.designation,
        experience_level: v.experience,
        years_of_experience: v.yearsOfExperience ? Number(v.yearsOfExperience) : null,
        professional_domain: v.industry,
        skills: v.skills.split(',').map((x) => x.trim()).filter(Boolean),
        phone: v.phone,
        city: v.city,
        state: v.state,
        linkedin_url: v.linkedin,
        github_url: v.github,
        portfolio_url: v.portfolio,
        expected_salary: v.expectedSalary,
        career_goal: v.careerGoal,
        target_role: v.targetRole,
    });
}

const evidenceKey = (id: string) => `talentsphere_professional_evidence_${id}`;

export const emptyEvidence = (): ProfessionalEvidence => ({
    assessmentScores: [], interviewScores: [], certifications: [], learningCompleted: [], applications: [], resumeText: '',
});

export function getProfessionalEvidence(id: string): ProfessionalEvidence {
    try {
        const parsed = JSON.parse(localStorage.getItem(evidenceKey(id)) || '{}');
        const evidence: ProfessionalEvidence = { ...emptyEvidence(), ...parsed };

        // Interview evidence is a single current evidence level, not an accumulating history.
        // Migrate old localStorage data that may contain [40, 60, 80, ...].
        const interviewScores = Array.isArray(evidence.interviewScores)
            ? evidence.interviewScores.filter((value): value is number =>
                typeof value === 'number' && Number.isFinite(value) && value >= 0 && value <= 100,
            )
            : [];
        evidence.interviewScores = interviewScores.length ? [interviewScores[interviewScores.length - 1]] : [];

        return evidence;
    } catch {
        return emptyEvidence();
    }
}

export function saveProfessionalEvidence(id: string, v: ProfessionalEvidence) {
    const next: ProfessionalEvidence = {
        ...v,
        interviewScores: Array.isArray(v.interviewScores) && v.interviewScores.length
            ? [v.interviewScores[v.interviewScores.length - 1]]
            : [],
    };
    localStorage.setItem(evidenceKey(id), JSON.stringify(next));
}

const avg = (a: number[]) => a.length ? Math.round(a.reduce((x, y) => x + y, 0) / a.length) : 0;

export function professionalStats(id: string, name = '', email = '') {
    const p = getProfessionalProfile(id, name, email);
    const e = getProfessionalEvidence(id);
    const profileFields = [p.company, p.designation, p.experience, p.industry, p.skills, p.careerGoal, p.targetRole];
    const profile = Math.round((profileFields.filter(Boolean).length / profileFields.length) * 100);
    const skill = avg(e.assessmentScores);
    const interview = avg(e.interviewScores);
    const resume = Math.min(100, (p.skills ? 20 : 0) + (p.designation ? 15 : 0) + (p.company ? 15 : 0) + (p.linkedin ? 15 : 0) + (p.portfolio || p.github ? 15 : 0) + (e.resumeText.trim().length > 120 ? 20 : 0));
    const certification = Math.min(100, e.certifications.length * 20);
    const learning = Math.min(100, e.learningCompleted.length * 20);
    const promotion = Math.round(profile * 0.2 + skill * 0.3 + interview * 0.2 + resume * 0.2 + certification * 0.1);
    const career = Math.round((promotion + learning + skill) / 3);
    return { profile, skill, interview, resume, certification, learning, promotion, career, e, p };
}

export const roleSkills = (role: string) => {
    const r = role.toLowerCase();
    if (r.includes('data')) return ['SQL', 'Python', 'Data Visualization', 'Statistics'];
    if (r.includes('manager') || r.includes('lead')) return ['Leadership', 'Communication', 'Stakeholder Management', 'Planning'];
    if (r.includes('cloud')) return ['Cloud', 'Docker', 'Networking', 'Security'];
    return ['Communication', 'Problem Solving', 'Industry Knowledge', 'Leadership'];
};
