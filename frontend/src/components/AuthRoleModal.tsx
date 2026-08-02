import { useState } from "react";
import { useNavigate } from "react-router-dom";

import {
  ArrowLeft,
  Briefcase,
  GraduationCap,
  School,
  X,
} from "lucide-react";

import Input from "./ui/Input";
import PasswordInput from "./ui/PasswordInput";
import Button from "./ui/Button";

import {
  isValidEmail,
  isValidPassword,
  loginUser,
  registerUser,
  verifyEmail,
  type UserRole,
} from "../services/authService";

import { useAuth } from "../contexts/AuthContext";


type AuthMode =
  | "login"
  | "signup";


interface AuthRoleModalProps {

  mode: AuthMode;

  onClose: () => void;

}


const roles = [

  {
    title: "High School Student",
    role: "high_school_student" as UserRole,
    icon: School,
  },

  {
    title: "College Student",
    role: "college_student" as UserRole,
    icon: GraduationCap,
  },

  {
    title: "Working Professional",
    role: "working_professional" as UserRole,
    icon: Briefcase,
  },

];



function AuthRoleModal({

  mode,

  onClose,

}: AuthRoleModalProps) {


  const navigate = useNavigate();

  const { login } = useAuth();



  const [selectedRole, setSelectedRole]
    =
    useState<UserRole | null>(null);


  const [currentMode, setCurrentMode]
    =
    useState<AuthMode>(mode);



  const [name, setName] = useState("");

  const [email, setEmail] = useState("");

  const [password, setPassword] = useState("");

  const [confirmPassword, setConfirmPassword] = useState("");

  const [otp, setOtp] = useState("");

  const [registeredEmail, setRegisteredEmail] = useState("");



  const [showOtp, setShowOtp] = useState(false);

  const [loading, setLoading] = useState(false);


  const [error, setError] = useState("");

  const [success, setSuccess] = useState("");



  const selectedRoleTitle =
    roles.find(
      (item) => item.role === selectedRole
    )?.title;



  const resetMessages = () => {

    setError("");

    setSuccess("");

  };




  const switchMode = (newMode: AuthMode) => {

    resetMessages();

    setCurrentMode(newMode);

    setShowOtp(false);

    setOtp("");

    setPassword("");

    setConfirmPassword("");

  };



  // LOGIN

  const handleLogin = async (
    e: React.FormEvent
  ) => {


    e.preventDefault();

    resetMessages();



    if (!selectedRole) {

      setError(
        "Please select your career stage."
      );

      return;

    }


    try {


      setLoading(true);


      const result =
        await loginUser(
          email.trim().toLowerCase(),
          password
        );



      login(
        result.access_token,
        result.user
      );


      onClose();


      navigate(
        `/${result.user.role}/dashboard`,
        {
          replace: true
        }
      );


    }

    catch (err) {

      setError(
        err instanceof Error
          ?
          err.message
          :
          "Login failed."
      );


    }

    finally {

      setLoading(false);

    }

  };



  // REGISTER

  const handleSignUp = async (
    e: React.FormEvent
  ) => {


    e.preventDefault();


    if (showOtp)
      return;


    resetMessages();



    if (!selectedRole) {

      setError(
        "Please select your career stage."
      );

      return;

    }



    if (
      !name.trim()
      ||
      !email.trim()
      ||
      !password.trim()
      ||
      !confirmPassword.trim()
    ) {

      setError(
        "Please fill all required fields."
      );

      return;

    }



    if (!isValidEmail(email)) {


      setError(
        "Invalid email address."
      );

      return;

    }



    if (!isValidPassword(password)) {


      setError(
        "Password must contain 8 characters, uppercase and number."
      );

      return;

    }



    if (password !== confirmPassword) {

      setError(
        "Passwords do not match."
      );

      return;

    }


    try {


      setLoading(true);


      const result =
        await registerUser({

          full_name: name.trim(),

          email: email.trim().toLowerCase(),

          password,

          role: selectedRole,

        });



      setRegisteredEmail(
        result.email
      );


      setShowOtp(true);


      setSuccess(
        "OTP sent successfully. Please verify your email."
      );



    }

    catch (err) {


      setError(
        err instanceof Error
          ?
          err.message
          :
          "Registration failed."
      );


    }

    finally {

      setLoading(false);

    }


  };

  // =======================
  // VERIFY OTP
  // =======================

  const handleVerifyOtp = async () => {


    if (!otp.trim()) {

      setError(
        "Please enter OTP."
      );

      return;

    }



    try {


      setLoading(true);

      resetMessages();



      await verifyEmail({

        email: registeredEmail,

        otp: otp.trim(),

      });



      setSuccess(
        "Email verified successfully."
      );



      // switch to login after verification

      setTimeout(() => {


        setShowOtp(false);

        setOtp("");

        setCurrentMode("login");

        setPassword("");

        setConfirmPassword("");


      }, 800);



    }


    catch (err) {


      setError(

        err instanceof Error

          ?

          err.message

          :

          "OTP verification failed."

      );


    }


    finally {


      setLoading(false);


    }


  };

  return (

    <div

      className="
fixed
inset-0
z-[100]
flex
items-center
justify-center
bg-slate-900/30
p-5
backdrop-blur-sm
"

      onClick={onClose}

    >


      <div

        className="
relative
w-full
max-w-md
rounded-3xl
bg-white
px-6
py-5
shadow-2xl
"

        onClick={(e) => e.stopPropagation()}

      >


        <button

          type="button"

          onClick={onClose}

          className="
absolute
right-4
top-4
rounded-full
p-2
text-slate-500
hover:bg-slate-100
"

        >

          <X size={20} />

        </button>





        {

          !selectedRole

            ?

            <>


              <div className="text-center">


                <h2 className="text-2xl font-bold text-slate-900">

                  {
                    currentMode === "login"
                      ?
                      "Login to TalentSphere"
                      :
                      "Signup for TalentSphere"
                  }

                </h2>


                <p className="mt-2 text-sm text-slate-600">

                  Select your career stage

                </p>


              </div>





              <div className="mt-5 space-y-3">


                {

                  roles.map((item) => {


                    const Icon = item.icon;


                    return (

                      <button

                        key={item.role}

                        type="button"

                        onClick={() => setSelectedRole(item.role)}

                        className="
flex
w-full
items-center
gap-4
rounded-xl
border
border-slate-200
p-3
transition
hover:border-cyan-500
hover:bg-cyan-50
"

                      >


                        <div

                          className="
flex
h-10
w-10
items-center
justify-center
rounded-xl
bg-cyan-100
text-cyan-600
"

                        >

                          <Icon size={22} />

                        </div>



                        <span className="font-semibold text-slate-800">

                          {item.title}

                        </span>



                      </button>

                    )


                  })

                }


              </div>





              <p className="mt-5 text-center text-sm text-slate-600">


                {
                  currentMode === "login"
                    ?
                    "Don't have an account?"
                    :
                    "Already have an account?"
                }


                {" "}


                <button

                  type="button"

                  onClick={() => switchMode(
                    currentMode === "login"
                      ?
                      "signup"
                      :
                      "login"
                  )}

                  className="
font-semibold
text-cyan-600
"

                >

                  {
                    currentMode === "login"
                      ?
                      "Signup"
                      :
                      "Login"
                  }

                </button>


              </p>



            </>



            :





            <>



              <button

                type="button"

                onClick={() => {

                  setSelectedRole(null);

                  resetMessages();

                }}

                className="
flex
items-center
gap-2
text-sm
font-semibold
text-cyan-600
"

              >

                <ArrowLeft size={16} />

                Back

              </button>






              <div className="mt-3 text-center">


                <h2 className="text-xl font-bold text-slate-900">

                  {selectedRoleTitle}

                  {" "}

                  {
                    currentMode === "login"
                      ?
                      "Login"
                      :
                      "Signup"
                  }

                </h2>


                <p className="mt-1 text-xs text-slate-600">

                  Create your TalentSphere account

                </p>


              </div>





              <form

                onSubmit={
                  currentMode === "login"
                    ?
                    handleLogin
                    :
                    handleSignUp
                }

                className="
mt-4
space-y-3
"

              >



                {

                  currentMode === "signup"

                  &&

                  <Input

                    label="Full Name"

                    placeholder="Enter full name"

                    value={name}

                    disabled={showOtp}

                    onChange={(e) =>
                      setName(e.target.value)
                    }

                  />

                }




                <Input

                  label="Email"

                  type="email"

                  placeholder="Enter email"

                  value={email}

                  disabled={showOtp}

                  onChange={(e) =>
                    setEmail(e.target.value)
                  }

                />






                <PasswordInput

                  label="Password"

                  placeholder="Password"

                  value={password}

                  disabled={showOtp}

                  onChange={(e) =>
                    setPassword(e.target.value)
                  }

                />






                {

                  currentMode === "signup"

                  &&

                  <PasswordInput

                    label="Confirm Password"

                    placeholder="Confirm password"

                    value={confirmPassword}

                    disabled={showOtp}

                    onChange={(e) =>
                      setConfirmPassword(e.target.value)
                    }

                  />

                }





                {

                  showOtp &&

                  <Input

                    label="Email OTP"

                    placeholder="Enter OTP"

                    value={otp}

                    onChange={(e) =>
                      setOtp(e.target.value)
                    }

                  />

                }





                {

                  error &&

                  <div

                    className="
rounded-lg
border
border-red-200
bg-red-50
p-2
text-sm
text-red-700
"

                  >

                    {error}

                  </div>

                }





                {

                  success &&

                  <div

                    className="
rounded-lg
border
border-green-200
bg-green-50
p-2
text-sm
text-green-700
"

                  >

                    {success}

                  </div>

                }





                <Button

                  type={
                    showOtp
                      ?
                      "button"
                      :
                      "submit"
                  }

                  onClick={
                    showOtp
                      ?
                      handleVerifyOtp
                      :
                      undefined
                  }

                  className="w-full"

                  disabled={loading}

                >

                  {

                    loading

                      ?

                      "Processing..."

                      :

                      showOtp

                        ?

                        "Verify Email"

                        :

                        currentMode === "login"

                          ?

                          "Login"

                          :

                          "Signup"

                  }


                </Button>



              </form>






              <p className="mt-4 text-center text-sm text-slate-600">


                {
                  currentMode === "login"
                    ?
                    "Don't have an account?"
                    :
                    "Already have an account?"
                }


                {" "}


                <button

                  type="button"

                  onClick={() => switchMode(
                    currentMode === "login"
                      ?
                      "signup"
                      :
                      "login"
                  )}

                  className="
font-semibold
text-cyan-600
"

                >

                  {
                    currentMode === "login"
                      ?
                      "Create Account"
                      :
                      "Login"
                  }


                </button>


              </p>



            </>


        }


      </div>


    </div>

  );


}


export default AuthRoleModal;