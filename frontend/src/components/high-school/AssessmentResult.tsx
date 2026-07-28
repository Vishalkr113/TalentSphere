type AssessmentResultProps = {
    score: number;
    total: number;
    percentage: number;
    onBack: () => void;
    onReport: () => void;
};

function AssessmentResult({
    score,
    total,
    percentage,
    onBack,
    onReport,
}: AssessmentResultProps) {
    return (
        <div className="mx-auto max-w-2xl rounded-3xl bg-white p-10 shadow-lg">

            <div className="text-center">

                <div className="mx-auto flex h-24 w-24 items-center justify-center rounded-full bg-green-100 text-5xl">
                    🎉
                </div>

                <h1 className="mt-6 text-4xl font-bold text-slate-900">
                    Assessment Completed
                </h1>

                <p className="mt-3 text-slate-500">
                    Great job! Here is your performance summary.
                </p>

            </div>

            <div className="mt-10 grid grid-cols-3 gap-5">

                <div className="rounded-2xl bg-cyan-50 p-5 text-center">

                    <p className="text-sm text-slate-500">
                        Score
                    </p>

                    <h2 className="mt-2 text-3xl font-bold text-cyan-600">
                        {score}/{total}
                    </h2>

                </div>

                <div className="rounded-2xl bg-blue-50 p-5 text-center">

                    <p className="text-sm text-slate-500">
                        Percentage
                    </p>

                    <h2 className="mt-2 text-3xl font-bold text-blue-600">
                        {percentage}%
                    </h2>

                </div>

                <div className="rounded-2xl bg-green-50 p-5 text-center">

                    <p className="text-sm text-slate-500">
                        Performance
                    </p>

                    <h2 className="mt-2 text-2xl font-bold text-green-600">

                        {percentage >= 80
                            ? "Excellent"
                            : percentage >= 60
                                ? "Good"
                                : percentage >= 40
                                    ? "Average"
                                    : "Needs Improvement"}

                    </h2>

                </div>

            </div>

            <div className="mt-10 flex justify-center gap-4">

                <button
                    onClick={onReport}
                    className="rounded-xl bg-cyan-600 px-6 py-3 font-semibold text-white hover:bg-cyan-700"
                >
                    View Report
                </button>

                <button
                    onClick={onBack}
                    className="rounded-xl border px-6 py-3 font-semibold hover:bg-slate-100"
                >
                    Dashboard
                </button>

            </div>

        </div>
    );
}

export default AssessmentResult;