import { useState } from "react";
import { Menu, X } from "lucide-react";

import Logo from "./ui/Logo";
import Button from "./ui/Button";
import AuthRoleModal from "./AuthRoleModal";

function Navbar() {
  const [authMode, setAuthMode] = useState<
    "login" | "signup" | null
  >(null);

  const [isOpen, setIsOpen] = useState(false);

  const openAuthModal = (
    mode: "login" | "signup"
  ) => {
    setIsOpen(false);
    setAuthMode(mode);
  };

  return (
    <>
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
            <button
              type="button"
              onClick={() => openAuthModal("login")}
              className="font-semibold text-slate-700 transition hover:text-cyan-600"
            >
              Login
            </button>

            <Button
              type="button"
              onClick={() => openAuthModal("signup")}
            >
              signup
            </Button>
          </div>

          {/* Mobile Menu Button */}

          <button
            type="button"
            onClick={() => setIsOpen(!isOpen)}
            className="lg:hidden"
            aria-label="Toggle menu"
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
                onClick={() => setIsOpen(false)}
              >
                Home
              </a>

              <a
                href="#about"
                onClick={() => setIsOpen(false)}
              >
                About
              </a>

              <a
                href="#features"
                onClick={() => setIsOpen(false)}
              >
                Features
              </a>

              <a
                href="#contact"
                onClick={() => setIsOpen(false)}
              >
                Contact
              </a>

              <button
                type="button"
                onClick={() => openAuthModal("login")}
                className="text-left font-semibold text-slate-700 transition hover:text-cyan-600"
              >
                Login
              </button>

              <button
                type="button"
                onClick={() => openAuthModal("signup")}
                className="rounded-xl bg-cyan-600 px-6 py-3 font-semibold text-white transition hover:bg-cyan-700"
              >
                signup
              </button>
            </nav>
          </div>
        )}
      </header>

      {/* Authentication Role Modal */}

      {authMode && (
        <AuthRoleModal
          mode={authMode}
          onClose={() => setAuthMode(null)}
        />
      )}
    </>
  );
}

export default Navbar;