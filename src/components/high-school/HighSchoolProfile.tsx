import { useState } from "react";
import { Save } from "lucide-react";
import { useAuth } from "../../contexts/AuthContext";
import Input from "../ui/Input";

function HighSchoolProfile() {
  const { user } = useAuth();

  const [formData, setFormData] = useState({
    fullName: user?.name || "",
    email: user?.email || "",
    school: "",
    class: "",
    board: "",
    dob: "",
    gender: "",
    parentName: "",
    parentMobile: "",
    city: "",
    state: "",
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
      "highSchoolProfile",
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
        Complete your profile information.
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
          name="email"
          value={formData.email}
          onChange={handleChange}
        />

        <Input
          label="School Name"
          name="school"
          value={formData.school}
          onChange={handleChange}
        />

        <select
          name="class"
          value={formData.class}
          onChange={handleChange}
          className="rounded-xl border border-slate-300 p-3"
        >
          <option value="">Select Class</option>
          <option>9</option>
          <option>10</option>
          <option>11</option>
          <option>12</option>
        </select>

        <select
          name="board"
          value={formData.board}
          onChange={handleChange}
          className="rounded-xl border border-slate-300 p-3"
        >
          <option value="">Select Board</option>
          <option>CBSE</option>
          <option>ICSE</option>
          <option>BSEB</option>
          <option>UP Board</option>
          <option>MP Board</option>
          <option>RBSE</option>
          <option>JAC</option>
          <option>HBSE</option>
          <option>PSEB</option>
          <option>Maharashtra Board</option>
        </select>

        <Input
          label="Date of Birth"
          type="date"
          name="dob"
          value={formData.dob}
          onChange={handleChange}
        />

        <Input
          label="Parent Name"
          name="parentName"
          value={formData.parentName}
          onChange={handleChange}
        />

        <Input
          label="Parent Mobile"
          name="parentMobile"
          value={formData.parentMobile}
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
          label="Career Goal"
          name="careerGoal"
          value={formData.careerGoal}
          onChange={handleChange}
        />

      </div>

      <button
        onClick={handleSave}
        className="mt-10 flex items-center gap-2 rounded-xl bg-cyan-600 px-6 py-3 font-semibold text-white hover:bg-cyan-700"
      >
        <Save size={18} />
        Save Profile
      </button>

    </div>
  );
}

export default HighSchoolProfile;