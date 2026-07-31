import { useState } from "react";
import { Link } from "react-router-dom";

import Card from "./ui/Card";
import Logo from "./ui/Logo";
import Input from "./ui/Input";
import Button from "./ui/Button";

import {
  forgotPassword,
  isValidEmail,
} from "../services/authService";

function ForgotPassword() {
  const [email, setEmail] = useState("");

  const [loading, setLoading] =
    useState(false);

  const [error, setError] =
    useState("");

  const [success, setSuccess] =
    useState("");

  const handleSubmit = async (
    e: React.FormEvent<HTMLFormElement>
  ) => {
    e.preventDefault();

    if (loading) return;

    setError("");
    setSuccess("");

    const normalizedEmail =
      email.trim().toLowerCase();

    if (!normalizedEmail) {
      setError("Please enter your email.");
      return;
    }

    if (!isValidEmail(normalizedEmail)) {
      setError(
        "Please enter a valid email address."
      );
      return;
    }

    setLoading(true);

    try {
      const result =
        await forgotPassword({
          email: normalizedEmail,
        });

      setSuccess(result.message);
      setEmail("");
    } catch (err) {
      setError(
        err instanceof Error
          ? err.message
          : "Unable to process request."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="flex min-h-screen items-center justify-center bg-slate-100 px-6 py-12">
      <Card className="w-full max-w-md p-8">
        <div className="flex justify-center">
          <Logo size="md" />
        </div>

        <div className="mt-8 text-center">
          <h1 className="text-3xl font-bold text-slate-900">
            Forgot Password
          </h1>

          <p className="mt-2 text-sm text-slate-600">
            Enter your registered email.
          </p>
        </div>

        <form
          onSubmit={handleSubmit}
          className="mt-8 space-y-5"
        >
          <Input
            label="Email"
            type="email"
            placeholder="Enter your email"
            value={email}
            onChange={(e) =>
              setEmail(e.target.value)
            }
            autoComplete="email"
            required
          />

          {error && (
            <div className="rounded-lg border border-red-200 bg-red-50 p-3 text-sm text-red-700">
              {error}
            </div>
          )}

          {success && (
            <div className="rounded-lg border border-green-200 bg-green-50 p-3 text-sm text-green-700">
              {success}
            </div>
          )}

          <Button
            type="submit"
            className="w-full"
            disabled={loading}
          >
            {loading
              ? "Submitting..."
              : "Send Reset Link"}
          </Button>
        </form>

        <p className="mt-8 text-center text-sm text-slate-600">
          Remember your password?{" "}
          <Link
            to="/college-student/login"
            className="font-semibold text-cyan-600 hover:underline"
          >
            Login
          </Link>
        </p>
      </Card>
    </main>
  );
}

export default ForgotPassword;