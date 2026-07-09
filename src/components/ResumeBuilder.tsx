import { useState } from "react";

import DashboardLayout from "./DashboardLayout";
import Card from "./ui/Card";
import Input from "./ui/Input";
import Button from "./ui/Button";

import { useRef } from "react";
import { useReactToPrint } from "react-to-print";

import ResumePreview from "./ResumePreview";

function ResumeBuilder() {

  const [step, setStep] = useState(1);

  const resumeRef = useRef<HTMLDivElement>(null);

  const handlePrint = useReactToPrint({
    contentRef: resumeRef,
    documentTitle: "TalentSphere_Resume",
  });

  const [resumeData, setResumeData] = useState({


  fullName: "",

  email: "",

  phone: "",

  linkedin: "",

  github: "",

  portfolio: "",

  college: "",

  degree: "",

  branch: "",

  passingYear: "",

  cgpa: "",

  technicalSkills: "",

  softSkills: "",

  languages: "",
  
  projectName: "",

  projectTech: "",

  githubLink: "",

  liveDemo: "",

  projectDescription: "",

  company: "",

  jobRole: "",

  duration: "",

  location: "",

  experienceDescription: "",

  certificateName: "",

  certificateProvider: "",

  certificateYear: "",

  certificateLink: "",



});
  const handleChange = (
    e: React.ChangeEvent<HTMLInputElement>
  ) => {

    setResumeData({

      ...resumeData,

      [e.target.name]: e.target.value,

    });

  };

  const nextStep = () => {

    setStep(step + 1);

  };

  const previousStep = () => {

    setStep(step - 1);

  };

  return (

    <DashboardLayout>

      <div className="mb-8">

        <h2 className="text-3xl font-bold text-slate-900">

          Resume Builder

        </h2>

        <p className="mt-2 text-slate-600">

          Build your professional resume step by step.

        </p>
        

      </div>

      <Card className="p-8">
                {/* Progress */}

        <div className="mb-8">

          <p className="mb-2 text-sm font-medium text-slate-600">

            Step {step} of 7

          </p>

          <div className="h-2 w-full rounded-full bg-slate-200">

            <div
              className="h-2 rounded-full bg-cyan-600 transition-all duration-300"
              style={{
                width: `${(step / 7) * 100}%`,
              }}
            />

          </div>

        </div>

        {step === 1 && (

          <div>

            <h3 className="mb-6 text-2xl font-semibold text-slate-900">

              Personal Details

            </h3>

            <div className="grid gap-6 md:grid-cols-2">

              <Input
                label="Full Name"
                name="fullName"
                value={resumeData.fullName}
                onChange={handleChange}
                placeholder="Enter full name"
              />

              <Input
                label="Email"
                type="email"
                name="email"
                value={resumeData.email}
                onChange={handleChange}
                placeholder="Enter email"
              />

              <Input
                label="Phone Number"
                name="phone"
                value={resumeData.phone}
                onChange={handleChange}
                placeholder="Enter phone number"
              />

              <Input
                label="LinkedIn"
                name="linkedin"
                value={resumeData.linkedin}
                onChange={handleChange}
                placeholder="LinkedIn Profile URL"
              />

              <Input
                label="GitHub"
                name="github"
                value={resumeData.github}
                onChange={handleChange}
                placeholder="GitHub Profile URL"
              />

              <Input
                label="Portfolio"
                name="portfolio"
                value={resumeData.portfolio}
                onChange={handleChange}
                placeholder="Portfolio Website URL"
              />

            </div>

          </div>

        )}
        {/* Step 2 */}

{step === 2 && (

  <div>

    <h3 className="mb-6 text-2xl font-semibold text-slate-900">

      Education

    </h3>

    <div className="grid gap-6 md:grid-cols-2">

      <Input
        label="College"
        name="college"
        value={(resumeData as any).college || ""}
        onChange={handleChange}
        placeholder="Enter college name"
      />

      <Input
        label="Degree"
        name="degree"
        value={(resumeData as any).degree || ""}
        onChange={handleChange}
        placeholder="B.Tech"
      />

      <Input
        label="Branch"
        name="branch"
        value={(resumeData as any).branch || ""}
        onChange={handleChange}
        placeholder="Computer Science"
      />

      <Input
        label="Passing Year"
        name="passingYear"
        value={(resumeData as any).passingYear || ""}
        onChange={handleChange}
        placeholder="2027"
      />

      <Input
        label="CGPA"
        name="cgpa"
        value={(resumeData as any).cgpa || ""}
        onChange={handleChange}
        placeholder="8.50"
      />

    </div>

  </div>

   )}

   {/* Step 3 */}

{step === 3 && (

  <div>

    <h3 className="mb-6 text-2xl font-semibold text-slate-900">

      Skills

    </h3>

    <div className="grid gap-6">

      <Input
        label="Technical Skills"
        name="technicalSkills"
        value={resumeData.technicalSkills}
        onChange={handleChange}
        placeholder="React, Java, Python, SQL"
      />

      <Input
        label="Soft Skills"
        name="softSkills"
        value={resumeData.softSkills}
        onChange={handleChange}
        placeholder="Communication, Leadership"
      />

      <Input
        label="Languages"
        name="languages"
        value={resumeData.languages}
        onChange={handleChange}
        placeholder="English, Hindi"
      />

    </div>

  </div>

)}

{/* Step 4 */}

{step === 4 && (

  <div>

    <h3 className="mb-6 text-2xl font-semibold text-slate-900">

      Projects

    </h3>

    <div className="grid gap-6">

      <Input
        label="Project Name"
        name="projectName"
        value={resumeData.projectName}
        onChange={handleChange}
        placeholder="TalentSphere Elevate"
      />

      <Input
        label="Technology Used"
        name="projectTech"
        value={resumeData.projectTech}
        onChange={handleChange}
        placeholder="React, FastAPI, MySQL"
      />

      <Input
        label="GitHub Repository"
        name="githubLink"
        value={resumeData.githubLink}
        onChange={handleChange}
        placeholder="https://github.com/username/project"
      />

      <Input
        label="Live Demo"
        name="liveDemo"
        value={resumeData.liveDemo}
        onChange={handleChange}
        placeholder="https://project.vercel.app"
      />

      <Input
        label="Project Description"
        name="projectDescription"
        value={resumeData.projectDescription}
        onChange={handleChange}
        placeholder="Short description of your project"
      />

    </div>

  </div>

)}
 {/* Step 5 */}

{step === 5 && (

  <div>

    <h3 className="mb-6 text-2xl font-semibold text-slate-900">

      Experience

    </h3>

    <div className="grid gap-6 md:grid-cols-2">

      <Input
        label="Company Name"
        name="company"
        value={resumeData.company}
        onChange={handleChange}
        placeholder="Google"
      />

      <Input
        label="Job Role"
        name="jobRole"
        value={resumeData.jobRole}
        onChange={handleChange}
        placeholder="Frontend Developer Intern"
      />

      <Input
        label="Duration"
        name="duration"
        value={resumeData.duration}
        onChange={handleChange}
        placeholder="Jan 2026 - Jun 2026"
      />

      <Input
        label="Location"
        name="location"
        value={resumeData.location}
        onChange={handleChange}
        placeholder="Remote / Bangalore"
      />

      <Input
        label="Experience Description"
        name="experienceDescription"
        value={resumeData.experienceDescription}
        onChange={handleChange}
        placeholder="Worked on React and FastAPI applications."
      />

    </div>

  </div>

)}

{/* Step 6 */}

{step === 6 && (

  <div>

    <h3 className="mb-6 text-2xl font-semibold text-slate-900">

      Certifications

    </h3>

    <div className="grid gap-6 md:grid-cols-2">

      <Input
        label="Certificate Name"
        name="certificateName"
        value={resumeData.certificateName}
        onChange={handleChange}
        placeholder="Python Programming"
      />

      <Input
        label="Provider"
        name="certificateProvider"
        value={resumeData.certificateProvider}
        onChange={handleChange}
        placeholder="Infosys Springboard"
      />

      <Input
        label="Completion Year"
        name="certificateYear"
        value={resumeData.certificateYear}
        onChange={handleChange}
        placeholder="2026"
      />

      <Input
        label="Certificate Link"
        name="certificateLink"
        value={resumeData.certificateLink}
        onChange={handleChange}
        placeholder="https://..."
      />

    </div>

  </div>

)}
 
 <div className="space-y-6">

  <div ref={resumeRef}>

    <ResumePreview
      resumeData={resumeData}
    />

  </div>

  <Button
    onClick={handlePrint}
    className="w-full"
  >
    Download PDF
  </Button>

</div>
   
   <div className="mt-10 flex items-center justify-between">

  <Button
    type="button"
    onClick={previousStep}
    disabled={step === 1}
    className="bg-slate-200 text-slate-800 hover:bg-slate-300"
  >
    Previous
  </Button>

  <Button
    type="button"
    onClick={nextStep}
  >
    {step === 7 ? "Finish" : "Next"}
  </Button>

</div>
</Card>

    </DashboardLayout>
  );

}

export default ResumeBuilder;