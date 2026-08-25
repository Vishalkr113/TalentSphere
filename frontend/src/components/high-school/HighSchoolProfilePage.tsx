import { useEffect, useMemo, useState } from "react";
import { CheckCircle2, Circle, MapPin, Pencil, Target, UserRound } from "lucide-react";
import HighSchoolProfileForm from "./HighSchoolProfileForm";
import { getCurrentUser } from "../../services/authService";
import {
  getCanonicalProfile,
  hydrateCanonicalProfile,
  updateCanonicalProfile,
  uploadProfilePhoto,
  type CanonicalProfile,
} from "../../services/canonicalProfileService";
import type { SelectOption } from "../common/Select/SearchSelect";

type FormProfile = any;

const emptyFormProfile: FormProfile = {
  profileImage: null,
  fullName: "",
  email: "",
  mobile: "",
  dob: "",
  gender: null,
  bloodGroup: null,
  school: "",
  class: null,
  board: null,
  medium: "",
  rollNumber: "",
  admissionYear: "",
  percentage: "",
  parent: { parentName: "", parentMobile: "", parentEmail: "", occupation: "" },
  address: { country: "", state: "", district: "", city: "", pinCode: "" },
  careerGoal: null,
  stream: null,
  favoriteSubject: null,
  weakSubject: null,
  skills: [],
  hobbies: [],
  languages: [],
  lastUpdated: "",
};

function textToOption(value: string | null | undefined): SelectOption | null {
  return value ? { value, label: value } : null;
}

function optionToText(option: SelectOption | null) {
  return option?.label ?? null;
}

function sectionReady(profile: CanonicalProfile | null, section: "basic" | "academic" | "location" | "career") {
  if (!profile) return false;
  if (section === "basic") return Boolean(profile.phone?.trim() && profile.date_of_birth);
  if (section === "academic") {
    const base = Boolean(profile.student_class?.trim() && profile.board?.trim() && profile.medium?.trim());
    if (!base) return false;
    return !["11", "12"].includes(profile.student_class ?? "") || Boolean(profile.stream?.trim());
  }
  if (section === "location") return Boolean(profile.country?.trim() && profile.state?.trim() && profile.city?.trim());
  return Boolean(profile.career_goal?.trim());
}

function SectionStatus({ ready }: { ready: boolean }) {
  return ready ? (
    <span className="inline-flex items-center gap-1 text-sm font-semibold text-emerald-600"><CheckCircle2 size={16} /> Complete</span>
  ) : (
    <span className="inline-flex items-center gap-1 text-sm font-semibold text-slate-400"><Circle size={16} /> In progress</span>
  );
}

