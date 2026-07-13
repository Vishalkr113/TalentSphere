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
  loginUser,
  isValidEmail,
  type UserRole,
} from "../services/authService";

import { useAuth } from "../contexts/AuthContext";

function Login() {
  const navigate = useNavigate();
  const location = useLocation();

  const { login } = useAuth();

  const role = location.pathname.split("/")[1] as UserRole;

  const title =
    role === "high-school-student"
      ? "High School Student"
      : role === "college-student"
        ? "College Student"
        : "Working Professional";

  const [email, setEmail] =
    useState("");

  const [password, setPassword] =
    useState("");

  const [loading, setLoading] =
    useState(false);

  const [error, setError] =
    useState("");

  const handleLogin = (
    e: React.FormEvent
  ) => {
    e.preventDefault();

    setError("");

    if (
      !email.trim() ||
      !password.trim()
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

    setLoading(true);

    const result = loginUser(
      email.trim().toLowerCase(),
      password,
      role
    );

    if (!result.success) {
      setLoading(false);

      setError(
        result.message ??
        "Login failed."
      );

      return;
    }

    if (!result.user) {
      setLoading(false);

      setError(
        "User not found."
      );

      return;
    }

    login(result.user);

    setLoading(false);

    navigate(
      `/${role}/dashboard`,
      {
        replace: true,
      }
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
            {title} Login
          </h1>

          <p className="mt-2 text-sm text-slate-600">
            Sign in to continue to your TalentSphere account.
          </p>

        </div>

        <form
          onSubmit={handleLogin}
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
          />

          <PasswordInput
            label="Password"
            placeholder="Enter your password"
            value={password}
            onChange={(e) =>
              setPassword(e.target.value)
            }
          />

          <div className="flex items-center justify-between">

            <label className="flex items-center gap-2 text-sm text-slate-600">

              <input
                type="checkbox"
              />

              Remember Me

            </label>

            <Link
              to="/forgot-password"
              className="text-sm font-medium text-cyan-600 hover:underline"
            >
              Forgot Password?
            </Link>

          </div>

          {error && (
            <div className="rounded-lg border border-red-200 bg-red-50 p-3 text-sm text-red-600">
              {error}
            </div>
          )}

          <Button
            type="submit"
            className="w-full"
            disabled={loading}
          >
            {loading
              ? "Signing In..."
              : "Login"}
          </Button>

        </form>

        <p className="mt-8 text-center text-sm text-slate-600">

          Don't have an account?{" "}

          <Link
            to={`/${role}/Sign Up`}
            className="font-semibold text-cyan-600 hover:underline"
          >
            Create Account
          </Link>

        </p>

      </Card >

    </main >
  );
}

export default Login;