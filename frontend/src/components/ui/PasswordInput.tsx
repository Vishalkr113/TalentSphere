import {
  forwardRef,
  useState,
  type InputHTMLAttributes,
} from "react";

import { Eye, EyeOff } from "lucide-react";

type PasswordInputProps =
  InputHTMLAttributes<HTMLInputElement> & {
    label: string;
    error?: string;
  };

const PasswordInput = forwardRef<
  HTMLInputElement,
  PasswordInputProps
>(
  (
    {
      label,
      error,
      className = "",
      ...props
    },
    ref
  ) => {
    const [showPassword, setShowPassword] =
      useState(false);

    return (
      <div className="space-y-2">

        <label className="block text-sm font-medium text-slate-700">
          {label}
        </label>
  < div className="relative" >

    <input
      ref={ref}
      {...props}
      type={
        showPassword
          ? "text"
          : "password"
      }
      className={`
              w-full
              rounded-xl
              border
              border-slate-300
              bg-white
              px-4
              py-3
              pr-12
              text-slate-800
              outline-none
              transition-all
              duration-200
              placeholder:text-slate-400
              focus:border-cyan-500
              focus:ring-4
              focus:ring-cyan-100
              ${error
          ? "border-red-500 focus:border-red-500 focus:ring-red-100"
          : ""
        }
              ${className}
            `}
    />

    <button
      type="button"
      onClick={() =>
        setShowPassword(
          !showPassword
        )
      }
      className="absolute right-4 top-1/2 -translate-y-1/2 text-slate-500 transition hover:text-cyan-600"
    >
      {showPassword ? (
        <EyeOff size={20} />
      ) : (
        <Eye size={20} />
      )}
    </button>

  </div >

{
  error && (
    <p className="text-sm text-red-500">
      {error}
    </p>
  )
}

      </div >
    );
}
);

PasswordInput.displayName =
  "PasswordInput";

export default PasswordInput;