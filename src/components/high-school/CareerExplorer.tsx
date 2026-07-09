import {
  Laptop,
  Stethoscope,
  Scale,
  Calculator,
  Palette,
  Cpu,
  ChevronRight,
} from "lucide-react";

const careers = [
  {
    title: "Engineering",
    description: "Software, AI, Civil, Mechanical, Electrical and more.",
    icon: Cpu,
  },
  {
    title: "Medical",
    description: "Doctor, Dentist, Nursing, Pharmacy, MBBS and more.",
    icon: Stethoscope,
  },
  {
    title: "Commerce",
    description: "CA, CS, Banking, Finance, Business and Management.",
    icon: Calculator,
  },
  {
    title: "Law",
    description: "Judiciary, Advocate, Legal Advisor and Corporate Law.",
    icon: Scale,
  },
  {
    title: "Arts & Design",
    description: "Animation, Fashion, Graphic Design, Fine Arts.",
    icon: Palette,
  },
  {
    title: "Computer Science",
    description: "Software Engineer, AI Engineer, Data Scientist.",
    icon: Laptop,
  },
];

function CareerExplorer() {
  return (
    <div className="space-y-10">

      {/* Heading */}

      <div>

        <h1 className="text-4xl font-bold text-slate-900">
          Career Explorer
        </h1>

        <p className="mt-3 text-slate-600 text-lg">
          Discover career opportunities based on your interests,
          strengths and future goals.
        </p>

      </div>

      {/* Cards */}

      <div className="grid gap-8 md:grid-cols-2 xl:grid-cols-3">

        {careers.map((career) => {

          const Icon = career.icon;

          return (

            <div
              key={career.title}
              className="rounded-3xl border border-slate-200 bg-white p-7 shadow-sm transition hover:-translate-y-2 hover:shadow-xl"
            >

              <div className="flex h-16 w-16 items-center justify-center rounded-2xl bg-cyan-100 text-cyan-600">

                <Icon size={32} />

              </div>

              <h2 className="mt-6 text-2xl font-bold text-slate-900">
                {career.title}
              </h2>

              <p className="mt-4 leading-7 text-slate-600">
                {career.description}
              </p>

              <button className="mt-8 flex items-center gap-2 rounded-xl bg-cyan-600 px-5 py-3 font-medium text-white transition hover:bg-cyan-700">

                Explore Career

                <ChevronRight size={18} />

              </button>

            </div>

          );

        })}

      </div>

    </div>
  );
}

export default CareerExplorer;