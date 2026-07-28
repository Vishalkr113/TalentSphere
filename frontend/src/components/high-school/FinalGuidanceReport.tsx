import {
    AlertTriangle,
    ArrowRight,
    Award,
    BarChart3,
    Brain,
    CheckCircle2,
    Compass,
    Lightbulb,
    Target,
    TrendingUp,
} from "lucide-react";

import { useAuth } from "../../contexts/AuthContext";

import {
    generateFinalStreamGuidance,
    type StreamScore,
} from "../../data/assessment/streamGuidanceService";

function StreamRankingCard({
    stream,
}: {
    stream: StreamScore;
}) {
    return (
        <div className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
            <div className="flex items-start justify-between gap-4">
                <div className="flex items-center gap-4">
                    <div className="flex h-12 w-12 items-center justify-center rounded-xl bg-cyan-100 font-bold text-cyan-700">
                        #{stream.rank}
                    </div>

                    <div>
                        <h3 className="text-xl font-bold text-slate-900">
                            {stream.stream}
                        </h3>

                        <p className="mt-1 text-sm font-medium text-slate-500">
                            {stream.fitLevel}
                        </p>
                    </div>
                </div>

                <p className="text-3xl font-bold text-slate-900">
                    {stream.score}%
                </p>
            </div>

            <div className="mt-5 h-3 overflow-hidden rounded-full bg-slate-100">
                <div
                    className="h-full rounded-full bg-cyan-600"
                    style={{
                        width: `${stream.score}%`,
                    }}
                />
            </div>

            <p className="mt-5 leading-7 text-slate-600">
                {stream.reason}
            </p>

            {stream.strengths.length > 0 && (
                <div className="mt-5">
                    <p className="text-sm font-semibold text-emerald-700">
                        Supporting strengths
                    </p>

                    <div className="mt-3 flex flex-wrap gap-2">
                        {stream.strengths
                            .slice(0, 4)
                            .map((strength) => (
                                <span
                                    key={strength}
                                    className="rounded-full bg-emerald-50 px-3 py-2 text-sm font-medium text-emerald-700"
                                >
                                    {strength}
                                </span>
                            ))}
                    </div>
                </div>
            )}

            {stream.concerns.length > 0 && (
                <div className="mt-5">
                    <p className="text-sm font-semibold text-amber-700">
                        Current concerns
                    </p>

                    <div className="mt-3 flex flex-wrap gap-2">
                        {stream.concerns
                            .slice(0, 3)
                            .map((concern) => (
                                <span
                                    key={concern}
                                    className="rounded-full bg-amber-50 px-3 py-2 text-sm font-medium text-amber-700"
                                >
                                    {concern}
                                </span>
                            ))}
                    </div>
                </div>
            )}
        </div>
    );
}

