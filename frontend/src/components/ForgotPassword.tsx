import { useState } from "react";
import { Link } from "react-router-dom";

import Logo from "./ui/Logo";
import Card from "./ui/Card";
import Input from "./ui/Input";
import Button from "./ui/Button";

import {
  isValidEmail,
} from "../services/authService";

function ForgotPassword() {

  const [email, setEmail] =
    useState("");

  const [error, setError] =
    useState("");

  const [success, setSuccess] =
    useState("");

  const handleSubmit = (
    e: React.FormEvent
  ) => {

    e.preventDefault();

    setError("");
    setSuccess("");

    if (!email.trim()) {

      setError(
        "Please enter your email."
      );

      return;

    }

    if (!isValidEmail(email)) {

      setError(
        "Please enter a valid email address."
      );

      return;

    }

    const users = JSON.parse(
      localStorage.getItem(
        "talentsphere_users"
      ) || "[]"
    );

    const exists = users.find(
      (user: any) =>
        user.email ===
        email.trim().toLowerCase()
    );

    if (!exists) {

      setError(
        "No account found with this email."
      );

      return;

    }

    setSuccess(
      "Password reset link sent successfully. (Demo)"
    );

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
              setEmail(
                e.target.value
              )
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
          >

            Send Reset Link

          </Button>

        </form>

        <p className="mt-8 text-center text-sm text-slate-600">

          <Link
            to="/"
            className="font-semibold text-cyan-600 hover:underline"
          >

            Back to Home

          </Link>

        </p>

      </Card>

    </main>

  );

}

export default ForgotPassword;