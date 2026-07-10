import {
  forwardRef,
} from "react";

interface InputProps
  extends React.InputHTMLAttributes<HTMLInputElement> {
  label?: string;
  error?: string;
}

const Input = forwardRef<
  HTMLInputElement,
  InputProps
>(({ label, error, className = "", ...props }, ref) => {
  return (
    <div className="space-y-2">

      <label className="block text-sm font-medium text-slate-700">
        {label}
      </label>

  < input
    ref={ref}
    {...props}
    className={`
          w-full
          rounded-xl
          border
          border-slate-300
          bg-white
          px-4
          py-3
          text-slate-800
          outline-none
          transition-all
          duration-200
          placeholder:text-slate-400
          focus:border-cyan-500
          focus:ring-4
          focus:ring-cyan-100
          ${error ? "border-red-500 focus:ring-red-100 focus:border-red-500" : ""}
          ${className}
        `}
  />

{
  error && (
    <p className="text-sm text-red-500">
      {error}
    </p>
  )
}

    </div >
  );
});

Input.displayName = "Input";

export default Input;