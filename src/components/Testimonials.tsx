import { testimonials } from "../data/home/testimonials";
import {
  Star,
  Quote,
} from "lucide-react";

import Card from "./ui/Card";

function Testimonials() {
  return (
    <section className="bg-white py-24">

      <div className="mx-auto max-w-7xl px-6">

        <div className="text-center">

          <span className="rounded-full bg-cyan-100 px-4 py-2 text-sm font-semibold text-cyan-700">
            Testimonials
          </span>

          <h2 className="mt-6 text-4xl font-bold text-slate-900">
            What Our Users Say
          </h2>

          <p className="mx-auto mt-5 max-w-3xl text-lg text-slate-600">
            Students, professionals and institutes
            trust TalentSphere to support their career
            development journey.
          </p>

        </div>

        <div className="mt-16 grid gap-8 lg:grid-cols-3">

          {testimonials.map((item) => (

            <Card key={item.name}>

              <Quote
                className="text-cyan-600"
                size={34}
              />

              <p className="mt-6 leading-8 text-slate-600">
                "{item.message}"
              </p>

              <div className="mt-8 flex">

                {[1, 2, 3, 4, 5].map((star) => (

                  <Star
                    key={star}
                    size={18}
                    className="fill-yellow-400 text-yellow-400"
                  />

                ))}

              </div>

              <div className="mt-8">

                <h3 className="text-lg font-bold text-slate-900">
                  {item.name}
                </h3>

                <p className="text-sm text-slate-500">
                  {item.role}
                </p>

              </div>

            </Card>

          ))}

        </div>

      </div>

    </section>
  );
}

export default Testimonials;