import { useEffect, useState } from "react";

import DashboardLayout from "./DashboardLayout";
import Card from "./ui/Card";
import Input from "./ui/Input";
import Button from "./ui/Button";

function StudentProfile() {

  const [formData, setFormData] = useState({

    fullName: "",

    email: "",

    phone: "",

    college: "",

    branch: "",

    semester: "",

    cgpa: "",

    skills: "",

    careerGoal: "",

  });

  const [error, setError] = useState("");

  const [success, setSuccess] = useState("");

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
