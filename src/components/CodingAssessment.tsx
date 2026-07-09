import { useState } from "react";

import DashboardLayout from "./DashboardLayout";
import Card from "./ui/Card";
import Button from "./ui/Button";

function CodingAssessment() {

  const languages = [
    "C",
    "C++",
    "Java",
    "Python",
    "JavaScript",
  ];

  const [selectedLanguage, setSelectedLanguage] =
    useState("");

  return (

    <DashboardLayout>

      <div className="mb-8">

        <h2 className="text-3xl font-bold text-slate-900">
          Coding Assessment
        </h2>

        <p className="mt-2 text-slate-600">
          Select your preferred programming language.
        </p>

      </div>

      <div className="grid gap-6 md:grid-cols-3">

        {languages.map((language) => (

          <Card
            key={language}
            onClick={() =>
              setSelectedLanguage(language)
            }
            className={`p-6 text-center transition ${
              selectedLanguage === language
                ? "border-2 border-cyan-600"
                : ""
            }`}
          >

            <h3 className="text-xl font-semibold">
              {language}
            </h3>

          </Card>

        ))}

      </div>

      {selectedLanguage && (

        <Card className="mt-8 p-8">

          <h3 className="text-2xl font-bold">
            Selected Language
          </h3>

          <p className="mt-3 text-lg text-cyan-600">
            {selectedLanguage}
          </p>

          <Button className="mt-6">
            Start Coding Test
          </Button>

        </Card>

      )}

    </DashboardLayout>

  );

}

export default CodingAssessment;