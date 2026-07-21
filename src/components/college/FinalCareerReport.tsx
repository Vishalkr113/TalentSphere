import React, { useMemo } from "react";
import {
    User,
    FileText,
    BarChart3,
    Target,
    Code2,
    MessageSquare,
    Briefcase,
    Trophy,
    Brain,
    CheckCircle,
} from "lucide-react";

import { useAuth } from "../../contexts/AuthContext";

import {
    getCollegeProfile,
    getCollegeProfileCompletion,
} from "../../services/college/collegeProfileService";

import {
    getResume,
    analyzeResume,
} from "../../services/college/collegeResumeService";

import {
    getCurrentContextAttempts,
} from "../../services/college/collegeAssessmentService";

import {
    FinalCareerReport as Report,
    calculateOverallScore,
} from "../../services/college/finalCareerReportService";

export default function FinalCareerReport() {
    const { user } = useAuth();

    const profile = useMemo(() => {
        if (!user) return null;
        return getCollegeProfile(user.id);
    }, [user]);

    const resume = useMemo(() => {
        if (!user) return null;
        return getResume(user.id);
    }, [user]);

    const resumeAnalysis = useMemo(() => {
        if (!resume || !profile) return null;
        return analyzeResume(resume, profile);
    }, [resume, profile]);

    const attempts = useMemo(() => {
        if (!user || !profile) return [];

        return getCurrentContextAttempts(
            user.id,
            profile
        );
    }, [user, profile]);

    const assessmentAverage = useMemo(() => {
        if (attempts.length === 0) return 0;

        return Math.round(
            attempts.reduce(
                (total, item) => total + item.percentage,
                0
            ) / attempts.length
        );
    }, [attempts]);

    const report: Report = useMemo(() => {
        const data: Report = {
            profileCompletion: profile
                ? getCollegeProfileCompletion(profile)
                : 0,

            resumeScore:
                resumeAnalysis?.resumeScore ?? 0,

            atsScore:
                resumeAnalysis?.atsScore ?? 0,

            assessmentScore:
                assessmentAverage,

            codingScore:
                assessmentAverage,

            interviewScore: 0,

            placementScore: Math.round(
                (
                    (resumeAnalysis?.resumeScore ?? 0) +
                    (resumeAnalysis?.atsScore ?? 0) +
                    assessmentAverage
                ) / 3
            ),

            achievementScore: 0,

            overallScore: 0,
        };

        data.overallScore =
            calculateOverallScore(data);

        return data;
    }, [
        profile,
        resumeAnalysis,
        assessmentAverage,
    ]);

    if (!user) {
        return null;
    }

    return (
        <div className="space-y-8 p-8">

            <div>
                <h1 className="text-3xl font-bold text-slate-900">
                    Final Career Report
                </h1>

                <p className="mt-2 text-slate-500">
                    Complete career performance summary generated from your profile, resume and assessments.
                </p>
            </div>

            <section className="rounded-3xl bg-gradient-to-r from-cyan-600 to-blue-700 p-8 text-white shadow-lg">

                <div className="flex flex-col justify-between gap-8 lg:flex-row lg:items-center">

                    <div>

                        <p className="text-cyan-100">
                            Overall Career Readiness
                        </p>

                        <h2 className="mt-3 text-6xl font-bold">
                            {report.overallScore}%
                        </h2>

                        <p className="mt-4 max-w-2xl text-cyan-100">
                            Generated using profile completion,
                            resume quality, ATS score,
                            assessments and placement readiness.
                        </p>

                    </div>

                    <div className="grid grid-cols-2 gap-4">

                        <StatCard
                            title="Profile"
                            value={`${report.profileCompletion}%`}
                            icon={<User size={20} />}
                        />

                        <StatCard
                            title="Resume"
                            value={`${report.resumeScore}%`}
                            icon={<FileText size={20} />}
                        />

                        <StatCard
                            title="ATS"
                            value={`${report.atsScore}%`}
                            icon={<Target size={20} />}
                        />

                        <StatCard
                            title="Assessment"
                            value={`${report.assessmentScore}%`}
                            icon={<BarChart3 size={20} />}
                        />

                    </div>

                </div>

            </section>

            <section className="rounded-3xl border border-slate-200 bg-white p-8 shadow-sm">

                <div className="mb-8 flex items-center gap-3">

                    <User className="text-cyan-600" />

                    <h2 className="text-2xl font-bold text-slate-900">
                        Student Information
                    </h2>

                </div>

                <div className="grid gap-5 md:grid-cols-2 lg:grid-cols-3">

                    <SummaryItem
                        title="Full Name"
                        value={profile?.fullName ?? "-"}
                    />

                    <SummaryItem
                        title="Email"
                        value={profile?.email ?? "-"}
                    />

                    <SummaryItem
                        title="College"
                        value={profile?.college ?? "-"}
                    />

                    <SummaryItem
                        title="Degree"
                        value={profile?.degree ?? "-"}
                    />

                    <SummaryItem
                        title="Branch"
                        value={profile?.branch ?? "-"}
                    />

                    <SummaryItem
                        title="Semester"
                        value={profile?.semester ?? "-"}
                    />

                </div>

            </section>
            <section className="grid gap-6 xl:grid-cols-4 lg:grid-cols-2">

                <ScoreCard
                    title="Resume Score"
                    value={report.resumeScore}
                    icon={<FileText size={22} />}
                    color="cyan"
                />

                <ScoreCard
                    title="ATS Score"
                    value={report.atsScore}
                    icon={<Target size={22} />}
                    color="emerald"
                />

                <ScoreCard
                    title="Assessment"
                    value={report.assessmentScore}
                    icon={<BarChart3 size={22} />}
                    color="violet"
                />

                <ScoreCard
                    title="Placement Readiness"
                    value={report.placementScore}
                    icon={<Briefcase size={22} />}
                    color="amber"
                />

            </section>

            <section className="rounded-3xl border border-slate-200 bg-white p-8 shadow-sm">

                <div className="mb-8 flex items-center gap-3">

                    <FileText className="text-cyan-600" />

                    <h2 className="text-2xl font-bold text-slate-900">
                        Resume Summary
                    </h2>

                </div>

                <div className="grid gap-6 lg:grid-cols-2">

                    <SummaryItem
                        title="Resume Score"
                        value={`${resumeAnalysis?.resumeScore ?? 0}%`}
                    />

                    <SummaryItem
                        title="ATS Score"
                        value={`${resumeAnalysis?.atsScore ?? 0}%`}
                    />

                    <SummaryItem
                        title="Target Role Match"
                        value={`${resumeAnalysis?.roleMatch ?? 0}%`}
                    />

                    <SummaryItem
                        title="Skills"
                        value={`${resume?.skills?.length ?? 0}`}
                    />

                    <SummaryItem
                        title="Projects"
                        value={`${resume?.projects?.length ?? 0}`}
                    />

                    <SummaryItem
                        title="Certifications"
                        value={`${resume?.certifications?.length ?? 0}`}
                    />

                </div>

                {resumeAnalysis?.strengths &&
                    resumeAnalysis.strengths.length > 0 && (

                        <div className="mt-10">

                            <h3 className="mb-4 text-lg font-bold text-slate-900">
                                Resume Strengths
                            </h3>

                            <div className="flex flex-wrap gap-3">

                                {resumeAnalysis.strengths.map((item) => (

                                    <span
                                        key={item}
                                        className="rounded-full bg-emerald-100 px-4 py-2 text-sm font-medium text-emerald-700"
                                    >
                                        {item}
                                    </span>

                                ))}

                            </div>

                        </div>

                    )}

                {resumeAnalysis?.improvements &&
                    resumeAnalysis.improvements.length > 0 && (

                        <div className="mt-10">

                            <h3 className="mb-4 text-lg font-bold text-slate-900">
                                Suggested Improvements
                            </h3>

                            <div className="space-y-3">

                                {resumeAnalysis.improvements.map((item) => (

                                    <div
                                        key={item}
                                        className="flex items-start gap-3 rounded-xl bg-amber-50 p-4"
                                    >
                                        <CheckCircle
                                            size={18}
                                            className="mt-1 text-amber-600"
                                        />

                                        <p className="text-slate-700">
                                            {item}
                                        </p>

                                    </div>

                                ))}

                            </div>

                        </div>

                    )}

            </section>
            <section className="rounded-3xl border border-slate-200 bg-white p-8 shadow-sm">

                <div className="mb-8 flex items-center gap-3">

                    <BarChart3 className="text-cyan-600" />

                    <h2 className="text-2xl font-bold text-slate-900">
                        Assessment Summary
                    </h2>

                </div>

                {attempts.length === 0 ? (

                    <div className="rounded-2xl border border-dashed border-slate-300 p-10 text-center">

                        <Brain
                            size={52}
                            className="mx-auto text-slate-300"
                        />

                        <h3 className="mt-5 text-xl font-semibold text-slate-900">
                            No Assessment Available
                        </h3>

                        <p className="mt-3 text-slate-500">
                            Complete assessments to generate
                            your performance report.
                        </p>

                    </div>

                ) : (

                    <>

                        <div className="grid gap-6 md:grid-cols-4">

                            <ScoreCard
                                title="Completed"
                                value={attempts.length}
                                icon={<CheckCircle size={20} />}
                                color="cyan"
                            />

                            <ScoreCard
                                title="Average Score"
                                value={assessmentAverage}
                                icon={<BarChart3 size={20} />}
                                color="emerald"
                            />

                            <ScoreCard
                                title="Highest Score"
                                value={Math.max(
                                    ...attempts.map(
                                        (item) =>
                                            item.percentage
                                    )
                                )}
                                icon={<Trophy size={20} />}
                                color="amber"
                            />

                            <ScoreCard
                                title="Career Readiness"
                                value={report.overallScore}
                                icon={<Target size={20} />}
                                color="violet"
                            />

                        </div>

                        <div className="mt-10 overflow-hidden rounded-2xl border border-slate-200">

                            <table className="w-full">

                                <thead>

                                    <tr className="bg-slate-50">

                                        <th className="p-4 text-left">
                                            Assessment
                                        </th>

                                        <th className="p-4 text-left">
                                            Score
                                        </th>

                                        <th className="p-4 text-left">
                                            Percentage
                                        </th>

                                        <th className="p-4 text-left">
                                            Date
                                        </th>

                                    </tr>

                                </thead>

                                <tbody>

                                    {attempts.map((attempt) => (

                                        <tr
                                            key={attempt.id}
                                            className="border-t border-slate-100"
                                        >

                                            <td className="p-4 font-medium text-slate-800">
                                                {attempt.category}
                                            </td>

                                            <td className="p-4">
                                                {attempt.score}/
                                                {attempt.total}
                                            </td>

                                            <td className="p-4">

                                                <span className="rounded-full bg-cyan-100 px-3 py-1 text-sm font-semibold text-cyan-700">
                                                    {attempt.percentage}%
                                                </span>

                                            </td>

                                            <td className="p-4 text-slate-500">
                                                {new Date(
                                                    attempt.completedAt
                                                ).toLocaleDateString()}
                                            </td>

                                        </tr>

                                    ))}

                                </tbody>

                            </table>

                        </div>

                    </>

                )}

            </section>

            <section className="grid gap-6 lg:grid-cols-2">

                <div className="rounded-3xl border border-slate-200 bg-white p-8 shadow-sm">

                    <div className="mb-6 flex items-center gap-3">

                        <Code2 className="text-cyan-600" />

                        <h2 className="text-2xl font-bold text-slate-900">
                            Coding Summary
                        </h2>

                    </div>

                    <div className="space-y-5">

                        <SummaryItem
                            title="Coding Readiness"
                            value={`${report.codingScore}%`}
                        />

                        <SummaryItem
                            title="Practice Completed"
                            value={`${attempts.length}`}
                        />

                        <SummaryItem
                            title="Current Level"
                            value={
                                report.codingScore >= 80
                                    ? "Advanced"
                                    : report.codingScore >= 60
                                        ? "Intermediate"
                                        : "Beginner"
                            }
                        />

                    </div>

                </div>

                <div className="rounded-3xl border border-slate-200 bg-white p-8 shadow-sm">

                    <div className="mb-6 flex items-center gap-3">

                        <Briefcase className="text-cyan-600" />

                        <h2 className="text-2xl font-bold text-slate-900">
                            Placement Readiness
                        </h2>

                    </div>

                    <div className="space-y-5">

                        <SummaryItem
                            title="Placement Score"
                            value={`${report.placementScore}%`}
                        />

                        <SummaryItem
                            title="Resume Status"
                            value={
                                report.resumeScore >= 70
                                    ? "Ready"
                                    : "Needs Improvement"
                            }
                        />

                        <SummaryItem
                            title="Assessment Status"
                            value={
                                report.assessmentScore >= 70
                                    ? "Ready"
                                    : "Practice Required"
                            }
                        />

                        <SummaryItem
                            title="Overall Status"
                            value={
                                report.overallScore >= 80
                                    ? "Placement Ready"
                                    : "Preparation Required"
                            }
                        />

                    </div>

                </div>

            </section>
            <section className="rounded-3xl border border-slate-200 bg-white p-8 shadow-sm">

                <div className="mb-8 flex items-center gap-3">

                    <Brain className="text-cyan-600" />

                    <h2 className="text-2xl font-bold text-slate-900">
                        AI Career Recommendation
                    </h2>

                </div>

                <div className="grid gap-6 lg:grid-cols-2">

                    <div className="rounded-2xl bg-cyan-50 p-6">

                        <h3 className="text-lg font-bold text-cyan-900">
                            Recommended Career
                        </h3>

                        <p className="mt-4 text-3xl font-bold text-cyan-700">
                            {profile?.targetRole ??
                                "Software Developer"}
                        </p>

                        <p className="mt-5 leading-7 text-slate-700">
                            Based on your resume,
                            assessment performance,
                            profile completion and ATS
                            analysis, this career path
                            currently provides the best
                            alignment with your skills.
                        </p>

                    </div>

                    <div className="rounded-2xl bg-slate-50 p-6">

                        <h3 className="text-lg font-bold text-slate-900">
                            Recommended Next Steps
                        </h3>

                        <ul className="mt-5 space-y-3">

                            <li>
                                • Improve ATS score above
                                90%.
                            </li>

                            <li>
                                • Complete more coding
                                practice.
                            </li>

                            <li>
                                • Add real-world projects.
                            </li>

                            <li>
                                • Practice mock interviews.
                            </li>

                            <li>
                                • Earn one industry
                                certification.
                            </li>

                        </ul>

                    </div>

                </div>

            </section>

            <section className="rounded-3xl border border-slate-200 bg-white p-8 shadow-sm">

                <div className="mb-8 flex items-center gap-3">

                    <Target className="text-cyan-600" />

                    <h2 className="text-2xl font-bold text-slate-900">
                        30-Day Career Improvement Roadmap
                    </h2>

                </div>

                <div className="grid gap-6 md:grid-cols-2">

                    <RoadmapCard
                        week="Week 1"
                        tasks={[
                            "Improve Resume",
                            "Complete Profile",
                            "Update Skills",
                        ]}
                    />

                    <RoadmapCard
                        week="Week 2"
                        tasks={[
                            "Practice Coding",
                            "Solve Aptitude",
                            "Learn DSA",
                        ]}
                    />

                    <RoadmapCard
                        week="Week 3"
                        tasks={[
                            "Mock Interview",
                            "Mini Project",
                            "GitHub Update",
                        ]}
                    />

                    <RoadmapCard
                        week="Week 4"
                        tasks={[
                            "Apply Internship",
                            "Improve LinkedIn",
                            "Revise Core Subjects",
                        ]}
                    />

                </div>

            </section>

            <section className="rounded-3xl bg-gradient-to-r from-slate-900 to-slate-800 p-10 text-white">

                <div className="flex flex-col gap-8 lg:flex-row lg:items-center lg:justify-between">

                    <div>

                        <p className="text-cyan-300">
                            Final Verdict
                        </p>

                        <h2 className="mt-3 text-4xl font-bold">

                            {report.overallScore >= 85
                                ? "Excellent Career Readiness"

                                : report.overallScore >=
                                    70
                                    ? "Good Career Readiness"

                                    : report.overallScore >=
                                        50
                                        ? "Average Career Readiness"

                                        : "Needs Improvement"}

                        </h2>

                        <p className="mt-5 max-w-3xl leading-8 text-slate-300">

                            Continue improving your
                            resume, coding ability,
                            assessments and interview
                            preparation to become fully
                            placement ready.

                        </p>

                    </div>

                    <div className="text-center">

                        <p className="text-cyan-300">
                            Overall Score
                        </p>

                        <h1 className="mt-2 text-7xl font-bold">
                            {report.overallScore}%
                        </h1>

                    </div>

                </div>

            </section>

        </div>

    );

}

