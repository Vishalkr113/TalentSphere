import {
  useEffect,
  useMemo,
  useState,
} from "react";

import { useNavigate } from "react-router-dom";

import {
  Brain,
  Calculator,
  BookOpen,
  FlaskConical,
  Puzzle,
  CheckCircle2,
  Lock,
  GraduationCap,
  Dna,
} from "lucide-react";

import { useAuth } from "../../contexts/AuthContext";

import {
  getAssessmentQuestionBank,
  type AssessmentCategory,
  type AssessmentQuestionBank,
  type Question,
} from "../../data/assessment/assessmentQuestions";

import {
  getUserAssessmentResults,
  saveAssessmentResult,
  type AssessmentResult,
} from "../../data/assessment/assessmentService";

import {
  getAssessmentPurpose,
  getHighSchoolProfile,
  type HighSchoolProfile as HighSchoolProfileData,
} from "../../services/highSchoolProfileService";

type AssessmentCard = {
  category: AssessmentCategory;
  title: string;
  description: string;
  questions: Question[];
  icon: typeof Brain;
};

type StreamKey =
  | "pcm"
  | "pcb"
  | "pcmb"
  | "commerce"
  | "humanities"
  | "unknown";

function getStreamKey(
  currentStream?: string | null
): StreamKey {
  if (!currentStream) {
    return "unknown";
  }

  const stream = currentStream
    .trim()
    .toLowerCase();

  if (
    stream.includes("pcmb") ||
    (
      stream.includes("physics") &&
      stream.includes("chemistry") &&
      stream.includes("mathematics") &&
      stream.includes("biology")
    )
  ) {
    return "pcmb";
  }

  if (
    stream.includes("pcm") ||
    (
      stream.includes("physics") &&
      stream.includes("chemistry") &&
      stream.includes("mathematics")
    )
  ) {
    return "pcm";
  }

  if (
    stream.includes("pcb") ||
    (
      stream.includes("physics") &&
      stream.includes("chemistry") &&
      stream.includes("biology")
    )
  ) {
    return "pcb";
  }

  if (
    stream.includes("commerce") ||
    stream.includes("business")
  ) {
    return "commerce";
  }

  if (
    stream.includes("humanities") ||
    stream.includes("arts")
  ) {
    return "humanities";
  }

  return "unknown";
}

