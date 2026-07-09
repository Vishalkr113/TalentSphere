import { useEffect, useState } from "react";

import DashboardLayout from "./DashboardLayout";
import Card from "./ui/Card";
import Button from "./ui/Button";
import { skillQuestions } from "../data/skillQuestions";

function SkillAssessment() {

  const categories = [
  {
    id: "logical",
    title: "Logical Reasoning",
  },
  {
    id: "aptitude",
    title: "Quantitative Aptitude",
  },
  {
    id: "verbal",
    title: "Verbal Ability",
  },
  {
    id: "programming",
    title: "Programming Basics",
  },
] as const;

  const [selected, setSelected] = useState<
  "logical" | "aptitude" | "verbal" | "programming" | ""
>("");

  const [currentQuestion, setCurrentQuestion] = useState(0);

  const [selectedAnswer, setSelectedAnswer] = useState("");
  
  const questions =
  selected ? skillQuestions[selected] : [];
  
  const [score, setScore] = useState(0);

  const [isFinished, setIsFinished] = useState(false);

  const [timeLeft, setTimeLeft] = useState(60);

    useEffect(() => {

  if (!selected || isFinished) return;

  if (timeLeft === 0) {

    if (currentQuestion < questions.length - 1) {

      setCurrentQuestion((prev) => prev + 1);

      setSelectedAnswer("");

      setTimeLeft(60);

    } else {

      setIsFinished(true);

    }

    return;

  }

  const timer = setTimeout(() => {

    setTimeLeft((prev) => prev - 1);

  }, 1000);

  return () => clearTimeout(timer);

}, [
  timeLeft,
  currentQuestion,
  selected,
  isFinished,
  questions.length,
]);

  return (

    <DashboardLayout>

      <div className="mb-8">

        <h2 className="text-3xl font-bold text-slate-900">

          Skill Assessment

        </h2>

        <p className="mt-2 text-slate-600">

          Choose a category to start your assessment.

        </p>

      </div>

      <div className="grid gap-6 md:grid-cols-2">

       {categories.map((item) => (

  <Card
    key={item.id}
    className={`p-6 transition ${
      selected === item.id
        ? "border-2 border-cyan-600"
        : ""
    }`}
   onClick={() => {
  setSelected(item.id);
  setCurrentQuestion(0);
  setSelectedAnswer("");
  setScore(0);
  setIsFinished(false);
  setTimeLeft(60); 
}}
  >

    <h3 className="text-xl font-semibold">
      {item.title}
    </h3>

  </Card>

))}

      </div>

       
    {selected && !isFinished && (

     <Card className="mt-8 p-8">

    <div className="mb-6">

  <div className="flex items-center justify-between">

    <p className="text-sm font-medium text-slate-600">

      Question {currentQuestion + 1} of {questions.length}

    </p>

    <p className="text-sm font-medium text-cyan-600">

      {Math.round(
        ((currentQuestion + 1) / questions.length) * 100
      )}%

    </p>

  </div>

  <div className="mt-2 h-2 w-full rounded-full bg-slate-200">

    <div
      className="h-2 rounded-full bg-cyan-600 transition-all duration-500"
      style={{
        width: `${((currentQuestion + 1) / questions.length) * 100}%`,
      }}
    />

  </div>

</div>
     <p className="mt-4 text-center text-lg font-semibold text-red-500">
  ⏱ Time Left : {timeLeft}s
    </p>

    <h3 className="text-2xl font-semibold mb-6">
      {questions[currentQuestion].question}
    </h3>

    <div className="space-y-4">

      {questions[currentQuestion].options.map((option) => (

        <button
          key={option}
          onClick={() => setSelectedAnswer(option)}
          className={`w-full rounded-lg border p-4 text-left transition ${
            selectedAnswer === option
              ? "border-cyan-600 bg-cyan-50"
              : "border-slate-200"
          }`}
        >
          {option}
        </button>

      ))}

    </div>
     
     <Button
       className="mt-6"
       disabled={!selectedAnswer}
       onClick={() => {
    if (
      selectedAnswer ===
      questions[currentQuestion].answer
    ) {
      setScore(score + 1);
    }

    if (
      currentQuestion <
      questions.length - 1
    ) {

      setCurrentQuestion(
        currentQuestion + 1
      );

      setSelectedAnswer("");

      setTimeLeft(60);

    } else {

      setIsFinished(true);

    }

  }}
>
  {currentQuestion === questions.length - 1
    ? "Finish"
    : "Next"}
</Button>

  </Card>
)}
   
   {/*  Results */}

 {isFinished && (

  <Card className="mt-8 p-8">

    <h2 className="text-3xl font-bold text-slate-900">

      Assessment Completed 🎉

    </h2>

    <p className="mt-4 text-xl">

      Your Score

    </p>

    <h1 className="mt-2 text-5xl font-bold text-cyan-600">

      {score} / {questions.length}

    </h1>

       {/* Percentage */}

    <p className="mt-4 text-lg text-slate-700">
      Percentage:{" "}
       {Math.round((score / questions.length) * 100)}%
    </p>

    <p className="mt-4 text-xl font-semibold">

       {score === questions.length
         ? "🏆 Excellent"

         : score >= questions.length / 2

         ? "👍 Good"

         : "📚 Needs Improvement"}

    </p>

    <p className="mt-6 text-lg">

        Category :

    <strong>

    {" "}
    {selected.toUpperCase()}

    </strong>

    </p>

    <p className="mt-6 text-slate-600">

      Keep practicing to improve your skills.

    </p>

      {/*  Retake Button */}

    <Button
      className="mt-6"
        onClick={() => {
          setSelected("");
          setCurrentQuestion(0);
          setSelectedAnswer("");
          setScore(0);
          setIsFinished(false);
          setTimeLeft(60);
   }}
    >
        Retake Test
    </Button>

  </Card>

)}

    </DashboardLayout>

  );
}

export default SkillAssessment;