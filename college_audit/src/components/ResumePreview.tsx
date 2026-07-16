import Card from "./ui/Card";

interface ResumePreviewProps {
  resumeData: any;
}

function ResumePreview({
  resumeData,
}: ResumePreviewProps) {
  return (
    <Card className="p-8">

      <div className="border-b pb-6">

        <h1 className="text-3xl font-bold text-slate-900">
          {resumeData.fullName || "Your Name"}
        </h1>

        <p className="mt-2 text-slate-600">
          {resumeData.email}
        </p>

        <p className="text-slate-600">
          {resumeData.phone}
        </p>

        <p className="text-cyan-600">
          {resumeData.linkedin}
        </p>

        <p className="text-cyan-600">
          {resumeData.github}
        </p>

      </div>

      <div className="mt-6">

        <h2 className="mb-2 text-lg font-semibold">
          Education
        </h2>

        <p>{resumeData.college}</p>

        <p>
          {resumeData.degree} • {resumeData.branch}
        </p>

        <p>
          CGPA : {resumeData.cgpa}
        </p>

      </div>

      <div className="mt-6">

        <h2 className="mb-2 text-lg font-semibold">
          Skills
        </h2>

        <p>{resumeData.technicalSkills}</p>

        <p>{resumeData.softSkills}</p>

        <p>{resumeData.languages}</p>

      </div>

      <div className="mt-6">

        <h2 className="mb-2 text-lg font-semibold">
          Projects
        </h2>

        <h3 className="font-semibold">
          {resumeData.projectName}
        </h3>

        <p>{resumeData.projectDescription}</p>

        <p>{resumeData.projectTech}</p>

      </div>

      <div className="mt-6">

        <h2 className="mb-2 text-lg font-semibold">
          Experience
        </h2>

        <h3 className="font-semibold">
          {resumeData.company}
        </h3>

        <p>{resumeData.jobRole}</p>

        <p>{resumeData.duration}</p>

      </div>

      <div className="mt-6">

        <h2 className="mb-2 text-lg font-semibold">
          Certifications
        </h2>

        <p>{resumeData.certificateName}</p>

        <p>{resumeData.certificateProvider}</p>

      </div>

    </Card>
  );
}

export default ResumePreview;