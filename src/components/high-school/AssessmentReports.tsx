import {
  AlertTriangle,
  BarChart3,
  Brain,
  CheckCircle2,
  GraduationCap,
  Lightbulb,
  Target,
  TrendingUp,
} from "lucide-react";

import { useNavigate } from "react-router-dom";

import { useAuth } from "../../contexts/AuthContext";

import {
  getAssessmentQuestionBank,
  type AssessmentCategory,
} from "../../data/assessment/assessmentQuestions";

import {
  getUserAssessmentResults,
  type AssessmentResult,
} from "../../data/assessment/assessmentService";

import {
  analyzeAssessmentResult,
  type IndividualAssessmentAnalysis,
  type SkillAnalysis,
} from "../../data/assessment/assessmentAnalysisService";

import {
  getAssessmentPurpose,
  getHighSchoolProfile,
  type HighSchoolProfile as HighSchoolProfileData,
} from "../../services/highSchoolProfileService";

const categoryLabels: Record<
  AssessmentCategory,
  string
> = {
  aptitude: "Aptitude Assessment",
  math: "Mathematics Assessment",
  english: "English Assessment",
  science: "Science Assessment",
  reasoning: "Logical Reasoning Assessment",
};

const categories: AssessmentCategory[] = [
  "aptitude",
  "math",
  "english",
  "science",
  "reasoning",
];

function getContextualCategoryLabel(
  category: AssessmentCategory,
  profile: HighSchoolProfileData
): string {
  if ((profile.studentClass === "9" || profile.studentClass === "10")) {
    return categoryLabels[category];
  }

  if (profile.studentClass === "11") {
    const labels: Record<
      AssessmentCategory,
      string
    > = {
      aptitude: "Academic Aptitude",
      math: "Quantitative Assessment",
      english: "Communication Assessment",
      science: "Stream Subject Assessment",
      reasoning: "Analytical Reasoning",
    };

    return labels[category];
  }

  const labels: Record<
    AssessmentCategory,
    string
  > = {
    aptitude: "Career Aptitude Assessment",
    math: "Quantitative Readiness",
    english: "Communication Readiness",
    science: "Core Subject Assessment",
    reasoning: "Career Reasoning Assessment",
  };

  return labels[category];
}

function getReportContext(
  profile: HighSchoolProfileData
) {
  if ((profile.studentClass === "9" || profile.studentClass === "10")) {
    return {
      eyebrow: "Class 10 Stream Discovery",
      title: "Your Stream Discovery Reports",
      description:
        "Review your subject strengths, reasoning ability and academic performance before generating your Class 11 stream guidance.",
      guidanceLabel: "Stream Guidance Status",
    };
  }

  if (profile.studentClass === "11") {
    return {
      eyebrow: `Class 11${profile.currentStream
          ? ` • ${profile.currentStream}`
          : ""
        }`,
      title: "Your Stream Performance Reports",
      description:
        "Review your current stream performance, subject strengths and improvement priorities for Class 12 preparation.",
      guidanceLabel: "Stream Analysis Status",
    };
  }

  return {
    eyebrow: `Class 12${profile.currentStream
        ? ` • ${profile.currentStream}`
        : ""
      }`,
    title: "Your Higher Study Readiness Reports",
    description:
      "Review your subject performance, academic strengths and readiness before generating higher study and career guidance.",
    guidanceLabel: "Career Guidance Status",
  };
}

function getLatestResultByCategory(
  results: AssessmentResult[],
  category: AssessmentCategory
) {
  const categoryResults = results.filter(
    (result) =>
      result.category === category
  );

  if (categoryResults.length === 0) {
    return null;
  }

  return categoryResults.reduce(
    (latestResult, currentResult) => {
      return new Date(
        currentResult.completedAt
      ).getTime() >
        new Date(
          latestResult.completedAt
        ).getTime()
        ? currentResult
        : latestResult;
    }
  );
}

