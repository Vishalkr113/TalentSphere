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

const key = (u: string) =>
    `college_profile_${u || 'guest'}`;

const empty: CollegeProfileData = {
    fullName: '',
    email: '',
    college: '',
    university: '',
    degree: '',
    branch: '',
    semester: '',
    cgpa: '',
    phone: '',
    city: '',
    state: '',
    linkedin: '',
    github: '',
    portfolio: '',
    careerGoal: '',
    targetRole: '',
    skills: '',
};

export const getCollegeProfile = (
    u: string
): CollegeProfileData => {
    try {
        return {
            ...empty,
            ...JSON.parse(
                localStorage.getItem(key(u)) || '{}'
            ),
        };
    } catch {
        return { ...empty };
    }
};

export const saveCollegeProfile = (
    u: string,
    v: CollegeProfileData
) =>
    localStorage.setItem(
        key(u),
        JSON.stringify(v)
    );

export const isCollegeProfileReady = (
    p: CollegeProfileData
) =>
    Boolean(
        p.degree.trim() &&
        p.branch.trim() &&
        p.semester.trim()
    );

export const getCollegeProfileCompletion = (
    p: CollegeProfileData
) => {
    const fields: [
        keyof CollegeProfileData,
        ...(keyof CollegeProfileData)[]
    ] = [
            'fullName',
            'email',
            'college',
            'university',
            'degree',
            'branch',
            'semester',
            'cgpa',
            'phone',
            'city',
            'careerGoal',
            'targetRole',
            'skills',
        ];

    return Math.round(
        (fields.filter((k) =>
            String(p[k] || '').trim()
        ).length /
            fields.length) *
        100
    );
};