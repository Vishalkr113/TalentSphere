import { Link } from "react-router-dom";

import Logo from "./ui/Logo";
import Button from "./ui/Button";

function Navbar() {
  return (
    <header className="sticky top-0 z-50 border-b border-slate-200 bg-white/90 backdrop-blur">
      <div className="mx-auto flex h-20 max-w-7xl items-center justify-between px-6">

        {/* Logo */}
        <Logo size="sm" />

        {/* Navigation */}

        <nav className="hidden items-center gap-8 md:flex">

          <Link
            to="/"
            className="font-medium text-slate-600 transition hover:text-cyan-600"
          >
            Home
          </Link>

          <a
            href="#features"
            className="font-medium text-slate-600 transition hover:text-cyan-600"
          >
            Features
          </a>

          <a
            href="#about"
            className="font-medium text-slate-600 transition hover:text-cyan-600"
          >
            About
          </a>

          <a
            href="#contact"
            className="font-medium text-slate-600 transition hover:text-cyan-600"
          >
            Contact
          </a>

        </nav>

        {/* Right */}

        <div className="flex items-center gap-3">

          <Link
            to="/student/login"
            className="font-semibold text-slate-700 hover:text-cyan-600"
          >
            Login
          </Link>

          <div className="w-32">
            <Button>
              Get Started
            </Button>
          </div>

        </div>

      </div>
    </header>
  );
}

export default Navbar;