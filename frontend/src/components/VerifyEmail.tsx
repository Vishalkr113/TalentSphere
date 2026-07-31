import { useState } from "react";
import {
    useLocation,
    useNavigate,
} from "react-router-dom";

import Card from "./ui/Card";
import Logo from "./ui/Logo";
import Input from "./ui/Input";
import Button from "./ui/Button";

import { verifyEmail } from "../services/authService";

function VerifyEmail() {
    const navigate = useNavigate();
    const location = useLocation();

    const email =
        location.state?.email ?? "";

    const role =
        location.state?.role ??
        "college-student";

    const [otp, setOtp] =
        useState("");

    const [loading, setLoading] =
        useState(false);

    const [error, setError] =
        useState("");

    const [success, setSuccess] =
        useState("");

    const handleVerify = async (
        e: React.FormEvent<HTMLFormElement>
    ) => {
        e.preventDefault();

        if (loading) return;

        setError("");
        setSuccess("");

        if (!email) {
            setError(
                "Email not found. Please register again."
            );
            return;
        }

        if (!otp.trim()) {
            setError("Please enter OTP.");
            return;
        }

        if (!/^\d{6}$/.test(otp.trim())) {
            setError(
                "OTP must contain exactly 6 digits."
            );
            return;
        }

        setLoading(true);

        try {
            const result =
                await verifyEmail({
                    email,
                    otp: otp.trim(),
                });

            setSuccess(
                result.message ??
                "Email verified successfully."
            );

            setTimeout(() => {
                navigate(
                    `/${role}/login`,
                    {
                        replace: true,
                    }
                );
            }, 1500);
        } catch (err) {
            setError(
                err instanceof Error
                    ? err.message
                    : "Verification failed."
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
                        Verify Email
                    </h1>

                    <p className="mt-2 text-sm text-slate-600">
                        Enter the OTP sent to
                    </p>

                    <p className="mt-1 font-medium text-cyan-700">
                        {email}
                    </p>
                </div>

                <form
                    onSubmit={handleVerify}
                    className="mt-8 space-y-5"
                >
                    <Input
                        label="OTP"
                        placeholder="Enter 6-digit OTP"
                        value={otp}
                        onChange={(e) =>
                            setOtp(e.target.value)
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
                            ? "Verifying..."
                            : "Verify Email"}
                    </Button>
                </form>
            </Card>
        </main>
    );
}

export default VerifyEmail;