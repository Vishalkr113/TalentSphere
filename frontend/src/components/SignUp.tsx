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
  registerUser,
  verifyEmail,
  isValidEmail,
  isValidPassword,
  type UserRole,
} from "../services/authService";



const ALLOWED_ROLES: UserRole[] = [
  "high_school_student",
  "college_student",
  "working_professional",
];



function SignUp(){


const navigate = useNavigate();

const location = useLocation();



const pathRole =
location.pathname.split("/")[1];



const role:UserRole =
ALLOWED_ROLES.includes(
pathRole as UserRole
)
?
(pathRole as UserRole)
:
"college_student";



const title =
role==="high_school_student"
?
"High School Student"
:
role==="college_student"
?
"College Student"
:
"Working Professional";



const [name,setName]=useState("");

const [email,setEmail]=useState("");

const [password,setPassword]=useState("");

const [confirmPassword,setConfirmPassword]=useState("");

const [otp,setOtp]=useState("");



const [registeredEmail,setRegisteredEmail]=useState("");



const [showOtp,setShowOtp]=useState(false);


const [loading,setLoading]=useState(false);


const [verifyLoading,setVerifyLoading]=useState(false);


const [message,setMessage]=useState("");


const [error,setError]=useState("");





// ============================
// REGISTER
// ============================


const handleSignUp =
async(
e:React.FormEvent
)=>{


e.preventDefault();



if(showOtp)
return;



if(loading)
return;



setError("");

setMessage("");



const fullName =
name.trim();


const normalizedEmail =
email.trim().toLowerCase();



if(
!fullName ||
!normalizedEmail ||
!password ||
!confirmPassword
){

setError(
"Please fill all fields."
);

return;

}



if(!isValidEmail(normalizedEmail)){


setError(
"Invalid email address."
);

return;

}



if(!isValidPassword(password)){


setError(
"Password must contain 8 characters, uppercase and number."
);

return;

}



if(password!==confirmPassword){


setError(
"Passwords do not match."
);

return;

}




try{


setLoading(true);



const response =
await registerUser({

full_name:fullName,

email:normalizedEmail,

password,

role,

});



console.log(
"REGISTER SUCCESS",
response
);



setRegisteredEmail(
response.email
??
normalizedEmail
);



setShowOtp(true);



setMessage(
"OTP sent successfully. Please verify your email."
);



}


catch(err){


console.error(err);


setError(
err instanceof Error
?
err.message
:
"Registration failed."
);


}


finally{


setLoading(false);


}


};







// ============================
// VERIFY OTP
// ============================


const handleVerifyOtp =
async()=>{


if(verifyLoading)
return;



if(!otp.trim()){


setError(
"Please enter OTP."
);

return;

}



try{


setVerifyLoading(true);

setError("");



console.log(
"VERIFY OTP",
registeredEmail,
otp
);



await verifyEmail({

email:registeredEmail,

otp:otp.trim(),

});



setMessage(
"Email verified successfully."
);



setTimeout(()=>{


navigate(
`/${role}/login`,
{
replace:true
}
);


},800);



}



catch(err){


setError(
err instanceof Error
?
err.message
:
"OTP verification failed."
);


}



finally{


setVerifyLoading(false);


}



};








return(


<main className="
flex 
min-h-screen 
items-center 
justify-center 
bg-slate-100 
px-6 
py-12
">


<Card className="w-full max-w-md p-8">



<div className="flex justify-center">

<Logo size="md"/>

</div>





<div className="mt-8 text-center">


<h1 className="text-3xl font-bold text-slate-900">

{title} Sign Up

</h1>



<p className="mt-2 text-sm text-slate-600">

Create your TalentSphere account.

</p>


</div>






<form
onSubmit={handleSignUp}
className="mt-8 space-y-5"
>



<Input

label="Full Name"

placeholder="Enter your full name"

value={name}

disabled={showOtp}

onChange={
(e)=>setName(e.target.value)
}

/>





<Input

label="Email"

type="email"

placeholder="Enter email"

value={email}

disabled={showOtp}

onChange={
(e)=>setEmail(e.target.value)
}

/>





<PasswordInput

label="Password"

placeholder="Create password"

value={password}

disabled={showOtp}

onChange={
(e)=>setPassword(e.target.value)
}

/>





<PasswordInput

label="Confirm Password"

placeholder="Confirm password"

value={confirmPassword}

disabled={showOtp}

onChange={
(e)=>setConfirmPassword(e.target.value)
}

/>






{
showOtp &&

<Input

label="Email OTP"

placeholder="Enter 6 digit OTP"

value={otp}

onChange={
(e)=>setOtp(e.target.value)
}

/>

}






{
message &&

<div className="
rounded-lg
border
border-green-200
bg-green-50
p-3
text-sm
text-green-700
">

{message}

</div>

}






{
error &&

<div className="
rounded-lg
border
border-red-200
bg-red-50
p-3
text-sm
text-red-700
">

{error}

</div>

}







{
showOtp

?

<Button

type="button"

className="w-full"

disabled={verifyLoading}

onClick={handleVerifyOtp}

>

{
verifyLoading
?
"Verifying..."
:
"Verify Email"
}


</Button>



:


<Button

type="submit"

className="w-full"

disabled={loading}

>

{
loading
?
"Sending OTP..."
:
"Create Account"
}


</Button>


}




</form>






<p className="mt-8 text-center text-sm text-slate-600">


Already have an account?{" "}


<Link

to={`/${role}/login`}

className="font-semibold text-cyan-600 hover:underline"

>

Login

</Link>



</p>



</Card>



</main>


);


}



export default SignUp;