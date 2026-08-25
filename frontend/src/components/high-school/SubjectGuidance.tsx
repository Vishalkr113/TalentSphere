import {
    Atom,
    BookOpen,
    Calculator,
    ChevronRight,
    X,
} from "lucide-react";

import { useState } from "react";

import { useAuth } from "../../contexts/AuthContext";

const streams = [
    {
        title: "Science - PCM",
        key: "PCM",
        icon: Atom,
        subjects: [
            "Physics",
            "Chemistry",
            "Mathematics",
        ],
        careers:
            "Engineering, computing, architecture, physical sciences",
    },

    {
        title: "Science - PCB",
        key: "PCB",
        icon: Atom,
        subjects: [
            "Physics",
            "Chemistry",
            "Biology",
        ],
        careers:
            "Medicine, health sciences, pharmacy, life sciences",
    },

    {
        title: "Commerce",
        key: "Commerce",
        icon: Calculator,
        subjects: [
            "Accountancy",
            "Economics",
            "Business Studies",
            "Mathematics / Informatics",
        ],
        careers:
            "Finance, CA, CS, banking, business and management",
    },

    {
        title: "Humanities",
        key: "Humanities",
        icon: BookOpen,
        subjects: [
            "History",
            "Political Science",
            "Geography",
            "Psychology / Sociology",
        ],
        careers:
            "Law, civil services, media, social sciences",
    },

] as const;

const guidance = {
    ready: false,
    recommendedStream: "",
    recommendationScore: 0,
    recommendationReason: "",
};



function SubjectGuidance() {

    const { user } = useAuth();


    const [selected, setSelected] =
        useState<
            typeof streams[number] | null
        >(null);



    if (!user) {
        return null;
    }



    return (

        <div className="space-y-6">


            <section className="rounded-2xl border bg-white p-6">

                <h1 className="text-3xl font-bold">
                    Subject Guidance
                </h1>


                <p className="mt-2 text-slate-600">

                    {
                        guidance.ready

                        ?

                        `Assessment evidence currently shows strongest alignment with ${guidance.recommendedStream} (${guidance.recommendationScore}%).`

                        :

                        "Complete an assessment to connect this page with your saved assessment evidence."
                    }

                </p>


            </section>





            <div className="grid gap-5 md:grid-cols-2">


                {
                    streams.map((stream)=>{


                        const Icon =
                            stream.icon;



                        const isMatch =
                            guidance.ready &&
                            guidance.recommendedStream === stream.key;



                        return (

                            <div

                                key={stream.key}

                                className={`
                                    rounded-2xl
                                    border
                                    bg-white
                                    p-5
                                    ${
                                        isMatch
                                        ?
                                        "border-cyan-500 ring-2 ring-cyan-100"
                                        :
                                        ""
                                    }
                                `}

                            >


                                <div className="flex items-center gap-3">


                                    <Icon size={24}/>


                                    <h2 className="text-xl font-bold">
                                        {stream.title}
                                    </h2>


                                </div>




                                {
                                    isMatch && (

                                        <p className="mt-3 text-sm font-semibold text-cyan-700">
                                            CURRENT TOP MATCH
                                        </p>

                                    )
                                }





                                <p className="mt-3 text-slate-600">

                                    {stream.careers}

                                </p>




                                <ul className="mt-4 space-y-2">

                                    {
                                        stream.subjects.map(
                                            (subject)=>(
                                                <li
                                                    key={subject}
                                                    className="text-sm"
                                                >
                                                    • {subject}
                                                </li>
                                            )
                                        )
                                    }

                                </ul>




                                <button

                                    className="mt-5 flex items-center gap-2 font-semibold text-cyan-700"

                                    onClick={()=>
                                        setSelected(stream)
                                    }

                                >

                                    View Guidance

                                    <ChevronRight size={18}/>

                                </button>



                            </div>

                        );

                    })
                }


            </div>







            {
                selected && (

                    <div

                        className="fixed inset-0 z-[80] flex items-center justify-center bg-slate-950/50 p-4"

                        onClick={()=>
                            setSelected(null)
                        }

                    >


                        <div

                            className="w-full max-w-xl rounded-2xl bg-white p-6"

                            onClick={(e)=>
                                e.stopPropagation()
                            }

                        >


                            <div className="flex justify-between">

                                <h2 className="text-2xl font-bold">

                                    {selected.title}

                                </h2>


                                <button

                                    onClick={()=>
                                        setSelected(null)
                                    }

                                >

                                    <X/>

                                </button>


                            </div>





                            <p className="mt-4">

                                Core subject direction:

                                {" "}

                                {selected.subjects.join(", ")}

                            </p>




                            <p className="mt-3">

                                Common pathway examples:

                                {" "}

                                {selected.careers}

                            </p>





                            {
                                guidance.ready && (

                                    <p className="mt-4 rounded-xl bg-cyan-50 p-4">

                                        {
                                            selected.key ===
                                            guidance.recommendedStream

                                            ?

                                            guidance.recommendationReason

                                            :

                                            `Your current top assessment match is ${guidance.recommendedStream}. Compare the evidence in Final Guidance before choosing.`
                                        }

                                    </p>

                                )
                            }



                        </div>


                    </div>

                )
            }



        </div>

    );
}



export default SubjectGuidance;