export default function HighSchoolProfilePage() {
  const [profile, setProfile] = useState<FormProfile>(emptyFormProfile);
  const [canonical, setCanonical] = useState<CanonicalProfile | null>(null);
  const [loading, setLoading] = useState(true);
  const [editing, setEditing] = useState(false);

  async function loadProfile() {
    try {
      const user = await getCurrentUser();
      let backendProfile = getCanonicalProfile(String(user.id));
      if (!backendProfile) backendProfile = await hydrateCanonicalProfile(user as any);
      setCanonical(backendProfile);
      setProfile({
        ...emptyFormProfile,
        fullName: user.full_name || user.name || "",
        email: user.email || "",
        mobile: backendProfile.phone ?? "",
        dob: backendProfile.date_of_birth ?? "",
        gender: textToOption(backendProfile.gender),
        bloodGroup: textToOption(backendProfile.blood_group),
        school: backendProfile.school_name ?? "",
        class: textToOption(backendProfile.student_class),
        board: textToOption(backendProfile.board),
        medium: backendProfile.medium ?? "",
        rollNumber: backendProfile.roll_number ?? "",
        admissionYear: backendProfile.admission_year ? String(backendProfile.admission_year) : "",
        percentage: backendProfile.percentage ?? "",
        parent: {
          parentName: backendProfile.parent_name ?? "",
          parentMobile: backendProfile.parent_mobile ?? "",
          parentEmail: backendProfile.parent_email ?? "",
          occupation: backendProfile.parent_occupation ?? "",
        },
        address: {
          country: backendProfile.country ?? "",
          state: backendProfile.state ?? "",
          district: backendProfile.district ?? "",
          city: backendProfile.city ?? "",
          pinCode: backendProfile.pin_code ?? "",
        },
        careerGoal: textToOption(backendProfile.career_goal),
        stream: textToOption(backendProfile.stream),
        favoriteSubject: textToOption(backendProfile.favorite_subject),
        weakSubject: textToOption(backendProfile.weak_subject),
        skills: (backendProfile.skills ?? []).map((x: string) => ({ value: x, label: x })),
        hobbies: (backendProfile.hobbies ?? []).map((x: string) => ({ value: x, label: x })),
        languages: (backendProfile.languages ?? []).map((x: string) => ({ value: x, label: x })),
        profileImage: backendProfile.profile_photo ?? null,
      });
    } catch (error) {
      console.error("Profile load error", error);
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => { void loadProfile(); }, []);

  const completion = Math.max(0, Math.min(100, canonical?.profile_completion ?? 0));
  const sections = useMemo(() => ({
    basic: sectionReady(canonical, "basic"),
    academic: sectionReady(canonical, "academic"),
    location: sectionReady(canonical, "location"),
    career: sectionReady(canonical, "career"),
  }), [canonical]);

  async function saveProfile(data: FormProfile) {
    try {
      const user = await getCurrentUser();
      const updated = await updateCanonicalProfile(String(user.id), {
        phone: data.mobile,
        date_of_birth: data.dob || null,
        gender: optionToText(data.gender),
        city: data.address.city,
        state: data.address.state,
        country: data.address.country,
        district: data.address.district,
        pin_code: data.address.pinCode,
        career_goal: optionToText(data.careerGoal),
        school_name: data.school || null,
        student_class: optionToText(data.class),
        board: optionToText(data.board),
        stream: optionToText(data.stream),
        medium: data.medium || null,
      });
      let finalProfile = updated;
      if (data.profileImage && data.profileImage.startsWith("data:")) {
        try {
          const response = await fetch(data.profileImage);
          const blob = await response.blob();
          const file = new File([blob], "profile-photo.jpg", { type: blob.type || "image/jpeg" });
          finalProfile = await uploadProfilePhoto(String(user.id), file);
        } catch (photoError) {
          console.warn("Profile photo upload failed; other profile data was saved.", photoError);
        }
      }
      setCanonical(finalProfile);
      setEditing(false);
      await loadProfile();
    } catch (error) {
      console.error("Profile save failed:", error);
      alert(`Profile save failed: ${error instanceof Error ? error.message : "Please try again."}`);
    }
  }

  if (loading) return <div className="p-6">Loading profile...</div>;

  if (editing) {
    return (
      <HighSchoolProfileForm
        initialData={profile}
        onSave={saveProfile}
        onCancel={() => { setEditing(false); void loadProfile(); }}
      />
    );
  }

  return (
    <div className="space-y-5 rounded-[28px] bg-slate-50 p-4 sm:p-6">
      <section className="overflow-hidden rounded-[28px] bg-white shadow-sm">
        <div className="bg-gradient-to-r from-cyan-50 via-white to-blue-50 p-6 sm:p-8">
          <div className="flex flex-wrap items-start justify-between gap-5">
            <div className="flex items-center gap-4">
              <div className="flex h-16 w-16 items-center justify-center rounded-2xl bg-cyan-600 text-xl font-bold text-white shadow-sm">
                {(profile.fullName || "U").trim().charAt(0).toUpperCase()}
              </div>
              <div>
                <p className="text-sm font-semibold text-cyan-600">MY PROFILE</p>
                <h1 className="mt-1 text-3xl font-bold text-slate-900">{profile.fullName || "Your Profile"}</h1>
                <p className="mt-1 text-sm text-slate-500">Your academic and career profile</p>
              </div>
            </div>
            <button type="button" onClick={() => setEditing(true)} className="inline-flex items-center gap-2 rounded-xl bg-cyan-600 px-5 py-3 font-semibold text-white shadow-sm hover:bg-cyan-700">
              <Pencil size={17} /> Edit Profile
            </button>
          </div>

          <div className="mt-7 rounded-2xl border border-white/80 bg-white/80 p-5 backdrop-blur">
            <div className="flex flex-wrap items-center justify-between gap-2">
              <div>
                <p className="font-bold text-slate-900">Profile completion</p>
                <p className="mt-1 text-sm text-slate-500">Complete the essentials to unlock personalized features.</p>
              </div>
              <span className="text-2xl font-bold text-cyan-700">{completion}%</span>
            </div>
            <div className="mt-4 h-2.5 overflow-hidden rounded-full bg-slate-100">
              <div className="h-full rounded-full bg-cyan-600 transition-all" style={{ width: `${completion}%` }} />
            </div>
          </div>
        </div>

        <div className="grid gap-px bg-slate-100 sm:grid-cols-2 lg:grid-cols-4">
          {([
            ["Basic Information", sections.basic],
            ["Academic Information", sections.academic],
            ["Location", sections.location],
            ["Career Goal", sections.career],
          ] as const).map(([label, ready]) => (
            <div key={label} className="bg-white p-5">
              <p className="text-sm font-semibold text-slate-700">{label}</p>
              <div className="mt-2"><SectionStatus ready={ready} /></div>
            </div>
          ))}
        </div>
      </section>

      <div className="grid gap-5 lg:grid-cols-2">
        <section className="rounded-2xl bg-white p-6 shadow-sm">
          <div className="flex items-center gap-3"><UserRound className="text-cyan-600" size={21} /><h2 className="text-lg font-bold text-slate-900">Academic Profile</h2></div>
          <div className="mt-5 grid gap-4 sm:grid-cols-2">
            <div><p className="text-xs uppercase tracking-wide text-slate-400">Class</p><p className="mt-1 font-semibold text-slate-800">{profile.class?.label || "Not set"}</p></div>
            <div><p className="text-xs uppercase tracking-wide text-slate-400">Board</p><p className="mt-1 font-semibold text-slate-800">{profile.board?.label || "Not set"}</p></div>
            <div><p className="text-xs uppercase tracking-wide text-slate-400">Stream</p><p className="mt-1 font-semibold text-slate-800">{profile.stream?.label || "Not required"}</p></div>
            <div><p className="text-xs uppercase tracking-wide text-slate-400">Medium</p><p className="mt-1 font-semibold text-slate-800">{profile.medium || "Not set"}</p></div>
            {profile.school && <div className="sm:col-span-2"><p className="text-xs uppercase tracking-wide text-slate-400">School</p><p className="mt-1 font-semibold text-slate-800">{profile.school}</p></div>}
          </div>
        </section>

        <section className="rounded-2xl bg-white p-6 shadow-sm">
          <div className="flex items-center gap-3"><Target className="text-cyan-600" size={21} /><h2 className="text-lg font-bold text-slate-900">Career Direction</h2></div>
          <p className="mt-5 text-xs uppercase tracking-wide text-slate-400">Dream Career</p>
          <p className="mt-1 text-lg font-bold text-slate-900">{profile.careerGoal?.label || "Not set"}</p>
          <div className="mt-5 flex items-start gap-3 rounded-xl bg-slate-50 p-4"><MapPin size={19} className="mt-0.5 text-cyan-600" /><div><p className="text-xs uppercase tracking-wide text-slate-400">Location</p><p className="mt-1 font-semibold text-slate-800">{[profile.address.city, profile.address.state].filter(Boolean).join(", ") || "Not set"}</p></div></div>
        </section>
      </div>
    </div>
  );
}
