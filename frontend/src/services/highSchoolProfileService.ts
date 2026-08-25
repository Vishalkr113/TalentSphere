import { getCanonicalProfile, updateCanonicalProfile } from './canonicalProfileService';

export type HighSchoolClass = '9' | '10' | '11' | '12';
export type SchoolBoard = string;
export type HighSchoolStream =
    | 'Science - PCM'
    | 'Science - PCB'
    | 'Science - PCMB'
    | 'Commerce with Mathematics'
    | 'Commerce without Mathematics'
    | 'Humanities / Arts';

export interface HighSchoolProfile {
    id: string;
    userId: string;
    fullName: string;
    email: string;
    studentClass: HighSchoolClass;
    board: SchoolBoard;
    currentStream: HighSchoolStream | null;
    careerGoal: string;
    schoolName: string;
    city: string;
    state?: string;
    district?: string;
    profilePhoto?: string | null;
    createdAt: string;
    updatedAt: string;
}

export type HighSchoolProfileInput = {
    userId: string;
    fullName: string;
    email: string;
    studentClass: HighSchoolClass;
    board: SchoolBoard;
    currentStream: HighSchoolStream | null;
    careerGoal: string;
    schoolName: string;
    city: string;
    state?: string;
    district?: string;
    profilePhoto?: string | null;
};

export function getHighSchoolProfile(userId: string): HighSchoolProfile | null {
    const p = getCanonicalProfile(String(userId));
    if (!p || !p.student_class) return null;
    return {
        id: String(p.id),
        userId: String(p.user_id),
        fullName: p.full_name,
        email: p.email,
        studentClass: p.student_class as HighSchoolClass,
        board: p.board ?? '',
        currentStream: p.stream as HighSchoolStream | null,
        careerGoal: p.career_goal ?? '',
        schoolName: p.school_name ?? '',
        city: p.city ?? '',
        state: p.state ?? undefined,
        district: p.district ?? undefined,
        profilePhoto: p.profile_photo,
        createdAt: '',
        updatedAt: '',
    };
}

export function getAcademicProfileMissingFields(profile: HighSchoolProfile | null): string[] {
    if (!profile) {
        return ['Mobile Number', 'Date of Birth', 'Class', 'Board', 'Medium', 'Dream Career', 'Country', 'State', 'City'];
    }
    // Assessment-specific required data. Class 11/12 additionally require stream.
    const missing: string[] = [];
    if (!profile.fullName.trim()) missing.push('Full Name');
    if (!profile.studentClass) missing.push('Class');
    if (!profile.board.trim()) missing.push('Board');
    if (!profile.city.trim()) missing.push('City');
    if (!profile.state?.trim()) missing.push('State');
    if (isStreamRequired(profile.studentClass) && !profile.currentStream) missing.push('Interested Stream');
    return missing;
}

export function isAcademicProfileReady(profile: HighSchoolProfile | null): boolean {
    return getAcademicProfileMissingFields(profile).length === 0;
}

export async function saveHighSchoolProfile(input: HighSchoolProfileInput): Promise<HighSchoolProfile | null> {
    const p = await updateCanonicalProfile(input.userId, {
        school_name: input.schoolName,
        student_class: input.studentClass,
        board: input.board,
        stream: input.currentStream,
        career_goal: input.careerGoal,
        city: input.city,
        state: input.state ?? null,
        district: input.district ?? null,
        profile_photo: input.profilePhoto ?? null,
    });
    return getHighSchoolProfile(String(p.user_id));
}

export function getAssessmentPurpose(studentClass: HighSchoolClass) {
    switch (studentClass) {
        case '9': return { title: 'Foundation & Career Exploration Assessment', description: 'Understand your subject strengths, aptitude and interests early so you can build a strong Class 10 foundation and explore future stream directions.', reportTitle: 'Foundation & Early Career Direction Report' };
        case '10': return { title: 'Stream Guidance Assessment', description: 'Discover the most suitable academic stream based on your subject strengths, aptitude and reasoning ability.', reportTitle: 'Final Stream Guidance Report' };
        case '11': return { title: 'Stream Fit & Academic Direction Assessment', description: 'Evaluate how well your current stream matches your academic strengths and identify suitable future directions.', reportTitle: 'Stream Fit & Direction Report' };
        case '12': return { title: 'Post-12th Course & Career Guidance Assessment', description: 'Analyze your academic strengths and identify suitable courses and career directions after Class 12.', reportTitle: 'Post-12th Course & Career Guidance Report' };
    }
}

export function isStreamRequired(studentClass: HighSchoolClass) {
    return studentClass === '11' || studentClass === '12';
}

export function calculateProfileCompletion(profile: HighSchoolProfile | null) {
    if (!profile) return 0;
    const requiredValues = [profile.fullName, profile.email, profile.studentClass, profile.board, profile.city, profile.state ?? ''];
    if (isStreamRequired(profile.studentClass)) requiredValues.push(profile.currentStream ?? '');
    return Math.round((requiredValues.filter((value) => value.trim().length > 0).length / requiredValues.length) * 100);
}