function FinalGuidanceReport() {
    const { user } = useAuth();

    const guidance =
        generateFinalStreamGuidance(
            user?.id ?? ""
        );

    if (!guidance.ready) {
        const progress = Math.round(
            (
                guidance.completedAssessments /
                guidance.requiredAssessments
            ) *
            100
        );

        return (
            <div className="space-y-8">
                <div>
                    <p className="font-semibold text-cyan-600">
                        Final Guidance Report
                    </p>

                    <h1 className="mt-2 text-3xl font-bold text-slate-900">
                        Stream Guidance Analysis
                    </h1>

                    <p className="mt-3 max-w-3xl leading-7 text-slate-600">
                        Complete all five assessments to
                        generate your combined academic
                        stream guidance report.
                    </p>
                </div>

                <div className="rounded-3xl border border-slate-200 bg-white p-8 shadow-sm">
                    <div className="flex items-start gap-4">
                        <div className="flex h-14 w-14 items-center justify-center rounded-2xl bg-amber-100 text-amber-700">
                            <AlertTriangle size={28} />
                        </div>

                        <div className="flex-1">
                            <h2 className="text-2xl font-bold text-slate-900">
                                Final analysis is not ready yet
                            </h2>

                            <p className="mt-3 leading-7 text-slate-600">
                                {guidance.summary}
                            </p>
                        </div>
                    </div>

                    <div className="mt-8">
                        <div className="flex items-center justify-between">
                            <p className="font-semibold text-slate-700">
                                Assessment Completion
                            </p>

                            <p className="font-bold text-slate-900">
                                {
                                    guidance.completedAssessments
                                }{" "}
                                /{" "}
                                {
                                    guidance.requiredAssessments
                                }
                            </p>
                        </div>

                        <div className="mt-3 h-3 overflow-hidden rounded-full bg-slate-100">
                            <div
                                className="h-full rounded-full bg-cyan-600"
                                style={{
                                    width: `${progress}%`,
                                }}
                            />
                        </div>

                        <p className="mt-3 text-sm text-slate-500">
                            {progress}% completed
                        </p>
                    </div>

                    <div className="mt-8 rounded-2xl bg-slate-50 p-6">
                        <h3 className="font-bold text-slate-900">
                            Why all assessments are
                            required
                        </h3>

                        <p className="mt-3 leading-7 text-slate-600">
                            The final stream recommendation
                            compares academic subject
                            performance with numerical,
                            analytical, language and
                            reasoning skills. A partial
                            assessment profile is not used
                            for the final recommendation.
                        </p>
                    </div>
                </div>
            </div>
        );
    }

    const recommendedStream =
        guidance.streamScores[0];

    return (
        <div className="space-y-8">
            <div>
                <p className="font-semibold text-cyan-600">
                    Final Guidance Report
                </p>

                <h1 className="mt-2 text-3xl font-bold text-slate-900">
                    Your Stream Guidance Analysis
                </h1>

                <p className="mt-3 max-w-3xl leading-7 text-slate-600">
                    This report combines your latest
                    performance across Aptitude,
                    Mathematics, English, Science and
                    Logical Reasoning assessments.
                </p>
            </div>

            <section className="rounded-3xl bg-gradient-to-r from-cyan-600 to-blue-700 p-8 text-white shadow-lg">
                <div className="flex flex-col gap-8 lg:flex-row lg:items-center lg:justify-between">
                    <div className="max-w-3xl">
                        <div className="flex items-center gap-3">
                            <Award size={28} />

                            <p className="font-semibold uppercase tracking-wider text-cyan-100">
                                Recommended Stream
                            </p>
                        </div>

                        <h2 className="mt-5 text-5xl font-bold">
                            {guidance.recommendedStream}
                        </h2>

                        <p className="mt-5 text-lg leading-8 text-cyan-50">
                            {guidance.summary}
                        </p>
                    </div>

                    <div className="min-w-56 rounded-3xl bg-white/10 p-6 backdrop-blur">
                        <p className="text-sm text-cyan-100">
                            Alignment Score
                        </p>

                        <p className="mt-2 text-5xl font-bold">
                            {
                                guidance.recommendationScore
                            }
                            %
                        </p>

                        <div className="mt-5 border-t border-white/20 pt-5">
                            <p className="text-sm text-cyan-100">
                                Confidence
                            </p>

                            <p className="mt-1 text-xl font-bold">
                                {guidance.confidenceLevel}
                            </p>
                        </div>
                    </div>
                </div>
            </section>

            <section className="rounded-3xl border border-slate-200 bg-white p-7 shadow-sm">
                <div className="flex items-center gap-3">
                    <Brain
                        size={24}
                        className="text-cyan-600"
                    />

                    <h2 className="text-2xl font-bold text-slate-900">
                        Why this stream is recommended
                    </h2>
                </div>

                <p className="mt-5 leading-8 text-slate-600">
                    {guidance.recommendationReason}
                </p>

                <div className="mt-6 rounded-2xl border border-cyan-200 bg-cyan-50 p-5">
                    <div className="flex items-start gap-3">
                        <Lightbulb
                            size={22}
                            className="mt-1 shrink-0 text-cyan-700"
                        />

                        <p className="leading-7 text-cyan-900">
                            The recommendation is generated
                            from your assessed skill
                            evidence. It should support,
                            not replace, discussion with
                            teachers, mentors and parents.
                        </p>
                    </div>
                </div>
            </section>

            <section>
                <div className="flex items-center gap-3">
                    <BarChart3
                        size={24}
                        className="text-cyan-600"
                    />

                    <h2 className="text-2xl font-bold text-slate-900">
                        Stream Alignment Comparison
                    </h2>
                </div>

                <p className="mt-3 text-slate-600">
                    Compare how your current assessed
                    skills align with each academic
                    stream.
                </p>

                <div className="mt-6 grid gap-5 xl:grid-cols-2">
                    {guidance.streamScores.map(
                        (stream) => (
                            <StreamRankingCard
                                key={stream.stream}
                                stream={stream}
                            />
                        )
                    )}
                </div>
            </section>

            <div className="grid gap-6 lg:grid-cols-2">
                <section className="rounded-3xl border border-emerald-200 bg-emerald-50 p-7">
                    <div className="flex items-center gap-3">
                        <CheckCircle2
                            size={24}
                            className="text-emerald-700"
                        />

                        <h2 className="text-xl font-bold text-emerald-900">
                            Strongest Assessed Skills
                        </h2>
                    </div>

                    <div className="mt-5 space-y-3">
                        {guidance.strongestSkills
                            .length > 0 ? (
                            guidance.strongestSkills.map(
                                (skill) => (
                                    <div
                                        key={skill.skill}
                                        className="flex items-center justify-between rounded-xl bg-white/80 p-4"
                                    >
                                        <span className="font-medium text-slate-800">
                                            {skill.skill}
                                        </span>

                                        <span className="font-bold text-emerald-700">
                                            {skill.percentage}%
                                        </span>
                                    </div>
                                )
                            )
                        ) : (
                            <p className="leading-7 text-emerald-800">
                                Continue developing your
                                assessed skills through
                                regular practice.
                            </p>
                        )}
                    </div>
                </section>

                <section className="rounded-3xl border border-amber-200 bg-amber-50 p-7">
                    <div className="flex items-center gap-3">
                        <Target
                            size={24}
                            className="text-amber-700"
                        />

                        <h2 className="text-xl font-bold text-amber-900">
                            Improvement Priorities
                        </h2>
                    </div>

                    <div className="mt-5 space-y-3">
                        {guidance.improvementSkills
                            .length > 0 ? (
                            guidance.improvementSkills.map(
                                (skill) => (
                                    <div
                                        key={skill.skill}
                                        className="flex items-center justify-between rounded-xl bg-white/80 p-4"
                                    >
                                        <span className="font-medium text-slate-800">
                                            {skill.skill}
                                        </span>

                                        <span className="font-bold text-amber-700">
                                            {skill.percentage}%
                                        </span>
                                    </div>
                                )
                            )
                        ) : (
                            <p className="leading-7 text-amber-800">
                                No major low-scoring skill
                                area was identified in your
                                current assessment profile.
                            </p>
                        )}
                    </div>
                </section>
            </div>

            <section className="rounded-3xl border border-slate-200 bg-white p-7 shadow-sm">
                <div className="flex items-center gap-3">
                    <Compass
                        size={24}
                        className="text-cyan-600"
                    />

                    <h2 className="text-2xl font-bold text-slate-900">
                        Recommended Next Steps
                    </h2>
                </div>

                <div className="mt-6 space-y-4">
                    {guidance.nextSteps.map(
                        (step, index) => (
                            <div
                                key={`${step}-${index}`}
                                className="flex items-start gap-4 rounded-2xl bg-slate-50 p-5"
                            >
                                <div className="flex h-9 w-9 shrink-0 items-center justify-center rounded-full bg-cyan-600 font-bold text-white">
                                    {index + 1}
                                </div>

                                <p className="pt-1 leading-7 text-slate-700">
                                    {step}
                                </p>
                            </div>
                        )
                    )}
                </div>
            </section>

            <section className="rounded-3xl bg-slate-900 p-7 text-white">
                <div className="flex flex-col gap-5 lg:flex-row lg:items-center lg:justify-between">
                    <div>
                        <div className="flex items-center gap-3">
                            <TrendingUp
                                size={22}
                                className="text-cyan-400"
                            />

                            <h2 className="text-xl font-bold">
                                Current Best Alignment
                            </h2>
                        </div>

                        <p className="mt-3 max-w-2xl leading-7 text-slate-300">
                            {recommendedStream.stream} is
                            currently ranked #1 with a{" "}
                            {recommendedStream.score}%
                            alignment score and a{" "}
                            {recommendedStream.fitLevel.toLowerCase()}
                            .
                        </p>
                    </div>

                    <div className="flex items-center gap-3 font-semibold text-cyan-300">
                        Review Guidance
                        <ArrowRight size={20} />
                    </div>
                </div>
            </section>
        </div>
    );
}

export default FinalGuidanceReport;