function StatCard({
    title,
    value,
    icon,
}: {
    title: string;
    value: React.ReactNode;
    icon: React.ReactNode;
}) {
    return (
        <div className="rounded-2xl bg-white/10 p-5 backdrop-blur">
            <div className="flex items-center justify-between">
                {icon}
                <span className="text-2xl font-bold">
                    {value}
                </span>
            </div>

            <p className="mt-4 text-sm text-cyan-100">
                {title}
            </p>
        </div>
    );
}

function SummaryItem({
    title,
    value,
}: {
    title: string;
    value: React.ReactNode;
}) {
    return (
        <div className="rounded-2xl border border-slate-200 p-5">
            <p className="text-sm text-slate-500">
                {title}
            </p>

            <p className="mt-2 text-lg font-semibold text-slate-900">
                {value}
            </p>
        </div>
    );
}
function ScoreCard({
    title,
    value,
    icon,
    color,
}: {
    title: string;
    value: number;
    icon: React.ReactNode;
    color:
    | "cyan"
    | "emerald"
    | "amber"
    | "violet";
}) {
    const styles = {
        cyan: {
            bg: "bg-cyan-50",
            icon: "bg-cyan-100 text-cyan-700",
            text: "text-cyan-700",
        },

        emerald: {
            bg: "bg-emerald-50",
            icon: "bg-emerald-100 text-emerald-700",
            text: "text-emerald-700",
        },

        amber: {
            bg: "bg-amber-50",
            icon: "bg-amber-100 text-amber-700",
            text: "text-amber-700",
        },

        violet: {
            bg: "bg-violet-50",
            icon: "bg-violet-100 text-violet-700",
            text: "text-violet-700",
        },
    };

    const style = styles[color];

    return (
        <div
            className={`rounded-3xl ${style.bg} p-6`}
        >
            <div className="flex items-center justify-between">

                <div
                    className={`flex h-12 w-12 items-center justify-center rounded-xl ${style.icon}`}
                >
                    {icon}
                </div>

                <h2
                    className={`text-4xl font-bold ${style.text}`}
                >
                    {value}%
                </h2>

            </div>

            <p className="mt-6 text-sm font-medium text-slate-600">
                {title}
            </p>

            <div className="mt-4 h-2 overflow-hidden rounded-full bg-white">

                <div
                    className={`h-full rounded-full ${color === "cyan"
                        ? "bg-cyan-600"
                        : color === "emerald"
                            ? "bg-emerald-600"
                            : color === "amber"
                                ? "bg-amber-500"
                                : "bg-violet-600"
                        }`}
                    style={{
                        width: `${Math.min(
                            value,
                            100
                        )}%`,
                    }}
                />

            </div>

        </div>
    );
}

function RoadmapCard({
    week,
    tasks,
}: {
    week: string;
    tasks: string[];
}) {
    return (
        <div className="rounded-3xl border border-slate-200 bg-slate-50 p-6">

            <div className="flex items-center gap-3">

                <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-cyan-100 font-bold text-cyan-700">
                    ✓
                </div>

                <h3 className="text-xl font-bold text-slate-900">
                    {week}
                </h3>

            </div>

            <div className="mt-6 space-y-4">

                {tasks.map((task) => (
                    <div
                        key={task}
                        className="flex items-start gap-3"
                    >
                        <CheckCircle
                            size={18}
                            className="mt-1 text-cyan-600"
                        />

                        <span className="text-slate-700">
                            {task}
                        </span>
                    </div>
                ))}

            </div>

        </div>
    );
}