import { API_BASE_URL, api, request } from './api';
import { getToken, type AuthUser } from './authService';

export type CanonicalProfile = {
  role: AuthUser['role'];
  id: number;
  user_id: number;
  full_name: string;
  email: string;
  phone: string | null;
  date_of_birth: string | null;
  gender: string | null;
  city: string | null;
  state: string | null;
  country: string | null;
  district: string | null;
  pin_code: string | null;
  skills: string[];
  interests: string[];
  hobbies: string[];
  languages: string[];
  career_goal: string | null;
  target_role: string | null;
  linkedin_url: string | null;
  github_url: string | null;
  portfolio_url: string | null;
  profile_photo: string | null;
  resume_url: string | null;
  profile_completion: number;
  school_name: string | null;
  student_class: string | null;
  stream: string | null;
  board: string | null;
  medium: string | null;
  roll_number: string | null;
  admission_year: number | null;
  percentage: string | null;
  blood_group: string | null;
  parent_name: string | null;
  parent_mobile: string | null;
  parent_email: string | null;
  parent_occupation: string | null;
  favorite_subject: string | null;
  weak_subject: string | null;
  college_name: string | null;
  university_name: string | null;
  course: string | null;
  branch: string | null;
  semester: string | null;
  cgpa: string | null;
  graduation_year: number | null;
  company_name: string | null;
  job_title: string | null;
  professional_domain: string | null;
  experience_level: string | null;
  years_of_experience: number | null;
  expected_salary: string | null;
};

type ProfileResponse = Omit<CanonicalProfile, 'full_name' | 'email'>;

const cache = new Map<string, CanonicalProfile>();

const emptyProfile = (user: AuthUser): CanonicalProfile => ({
  role: user.role,
  id: 0,
  user_id: Number(user.id),
  full_name: user.full_name || user.name || '',
  email: user.email,
  phone: null,
  date_of_birth: null,
  gender: null,
  city: null,
  state: null,
  country: null,
  district: null,
  pin_code: null,
  skills: [],
  interests: [],
  hobbies: [],
  languages: [],
  career_goal: null,
  target_role: null,
  linkedin_url: null,
  github_url: null,
  portfolio_url: null,
  profile_photo: null,
  resume_url: null,
  profile_completion: 0,
  school_name: null,
  student_class: null,
  stream: null,
  board: null,
  medium: null,
  roll_number: null,
  admission_year: null,
  percentage: null,
  blood_group: null,
  parent_name: null,
  parent_mobile: null,
  parent_email: null,
  parent_occupation: null,
  favorite_subject: null,
  weak_subject: null,
  college_name: null,
  university_name: null,
  course: null,
  branch: null,
  semester: null,
  cgpa: null,
  graduation_year: null,
  company_name: null,
  job_title: null,
  professional_domain: null,
  experience_level: null,
  years_of_experience: null,
  expected_salary: null,
});