function SkillProgress({
  skill,
}: {
  skill: SkillAnalysis;
}) {
  return (
    <div className="rounded-2xl border border-slate-200 bg-white p-5">
      <div className="flex items-start justify-between gap-4">
        <div>
          <h4 className="font-semibold text-slate-900">
            {skill.skill}
          </h4>

          <p className="mt-1 text-sm text-slate-500">
            {skill.score} correct out of{" "}
            {skill.total}
          </p>
        </div>

        <div className="text-right">
          <p className="text-xl font-bold text-slate-900">
            {skill.percentage}%
          </p>

          <p className="text-xs font-medium text-slate-500">
            {skill.performance}
          </p>
        </div>
      </div>

      <div className="mt-4 h-2 overflow-hidden rounded-full bg-slate-100">
        <div
          className="h-full rounded-full bg-cyan-600 transition-all"
          style={{
            width: `${skill.percentage}%`,
          }}
        />
      </div>
    </div>
  );
}

function AssessmentReportCard({
  analysis,
  profile,
}: {
  analysis: IndividualAssessmentAnalysis;
  profile: HighSchoolProfileData;
}) {
  const reportTitle =
    getContextualCategoryLabel(
      analysis.category,
      profile
    );

  return (
    <section className="rounded-3xl border border-slate-200 bg-white p-6 shadow-sm md:p-7">
      <div className="flex flex-col gap-5 lg:flex-row lg:items-start lg:justify-between">
        <div>
          <p className="text-sm font-semibold uppercase tracking-wider text-cyan-600">
            Class {profile.studentClass} Individual Report
          </p>

          <h2 className="mt-2 text-2xl font-bold text-slate-900">
            {reportTitle}
          </h2>

          <p className="mt-3 max-w-3xl leading-7 text-slate-600">
            {analysis.summary}
          </p>
        </div>

        <div className="min-w-40 rounded-2xl border border-slate-200 bg-slate-50 p-5">
          <p className="text-sm text-slate-500">
            Overall Score
          </p>

          <p className="mt-2 text-3xl font-bold text-slate-900">
            {analysis.percentage}%
          </p>

          <p className="mt-1 text-sm font-semibold text-cyan-700">
            {analysis.performance}
          </p>

          <p className="mt-3 text-xs text-slate-500">
            {analysis.score} /{" "}
            {analysis.total} correct
          </p>
        </div>
      </div>

      <div className="mt-8">
        <div className="flex items-center gap-3">
          <BarChart3
            size={22}
            className="text-cyan-600"
          />

          <h3 className="text-xl font-bold text-slate-900">
            Skill Performance
          </h3>
        </div>

        <div className="mt-5 grid gap-4 md:grid-cols-2 xl:grid-cols-3">
          {analysis.skillAnalysis.map(
            (skill) => (
              <SkillProgress
                key={skill.skill}
                skill={skill}
              />
            )
          )}
        </div>
      </div>

      <div className="mt-8 grid gap-5 lg:grid-cols-2">
        <div className="rounded-2xl border border-emerald-200 bg-emerald-50 p-6">
          <div className="flex items-center gap-3">
            <CheckCircle2
              size={22}
              className="text-emerald-600"
            />

            <h3 className="text-lg font-bold text-emerald-900">
              Strong Areas
            </h3>
          </div>

          {analysis.strongAreas.length > 0 ? (
            <div className="mt-4 space-y-3">
              {analysis.strongAreas.map(
                (area) => (
                  <div
                    key={area.skill}
                    className="rounded-xl bg-white/80 p-4"
                  >
                    <div className="flex items-center justify-between gap-3">
                      <span className="font-medium text-slate-800">
                        {area.skill}
                      </span>

                      <span className="font-bold text-emerald-700">
                        {area.percentage}%
                      </span>
                    </div>
                  </div>
                )
              )}
            </div>
          ) : (
            <p className="mt-4 leading-7 text-emerald-800">
              No skill has reached the strong
              performance threshold yet. Continue
              targeted practice.
            </p>
          )}
        </div>

        <div className="rounded-2xl border border-amber-200 bg-amber-50 p-6">
          <div className="flex items-center gap-3">
            <AlertTriangle
              size={22}
              className="text-amber-600"
            />

            <h3 className="text-lg font-bold text-amber-900">
              Improvement Areas
            </h3>
          </div>

          {analysis.improvementAreas.length > 0 ? (
            <div className="mt-4 space-y-3">
              {analysis.improvementAreas.map(
                (area) => (
                  <div
                    key={area.skill}
                    className="rounded-xl bg-white/80 p-4"
                  >
                    <div className="flex items-center justify-between gap-3">
                      <span className="font-medium text-slate-800">
                        {area.skill}
                      </span>

                      <span className="font-bold text-amber-700">
                        {area.percentage}%
                      </span>
                    </div>
                  </div>
                )
              )}
            </div>
          ) : (
            <p className="mt-4 leading-7 text-amber-800">
              No major weak area was identified in
              this assessment.
            </p>
          )}
        </div>
      </div>

      {analysis.moderateAreas.length > 0 && (
        <div className="mt-5 rounded-2xl border border-blue-200 bg-blue-50 p-6">
          <div className="flex items-center gap-3">
            <TrendingUp
              size={22}
              className="text-blue-600"
            />

            <h3 className="text-lg font-bold text-blue-900">
              Developing Areas
            </h3>
          </div>

          <div className="mt-4 flex flex-wrap gap-3">
            {analysis.moderateAreas.map(
              (area) => (
                <div
                  key={area.skill}
                  className="rounded-xl bg-white px-4 py-3 font-medium text-slate-700"
                >
                  {area.skill} —{" "}
                  {area.percentage}%
                </div>
              )
            )}
          </div>
        </div>
      )}

      <div className="mt-5 rounded-2xl border border-cyan-200 bg-cyan-50 p-6">
        <div className="flex items-center gap-3">
          <Lightbulb
            size={22}
            className="text-cyan-600"
          />

          <h3 className="text-lg font-bold text-cyan-900">
            Assessment Recommendation
          </h3>
        </div>

        <p className="mt-4 leading-7 text-cyan-900">
          {analysis.recommendation}
        </p>
      </div>
    </section>
  );
}

