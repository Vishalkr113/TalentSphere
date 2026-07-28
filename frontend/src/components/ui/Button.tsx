import type { ButtonHTMLAttributes, ReactNode } from "react";

type ButtonProps = ButtonHTMLAttributes<HTMLButtonElement> & {
  children: ReactNode;
  loading?: boolean;
};

function Button({
  children,
  loading = false,
  className = "",
  disabled,
  ...props
}: ButtonProps) {
  return (
    <button
      {...props}
      disabled={loading || disabled}
      className={`
        flex w-full items-center justify-center
        rounded-xl
        bg-cyan-600
        px-5
        py-3
        text-base
        font-semibold
        text-white
        transition-all
        duration-200
        hover:bg-cyan-700
        active:scale-[0.98]
        disabled:cursor-not-allowed
        disabled:opacity-60
        ${className}
      `}
    >
      {loading ? "Please wait..." : children}
    </button>
  );
}

export default Button;