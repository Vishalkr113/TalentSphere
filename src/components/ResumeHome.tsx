import { useRef } from "react";
import { useNavigate } from "react-router-dom";

import DashboardLayout from "./DashboardLayout";
import Card from "./ui/Card";
import Button from "./ui/Button";

function ResumeHome() {
  const navigate = useNavigate();

  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleUploadClick = () => {
    fileInputRef.current?.click();
  };

  const handleFileChange = (
    e: React.ChangeEvent<HTMLInputElement>
  ) => {
    const file = e.target.files?.[0];

    if (!file) return;

    const allowedTypes = [
      "application/pdf",
      "application/msword",
      "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    ];

    if (!allowedTypes.includes(file.type)) {
      alert("Please upload a PDF, DOC or DOCX file.");
      return;
    }

    alert(`${file.name} uploaded successfully.`);
  };

  return (
    <DashboardLayout>

      <div className="mb-8">

        <h2 className="text-3xl font-bold text-slate-900">
          Resume Center
        </h2>

        <p className="mt-2 text-slate-600">
          Build a new ATS resume or upload your existing resume.
        </p>

      </div>

      <div className="grid gap-8 lg:grid-cols-2">

        {/* Build Resume */}

        <Card className="p-8">

          <h3 className="text-2xl font-semibold text-slate-900">
            📄 Build Resume
          </h3>

          <p className="mt-4 text-slate-600">
            Create a professional ATS-friendly resume using the TalentSphere Resume Builder.
          </p>

          <Button
            className="mt-8 w-full"
            onClick={() => navigate("/student/resume-builder")}
          >
            Start Building
          </Button>

        </Card>

        {/* Upload Resume */}

        <Card className="p-8">

          <h3 className="text-2xl font-semibold text-slate-900">
            📤 Upload Resume
          </h3>

          <p className="mt-4 text-slate-600">
            Upload your existing PDF, DOC or DOCX resume for AI analysis.
          </p>

          <label htmlFor="resume-upload" className="hidden">
             Upload Resume
          </label>

        <input
          id="resume-upload"
          ref={fileInputRef}
          type="file"
          accept=".pdf,.doc,.docx"
          className="hidden"
          onChange={handleFileChange}
        />

          <Button
            className="mt-8 w-full"
            onClick={handleUploadClick}
          >
            Upload Resume
          </Button>

        </Card>

      </div>

      <Card className="mt-8 p-8">

        <h3 className="text-2xl font-semibold text-slate-900">
          Resume Tips
        </h3>

        <ul className="mt-6 space-y-3 text-slate-700">

          <li>✅ ATS Friendly Resume Format</li>

          <li>✅ Keep Resume within 1-2 Pages</li>

          <li>✅ Add GitHub & LinkedIn Profile</li>

          <li>✅ Mention Projects with Technologies</li>

          <li>✅ Highlight Certifications & Skills</li>

          <li>✅ AI Resume Score Available After Upload</li>

        </ul>

      </Card>

    </DashboardLayout>
  );
}

export default ResumeHome;