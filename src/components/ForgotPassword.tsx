import { Link } from "react-router-dom";

import Logo from "./ui/Logo";
import Card from "./ui/Card";
import Input from "./ui/Input";
import Button from "./ui/Button";

function ForgotPassword() {
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
            Enter your registered email address and we'll send you a password reset link.
          </p>

        </div>

        <form className="mt-8 space-y-5">

          <Input
            label="Email Address"
            type="email"
            placeholder="Enter your email"
          />

          <Button className="w-full">
            Send Reset Link
          </Button>

        </form>

        <p className="mt-8 text-center text-sm text-slate-600">

          Remember your password?{" "}

          <Link
            to="/portal?mode=login"
            className="font-semibold text-cyan-600 hover:underline"
          >
            Back to Login
          </Link>

        </p>

      </Card>

    </main>
  );
}

export default ForgotPassword;