function createAssessmentCards(
  questionBank: AssessmentQuestionBank,
  studentClass: string,
  currentStream?: string | null
): AssessmentCard[] {
  const stream = getStreamKey(currentStream);

  let mathTitle = "Mathematics Assessment";
  let mathDescription =
    "Evaluate arithmetic, algebra and mathematical problem-solving ability.";
  let mathIcon = Calculator;

  let scienceTitle = "Science Assessment";
  let scienceDescription =
    "Evaluate scientific understanding across Physics, Chemistry and Biology.";

  let reasoningTitle =
    "Logical Reasoning Assessment";
  let reasoningDescription =
    "Evaluate pattern recognition, logic and analytical reasoning.";

  if (studentClass === "11" || studentClass === "12") {
    switch (stream) {
      case "pcm":
        mathTitle = "Mathematics Assessment";
        mathDescription =
          "Evaluate Class-level mathematics, quantitative thinking and problem-solving ability.";
        scienceTitle =
          "Physics & Chemistry Assessment";
        scienceDescription =
          "Evaluate core understanding across Physics and Chemistry.";
        reasoningTitle =
          "Scientific Reasoning Assessment";
        reasoningDescription =
          "Evaluate analytical thinking, scientific interpretation and problem solving.";
        break;

      case "pcb":
        mathTitle = "Biology Assessment";
        mathDescription =
          "Evaluate biological concepts, living systems and scientific understanding.";
        mathIcon = Dna;
        scienceTitle =
          "Physics, Chemistry & Biology Assessment";
        scienceDescription =
          "Evaluate integrated understanding across the core PCB subjects.";
        reasoningTitle =
          "Scientific Reasoning Assessment";
        reasoningDescription =
          "Evaluate evidence-based thinking, interpretation and scientific problem solving.";
        break;

      case "pcmb":
        mathTitle =
          "Mathematics & Biology Assessment";
        mathDescription =
          "Evaluate mathematical ability and biological understanding for the PCMB stream.";
        scienceTitle =
          "Physics, Chemistry & Core Science Assessment";
        scienceDescription =
          "Evaluate integrated scientific understanding for PCMB studies.";
        reasoningTitle =
          "Scientific Reasoning Assessment";
        reasoningDescription =
          "Evaluate analytical thinking, interpretation and scientific problem solving.";
        break;

      case "commerce":
        mathTitle =
          "Quantitative & Commerce Assessment";
        mathDescription =
          "Evaluate numerical ability, commercial calculations and quantitative problem solving.";
        scienceTitle =
          "Commerce Fundamentals Assessment";
        scienceDescription =
          "Evaluate business, economics and commerce-oriented understanding.";
        reasoningTitle =
          "Business Reasoning Assessment";
        reasoningDescription =
          "Evaluate analytical thinking, decision making and practical business reasoning.";
        break;

      case "humanities":
        mathTitle =
          "Social Analysis Assessment";
        mathDescription =
          "Evaluate interpretation, structured thinking and analytical understanding.";
        scienceTitle =
          "Humanities Knowledge Assessment";
        scienceDescription =
          "Evaluate social, cultural and humanities-oriented understanding.";
        reasoningTitle =
          "Critical Reasoning Assessment";
        reasoningDescription =
          "Evaluate critical thinking, interpretation and evidence-based reasoning.";
        break;

      default:
        break;
    }
  }

  return [
    {
      category: "aptitude",
      title: "Aptitude Assessment",
      description:
        "Evaluate numerical ability, problem solving and analytical thinking.",
      questions: questionBank.aptitude,
      icon: Brain,
    },
    {
      category: "math",
      title: mathTitle,
      description: mathDescription,
      questions: questionBank.math,
      icon: mathIcon,
    },
    {
      category: "science",
      title: scienceTitle,
      description: scienceDescription,
      questions: questionBank.science,
      icon: FlaskConical,
    },
    {
      category: "english",
      title: "English Assessment",
      description:
        "Evaluate grammar, vocabulary and verbal understanding.",
      questions: questionBank.english,
      icon: BookOpen,
    },
    {
      category: "reasoning",
      title: reasoningTitle,
      description: reasoningDescription,
      questions: questionBank.reasoning,
      icon: Puzzle,
    },
  ];
}

