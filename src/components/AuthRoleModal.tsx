import { useState } from "react";
import { useNavigate } from "react-router-dom";
import {
  ArrowLeft,
  Briefcase,
  GraduationCap,
  School,
  X,
} from "lucide-react";

import Input from "./ui/Input";
import PasswordInput from "./ui/PasswordInput";
import Button from "./ui/Button";

import {
  isValidEmail,
  isValidPassword,
  loginUser,
  registerUser,
  type UserRole,
} from "../services/authService";

import { useAuth } from "../contexts/AuthContext";

type AuthMode = "login" | "signup";

interface AuthRoleModalProps {
  mode: AuthMode;
  onClose: () => void;
}

const roles = [
  {
    title: "High School Student",
    role: "high-school-student" as UserRole,
    icon: School,
  },
  {
    title: "College Student",
    role: "college-student" as UserRole,
    icon: GraduationCap,
  },
  {
    title: "Working Professional",
    role: "working-professional" as UserRole,
    icon: Briefcase,
  },
];

function AuthRoleModal({
  mode,
  onClose,
}: AuthRoleModalProps) {
  const navigate = useNavigate();
  const { login } = useAuth();

  const [selectedRole, setSelectedRole] =
    useState<UserRole | null>(null);

  const [currentMode, setCurrentMode] =
    useState<AuthMode>(mode);

  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] =
    useState("");
  const [confirmPassword, setConfirmPassword] =
    useState("");

  const [loading, setLoading] =
    useState(false);

  const [error, setError] = useState("");
  const [success, setSuccess] =
    useState("");

  const selectedRoleTitle = roles.find(
    (item) => item.role === selectedRole
  )?.title;

  const resetMessages = () => {
    setError("");
    setSuccess("");
  };

  const switchMode = (newMode: AuthMode) => {
    resetMessages();

    setCurrentMode(newMode);
    setPassword("");
    setConfirmPassword("");
  };

  const handleLogin = (
    e: React.FormEvent
  ) => {
    e.preventDefault();

    resetMessages();

    if (!selectedRole) {
      setError("Please select your career stage.");
      return;
    }

    if (!email.trim() || !password.trim()) {
      setError(
        "Please fill in all required fields."
      );
      return;
    }

    if (!isValidEmail(email)) {
      setError(
        "Please enter a valid email address."
      );
      return;
    }

    setLoading(true);

    const result = loginUser(
      email.trim().toLowerCase(),
      password,
      selectedRole
    );

    if (!result.success || !result.user) {
      setLoading(false);

      setError(
        result.message ?? "Login failed."
      );

      return;
    }

    login(result.user);

    setLoading(false);

    onClose();

    navigate(
      `/${selectedRole}/dashboard`,
      {
        replace: true,
      }
    );
  };

  const handleSignUp = (
    e: React.FormEvent
  ) => {
    e.preventDefault();

    resetMessages();

    if (!selectedRole) {
      setError("Please select your career stage.");
      return;
    }

    if (
      !name.trim() ||
      !email.trim() ||
      !password.trim() ||
      !confirmPassword.trim()
    ) {
      setError(
        "Please fill in all required fields."
      );
      return;
    }

    if (!isValidEmail(email)) {
      setError(
        "Please enter a valid email address."
      );
      return;
    }

    if (!isValidPassword(password)) {
      setError(
        "Password must contain at least 8 characters, one uppercase letter and one number."
      );
      return;
    }

    if (password !== confirmPassword) {
      setError("Passwords do not match.");
      return;
    }

    setLoading(true);

    const result = registerUser({
      name: name.trim(),
      email: email.trim().toLowerCase(),
      password,
      role: selectedRole,
    });

    if (!result.success) {
      setLoading(false);

      setError(
        result.message ?? "Sign up failed."
      );

      return;
    }

    setLoading(false);

    setSuccess(
      result.message ??
        "Account created successfully."
    );

    setPassword("");
    setConfirmPassword("");

    setTimeout(() => {
      setSuccess("");
      setCurrentMode("login");
    }, 1200);
  };

  return (
    <div
      className="fixed inset-0 z-[100] flex items-center justify-center bg-slate-900/20 px-4 py-6 backdrop-blur-sm"
      onClick={onClose}
    >
      <div
        className="relative max-h-[90vh] w-full max-w-2xl overflow-y-auto rounded-3xl bg-white p-8 shadow-2xl"
        onClick={(e) => e.stopPropagation()}
      >
        <button
          type="button"
          onClick={onClose}
          className="absolute right-5 top-5 rounded-full p-2 text-slate-500 transition hover:bg-slate-100 hover:text-slate-900"
          aria-label="Close"
        >
          <X size={22} />
        </button>

        {!selectedRole ? (
          <>
            <div className="text-center">
              <h2 className="text-3xl font-bold text-slate-900">
                {currentMode === "login"
                  ? "Login to TalentSphere"
                  : "Sign Up for TalentSphere"}
              </h2>

              <p className="mt-3 text-slate-600">
                Select your career stage to continue.
              </p>
            </div>

            <div className="mt-8 grid gap-4 md:grid-cols-3">
              {roles.map((item) => {
                const Icon = item.icon;

                return (
                  <button
                    key={item.role}
                    type="button"
                    onClick={() =>
                      setSelectedRole(item.role)
                    }
                    className="rounded-2xl border border-slate-200 p-6 text-center transition hover:-translate-y-1 hover:border-cyan-500 hover:bg-cyan-50 hover:shadow-lg"
                  >
                    <div className="mx-auto flex h-14 w-14 items-center justify-center rounded-2xl bg-cyan-100 text-cyan-600">
                      <Icon size={28} />
                    </div>

                    <h3 className="mt-5 font-bold text-slate-900">
                      {item.title}
                    </h3>
                  </button>
                );
              })}
            </div>

            <p className="mt-7 text-center text-sm text-slate-600">
              {currentMode === "login"
                ? "Don't have an account?"
                : "Already have an account?"}{" "}
              <button
                type="button"
                onClick={() =>
                  switchMode(
                    currentMode === "login"
                      ? "signup"
                      : "login"
                  )
                }
                className="font-semibold text-cyan-600 hover:underline"
              >
                {currentMode === "login"
                  ? "Sign Up"
                  : "Login"}
              </button>
            </p>
          </>
        ) : (
          <>
            <button
              type="button"
              onClick={() => {
                setSelectedRole(null);
                resetMessages();
              }}
              className="flex items-center gap-2 text-sm font-semibold text-cyan-600 hover:underline"
            >
              <ArrowLeft size={18} />
              Back
            </button>

            <div className="mt-6 text-center">
              <h2 className="text-3xl font-bold text-slate-900">
                {selectedRoleTitle}{" "}
                {currentMode === "login"
                  ? "Login"
                  : "Sign Up"}
              </h2>

              <p className="mt-2 text-sm text-slate-600">
                {currentMode === "login"
                  ? "Sign in to continue to your TalentSphere account."
                  : "Create your TalentSphere account."}
              </p>
            </div>

            <form
              onSubmit={
                currentMode === "login"
                  ? handleLogin
                  : handleSignUp
              }
              className="mx-auto mt-8 max-w-md space-y-5"
            >
              {currentMode === "signup" && (
                <Input
                  label="Full Name"
                  placeholder="Enter your full name"
                  value={name}
                  onChange={(e) =>
                    setName(e.target.value)
                  }
                />
              )}

              <Input
                label="Email"
                type="email"
                placeholder="Enter your email"
                value={email}
                onChange={(e) =>
                  setEmail(e.target.value)
                }
              />

              <PasswordInput
                label="Password"
                placeholder={
                  currentMode === "login"
                    ? "Enter your password"
                    : "Create password"
                }
                value={password}
                onChange={(e) =>
                  setPassword(e.target.value)
                }
              />

              {currentMode === "signup" && (
                <PasswordInput
                  label="Confirm Password"
                  placeholder="Confirm password"
                  value={confirmPassword}
                  onChange={(e) =>
                    setConfirmPassword(
                      e.target.value
                    )
                  }
                />
              )}

              {error && (
                <div className="rounded-lg border border-red-200 bg-red-50 p-3 text-sm text-red-600">
                  {error}
                </div>
              )}

              {success && (
                <div className="rounded-lg border border-green-200 bg-green-50 p-3 text-sm text-green-600">
                  {success}
                </div>
              )}

              <Button
                type="submit"
                className="w-full"
                disabled={loading}
              >
                {loading
                  ? currentMode === "login"
                    ? "Signing In..."
                    : "Creating Account..."
                  : currentMode === "login"
                    ? "Login"
                    : "Sign Up"}
              </Button>
            </form>

            <p className="mt-7 text-center text-sm text-slate-600">
              {currentMode === "login"
                ? "Don't have an account?"
                : "Already have an account?"}{" "}
              <button
                type="button"
                onClick={() =>
                  switchMode(
                    currentMode === "login"
                      ? "signup"
                      : "login"
                  )
                }
                className="font-semibold text-cyan-600 hover:underline"
              >
                {currentMode === "login"
                  ? "Create Account"
                  : "Login"}
              </button>
            </p>
          </>
        )}
      </div>
    </div>
  );
}

export default AuthRoleModal;