function AssessmentReports() {
  const navigate = useNavigate();

  const { user } = useAuth();

  const userId = user?.id ?? "";

  const profile = user
    ? getHighSchoolProfile(user.id)
    : null;

  if (!user) {
    return null;
  }

  if (!profile) {
    return (
      <div className="rounded-3xl border border-amber-200 bg-amber-50 p-8">
        <GraduationCap
          size={36}
          className="text-amber-700"
        />

        <h1 className="mt-5 text-2xl font-bold text-slate-900">
          Complete your academic profile
        </h1>

        <p className="mt-3 max-w-2xl leading-7 text-slate-600">
          Your class and academic information are
          required before TalentSphere can prepare
          contextual assessment reports.
        </p>

        <button
          type="button"
          onClick={() =>
            navigate(
              "/high-school-student/profile"
            )
          }
          className="mt-6 rounded-xl bg-cyan-600 px-6 py-3 font-semibold text-white transition hover:bg-cyan-700"
        >
          Complete Profile
        </button>
      </div>
    );
  }

  if (
    (profile.studentClass === "11" ||
      profile.studentClass === "12") &&
    !profile.currentStream
  ) {
    return (
      <div className="rounded-3xl border border-amber-200 bg-amber-50 p-8">
        <GraduationCap
          size={36}
          className="text-amber-700"
        />

        <h1 className="mt-5 text-2xl font-bold text-slate-900">
          Select your current stream
        </h1>

        <p className="mt-3 max-w-2xl leading-7 text-slate-600">
          Class {profile.studentClass} reports are
          based on your current stream. Update your
          profile before viewing contextual analysis.
        </p>

        <button
          type="button"
          onClick={() =>
            navigate(
              "/high-school-student/profile"
            )
          }
          className="mt-6 rounded-xl bg-cyan-600 px-6 py-3 font-semibold text-white transition hover:bg-cyan-700"
        >
          Update Profile
        </button>
      </div>
    );
  }

  const questionBank =
    getAssessmentQuestionBank({
      studentClass: profile.studentClass,
      currentStream: profile.currentStream,
    });

  const results =
    getUserAssessmentResults(userId);

  const reports = categories
    .map((category) => {
      const result =
        getLatestResultByCategory(
          results,
          category
        );

      if (!result) {
        return null;
      }

      return analyzeAssessmentResult({
        category,
        questions: questionBank[category],
        result,
      });
    })
    .filter(
      (
        report
      ): report is IndividualAssessmentAnalysis =>
        report !== null
    );

  const reportContext =
    getReportContext(profile);

  const assessmentPurpose =
    getAssessmentPurpose(
      profile.studentClass
    );

  if (reports.length === 0) {
    return (
      <div className="space-y-8">
        <div>
          <p className="font-semibold text-cyan-600">
            {reportContext.eyebrow}
          </p>

          <h1 className="mt-2 text-3xl font-bold text-slate-900">
            {reportContext.title}
          </h1>

          <p className="mt-3 max-w-3xl leading-7 text-slate-600">
            {reportContext.description}
          </p>
        </div>

        <div className="rounded-3xl border border-slate-200 bg-white p-10 text-center shadow-sm">
          <Brain
            size={48}
            className="mx-auto text-slate-300"
          />

          <h2 className="mt-5 text-xl font-bold text-slate-900">
            No assessment report available
          </h2>

          <p className="mx-auto mt-3 max-w-xl leading-7 text-slate-600">
            Complete at least one assessment to
            generate your first Class{" "}
            {profile.studentClass} individual
            performance report.
          </p>

          <button
            type="button"
            onClick={() =>
              navigate(
                "/high-school-student/assessment"
              )
            }
            className="mt-6 rounded-xl bg-cyan-600 px-6 py-3 font-semibold text-white transition hover:bg-cyan-700"
          >
            Go to Assessments
          </button>
        </div>
      </div>
    );
  }

  const completedAssessments =
    reports.length;

  const totalAssessments =
    categories.length;

  const averagePercentage = Math.round(
    reports.reduce(
      (total, report) =>
        total + report.percentage,
      0
    ) / reports.length
  );

  const finalGuidanceReady =
    completedAssessments ===
    totalAssessments;

  return (
    <div className="space-y-8">
      <div>
        <p className="font-semibold text-cyan-600">
          {reportContext.eyebrow}
        </p>

        <h1 className="mt-2 text-3xl font-bold text-slate-900">
          {reportContext.title}
        </h1>

        <p className="mt-3 max-w-3xl leading-7 text-slate-600">
          {reportContext.description}
        </p>
      </div>

      <div className="grid gap-5 md:grid-cols-3">
        <div className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
          <Brain
            size={24}
            className="text-cyan-600"
          />

          <p className="mt-4 text-sm text-slate-500">
            Assessments Completed
          </p>

          <p className="mt-2 text-3xl font-bold text-slate-900">
            {completedAssessments} /{" "}
            {totalAssessments}
          </p>
        </div>

        <div className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
          <TrendingUp
            size={24}
            className="text-cyan-600"
          />

          <p className="mt-4 text-sm text-slate-500">
            Average Performance
          </p>

          <p className="mt-2 text-3xl font-bold text-slate-900">
            {averagePercentage}%
          </p>
        </div>

        <div className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
          <Target
            size={24}
            className="text-cyan-600"
          />

          <p className="mt-4 text-sm text-slate-500">
            {reportContext.guidanceLabel}
          </p>

          <p className="mt-2 text-xl font-bold text-slate-900">
            {finalGuidanceReady
              ? "Ready for Analysis"
              : `${totalAssessments - completedAssessments} ${
                  totalAssessments - completedAssessments === 1
                    ? "Assessment"
                    : "Assessments"
                } Remaining`}
          </p>
        </div>
      </div>

      <div className="space-y-7">
        {reports.map((report) => (
          <AssessmentReportCard
            key={report.category}
            analysis={report}
            profile={profile}
          />
        ))}
      </div>

      <section className="rounded-3xl border border-slate-200 bg-white p-7 shadow-sm">
        <div className="flex flex-col justify-between gap-6 lg:flex-row lg:items-center">
          <div>
            <p className="text-sm font-semibold uppercase tracking-wider text-cyan-600">
              Combined Analysis
            </p>

            <h2 className="mt-2 text-2xl font-bold text-slate-900">
              {assessmentPurpose.reportTitle}
            </h2>

            <p className="mt-3 max-w-2xl leading-7 text-slate-600">
              {finalGuidanceReady
                ? `All Class ${profile.studentClass} assessment sections are complete. Your combined guidance report is ready for analysis.`
                : `Complete all ${totalAssessments} assessment sections before generating your combined guidance report.`}
            </p>
          </div>

          <button
            type="button"
            disabled={!finalGuidanceReady}
            onClick={() =>
              navigate(
                "/high-school-student/final-guidance"
              )
            }
            className="rounded-xl bg-cyan-600 px-6 py-3 font-semibold text-white transition hover:bg-cyan-700 disabled:cursor-not-allowed disabled:bg-slate-300"
          >
            {finalGuidanceReady
              ? "View Final Guidance Report"
              : "Final Report Locked"}
          </button>
        </div>
      </section>
    </div>
  );
}

export default AssessmentReports;