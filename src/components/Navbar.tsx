import { useState } from "react";
import { Link } from "react-router-dom";
import { Menu, X } from "lucide-react";

import Logo from "./ui/Logo";
import Button from "./ui/Button";

function Navbar() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <header className="sticky top-0 z-50 border-b border-slate-200 bg-white/90 backdrop-blur">

      <div className="mx-auto flex h-20 max-w-7xl items-center justify-between px-6">

        {/* Logo */}

        <Logo size="sm" />

        {/* Desktop Menu */}

        <nav className="hidden items-center gap-8 lg:flex">

          <a
            href="#home"
            className="font-medium text-slate-600 transition hover:text-cyan-600"
          >
            Home
          </a>

          <a
            href="#about"
            className="font-medium text-slate-600 transition hover:text-cyan-600"
          >
            About
          </a>

          <a
            href="#features"
            className="font-medium text-slate-600 transition hover:text-cyan-600"
          >
            Features
          </a>

          <a
            href="#contact"
            className="font-medium text-slate-600 transition hover:text-cyan-600"
          >
            Contact
          </a>

        </nav>

        {/* Desktop Right */}

        <div className="hidden items-center gap-4 lg:flex">

  <Link
    to="/portal?mode=login"
    className="font-semibold text-slate-700 transition hover:text-cyan-600"
  >
    Login
  </Link>

  <Link to="/portal?mode=register">

    <Button>
      Register
    </Button>

  </Link>

</div>

        {/* Mobile Menu Button */}

        <button
          onClick={() =>
            setIsOpen(!isOpen)
          }
          className="lg:hidden"
        >
          {isOpen ? (
            <X size={28} />
          ) : (
            <Menu size={28} />
          )}
        </button>

      </div>

      {/* Mobile Menu */}

      {isOpen && (

        <div className="border-t bg-white lg:hidden">

          <nav className="flex flex-col gap-5 p-6">

            <a
              href="#home"
              onClick={() =>
                setIsOpen(false)
              }
            >
              Home
            </a>

            <a
              href="#about"
              onClick={() =>
                setIsOpen(false)
              }
            >
              About
            </a>

            <a
              href="#features"
              onClick={() =>
                setIsOpen(false)
              }
            >
              Features
            </a>

            <a
              href="#contact"
              onClick={() =>
                setIsOpen(false)
              }
            >
              Contact
        </a>
              
            <Link
                to="/portal?mode=login"
                onClick={() =>
                    setIsOpen(false)
             }
             >
                Login
                </Link>

            <Link
                to="/portal?mode=register"
                onClick={() =>
                    setIsOpen(false)
            }
            >

            <Button>
                Register
            </Button>

        </Link>
            

          </nav>

        </div>

      )}

    </header>
  );
}

export default Navbar;