function mediaUrl(value: string | null | undefined): string | null {
  if (!value) return null;
  if (/^https?:\/\//i.test(value) || value.startsWith('data:')) return value;
  const normalized = value.replace(/^\/+/, '');
  return `${API_BASE_URL}/${normalized}`;
}

function normalizeProfile(user: AuthUser, profile: ProfileResponse): CanonicalProfile {
  return {
    ...emptyProfile(user),
    ...profile,
    role: user.role,
    profile_photo: mediaUrl(profile.profile_photo),
    resume_url: mediaUrl(profile.resume_url),
    full_name: user.full_name || user.name || '',
    email: user.email,
    skills: Array.isArray(profile.skills) ? profile.skills : [],
    interests: Array.isArray(profile.interests) ? profile.interests : [],
    hobbies: Array.isArray(profile.hobbies) ? profile.hobbies : [],
    languages: Array.isArray(profile.languages) ? profile.languages : [],
  };
}

function legacyString(value: unknown): string | null {
  if (typeof value !== 'string') return null;
  const trimmed = value.trim();
  return trimmed ? trimmed : null;
}



function readJson(key: string): unknown {
  try {
    const value = localStorage.getItem(key);
    return value ? JSON.parse(value) : null;
  } catch {
    return null;
  }
}

function legacyPayload(userId: string, role: AuthUser['role']): Record<string, unknown> | null {
  if (role === 'college_student') {
    const raw = readJson(`college_profile_${userId}`) as Record<string, unknown> | null;
    if (!raw) return null;
    return {
      college_name: legacyString(raw.college),
      university_name: legacyString(raw.university),
      course: legacyString(raw.degree),
      branch: legacyString(raw.branch),
      semester: legacyString(raw.semester),
      cgpa: legacyString(raw.cgpa),
      phone: legacyString(raw.phone),
      city: legacyString(raw.city),
      state: legacyString(raw.state),
      linkedin_url: legacyString(raw.linkedin),
      github_url: legacyString(raw.github),
      portfolio_url: legacyString(raw.portfolio),
      career_goal: legacyString(raw.careerGoal),
      target_role: legacyString(raw.targetRole),
      skills: legacyString(raw.skills)?.split(',').map((x) => x.trim()).filter(Boolean) ?? [],
    };
  }

  if (role === 'working_professional') {
    const raw = readJson(`talentsphere_professional_profile_${userId}`) as Record<string, unknown> | null;
    if (!raw) return null;
    return {
      company_name: legacyString(raw.company),
      job_title: legacyString(raw.designation),
      professional_domain: legacyString(raw.industry),
      experience_level: legacyString(raw.experience),
      phone: legacyString(raw.phone),
      city: legacyString(raw.city),
      state: legacyString(raw.state),
      linkedin_url: legacyString(raw.linkedin),
      github_url: legacyString(raw.github),
      portfolio_url: legacyString(raw.portfolio),
      career_goal: legacyString(raw.careerGoal),
      target_role: legacyString(raw.targetRole),
      expected_salary: legacyString(raw.expectedSalary),
      skills: legacyString(raw.skills)?.split(',').map((x) => x.trim()).filter(Boolean) ?? [],
    };
  }

  const rawProfiles = readJson('talentsphere_high_school_profiles');
  if (Array.isArray(rawProfiles)) {
    const raw = rawProfiles.find((item) => item && typeof item === 'object' && String((item as {userId?: unknown}).userId) === userId) as Record<string, unknown> | undefined;
    if (raw) {
      return {
        school_name: legacyString(raw.schoolName),
        student_class: legacyString(raw.studentClass),
        board: legacyString(raw.board),
        stream: legacyString(raw.currentStream),
        career_goal: legacyString(raw.careerGoal),
        city: legacyString(raw.city),
        state: legacyString(raw.state),
        district: legacyString(raw.district),
        profile_photo: legacyString(raw.profilePhoto),
      };
    }
  }
  return null;
}

function hasLegacyData(payload: Record<string, unknown> | null): boolean {
  if (!payload) return false;
  return Object.entries(payload).some(([key, value]) => key === 'skills' || Array.isArray(value) ? Array.isArray(value) ? value.length > 0 : Boolean(value) : Boolean(value));
}

function clearLegacyProfile(userId: string, role: AuthUser['role']) {
  if (role === 'college_student') {
    localStorage.removeItem(`college_profile_${userId}`);
  } else if (role === 'working_professional') {
    localStorage.removeItem(`talentsphere_professional_profile_${userId}`);
  } else {
    const raw = readJson('talentsphere_high_school_profiles');
    if (Array.isArray(raw)) {
      const remaining = raw.filter((item) => String(item?.userId ?? '') !== userId);
      localStorage.setItem('talentsphere_high_school_profiles', JSON.stringify(remaining));
    }
  }
}

export async function hydrateCanonicalProfile(user: AuthUser): Promise<CanonicalProfile> {
  const token = getToken() ?? undefined;
  let response: ProfileResponse;
  try {
    response = await api.get<ProfileResponse>('/profile/me', token);
  } catch (error) {
    const message = error instanceof Error ? error.message : '';
    if (!message.toLowerCase().includes('profile not found')) throw error;
    response = await api.post<ProfileResponse>('/profile', {}, token);
  }

  let profile = normalizeProfile(user, response);
  const legacy = legacyPayload(user.id, user.role);

  if (profile.profile_completion === 0 && hasLegacyData(legacy)) {
    const migrated = await api.patch<ProfileResponse>('/profile/me', legacy, token);
    profile = normalizeProfile(user, migrated);
    clearLegacyProfile(user.id, user.role);
  }

  cache.set(String(user.id), profile);
  return profile;
}

export function getCanonicalProfile(userId: string): CanonicalProfile | null {
  return cache.get(userId) ?? null;
}


export function getHighSchoolAssessmentMissingFields(profile: CanonicalProfile | null): string[] {
  if (!profile) {
    return ['Mobile Number', 'Date of Birth', 'Class', 'Board', 'Medium', 'Dream Career', 'Country', 'State', 'City'];
  }
  const missing: string[] = [];
  if (!profile.full_name?.trim()) missing.push('Full Name');
  if (!profile.phone?.trim()) missing.push('Mobile Number');
  if (!profile.date_of_birth) missing.push('Date of Birth');
  if (!profile.student_class?.trim()) missing.push('Class');
  if (!profile.board?.trim()) missing.push('Board');
  if (!profile.medium?.trim()) missing.push('Medium');
  if (!profile.career_goal?.trim()) missing.push('Dream Career');
  if (!profile.country?.trim()) missing.push('Country');
  if (!profile.state?.trim()) missing.push('State');
  if (!profile.city?.trim()) missing.push('City');
  if (profile.student_class === '11' || profile.student_class === '12') {
    if (!profile.stream?.trim()) missing.push('Interested Stream');
  }
  return missing;
}

export function isHighSchoolAssessmentReady(profile: CanonicalProfile | null): boolean {
  return getHighSchoolAssessmentMissingFields(profile).length === 0;
}

export async function updateCanonicalProfile(userId: string, data: Record<string, unknown>): Promise<CanonicalProfile> {
  const current = cache.get(String(userId));
  if (!current) throw new Error('Profile has not been hydrated yet.');
  const updated = await api.patch<ProfileResponse>('/profile/me', data, getToken() ?? undefined);
  const merged = normalizeProfile({ id: userId, full_name: current.full_name, email: current.email, role: current.role }, updated);
  cache.set(String(userId), merged);
  window.dispatchEvent(new CustomEvent('talentsphere:profile-updated', { detail: merged }));
  return merged;
}


export async function uploadProfilePhoto(userId: string, file: File): Promise<CanonicalProfile> {
  const form = new FormData();
  form.append('file', file);
  const updated = await request<ProfileResponse>('/profile/photo', {
    method: 'POST',
    token: getToken() ?? undefined,
    body: form,
  });
  const current = cache.get(String(userId));
  if (!current) throw new Error('Profile has not been hydrated yet.');
  const merged = normalizeProfile({
    id: userId,
    full_name: current.full_name,
    email: current.email,
    role: current.role,
  }, updated);
  cache.set(String(userId), merged);
  window.dispatchEvent(new CustomEvent('talentsphere:profile-updated', { detail: merged }));
  return merged;
}

export function replaceCachedProfile(profile: CanonicalProfile) {
  cache.set(String(profile.user_id), profile);
}


export async function deleteProfilePhoto(userId: string): Promise<CanonicalProfile> {
  const updated = await request<ProfileResponse>('/profile/photo', {
    method: 'DELETE',
    token: getToken() ?? undefined,
  });
  const current = cache.get(String(userId));
  if (!current) throw new Error('Profile has not been hydrated yet.');
  const merged = normalizeProfile({
    id: userId,
    full_name: current.full_name,
    email: current.email,
    role: current.role,
  }, updated);
  cache.set(String(userId), merged);
  window.dispatchEvent(new CustomEvent('talentsphere:profile-updated', { detail: merged }));
  return merged;
}
