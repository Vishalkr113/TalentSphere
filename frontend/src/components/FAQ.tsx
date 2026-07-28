import { ChevronDown } from "lucide-react";

import Card from "./ui/Card";
import { faqs } from "../data/home/faq";

function FAQ() {
  return (
    <section className="bg-slate-100 py-24">

      <div className="mx-auto max-w-5xl px-6">

        <div className="text-center">

          <span className="rounded-full bg-cyan-100 px-4 py-2 text-sm font-semibold text-cyan-700">
            FAQ
          </span>

          <h2 className="mt-6 text-4xl font-bold text-slate-900">
            Frequently Asked Questions
          </h2>

          <p className="mt-5 text-lg text-slate-600">
            Find answers to the most common questions
            about TalentSphere.
          </p>

        </div>

        <div className="mt-16 space-y-6">

          {faqs.map((faq) => (

            <Card key={faq.id}>

              <div className="flex items-start justify-between gap-6">

                <div>

                  <h3 className="text-xl font-semibold text-slate-900">
                    {faq.question}
                  </h3>

                  <p className="mt-3 leading-7 text-slate-600">
                    {faq.answer}
                  </p>

                </div>

                <ChevronDown
                  size={22}
                  className="text-cyan-600"
                />

              </div>

            </Card>

          ))}

        </div>

      </div>

    </section>
  );
}

export default FAQ;