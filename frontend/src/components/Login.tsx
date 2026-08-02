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

const ALLOWED_ROLES: UserRole[] = [
  "high_school_student",
  "college_student",
  "working_professional",
];
function Login() {
  const navigate = useNavigate();
  const location = useLocation();

  const { login } = useAuth();

  const pathRole = location.pathname.split("/")[1];

  const role: UserRole = ALLOWED_ROLES.includes(
  pathRole as UserRole
)
  ? (pathRole as UserRole)
  : "college_student";

  
  const title =
    role === "high_school_student"
      ? "High School Student"
      : role === "college_student"
        ? "College Student"
        : "Working Professional";

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleLogin = async (
    e: React.FormEvent<HTMLFormElement>
  ) => {
    e.preventDefault();

    if (loading) return;

    setError("");

    const normalizedEmail = email.trim().toLowerCase();

    if (!normalizedEmail || !password.trim()) {
      setError("Please fill in all required fields.");
      return;
    }

    if (!isValidEmail(normalizedEmail)) {
      setError("Please enter a valid email address.");
      return;
    }

    setLoading(true);

    try {
      const result = await loginUser(
        normalizedEmail,
        password
      );

      login(
        result.access_token,
        result.user
      );

      const dashboardRole = ALLOWED_ROLES.includes(
        result.user.role
      )
        ? result.user.role
        : role;

      navigate(
        `/${dashboardRole}/dashboard`,
        {
          replace: true,
        }
      );
    } catch (err) {
      setError(
        err instanceof Error
          ? err.message
          : "Unable to sign in."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="flex min-h-screen items-center justify-center bg-slate-100 px-4 py-8 sm:px-6 sm:py-12">
      <Card className="w-full max-w-md p-6 sm:p-8">
        <div className="flex justify-center">
          <Logo size="md" />
        </div>

        <div className="mt-8 text-center">
          <h1 className="text-2xl font-bold text-slate-900 sm:text-3xl">
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
            autoComplete="email"
            required
          />

          <PasswordInput
            label="Password"
            placeholder="Enter your password"
            value={password}
            onChange={(e) =>
              setPassword(e.target.value)
            }
            autoComplete="current-password"
            required
          />

          <div className="flex items-center justify-end">
            <Link
              to="/forgot-password"
              className="text-sm font-medium text-cyan-600 hover:underline"
            >
              Forgot Password?
            </Link>
          </div>

          {error && (
            <div
              role="alert"
              className="rounded-lg border border-red-200 bg-red-50 p-3 text-sm text-red-700"
            >
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
            to={`/${role}/signup`}
            className="font-semibold text-cyan-600 hover:underline"
          >
            Create Account
          </Link>
        </p>
      </Card>
    </main>
  );
}

export default Login;