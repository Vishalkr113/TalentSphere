import { useState } from "react";
import {
  Link,
  useLocation,
  useNavigate,
} from "react-router-dom";

import Logo from "./ui/Logo";
import Card from "./ui/Card";
import Input from "./ui/Input";
import PasswordInput from "./ui/PasswordInput";
import Button from "./ui/Button";

import {
  registerUser,
  isValidEmail,
  isValidPassword,
  type UserRole,
} from "../services/authService";

function SignUp() {
  const navigate = useNavigate();
  const location = useLocation();

  const role = location.pathname.split("/")[1] as UserRole;

  const title =
    role === "high-school-student"
      ? "High School Student"
      : role === "college-student"
        ? "College Student"
        : "Working Professional";

  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");

  const handleSignUp = (e: React.FormEvent) => {
    e.preventDefault();

    setError("");
    setSuccess("");

    if (
      !name.trim() ||
      !email.trim() ||
      !password.trim() ||
      !confirmPassword.trim()
    ) {
      setError("Please fill in all required fields.");
      return;
    }

    if (!isValidEmail(email)) {
      setError("Please enter a valid email address.");
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
      role,
    });

    if (!result.success) {
      setLoading(false);

      setError(
        result.message ?? "Sign up failed."
      );

      return;
    }

    setSuccess(
      result.message ?? "Account created successfully."
    );

    setName("");
    setEmail("");
    setPassword("");
    setConfirmPassword("");

    setLoading(false);

    setTimeout(() => {
      navigate(`/${role}/login`);
    }, 1500);
  };

  return (
    <main className="flex min-h-screen items-center justify-center bg-slate-100 px-6 py-12">
      <Card className="w-full max-w-md p-8">
        <div className="flex justify-center">
          <Logo size="md" />
        </div>

        <div className="mt-8 text-center">
          <h1 className="text-3xl font-bold text-slate-900">
            {title} Sign Up
          </h1>

          <p className="mt-2 text-sm text-slate-600">
            Create your TalentSphere account.
          </p>
        </div>

        <form
          onSubmit={handleSignUp}
          className="mt-8 space-y-5"
        >
          <Input
            label="Full Name"
            placeholder="Enter your full name"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />

          <Input
            label="Email"
            type="email"
            placeholder="Enter your email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />

          <PasswordInput
            label="Password"
            placeholder="Create password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />

          <PasswordInput
            label="Confirm Password"
            placeholder="Confirm password"
            value={confirmPassword}
            onChange={(e) =>
              setConfirmPassword(e.target.value)
            }
          />

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
              ? "Creating Account..."
              : "Sign Up"}
          </Button>
        </form>

        <p className="mt-8 text-center text-sm text-slate-600">
          Already have an account?{" "}
          <Link
            to={`/${role}/login`}
            className="font-semibold text-cyan-600 hover:underline"
          >
            Login
          </Link>
        </p>
      </Card>
    </main>
  );
}

export default SignUp;