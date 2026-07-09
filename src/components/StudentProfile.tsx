import { useEffect, useState } from "react";

import DashboardLayout from "./DashboardLayout";
import Card from "./ui/Card";
import Input from "./ui/Input";
import Button from "./ui/Button";

function StudentProfile() {

  const [formData, setFormData] = useState({
    
    profilePhoto: "",

    fullName: "",
    email: "",
    phone: "",

    dateOfBirth: "",
    gender: "",

    address: "",
    city: "",
    state: "",
    country: "",
    pincode: "",
    

    college: "",
    branch: "",
    semester: "",
    cgpa: "",

    skills: "",
    careerGoal: "",

  });


  
  const [error, setError] = useState("");

  const [success, setSuccess] = useState("");

  const handlePhotoUpload = (
  e: React.ChangeEvent<HTMLInputElement>
) => {

  const file = e.target.files?.[0];

  if (!file) return;

  const reader = new FileReader();

  reader.onloadend = () => {

    setFormData((prev) => ({
      ...prev,
      profilePhoto: reader.result as string,
    }));

  };

  reader.readAsDataURL(file);

};

  useEffect(() => {

    const savedProfile =
      localStorage.getItem("studentProfile");

    if (savedProfile) {

      setFormData(JSON.parse(savedProfile));

    }

  }, []);

  const handleChange = (
    e: React.ChangeEvent<HTMLInputElement>
  ) => {

    setFormData({

      ...formData,

      [e.target.name]: e.target.value,

    });

  };

  const handleSubmit = (
    e: React.FormEvent
  ) => {

    e.preventDefault();

    setError("");

    setSuccess("");

    if (

      !formData.fullName.trim() ||

      !formData.email.trim() ||

      !formData.phone.trim() ||

      !formData.college.trim() ||

      !formData.branch.trim() ||

      !formData.semester.trim() ||

      !formData.cgpa.trim() ||

      !formData.skills.trim() ||

      !formData.careerGoal.trim()

    ) {

      setError(
        "Please fill in all required fields."
      );

      return;

    }

    localStorage.setItem(

      "studentProfile",

      JSON.stringify(formData)

    );

    setSuccess(
      "Profile saved successfully."
    );

  };

  return (

    <DashboardLayout>

      <div className="mb-8">

        <h2 className="text-3xl font-bold text-slate-900">

          Student Profile

        </h2>

        <p className="mt-2 text-slate-600">

          Complete your profile to unlock all TalentSphere features.

        </p>

      </div>

       <Card className="mb-8">

  <div className="flex flex-col items-center justify-between gap-6 md:flex-row">

    {/* Left Side */}

    <div className="flex items-center gap-6">

      <img
        src={
          formData.profilePhoto ||
          "https://placehold.co/120x120"}
              alt="Profile"
              className="h-28 w-28 rounded-full border-4 border-cyan-500 object-cover"
      />

      <div>

        <h3 className="text-2xl font-bold text-slate-900">
          {formData.fullName || "Student Name"}
        </h3>

        <p className="mt-1 text-slate-500">
          Student ID : TS-2026-001
        </p>

      </div>

    </div>

    {/* Right Side */}

    <div className="w-full md:w-72">

      <div className="mb-2 flex justify-between">

        <span className="text-sm font-medium">
          Profile Completion
        </span>

        <span className="text-sm font-semibold text-cyan-600">
          20%
        </span>

      </div>

      <div className="h-3 rounded-full bg-slate-200">

        <div
          className="h-3 rounded-full bg-cyan-600"
          style={{ width: "20%" }}
        />

      </div>

      <Button
        type="button"
        className="mt-5 w-full"
      >

            Edit Profile
      </Button>

       <input
          type="file"
          accept="image/*"
          onChange={handlePhotoUpload}
          className="mt-3 w-full text-sm"
      />

    </div>

  </div>

</Card>

      <Card className="p-8">

        <form
            onSubmit={handleSubmit}
            className="space-y-8"
        >
            
                  {/* Personal Information */}

          <div>

            <h3 className="mb-5 text-xl font-semibold text-slate-900">
              Personal Information
            </h3>

            <div className="grid gap-6 md:grid-cols-2">

              <Input
                label="Full Name"
                name="fullName"
                value={formData.fullName}
                onChange={handleChange}
                placeholder="Enter your full name"
              />

              <Input
                label="Email"
                type="email"
                name="email"
                value={formData.email}
                onChange={handleChange}
                placeholder="Enter your email"
              />

              <Input
                label="Phone Number"
                name="phone"
                value={formData.phone}
                onChange={handleChange}
                placeholder="Enter your phone number"
              />

              <Input
  label="Date of Birth"
  type="date"
  name="dateOfBirth"
  value={formData.dateOfBirth}
  onChange={handleChange}
/>

<Input
  label="Gender"
  name="gender"
  value={formData.gender}
  onChange={handleChange}
  placeholder="Male / Female / Other"
/>

<Input
  label="Address"
  name="address"
  value={formData.address}
  onChange={handleChange}
  placeholder="Enter your address"
/>

<Input
  label="City"
  name="city"
  value={formData.city}
  onChange={handleChange}
  placeholder="Enter city"
/>

<Input
  label="State"
  name="state"
  value={formData.state}
  onChange={handleChange}
  placeholder="Enter state"
/>

<Input
  label="Country"
  name="country"
  value={formData.country}
  onChange={handleChange}
  placeholder="India"
/>

<Input
  label="Pincode"
  name="pincode"
  value={formData.pincode}
  onChange={handleChange}
  placeholder="462001"
/>


            </div>

          </div>

          {/* Education */}

          <div>

            <h3 className="mb-5 text-xl font-semibold text-slate-900">
              Education
            </h3>

            <div className="grid gap-6 md:grid-cols-2">

              <Input
                label="College"
                name="college"
                value={formData.college}
                onChange={handleChange}
                placeholder="Enter college name"
              />

              <Input
                label="Branch"
                name="branch"
                value={formData.branch}
                onChange={handleChange}
                placeholder="Computer Science"
              />

              <Input
                label="Semester"
                name="semester"
                value={formData.semester}
                onChange={handleChange}
                placeholder="6"
              />

              <Input
                label="CGPA"
                name="cgpa"
                value={formData.cgpa}
                onChange={handleChange}
                placeholder="8.50"
              />

            </div>

          </div>

          {/* Skills */}

          <div>

            <h3 className="mb-5 text-xl font-semibold text-slate-900">
              Skills
            </h3>

            <Input
              label="Skills"
              name="skills"
              value={formData.skills}
              onChange={handleChange}
              placeholder="React, Java, Python, SQL"
            />

          </div>

          {/* Career Goal */}

          <div>

            <h3 className="mb-5 text-xl font-semibold text-slate-900">
              Career Goal
            </h3>

            <Input
              label="Career Goal"
              name="careerGoal"
              value={formData.careerGoal}
              onChange={handleChange}
              placeholder="Software Engineer"
            />

          </div>

          {/* Messages */}

          {error && (

            <div className="rounded-xl border border-red-200 bg-red-50 p-4 text-sm font-medium text-red-600">

              {error}

            </div>

          )}

          {success && (

            <div className="rounded-xl border border-green-200 bg-green-50 p-4 text-sm font-medium text-green-600">

              {success}

            </div>

          )}

          <Button
            type="submit"
            className="w-full md:w-auto"
          >
            Save Profile
          </Button>

        </form>

      </Card>

    </DashboardLayout>

  );
}

export default StudentProfile;
