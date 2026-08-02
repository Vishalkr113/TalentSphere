import { useState } from "react";
import {
    useNavigate,
    useSearchParams,
} from "react-router-dom";

import Card from "./ui/Card";
import Logo from "./ui/Logo";
import PasswordInput from "./ui/PasswordInput";
import Button from "./ui/Button";

import {
    resetPassword,
    isValidPassword,
} from "../services/authService";

function ResetPassword() {
    const navigate = useNavigate();

    const [params] = useSearchParams();

    const token =
        params.get("token") ?? "";

    const [password, setPassword] =
        useState("");

    const [confirmPassword, setConfirmPassword] =
        useState("");

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

        if (!token) {
            setError(
                "Invalid password reset link."
            );
            return;
        }

        if (
            !password ||
            !confirmPassword
        ) {
            setError(
                "Please fill in all fields."
            );
            return;
        }

        if (
            !isValidPassword(password)
        ) {
            setError(
                "Password must contain at least 8 characters, one uppercase letter and one number."
            );
            return;
        }

        if (
            password !==
            confirmPassword
        ) {
            setError(
                "Passwords do not match."
            );
            return;
        }

        setLoading(true);

        try {
            const result =
                await resetPassword({
                    token,
                    new_password: password,
                });

            setSuccess(
                result.message
            );

            setTimeout(() => {
                navigate(
                    "/college_student/login",
                    {
                        replace: true,
                    }
                );
            }, 1500);
        } catch (err) {
            setError(
                err instanceof Error
                    ? err.message
                    : "Unable to reset password."
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
                    <h1 className="text-3xl font-bold">
                        Reset Password
                    </h1>

                    <p className="mt-2 text-sm text-slate-600">
                        Create a new password.
                    </p>
                </div>

                <form
                    onSubmit={handleSubmit}
                    className="mt-8 space-y-5"
                >
                    <PasswordInput
                        label="New Password"
                        placeholder="Enter new password"
                        value={password}
                        onChange={(e) =>
                            setPassword(
                                e.target.value
                            )
                        }
                        required
                    />

                    <PasswordInput
                        label="Confirm Password"
                        placeholder="Confirm password"
                        value={confirmPassword}
                        onChange={(e) =>
                            setConfirmPassword(
                                e.target.value
                            )
                        }
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
                            ? "Updating..."
                            : "Reset Password"}
                    </Button>
                </form>
            </Card>
        </main>
    );
}

export default ResetPassword;