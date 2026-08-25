import { useMemo, useState } from "react";
import { Save, X, CheckCircle2 } from "lucide-react";
import ProfilePhoto from "../common/Profile/ProfilePhoto";
import Input from "../ui/Input";
import SearchSelect from "../common/Select/SearchSelect";
import AddressSelector from "../common/address/AddressSelector";
import { boardOptions } from "../../data/academic/boards";
import { classOptions } from "../../data/academic/classes";
import { streamOptions } from "../../data/academic/streams";
import { careerOptions } from "../../data/career/careers";
import { genderOptions } from "../../data/profile/genders";
import type { HighSchoolProfile } from "../../types/profile";

interface HighSchoolProfileFormProps {
  initialData: HighSchoolProfile;
  onSave: (data: HighSchoolProfile) => void;
  onCancel: () => void;
}

export default function HighSchoolProfileForm({
  initialData,
  onSave,
  onCancel,
}: HighSchoolProfileFormProps) {
  const [formData, setFormData] = useState<HighSchoolProfile>(initialData);

  const streamRequired = useMemo(
    () => formData.class?.value === "11" || formData.class?.value === "12",
    [formData.class],
  );

  const update = (patch: Partial<HighSchoolProfile>) => {
    setFormData((current) => ({ ...current, ...patch }));
  };

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    update({ [e.target.name]: e.target.value } as Partial<HighSchoolProfile>);
  };

  return (
    <div className="rounded-[28px] bg-slate-50 p-4 sm:p-6 lg:p-8">
      <div className="mb-6 flex flex-wrap items-center justify-between gap-4 rounded-2xl bg-white p-5 shadow-sm">
        <div>
          <p className="text-sm font-semibold text-cyan-600">PROFILE SETUP</p>
          <h1 className="mt-1 text-2xl font-bold text-slate-900">Complete your profile</h1>
          <p className="mt-1 text-sm text-slate-500">Only the information that helps personalize your TalentSphere experience.</p>
        </div>
        <div className="flex gap-2">
          <button type="button" onClick={onCancel} className="flex items-center gap-2 rounded-xl border border-slate-200 bg-white px-4 py-2.5 font-semibold text-slate-700 hover:bg-slate-50">
            <X size={17} /> Cancel
          </button>
          <button type="button" onClick={() => onSave(formData)} className="flex items-center gap-2 rounded-xl bg-cyan-600 px-5 py-2.5 font-semibold text-white shadow-sm hover:bg-cyan-700">
            <Save size={17} /> Save Profile
          </button>
        </div>
      </div>

      <section className="mb-5 rounded-2xl border border-slate-200 bg-white p-5 shadow-sm">
        <div className="mb-5">
          <p className="text-xs font-semibold uppercase tracking-wider text-cyan-600">PROFILE PHOTO</p>
          <h2 className="mt-1 text-xl font-bold text-slate-900">Your profile identity</h2>
          <p className="text-sm text-slate-500">Optional. You can upload, change or remove your photo anytime.</p>
        </div>
        <ProfilePhoto image={formData.profileImage ?? null} editable name={formData.fullName || "User"} onChange={(image)=>update({profileImage:image})}/>
      </section>

      <section className="rounded-2xl border border-slate-200 bg-white p-5 shadow-sm">
        <div className="mb-5 flex items-start gap-3">
          <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-cyan-50 text-cyan-600"><CheckCircle2 size={20} /></div>
          <div>
            <h2 className="font-bold text-slate-900">Basic Information</h2>
            <p className="text-sm text-slate-500">Your account details and basic profile information.</p>
          </div>
        </div>
        <div className="grid gap-5 md:grid-cols-2">
          <Input label="Full Name" name="fullName" value={formData.fullName} onChange={handleInputChange} readOnly />
          <Input label="Email" type="email" name="email" value={formData.email} onChange={handleInputChange} readOnly />
          <Input label="Mobile Number *" name="mobile" value={formData.mobile} onChange={handleInputChange} placeholder="Enter mobile number" />
          <Input label="Date of Birth *" type="date" name="dob" value={formData.dob} onChange={handleInputChange} />
          <SearchSelect label="Gender (Optional)" options={genderOptions} value={formData.gender} onChange={(value) => update({ gender: value })} />
        </div>
      </section>

      <section className="mt-5 rounded-2xl border border-slate-200 bg-white p-5 shadow-sm">
        <div className="mb-5">
          <p className="text-xs font-semibold uppercase tracking-wider text-cyan-600">ACADEMICS</p>
          <h2 className="mt-1 text-xl font-bold text-slate-900">Academic Information</h2>
          <p className="text-sm text-slate-500">These details determine the right assessment for you.</p>
        </div>
        <div className="grid gap-5 md:grid-cols-2">
          <Input label="School Name (Optional)" name="school" value={formData.school} onChange={handleInputChange} placeholder="Enter school name" />
          <SearchSelect label="Class *" options={classOptions} value={formData.class} onChange={(value) => update({ class: value, stream: value?.value === "11" || value?.value === "12" ? formData.stream : null })} />
          <SearchSelect label="Board *" options={boardOptions} value={formData.board} onChange={(value) => update({ board: value })} />
          <Input label="Medium *" name="medium" value={formData.medium} onChange={handleInputChange} placeholder="e.g. English" />
          {streamRequired && (
            <SearchSelect label="Stream *" options={streamOptions} value={formData.stream} onChange={(value) => update({ stream: value })} />
          )}
        </div>
        <p className="mt-4 text-xs text-slate-400">School name is optional and does not affect assessment unlock.</p>
      </section>

      <section className="mt-5 rounded-2xl border border-slate-200 bg-white p-5 shadow-sm">
        <div className="mb-5">
          <p className="text-xs font-semibold uppercase tracking-wider text-cyan-600">LOCATION</p>
          <h2 className="mt-1 text-xl font-bold text-slate-900">Where are you based?</h2>
          <p className="text-sm text-slate-500">Used for relevant local opportunities and recommendations.</p>
        </div>
        <AddressSelector value={formData.address} onChange={(address) => update({ address })} />
      </section>

      <section className="mt-5 rounded-2xl border border-slate-200 bg-white p-5 shadow-sm">
        <div className="mb-5">
          <p className="text-xs font-semibold uppercase tracking-wider text-cyan-600">CAREER</p>
          <h2 className="mt-1 text-xl font-bold text-slate-900">Your direction</h2>
          <p className="text-sm text-slate-500">Tell us what you want to work toward.</p>
        </div>
        <div className="grid gap-5 md:grid-cols-2">
          <SearchSelect label="Dream Career *" options={careerOptions} value={formData.careerGoal} onChange={(value) => update({ careerGoal: value })} />
        </div>
      </section>

      <div className="mt-6 flex justify-end gap-3">
        <button type="button" onClick={onCancel} className="rounded-xl border border-slate-200 bg-white px-5 py-3 font-semibold text-slate-700 hover:bg-slate-50">Cancel</button>
        <button type="button" onClick={() => onSave(formData)} className="flex items-center gap-2 rounded-xl bg-cyan-600 px-6 py-3 font-semibold text-white shadow-sm hover:bg-cyan-700"><Save size={18} /> Save Profile</button>
      </div>
    </div>
  );
}