function Assessment() {
  const navigate = useNavigate();
  const { user } = useAuth();

  const [profile, setProfile] =
    useState<HighSchoolProfileData | null>(null);

  const [profileChecked, setProfileChecked] =
    useState(false);

  const [
    assessmentResults,
    setAssessmentResults,
  ] = useState<AssessmentResult[]>([]);

  const [
    selectedCategory,
    setSelectedCategory,
  ] = useState<AssessmentCategory | null>(null);

  const [
    currentQuestionIndex,
    setCurrentQuestionIndex,
  ] = useState(0);

  const [answers, setAnswers] =
    useState<number[]>([]);

  const [
    completedResult,
    setCompletedResult,
  ] = useState<AssessmentResult | null>(null);

  const [timeRemaining, setTimeRemaining] =
    useState(600);

  useEffect(() => {
    if (!user) {
      setProfileChecked(true);
      return;
    }

    const savedProfile =
      getHighSchoolProfile(user.id);

    const savedResults =
      getUserAssessmentResults(user.id);

    setProfile(savedProfile);
    setAssessmentResults(savedResults);
    setProfileChecked(true);
  }, [user]);

  const assessmentPurpose = profile
    ? getAssessmentPurpose(profile.studentClass)
    : null;

  const assessmentCards = useMemo(() => {
    if (!profile) {
      return [];
    }

    const questionBank =
      getAssessmentQuestionBank({
        studentClass: profile.studentClass,
        currentStream: profile.currentStream,
      });

    return createAssessmentCards(
      questionBank,
      profile.studentClass,
      profile.currentStream
    );
  }, [profile]);

  const selectedAssessment = useMemo(
    () =>
      assessmentCards.find(
        (assessment) =>
          assessment.category === selectedCategory
      ) ?? null,
    [assessmentCards, selectedCategory]
  );

  const questions =
    selectedAssessment?.questions ?? [];

  const currentQuestion =
    questions[currentQuestionIndex];

  const getLatestCategoryResult = (
    category: AssessmentCategory
  ) => {
    const categoryResults =
      assessmentResults.filter(
        (result) => result.category === category
      );

    if (categoryResults.length === 0) {
      return null;
    }

    return categoryResults.reduce(
      (latestResult, currentResult) =>
        new Date(
          currentResult.completedAt
        ).getTime() >
          new Date(
            latestResult.completedAt
          ).getTime()
          ? currentResult
          : latestResult
    );
  };

  const completedCategories =
    assessmentCards.filter(
      (assessment) =>
        getLatestCategoryResult(
          assessment.category
        ) !== null
    ).length;

  const overallProgress =
    assessmentCards.length === 0
      ? 0
      : Math.round(
        (completedCategories /
          assessmentCards.length) *
        100
      );

  const startAssessment = (
    category: AssessmentCategory
  ) => {
    const assessment =
      assessmentCards.find(
        (item) => item.category === category
      );

    if (!assessment) {
      return;
    }

    setSelectedCategory(category);
    setCurrentQuestionIndex(0);
    setAnswers(
      new Array(
        assessment.questions.length
      ).fill(-1)
    );
    setCompletedResult(null);
    setTimeRemaining(600);
  };

  const handleAnswer = (
    optionIndex: number
  ) => {
    setAnswers((previousAnswers) => {
      const updatedAnswers = [
        ...previousAnswers,
      ];

      updatedAnswers[currentQuestionIndex] =
        optionIndex;

      return updatedAnswers;
    });
  };

  const handlePrevious = () => {
    setCurrentQuestionIndex(
      (previousIndex) =>
        Math.max(previousIndex - 1, 0)
    );
  };

  const submitAssessment = () => {
    if (
      !user ||
      !selectedAssessment ||
      questions.length === 0
    ) {
      return;
    }

    const result = saveAssessmentResult({
      userId: user.id,
      category: selectedAssessment.category,
      questions,
      answers,
    });

    setAssessmentResults(
      getUserAssessmentResults(user.id)
    );

    setCompletedResult(result);
  };

  const handleNext = () => {
    if (
      currentQuestionIndex <
      questions.length - 1
    ) {
      setCurrentQuestionIndex(
        (previousIndex) =>
          previousIndex + 1
      );

      return;
    }

    submitAssessment();
  };

  useEffect(() => {
    if (
      !selectedAssessment ||
      completedResult
    ) {
      return;
    }

    if (timeRemaining <= 0) {
      submitAssessment();
      return;
    }

    const timer = window.setInterval(() => {
      setTimeRemaining(
        (previousTime) =>
          Math.max(previousTime - 1, 0)
      );
    }, 1000);

    return () => {
      window.clearInterval(timer);
    };
  }, [
    selectedAssessment,
    completedResult,
    timeRemaining,
  ]);

  const minutes = Math.floor(
    timeRemaining / 60
  );

  const seconds = timeRemaining % 60;

  const formattedTime = `${minutes}:${seconds
    .toString()
    .padStart(2, "0")}`;

  if (!profileChecked) {
    return (
      <div className="flex min-h-[60vh] items-center justify-center">
        <p className="text-slate-500">
          Loading assessment.
        </p>
      </div>
    );
  }

  if (!profile) {
    return (
      <div className="flex min-h-[70vh] items-center justify-center">
        <div className="w-full max-w-2xl rounded-3xl border border-amber-200 bg-white p-10 text-center shadow-lg">
          <div className="mx-auto flex h-20 w-20 items-center justify-center rounded-2xl bg-amber-100 text-amber-600">
            <Lock size={36} />
          </div>

          <h1 className="mt-7 text-3xl font-bold text-slate-900">
            Academic Profile Required
          </h1>

          <p className="mx-auto mt-4 max-w-lg leading-7 text-slate-600">
            Complete your academic profile before
            starting the guidance assessment. Your
            class and stream information determine
            the assessment question bank you receive.
          </p>

          <button
            type="button"
            onClick={() =>
              navigate(
                "/high-school-student/profile"
              )
            }
            className="mt-8 rounded-xl bg-cyan-600 px-7 py-3 font-semibold text-white transition hover:bg-cyan-700"
          >
            Complete Academic Profile
          </button>
        </div>
      </div>
    );
  }

  if (completedResult) {
    const performance =
      completedResult.percentage >= 85
        ? "Excellent"
        : completedResult.percentage >= 70
          ? "Good"
          : completedResult.percentage >= 50
            ? "Average"
            : "Needs Improvement";

    return (
      <div className="flex min-h-[60vh] items-center justify-center px-2 py-4 sm:px-4">
        <div className="w-full max-w-3xl rounded-[28px] border border-slate-200 bg-white p-5 text-center shadow-sm sm:p-7 lg:p-8">
          {/* Completion Icon */}

          <div className="mx-auto flex h-16 w-16 items-center justify-center rounded-2xl bg-emerald-50 text-3xl sm:h-18 sm:w-18">
            🎉
          </div>

          {/* Heading */}

          <h1 className="mt-5 text-2xl font-bold tracking-tight text-slate-900 sm:text-3xl">
            Assessment Part Completed
          </h1>

          <p className="mx-auto mt-2 max-w-lg text-sm leading-6 text-slate-500 sm:text-base">
            Your result has been saved to your
            assessment profile.
          </p>

          {/* Result Summary */}

          <div className="mt-6 grid grid-cols-1 gap-3 sm:grid-cols-3 sm:gap-4">
            <div className="rounded-2xl border border-cyan-100 bg-cyan-50/70 px-4 py-4">
              <p className="text-xs font-medium uppercase tracking-wide text-slate-500">
                Score
              </p>

              <p className="mt-2 text-2xl font-bold text-cyan-600 sm:text-3xl">
                {completedResult.score}/
                {completedResult.total}
              </p>
            </div>

            <div className="rounded-2xl border border-blue-100 bg-blue-50/70 px-4 py-4">
              <p className="text-xs font-medium uppercase tracking-wide text-slate-500">
                Percentage
              </p>

              <p className="mt-2 text-2xl font-bold text-blue-600 sm:text-3xl">
                {completedResult.percentage}%
              </p>
            </div>

            <div className="rounded-2xl border border-emerald-100 bg-emerald-50/70 px-4 py-4">
              <p className="text-xs font-medium uppercase tracking-wide text-slate-500">
                Performance
              </p>

              <p className="mt-2 flex min-h-9 items-center justify-center text-xl font-bold leading-tight text-emerald-600 sm:text-2xl">
                {performance}
              </p>
            </div>
          </div>

          {/* Actions */}

          <div className="mt-6 flex flex-col justify-center gap-3 sm:flex-row">
            <button
              type="button"
              onClick={() => {
                setSelectedCategory(null);
                setCompletedResult(null);
                setAnswers([]);
                setCurrentQuestionIndex(0);
                setTimeRemaining(600);
              }}
              className="w-full rounded-xl bg-cyan-600 px-5 py-2.5 text-sm font-semibold text-white transition hover:bg-cyan-700 sm:w-auto sm:min-w-56"
            >
              Continue Assessment Journey
            </button>

            <button
              type="button"
              onClick={() =>
                navigate(
                  "/high-school-student/assessment-reports"
                )
              }
              className="w-full rounded-xl border border-slate-300 bg-white px-5 py-2.5 text-sm font-semibold text-slate-700 transition hover:bg-slate-50 sm:w-auto"
            >
              View Reports
            </button>
          </div>
        </div>
      </div>
    );
  }

  if (
    selectedAssessment &&
    currentQuestion
  ) {
    const progress =
      ((currentQuestionIndex + 1) /
        questions.length) *
      100;

    const selectedAnswer =
      answers[currentQuestionIndex];

    return (
      <div className="mx-auto max-w-5xl">
        <div className="flex flex-wrap items-start justify-between gap-6">
          <div>
            <p className="text-sm font-semibold uppercase tracking-wide text-cyan-600">
              {assessmentPurpose?.title}
            </p>

            <h1 className="mt-2 text-3xl font-bold text-slate-900">
              {selectedAssessment.title}
            </h1>

            <p className="mt-2 text-slate-500">
              Class {profile.studentClass}
              {profile.currentStream
                ? ` • ${profile.currentStream}`
                : ""}
            </p>
          </div>

          <div className="rounded-2xl border border-slate-200 bg-white px-6 py-4 text-right shadow-sm">
            <p className="text-sm text-slate-500">
              Time Remaining
            </p>
            <p className="mt-1 text-2xl font-bold text-slate-900">
              {formattedTime}
            </p>
          </div>
        </div>

        <div className="mt-8">
          <div className="flex items-center justify-between text-sm font-medium text-slate-500">
            <span>
              Question {currentQuestionIndex + 1} of{" "}
              {questions.length}
            </span>
            <span>
              {Math.round(progress)}%
            </span>
          </div>

          <div className="mt-3 h-3 overflow-hidden rounded-full bg-slate-200">
            <div
              className="h-full rounded-full bg-cyan-600 transition-all"
              style={{
                width: `${progress}%`,
              }}
            />
          </div>
        </div>

        <div className="mt-8 rounded-3xl border border-slate-200 bg-white p-8 shadow-sm">
          <h2 className="text-xl font-bold text-slate-900">
            {currentQuestion.question}
          </h2>

          <div className="mt-8 space-y-4">
            {currentQuestion.options.map(
              (option, optionIndex) => {
                const isSelected =
                  selectedAnswer === optionIndex;

                return (
                  <button
                    key={`${currentQuestion.id}-${optionIndex}`}
                    type="button"
                    onClick={() =>
                      handleAnswer(optionIndex)
                    }
                    className={`w-full rounded-xl border p-5 text-left transition ${isSelected
                      ? "border-cyan-600 bg-cyan-50 text-cyan-700"
                      : "border-slate-200 bg-white text-slate-700 hover:border-cyan-300 hover:bg-slate-50"
                      }`}
                  >
                    {option}
                  </button>
                );
              }
            )}
          </div>
        </div>

        <div className="mt-8 flex items-center justify-between">
          <button
            type="button"
            onClick={handlePrevious}
            disabled={
              currentQuestionIndex === 0
            }
            className="rounded-xl border border-slate-300 bg-white px-6 py-3 font-semibold text-slate-700 transition hover:bg-slate-100 disabled:cursor-not-allowed disabled:opacity-40"
          >
            Previous
          </button>

          <button
            type="button"
            onClick={handleNext}
            disabled={selectedAnswer === -1}
            className="rounded-xl bg-cyan-600 px-7 py-3 font-semibold text-white transition hover:bg-cyan-700 disabled:cursor-not-allowed disabled:bg-slate-300"
          >
            {currentQuestionIndex ===
              questions.length - 1
              ? "Submit Assessment Part"
              : "Next"}
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="mx-auto max-w-6xl space-y-8">
      <div className="rounded-3xl bg-gradient-to-r from-cyan-600 to-blue-600 p-8 text-white shadow-lg">
        <div className="flex flex-col justify-between gap-8 lg:flex-row lg:items-center">
          <div className="max-w-3xl">
            <p className="text-sm font-semibold uppercase tracking-wide text-cyan-100">
              Class {profile.studentClass} Guidance
            </p>

            <h1 className="mt-3 text-3xl font-bold">
              {assessmentPurpose?.title}
            </h1>

            <p className="mt-3 leading-7 text-cyan-100">
              {assessmentPurpose?.description}
            </p>

            {profile.currentStream && (
              <p className="mt-4 inline-flex rounded-full bg-white/15 px-4 py-2 text-sm font-semibold text-white">
                Current Stream:{" "}
                {profile.currentStream}
              </p>
            )}
          </div>

          <div className="min-w-64 rounded-2xl bg-white/10 p-5">
            <div className="flex items-center justify-between">
              <p className="text-sm text-cyan-100">
                Overall Progress
              </p>
              <p className="font-bold">
                {overallProgress}%
              </p>
            </div>

            <div className="mt-3 h-3 overflow-hidden rounded-full bg-white/20">
              <div
                className="h-full rounded-full bg-white transition-all"
                style={{
                  width: `${overallProgress}%`,
                }}
              />
            </div>

            <p className="mt-3 text-sm font-medium text-cyan-100">
              {completedCategories} of{" "}
              {assessmentCards.length} sections
              completed
            </p>
          </div>
        </div>
      </div>

      <div className="rounded-2xl border border-cyan-200 bg-cyan-50 p-6">
        <div className="flex items-start gap-4">
          <div className="flex h-12 w-12 shrink-0 items-center justify-center rounded-xl bg-cyan-600 text-white">
            <GraduationCap size={24} />
          </div>

          <div>
            <h2 className="text-lg font-bold text-slate-900">
              Complete all five assessment parts
            </h2>

            <p className="mt-2 leading-7 text-slate-600">
              These assessment sections are selected
              using your Class {profile.studentClass}
              {profile.currentStream
                ? ` and ${profile.currentStream} stream`
                : ""}. Your latest results will be
              combined to generate your{" "}
              <span className="font-semibold text-cyan-700">
                {assessmentPurpose?.reportTitle}
              </span>
              .
            </p>
          </div>
        </div>
      </div>

      <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-3">
        {assessmentCards.map(
          (assessment, index) => {
            const Icon = assessment.icon;

            const latestResult =
              getLatestCategoryResult(
                assessment.category
              );

            return (
              <div
                key={assessment.category}
                className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm transition hover:-translate-y-1 hover:shadow-lg"
              >
                <div className="flex items-start justify-between gap-4">
                  <div className="flex h-14 w-14 items-center justify-center rounded-2xl bg-cyan-100 text-cyan-700">
                    <Icon size={28} />
                  </div>

                  {latestResult ? (
                    <CheckCircle2
                      size={24}
                      className="text-green-600"
                    />
                  ) : (
                    <span className="rounded-full bg-slate-100 px-3 py-1 text-xs font-bold text-slate-500">
                      Part {index + 1}
                    </span>
                  )}
                </div>

                <h2 className="mt-6 text-xl font-bold text-slate-900">
                  {assessment.title}
                </h2>

                <p className="mt-3 min-h-14 leading-7 text-slate-600">
                  {assessment.description}
                </p>

                <p className="mt-4 text-sm font-medium text-slate-500">
                  {assessment.questions.length} questions
                </p>

                {latestResult && (
                  <div className="mt-4 rounded-xl bg-green-50 p-4">
                    <p className="text-sm font-semibold text-green-700">
                      Latest Score:{" "}
                      {latestResult.score}/
                      {latestResult.total} —{" "}
                      {latestResult.percentage}%
                    </p>
                  </div>
                )}

                <button
                  type="button"
                  onClick={() =>
                    startAssessment(
                      assessment.category
                    )
                  }
                  className="mt-6 w-full rounded-xl bg-cyan-600 px-5 py-3 font-semibold text-white transition hover:bg-cyan-700"
                >
                  {latestResult
                    ? "Retake Assessment"
                    : "Start Assessment"}
                </button>
              </div>
            );
          }
        )}
      </div>

      <div className="rounded-3xl border border-slate-200 bg-white p-8 shadow-sm">
        <div className="flex flex-col justify-between gap-6 lg:flex-row lg:items-center">
          <div>
            <p className="text-sm font-semibold uppercase tracking-wide text-cyan-600">
              Final Guidance
            </p>

            <h2 className="mt-2 text-2xl font-bold text-slate-900">
              {assessmentPurpose?.reportTitle}
            </h2>

            <p className="mt-3 max-w-2xl leading-7 text-slate-600">
              {completedCategories ===
                assessmentCards.length
                ? "All assessment sections are complete. Your combined guidance report is ready for analysis."
                : `Complete all five assessment sections to unlock your final guidance report. ${completedCategories} of ${assessmentCards.length} sections are currently complete.`}
            </p>
          </div>

          <button
            type="button"
            disabled={
              completedCategories !==
              assessmentCards.length
            }
            onClick={() =>
              navigate(
                "/high-school-student/assessment-reports"
              )
            }
            className="rounded-xl bg-cyan-600 px-6 py-3 font-semibold text-white transition hover:bg-cyan-700 disabled:cursor-not-allowed disabled:bg-slate-300"
          >
            {completedCategories ===
              assessmentCards.length
              ? "View Final Guidance Report"
              : "Final Report Locked"}
          </button>
        </div>
      </div>
    </div>
  );
}

export default Assessment;
