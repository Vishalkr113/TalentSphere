import { useState } from "react";

import { Save, X } from "lucide-react";

import Input from "../ui/Input";

import ProfilePhoto from "../common/Profile/ProfilePhoto";
import SearchSelect from "../common/Select/SearchSelect";
import MultiSelect from "../common/Select/MultiSelect";
import AddressSelector from "../common/address/AddressSelector";

import { boardOptions } from "../../data/academic/boards";
import { classOptions } from "../../data/academic/classes";
import { streamOptions } from "../../data/academic/streams";
import { subjectOptions } from "../../data/academic/subjects";

import { careerOptions } from "../../data/career/careers";
import { skillOptions } from "../../data/career/skills";
import { hobbyOptions } from "../../data/career/hobbies";
import { languageOptions } from "../../data/career/languages";

import { genderOptions } from "../../data/profile/genders";
import { bloodGroupOptions } from "../../data/profile/bloodGroups";

import type { HighSchoolProfile } from "../../types/profile";

interface HighSchoolProfileFormProps {
  initialData: HighSchoolProfile;
  onSave: (data: HighSchoolProfile) => void;
  onCancel: () => void;
}

function HighSchoolProfileForm({
  initialData,
  onSave,
  onCancel,
}: HighSchoolProfileFormProps) {
  const [formData, setFormData] =
    useState<HighSchoolProfile>(initialData);

  const handleInputChange = (
    e: React.ChangeEvent<HTMLInputElement>
  ) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSave = () => {
    onSave(formData);
  };

  return (
    <div className="rounded-3xl bg-white p-8 shadow-sm">

      <div className="mb-10 flex items-center justify-between">

        <div>

          <h1 className="text-3xl font-bold text-slate-900">
            Edit Profile
          </h1>

          <p className="mt-2 text-slate-500">
            Update your profile information.
          </p>

        </div>

        <div className="flex gap-3">

          <button
            type="button"
            onClick={handleSave}
            className="flex items-center gap-2 rounded-xl bg-cyan-600 px-6 py-3 font-semibold text-white hover:bg-cyan-700"
          >
            <Save size={18} />
            Save
          </button>

          <button
            type="button"
            onClick={onCancel}
            className="flex items-center gap-2 rounded-xl border border-slate-300 px-6 py-3 font-semibold text-slate-700 hover:bg-slate-100"
          >
            <X size={18} />
            Cancel
          </button>

        </div>

      </div>

            {/* Profile Photo */}

      <div className="mb-10">

        <ProfilePhoto
          image={formData.profileImage}
          editable
          name={formData.fullName}
          onChange={(image) =>
            setFormData({
              ...formData,
              profileImage: image,
            })
          }
        />

      </div>

      {/* Personal Information */}

      <div className="rounded-2xl border border-slate-200 p-6">

        <h2 className="mb-6 text-2xl font-bold text-slate-900">

          Personal Information

        </h2>

        <div className="grid gap-6 md:grid-cols-2">

          <Input
            label="Full Name"
            name="fullName"
            value={formData.fullName}
            onChange={handleInputChange}
          />

          <Input
            label="Email"
            type="email"
            name="email"
            value={formData.email}
            onChange={handleInputChange}
          />

          <Input
            label="Mobile Number"
            name="mobile"
            value={formData.mobile}
            onChange={handleInputChange}
          />

          <Input
            label="Date of Birth"
            type="date"
            name="dob"
            value={formData.dob}
            onChange={handleInputChange}
          />

          <SearchSelect
            label="Gender"
            options={genderOptions}
            value={formData.gender}
            onChange={(value) =>
              setFormData({
                ...formData,
                gender: value,
              })
            }
          />

          <SearchSelect
            label="Blood Group"
            options={bloodGroupOptions}
            value={formData.bloodGroup}
            onChange={(value) =>
              setFormData({
                ...formData,
                bloodGroup: value,
              })
            }
          />

        </div>

      </div>

      {/* Academic Information */}

      <div className="mt-8 rounded-2xl border border-slate-200 p-6">

        <h2 className="mb-6 text-2xl font-bold text-slate-900">

          Academic Information

        </h2>

        <div className="grid gap-6 md:grid-cols-2">

          <Input
            label="School Name"
            name="school"
            value={formData.school}
            onChange={handleInputChange}
          />

          <SearchSelect
            label="Class"
            options={classOptions}
            value={formData.class}
            onChange={(value) =>
              setFormData({
                ...formData,
                class: value,
              })
            }
          />

          <SearchSelect
            label="Board"
            options={boardOptions}
            value={formData.board}
            onChange={(value) =>
              setFormData({
                ...formData,
                board: value,
              })
            }
          />

          <Input
            label="Medium"
            name="medium"
            value={formData.medium}
            onChange={handleInputChange}
          />

          <Input
            label="Roll Number"
            name="rollNumber"
            value={formData.rollNumber}
            onChange={handleInputChange}
          />

          <Input
            label="Admission Year"
            name="admissionYear"
            value={formData.admissionYear}
            onChange={handleInputChange}
          />

          <Input
            label="Percentage / CGPA"
            name="percentage"
            value={formData.percentage}
            onChange={handleInputChange}
          />

        </div>

      </div>

            {/* Parent Details */}

      <div className="mt-8 rounded-2xl border border-slate-200 p-6">

        <h2 className="mb-6 text-2xl font-bold text-slate-900">

          Parent / Guardian Details

        </h2>

        <div className="grid gap-6 md:grid-cols-2">

          <Input
            label="Parent Name"
            value={formData.parent.parentName}
            onChange={(e) =>
              setFormData({
                ...formData,
                parent: {
                  ...formData.parent,
                  parentName: e.target.value,
                },
              })
            }
          />

          <Input
            label="Parent Mobile"
            value={formData.parent.parentMobile}
            onChange={(e) =>
              setFormData({
                ...formData,
                parent: {
                  ...formData.parent,
                  parentMobile: e.target.value,
                },
              })
            }
          />

          <Input
            label="Parent Email"
            type="email"
            value={formData.parent.parentEmail}
            onChange={(e) =>
              setFormData({
                ...formData,
                parent: {
                  ...formData.parent,
                  parentEmail: e.target.value,
                },
              })
            }
          />

          <Input
            label="Occupation"
            value={formData.parent.occupation}
            onChange={(e) =>
              setFormData({
                ...formData,
                parent: {
                  ...formData.parent,
                  occupation: e.target.value,
                },
              })
            }
          />

        </div>

      </div>

      {/* Address */}

      <div className="mt-8 rounded-2xl border border-slate-200 p-6">

        <h2 className="mb-6 text-2xl font-bold text-slate-900">

          Address

        </h2>

        <AddressSelector
          value={formData.address}
          onChange={(address) =>
            setFormData({
              ...formData,
              address,
            })
          }
        />

      </div>

      {/* Career Information */}

      <div className="mt-8 rounded-2xl border border-slate-200 p-6">

        <h2 className="mb-6 text-2xl font-bold text-slate-900">

          Career Information

        </h2>

        <div className="grid gap-6 md:grid-cols-2">

          <SearchSelect
            label="Dream Career"
            options={careerOptions}
            value={formData.careerGoal}
            onChange={(value) =>
              setFormData({
                ...formData,
                careerGoal: value,
              })
            }
          />

          <SearchSelect
            label="Interested Stream"
            options={streamOptions}
            value={formData.stream}
            onChange={(value) =>
              setFormData({
                ...formData,
                stream: value,
              })
            }
          />

          <SearchSelect
            label="Favorite Subject"
            options={subjectOptions}
            value={formData.favoriteSubject}
            onChange={(value) =>
              setFormData({
                ...formData,
                favoriteSubject: value,
              })
            }
          />

          <SearchSelect
            label="Weak Subject"
            options={subjectOptions}
            value={formData.weakSubject}
            onChange={(value) =>
              setFormData({
                ...formData,
                weakSubject: value,
              })
            }
          />

        </div>

      </div>

            {/* Skills & Hobbies */}

      <div className="mt-8 rounded-2xl border border-slate-200 p-6">

        <h2 className="mb-6 text-2xl font-bold text-slate-900">

          Skills & Interests

        </h2>

        <div className="space-y-6">

          <MultiSelect
            label="Skills"
            options={skillOptions}
            value={formData.skills}
            onChange={(value) =>
              setFormData({
                ...formData,
                skills: value,
              })
            }
          />

          <MultiSelect
            label="Hobbies"
            options={hobbyOptions}
            value={formData.hobbies}
            onChange={(value) =>
              setFormData({
                ...formData,
                hobbies: value,
              })
            }
          />

          <MultiSelect
            label="Languages"
            options={languageOptions}
            value={formData.languages}
            onChange={(value) =>
              setFormData({
                ...formData,
                languages: value,
              })
            }
          />

        </div>

      </div>

      {/* Form Actions */}

      <div className="mt-10 flex justify-end gap-4">

        <button
          type="button"
          onClick={onCancel}
          className="rounded-xl border border-slate-300 px-6 py-3 font-semibold text-slate-700 transition hover:bg-slate-100"
        >
          Cancel
        </button>

        <button
          type="button"
          onClick={handleSave}
          className="flex items-center gap-2 rounded-xl bg-cyan-600 px-6 py-3 font-semibold text-white transition hover:bg-cyan-700"
        >
          <Save size={18} />
          Save Profile
        </button>

      </div>

    </div>

  );

}

export default HighSchoolProfileForm;