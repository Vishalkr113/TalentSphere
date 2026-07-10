import { useState } from "react";
import { Save } from "lucide-react";

import Input from "../ui/Input";
import { useAuth } from "../../contexts/AuthContext";

function CollegeProfile() {
  const { user } = useAuth();

  const [formData, setFormData] = useState({
    fullName: user?.name || "",
    email: user?.email || "",
    college: "",
    university: "",
    branch: "",
    semester: "",
    cgpa: "",
    phone: "",
    city: "",
    state: "",
    linkedin: "",
    github: "",
    portfolio: "",
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
      "collegeProfile",
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
        Complete your academic and professional profile.
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
          label="College Name"
          name="college"
          value={formData.college}
          onChange={handleChange}
        />

        <Input
          label="University"
          name="university"
          value={formData.university}
          onChange={handleChange}
        />

        <Input
          label="Branch"
          name="branch"
          value={formData.branch}
          onChange={handleChange}
        />

        <select
          name="semester"
          value={formData.semester}
          onChange={handleChange}
          className="rounded-xl border border-slate-300 px-4 py-3 outline-none focus:border-cyan-600"
        >
          <option value="">
            Select Semester
          </option>

          <option>1</option>
          <option>2</option>
          <option>3</option>
          <option>4</option>
          <option>5</option>
          <option>6</option>
          <option>7</option>
          <option>8</option>

        </select>

        <Input
          label="CGPA"
          name="cgpa"
          value={formData.cgpa}
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

export default CollegeProfile;