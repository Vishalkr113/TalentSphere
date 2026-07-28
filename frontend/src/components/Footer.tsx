import {
    Mail,
    Phone,
    MapPin,
} from "lucide-react";

import {
    FaGithub,
    FaLinkedin,
} from "react-icons/fa";

import Logo from "./ui/Logo";

function Footer() {
    return (
        <footer
            id="contact"
            className="bg-slate-950 text-white"
        >
            <div className="mx-auto max-w-7xl px-6 py-16">

                <div className="grid gap-12 md:grid-cols-2 lg:grid-cols-4">

                    {/* ================= Brand ================= */}

                    <div>

                        <Logo size="sm" />

                        <p className="mt-6 leading-7 text-slate-400">

                            TalentSphere is an AI-powered Career
                            Development Platform that helps
                            Students, Institutes and Professionals
                            build skills, prepare for placements
                            and achieve career success.

                        </p>

                    </div>

                    {/* ================= Quick Links ================= */}

                    <div>

                        <h3 className="text-lg font-semibold">
                            Quick Links
                        </h3>

                        <div className="mt-6 flex flex-col gap-3">

                            <a
                                href="#home"
                                className="text-slate-400 transition hover:text-cyan-400"
                            >
                                Home
                            </a>

                            <a
                                href="#about"
                                className="text-sm text-slate-400 transition hover:text-cyan-400"
                            >
                                About Us
                            </a>

                            <a
                                href="#features"
                                className="text-slate-400 transition hover:text-cyan-400"
                            >
                                Features
                            </a>

                            <a
                                href="#contact"
                                className="text-slate-400 transition hover:text-cyan-400"
                            >
                                Contact
                            </a>

                        </div>

                    </div>

                    {/* ================= Resources ================= */}

                    <div>

                        <h3 className="text-lg font-semibold">
                            Resources
                        </h3>

                        <div className="mt-6 flex flex-col gap-3">

                            <a
                                href="#faq"
                                className="text-slate-400 transition hover:text-cyan-400"
                            >
                                FAQ
                            </a>

                            <a
                                href="#"
                                className="text-slate-400 transition hover:text-cyan-400"
                            >
                                Privacy Policy
                            </a>

                            <a
                                href="#"
                                className="text-slate-400 transition hover:text-cyan-400"
                            >
                                Terms & Conditions
                            </a>

                        </div>

                    </div>

                    {/* ================= Contact ================= */}

                    <div>

                        <h3 className="text-lg font-semibold">
                            Contact
                        </h3>

                        <div className="mt-6 space-y-5">

                            <div className="flex items-center gap-3 text-slate-400">

                                <Mail size={18} />

                                <span>
                                    support@talentsphere.com
                                </span>

                            </div>

                            <div className="flex items-center gap-3 text-slate-400">

                                <Phone size={18} />

                                <span>
                                    +91 98765 43210
                                </span>

                            </div>

                            <div className="flex items-center gap-3 text-slate-400">

                                <MapPin size={18} />

                                <span>
                                    Bhopal, Madhya Pradesh
                                </span>

                            </div>

                            <div className="flex gap-4 pt-3">

                                <a
                                    href="https://github.com"
                                    target="_blank"
                                    rel="noopener noreferrer"
                                    aria-label="GitHub"
                                    title="GitHub"
                                    className="rounded-xl bg-slate-800 p-3 transition hover:bg-cyan-600"
                                >
                                    <FaGithub size={20} />
                                </a>

                                <a
                                    href="https://www.linkedin.com/"
                                    target="_blank"
                                    rel="noopener noreferrer"
                                    aria-label="LinkedIn"
                                    title="LinkedIn"
                                    className="rounded-xl bg-slate-800 p-3 transition hover:bg-cyan-600"
                                >
                                    <FaLinkedin size={20} />
                                </a>

                            </div>

                        </div>

                    </div>

                </div>

                {/* ================= Bottom ================= */}

                <div className="mt-14 border-t border-slate-800 pt-8 text-center text-sm text-slate-500">

                    © {new Date().getFullYear()} TalentSphere.
                    All Rights Reserved.

                </div>

            </div >

        </footer >
    );
}

export default Footer;