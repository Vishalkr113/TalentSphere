import { useState } from "react";
import { Save } from "lucide-react";

import Input from "../ui/Input";
import { useAuth } from "../../contexts/AuthContext";

function ProfessionalProfile() {
  const { user } = useAuth();

  const [formData, setFormData] = useState({
    fullName: user?.name || "",
    email: user?.email || "",
    company: "",
    designation: "",
    experience: "",
    industry: "",
    skills: "",
    phone: "",
    city: "",
    state: "",
    linkedin: "",
    github: "",
    portfolio: "",
    expectedSalary: "",
    careerGoal: "",
  });

  const handleChange = (
    e: React.ChangeEvent<
      HTMLInputElement | HTMLSelectElement
    >
  ) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSave = () => {
    localStorage.setItem(
      "professionalProfile",
      JSON.stringify(formData)
    );

    alert("Profile Saved Successfully");
  };

  return (
    <div className="rounded-3xl bg-white p-8 shadow-sm">

      <h1 className="text-3xl font-bold text-slate-900">
        My Profile
      </h1>

      <p className="mt-2 text-slate-500">
        Manage your professional information and career details.
      </p>

      <div className="mt-10 grid gap-6 md:grid-cols-2">

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
          label="Current Company"
          name="company"
          value={formData.company}
          onChange={handleChange}
        />

        <Input
          label="Designation"
          name="designation"
          value={formData.designation}
          onChange={handleChange}
        />

        <Input
          label="Experience"
          name="experience"
          placeholder="e.g. 2 Years"
          value={formData.experience}
          onChange={handleChange}
        />

        <Input
          label="Industry"
          name="industry"
          placeholder="Software / Finance / Healthcare"
          value={formData.industry}
          onChange={handleChange}
        />

        <Input
          label="Primary Skills"
          name="skills"
          placeholder="React, Java, AWS..."
          value={formData.skills}
          onChange={handleChange}
        />

        <Input
          label="Phone Number"
          name="phone"
          value={formData.phone}
          onChange={handleChange}
        />

        <Input
          label="City"
          name="city"
          value={formData.city}
          onChange={handleChange}
        />

        <Input
          label="State"
          name="state"
          value={formData.state}
          onChange={handleChange}
        />

        <Input
          label="LinkedIn Profile"
          name="linkedin"
          value={formData.linkedin}
          onChange={handleChange}
        />

        <Input
          label="GitHub Profile"
          name="github"
          value={formData.github}
          onChange={handleChange}
        />

        <Input
          label="Portfolio Website"
          name="portfolio"
          value={formData.portfolio}
          onChange={handleChange}
        />

        <Input
          label="Expected Salary"
          name="expectedSalary"
          placeholder="e.g. ₹15 LPA"
          value={formData.expectedSalary}
          onChange={handleChange}
        />

        <Input
          label="Career Goal"
          name="careerGoal"
          value={formData.careerGoal}
          onChange={handleChange}
        />

      </div>

      <button
        onClick={handleSave}
        className="mt-10 flex items-center gap-2 rounded-xl bg-cyan-600 px-6 py-3 font-semibold text-white transition hover:bg-cyan-700"
      >
        <Save size={18} />

        Save Profile

      </button>

    </div>
  );
}

export default ProfessionalProfile;