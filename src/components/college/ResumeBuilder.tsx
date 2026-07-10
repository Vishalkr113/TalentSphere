import { useState } from "react";
import { Save, Download, Eye } from "lucide-react";

import Input from "../ui/Input";

function ResumeBuilder() {
  const [formData, setFormData] = useState({
    fullName: "",
    email: "",
    phone: "",
    address: "",
    linkedin: "",
    github: "",
    portfolio: "",
    summary: "",
    skills: "",
    education: "",
    experience: "",
    projects: "",
    certifications: "",
    achievements: "",
  });

  const handleChange = (
    e: React.ChangeEvent<
      HTMLInputElement | HTMLTextAreaElement
    >
  ) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSave = () => {
    localStorage.setItem(
      "resumeData",
      JSON.stringify(formData)
    );

    alert("Resume Saved Successfully");
  };

  return (
    <div className="space-y-8">

      {/* Heading */}

      <div>

        <h1 className="text-4xl font-bold text-slate-900">
          Resume Builder
        </h1>

        <p className="mt-3 text-lg text-slate-600">
          Create an ATS-friendly professional resume in minutes.
        </p>

      </div>

      {/* Personal Information */}

      <div className="rounded-3xl bg-white p-8 shadow-sm">

        <h2 className="mb-6 text-2xl font-bold">
          Personal Information
        </h2>

        <div className="grid gap-6 md:grid-cols-2">

          <Input
            label="Full Name"
            name="fullName"
            value={formData.fullName}
            onChange={handleChange}
          />

          <Input
            label="Email"
            type="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
          />

          <Input
            label="Phone"
            name="phone"
            value={formData.phone}
            onChange={handleChange}
          />

          <Input
            label="Address"
            name="address"
            value={formData.address}
            onChange={handleChange}
          />

          <Input
            label="LinkedIn"
            name="linkedin"
            value={formData.linkedin}
            onChange={handleChange}
          />

          <Input
            label="GitHub"
            name="github"
            value={formData.github}
            onChange={handleChange}
          />

          <Input
            label="Portfolio"
            name="portfolio"
            value={formData.portfolio}
            onChange={handleChange}
          />

        </div>

      </div>

      {/* Professional Summary */}

      <div className="rounded-3xl bg-white p-8 shadow-sm">

        <h2 className="mb-6 text-2xl font-bold">
          Professional Summary
        </h2>

        <textarea
          rows={5}
          name="summary"
          value={formData.summary}
          onChange={handleChange}
          className="w-full rounded-xl border border-slate-300 p-4 outline-none focus:border-cyan-600"
          placeholder="Write a short professional summary..."
        />

      </div>

      {/* Skills */}

      <div className="rounded-3xl bg-white p-8 shadow-sm">

        <h2 className="mb-6 text-2xl font-bold">
          Skills
        </h2>

        <textarea
          rows={4}
          name="skills"
          value={formData.skills}
          onChange={handleChange}
          className="w-full rounded-xl border border-slate-300 p-4 outline-none focus:border-cyan-600"
          placeholder="Java, Python, React, SQL..."
        />

      </div>

      {/* Education */}

      <div className="rounded-3xl bg-white p-8 shadow-sm">

        <h2 className="mb-6 text-2xl font-bold">
          Education
        </h2>

        <textarea
          rows={5}
          name="education"
          value={formData.education}
          onChange={handleChange}
          className="w-full rounded-xl border border-slate-300 p-4 outline-none focus:border-cyan-600"
        />

      </div>

      {/* Experience */}

      <div className="rounded-3xl bg-white p-8 shadow-sm">

        <h2 className="mb-6 text-2xl font-bold">
          Experience
        </h2>

        <textarea
          rows={5}
          name="experience"
          value={formData.experience}
          onChange={handleChange}
          className="w-full rounded-xl border border-slate-300 p-4 outline-none focus:border-cyan-600"
        />

      </div>

      {/* Projects */}

      <div className="rounded-3xl bg-white p-8 shadow-sm">

        <h2 className="mb-6 text-2xl font-bold">
          Projects
        </h2>

        <textarea
          rows={5}
          name="projects"
          value={formData.projects}
          onChange={handleChange}
          className="w-full rounded-xl border border-slate-300 p-4 outline-none focus:border-cyan-600"
        />

      </div>

      {/* Certifications */}

      <div className="rounded-3xl bg-white p-8 shadow-sm">

        <h2 className="mb-6 text-2xl font-bold">
          Certifications
        </h2>

        <textarea
          rows={4}
          name="certifications"
          value={formData.certifications}
          onChange={handleChange}
          className="w-full rounded-xl border border-slate-300 p-4 outline-none focus:border-cyan-600"
        />

      </div>

      {/* Achievements */}

      <div className="rounded-3xl bg-white p-8 shadow-sm">

        <h2 className="mb-6 text-2xl font-bold">
          Achievements
        </h2>

        <textarea
          rows={4}
          name="achievements"
          value={formData.achievements}
          onChange={handleChange}
          className="w-full rounded-xl border border-slate-300 p-4 outline-none focus:border-cyan-600"
        />

      </div>

      {/* Buttons */}

      <div className="flex flex-wrap justify-end gap-4">

        <button className="flex items-center gap-2 rounded-xl border border-slate-300 px-6 py-3 font-semibold hover:bg-slate-100">

          <Eye size={18} />

          Preview

        </button>

        <button className="flex items-center gap-2 rounded-xl border border-slate-300 px-6 py-3 font-semibold hover:bg-slate-100">

          <Download size={18} />

          Download PDF

        </button>

        <button
          onClick={handleSave}
          className="flex items-center gap-2 rounded-xl bg-cyan-600 px-6 py-3 font-semibold text-white hover:bg-cyan-700"
        >

          <Save size={18} />

          Save Resume

        </button>

      </div>

    </div>
  );
}

export default ResumeBuilder;