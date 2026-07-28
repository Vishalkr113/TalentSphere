import { FcGoogle } from "react-icons/fc";

function GoogleButton() {
  const handleGoogleLogin = () => {
    // Firebase / Google OAuth later
    console.log("Google Login");
  };

  return (
    <button
      type="button"
      onClick={handleGoogleLogin}
      className="flex w-full items-center justify-center gap-3 rounded-xl border border-slate-300 bg-white px-4 py-3 font-semibold text-slate-700 transition-all duration-200 hover:border-cyan-500 hover:shadow-md"
    >
      <FcGoogle size={24} />

      Continue with Google
    </button>
  );
}

export default GoogleButton;