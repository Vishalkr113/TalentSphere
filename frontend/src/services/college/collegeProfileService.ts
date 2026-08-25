import { getCanonicalProfile, updateCanonicalProfile } from '../canonicalProfileService';

export type CollegeProfileData = {
    fullName: string;
    email: string;
    photo?: string;
    college: string;
    university: string;
    degree: string;
    branch: string;
    semester: string;
    cgpa: string;
    phone: string;
    city: string;
    state: string;
    linkedin: string;
    github: string;
    portfolio: string;
    careerGoal: string;
    targetRole: string;
    skills: string;
};

const empty: CollegeProfileData = {
    fullName: '', email: '', college: '', university: '', degree: '', branch: '', semester: '', cgpa: '', phone: '', city: '', state: '', linkedin: '', github: '', portfolio: '', careerGoal: '', targetRole: '', skills: '',
};

export const getCollegeProfile = (u: string): CollegeProfileData => {
    const p = getCanonicalProfile(u);
    if (!p) return { ...empty };
    return {
        fullName: p.full_name,
        email: p.email,
        photo: p.profile_photo ?? undefined,
        college: p.college_name ?? '',
        university: p.university_name ?? '',
        degree: p.course ?? '',
        branch: p.branch ?? '',
        semester: p.semester ?? '',
        cgpa: p.cgpa ?? '',
        phone: p.phone ?? '',
        city: p.city ?? '',
        state: p.state ?? '',
        linkedin: p.linkedin_url ?? '',
        github: p.github_url ?? '',
        portfolio: p.portfolio_url ?? '',
        careerGoal: p.career_goal ?? '',
        targetRole: p.target_role ?? '',
        skills: p.skills.join(', '),
    };
};

export const saveCollegeProfile = async (u: string, v: CollegeProfileData) => {
    return updateCanonicalProfile(u, {
        college_name: v.college,
        university_name: v.university,
        course: v.degree,
        branch: v.branch,
        semester: v.semester,
        cgpa: v.cgpa,
        phone: v.phone,
        city: v.city,
        state: v.state,
        linkedin_url: v.linkedin,
        github_url: v.github,
        portfolio_url: v.portfolio,
        career_goal: v.careerGoal,
        target_role: v.targetRole,
        skills: v.skills.split(',').map((x) => x.trim()).filter(Boolean),
    });
};

export const isCollegeProfileReady = (p: CollegeProfileData) => Boolean(p.degree.trim() && p.branch.trim() && p.semester.trim());

export const getCollegeProfileCompletion = (p: CollegeProfileData) => {
    const fields: (keyof CollegeProfileData)[] = ['fullName','email','college','university','degree','branch','semester','cgpa','phone','city','careerGoal','targetRole','skills'];
    return Math.round((fields.filter((k) => String(p[k] || '').trim()).length / fields.length) * 100);
};
