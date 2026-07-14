import { useEffect, useState } from "react";
import {
  BookOpen, CheckCircle2, GraduationCap, LocateFixed,
  MapPin, Pencil, Save, School, Target, User,
} from "lucide-react";

import { useAuth } from "../../contexts/AuthContext";
import ProfilePhoto from "../common/Profile/ProfilePhoto";
import { boardNames } from "../../data/academic/boards";
import {
  calculateProfileCompletion, getAssessmentPurpose, getHighSchoolProfile,
  isStreamRequired, saveHighSchoolProfile,
  type HighSchoolClass, type HighSchoolProfile as HighSchoolProfileData,
  type HighSchoolStream, type SchoolBoard,
} from "../../services/highSchoolProfileService";

const classOptions: HighSchoolClass[] = ["10", "11", "12"];
const streamOptions: HighSchoolStream[] = [
  "Science - PCM", "Science - PCB", "Science - PCMB",
  "Commerce with Mathematics", "Commerce without Mathematics", "Humanities / Arts",
];

function HighSchoolProfile() {
  const { user } = useAuth();
  const [studentClass, setStudentClass] = useState<HighSchoolClass>("10");
  const [board, setBoard] = useState<SchoolBoard>("CBSE");
  const [currentStream, setCurrentStream] = useState<HighSchoolStream | "">("");
  const [schoolName, setSchoolName] = useState("");
  const [state, setState] = useState("");
  const [district, setDistrict] = useState("");
  const [city, setCity] = useState("");
  const [careerGoal, setCareerGoal] = useState("");
  const [profilePhoto, setProfilePhoto] = useState<string | null>(null);
  const [savedProfile, setSavedProfile] = useState<HighSchoolProfileData | null>(null);
  const [isEditing, setIsEditing] = useState(false);
  const [locating, setLocating] = useState(false);
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");

  useEffect(() => {
    if (!user) return;
    const profile = getHighSchoolProfile(user.id);
    if (!profile) {
      setIsEditing(true);
      return;
    }
    setSavedProfile(profile);
    setStudentClass(profile.studentClass);
    setBoard(profile.board);
    setCurrentStream(profile.currentStream ?? "");
    setSchoolName(profile.schoolName);
    setState(profile.state ?? "");
    setDistrict(profile.district ?? "");
    setCity(profile.city);
    setCareerGoal(profile.careerGoal);
    setProfilePhoto(profile.profilePhoto ?? null);
  }, [user]);

  const streamRequired = isStreamRequired(studentClass);
  const assessmentPurpose = getAssessmentPurpose(studentClass);
  const profileCompletion = calculateProfileCompletion(savedProfile);
  const fieldClass = `w-full rounded-xl border px-4 py-2.5 text-slate-700 outline-none transition ${
    isEditing
      ? "border-slate-300 bg-white focus:border-cyan-500 focus:ring-2 focus:ring-cyan-100"
      : "cursor-not-allowed border-slate-200 bg-slate-100 text-slate-600"
  }`;

  const handleClassChange = (selectedClass: HighSchoolClass) => {
    setStudentClass(selectedClass);
    setError("");
    setSuccess("");
    if (selectedClass === "10") setCurrentStream("");
  };

  const useCurrentLocation = () => {
    setError("");
    setSuccess("");
    if (!navigator.geolocation) {
      setError("Current location is not supported by this browser.");
      return;
    }
    setLocating(true);
    navigator.geolocation.getCurrentPosition(
      async ({ coords }) => {
        try {
          const response = await fetch(
            `https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat=${coords.latitude}&lon=${coords.longitude}`,
            { headers: { "Accept-Language": "en" } }
          );
          if (!response.ok) throw new Error("Location lookup failed");
          const data = await response.json();
          const address = data.address ?? {};
          setCity(address.city || address.town || address.village || address.municipality || "");
          setDistrict(address.state_district || address.county || "");
          setState(address.state || "");
          setSuccess("Current location detected. Review it and save your profile.");
        } catch {
          setError("Location was detected, but city details could not be loaded. Please enter them manually.");
        } finally {
          setLocating(false);
        }
      },
      () => {
        setLocating(false);
        setError("Location permission was denied or unavailable. Please enter your location manually.");
      },
      { enableHighAccuracy: true, timeout: 12000 }
    );
  };

  const handleSave = (event: React.FormEvent) => {
    event.preventDefault();
    setError("");
    setSuccess("");
    if (!user) return setError("Please login again to update your profile.");
    if (!schoolName.trim()) return setError("Please enter your school name.");
    if (!state.trim()) return setError("Please enter your state.");
    if (!district.trim()) return setError("Please enter your district.");
    if (!city.trim()) return setError("Please enter your city.");
    if (streamRequired && !currentStream) return setError("Please select your current stream.");

    const profile = saveHighSchoolProfile({
      userId: user.id, fullName: user.name, email: user.email,
      studentClass, board,
      currentStream: studentClass === "10" ? null : (currentStream as HighSchoolStream),
      careerGoal: careerGoal.trim(), schoolName: schoolName.trim(),
      city: city.trim(), state: state.trim(), district: district.trim(),
      profilePhoto,
    });
    setSavedProfile(profile);
    setIsEditing(false);
    setSuccess("Profile saved successfully.");
  };

  if (!user) return null;

  return (
    <div className="mx-auto max-w-5xl space-y-5">
      <div className="flex flex-col justify-between gap-3 sm:flex-row sm:items-end">
        <div>
          <h1 className="text-3xl font-bold text-slate-900">My Profile</h1>
          <p className="mt-1 text-slate-600">
            Keep your academic and location details updated for personalized guidance.
          </p>
        </div>
        <button type="button" onClick={() => setIsEditing(true)}
          className="flex items-center justify-center gap-2 rounded-xl border border-cyan-200 bg-white px-5 py-2.5 font-semibold text-cyan-700 transition hover:bg-cyan-50">
          <Pencil size={17} /> Edit Profile
        </button>
      </div>

      <div className="grid gap-5 lg:grid-cols-[280px_1fr]">
        <ProfilePhoto image={profilePhoto} editable={isEditing} name={user.name} onChange={setProfilePhoto} />

        <div className="rounded-3xl bg-gradient-to-r from-cyan-600 to-blue-600 p-6 text-white shadow-lg">
          <p className="text-sm font-medium text-cyan-100">High School Student</p>
          <h2 className="mt-1 text-2xl font-bold">{user.name}</h2>
          <p className="mt-1 text-cyan-100">{user.email}</p>
          <div className="mt-6 rounded-2xl bg-white/10 p-4">
            <div className="flex items-center justify-between">
              <p className="text-sm text-cyan-100">Profile Completion</p>
              <p className="font-bold">{profileCompletion}%</p>
            </div>
            <div className="mt-3 h-2.5 overflow-hidden rounded-full bg-white/20">
              <div className="h-full rounded-full bg-white transition-all" style={{ width: `${profileCompletion}%` }} />
            </div>
          </div>
        </div>
      </div>

      <form onSubmit={handleSave} className="rounded-3xl border border-slate-200 bg-white p-6 shadow-sm">
        <div>
          <h2 className="text-2xl font-bold text-slate-900">Academic Profile</h2>
          <p className="mt-1 text-slate-500">Your details determine the guidance and assessment context you receive.</p>
        </div>

        <div className="mt-6 grid gap-5 md:grid-cols-2">
          <Field label="Full Name" icon={<User size={18} />}><input value={user.name} disabled className={fieldClass} /></Field>
          <Field label="Email"><input value={user.email} disabled className={fieldClass} /></Field>

          <Field label="Class" icon={<GraduationCap size={18} />}>
            <select value={studentClass} disabled={!isEditing} onChange={(e) => handleClassChange(e.target.value as HighSchoolClass)} className={fieldClass}>
              {classOptions.map((item) => <option key={item} value={item}>Class {item}</option>)}
            </select>
          </Field>

          <Field label="Board" icon={<BookOpen size={18} />}>
            <select value={board} disabled={!isEditing} onChange={(e) => setBoard(e.target.value)} className={fieldClass}>
              {boardNames.map((item) => <option key={item} value={item}>{item}</option>)}
            </select>
          </Field>

          {streamRequired && (
            <div className="md:col-span-2">
              <label className="mb-2 block text-sm font-semibold text-slate-700">Current Stream</label>
              <select value={currentStream} disabled={!isEditing} onChange={(e) => setCurrentStream(e.target.value as HighSchoolStream)} className={fieldClass}>
                <option value="">Select your current stream</option>
                {streamOptions.map((item) => <option key={item} value={item}>{item}</option>)}
              </select>
            </div>
          )}

          <Field label="School Name" icon={<School size={18} />}>
            <input value={schoolName} disabled={!isEditing} onChange={(e) => setSchoolName(e.target.value)} placeholder="Enter your school name" className={fieldClass} />
          </Field>

          <div className="md:col-span-2 rounded-2xl border border-slate-200 bg-slate-50 p-4">
            <div className="flex flex-col justify-between gap-3 sm:flex-row sm:items-center">
              <div>
                <p className="font-semibold text-slate-800">Location</p>
                <p className="text-sm text-slate-500">State, district and city are shown separately.</p>
              </div>
              <button type="button" disabled={!isEditing || locating} onClick={useCurrentLocation}
                className="flex items-center justify-center gap-2 rounded-xl bg-cyan-600 px-4 py-2.5 font-semibold text-white disabled:cursor-not-allowed disabled:opacity-50">
                <LocateFixed size={17} /> {locating ? "Detecting..." : "Use Current Location"}
              </button>
            </div>
            <div className="mt-4 grid gap-4 md:grid-cols-3">
              <Field label="State" icon={<MapPin size={18} />}><input value={state} disabled={!isEditing} onChange={(e) => setState(e.target.value)} placeholder="e.g. Bihar" className={fieldClass} /></Field>
              <Field label="District"><input value={district} disabled={!isEditing} onChange={(e) => setDistrict(e.target.value)} placeholder="e.g. Gopalganj" className={fieldClass} /></Field>
              <Field label="City / Town"><input value={city} disabled={!isEditing} onChange={(e) => setCity(e.target.value)} placeholder="e.g. Gopalganj" className={fieldClass} /></Field>
            </div>
          </div>

          <div className="md:col-span-2">
            <label className="mb-2 block text-sm font-semibold text-slate-700">Career Goal <span className="font-normal text-slate-400">Optional</span></label>
            <div className="relative">
              <Target size={18} className="absolute left-4 top-3.5 text-slate-400" />
              <textarea value={careerGoal} disabled={!isEditing} onChange={(e) => setCareerGoal(e.target.value)}
                placeholder="Example: I want to explore engineering, medicine, business or other career options."
                rows={3} className={`${fieldClass} resize-none pl-11`} />
            </div>
          </div>
        </div>

        <div className="mt-6 rounded-2xl border border-cyan-200 bg-cyan-50 p-5">
          <p className="text-sm font-semibold uppercase tracking-wide text-cyan-700">Your Guidance Assessment</p>
          <h3 className="mt-1 text-lg font-bold text-slate-900">{assessmentPurpose.title}</h3>
          <p className="mt-1 text-slate-600">{assessmentPurpose.description}</p>
        </div>

        {error && <div className="mt-5 rounded-xl border border-red-200 bg-red-50 p-4 text-sm font-medium text-red-600">{error}</div>}
        {success && <div className="mt-5 flex items-center gap-3 rounded-xl border border-green-200 bg-green-50 p-4 text-sm font-medium text-green-700"><CheckCircle2 size={20} />{success}</div>}

        <div className="mt-6 flex flex-wrap justify-end gap-3">
          <button type="button" onClick={() => setIsEditing(true)}
            className="flex items-center gap-2 rounded-xl border border-slate-300 bg-white px-6 py-2.5 font-semibold text-slate-700 hover:bg-slate-50">
            <Pencil size={17} /> Edit
          </button>
          <button type="submit" disabled={!isEditing}
            className="flex items-center gap-2 rounded-xl bg-cyan-600 px-6 py-2.5 font-semibold text-white transition hover:bg-cyan-700 disabled:cursor-not-allowed disabled:opacity-50">
            <Save size={17} /> Save Profile
          </button>
        </div>
      </form>
    </div>
  );
}

function Field({ label, icon, children }: { label: string; icon?: React.ReactNode; children: React.ReactNode }) {
  return (
    <div>
      <label className="mb-2 block text-sm font-semibold text-slate-700">{label}</label>
      <div className="relative">
        {icon && <span className="absolute left-4 top-1/2 z-10 -translate-y-1/2 text-slate-400">{icon}</span>}
        <div className={icon ? "[&_input]:pl-11 [&_select]:pl-11" : ""}>{children}</div>
      </div>
    </div>
  );
}

export default HighSchoolProfile;
