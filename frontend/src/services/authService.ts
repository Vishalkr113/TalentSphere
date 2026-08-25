import { API_BASE_URL, request } from "./api";


// =====================================================
// User Role
// =====================================================

export type UserRole =
  | "high_school_student"
  | "college_student"
  | "working_professional";



// =====================================================
// Auth User
// =====================================================

export interface AuthUser {

  id: string;

  full_name: string;

  email: string;

  role: UserRole;

  is_verified?: boolean;

  name?: string;

}



// =====================================================
// Responses
// =====================================================

export interface LoginResponse {

  access_token: string;

  token_type: string;

  user: AuthUser;

}


export interface RegisterRequest {

  full_name: string;

  email: string;

  password: string;

  role: UserRole;

}


export interface RegisterResponse {

  message: string;

  email: string;

}


export interface VerifyEmailRequest {

  email:string;

  otp:string;

}


export interface VerifyEmailResponse {

  message:string;

}


export interface ForgotPasswordRequest {

  email:string;

}


export interface ForgotPasswordResponse {

  message:string;

}


export interface ResetPasswordRequest {

  token:string;

  new_password:string;

}


export interface ResetPasswordResponse {

  message:string;

}


export interface ChangePasswordRequest {

  current_password:string;

  new_password:string;

}


export interface ChangePasswordResponse {

  message:string;

}



// =====================================================
// Token
// =====================================================


export const TOKEN_KEY="access_token";


export function saveToken(
token:string
){

localStorage.setItem(
TOKEN_KEY,
token
);

}



export function getToken(){

return localStorage.getItem(
TOKEN_KEY
);

}



export function removeToken(){

localStorage.removeItem(
TOKEN_KEY
);

}



export function logoutUser(){

removeToken();

}



// =====================================================
// Validation
// =====================================================


export function isValidEmail(
email:string
){

return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(
email
);

}



export function isValidPassword(
password:string
){

return /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$/.test(
password
);

}



// =====================================================
// Role Normalizer
// =====================================================


export function normalizeRole(
role:string
):UserRole{


switch(role){


case "high-school-student":

case "high_school_student":

return "high_school_student";



case "college-student":

case "college_student":

return "college_student";



case "working-professional":

case "working_professional":

return "working_professional";



default:

throw new Error("Invalid user role returned by the server.");


}


}



// =====================================================
// Error Parser
// =====================================================


function getErrorMessage(
data:any,
fallback:string
){


if(typeof data?.detail==="string"){

return data.detail;

}


if(Array.isArray(data?.detail)){

return data.detail
.map(
(item:any)=>item.msg
)
.join(",");

}



if(data?.detail){

return JSON.stringify(
data.detail
);

}



return fallback;


}




// =====================================================
// Login
// =====================================================


export async function loginUser(
email:string,
password:string,
role:UserRole
):Promise<LoginResponse>{



const response =
await fetch(
`${API_BASE_URL}/auth/login`,
{


method:"POST",


headers:{

"Content-Type":
"application/json",

},


body:JSON.stringify({

email,

password,

role,

}),


}
);



const data =
await response.json();



if(!response.ok){

throw new Error(
getErrorMessage(
data,
"Login failed."
)
);

}



const normalizedUser:AuthUser={


...data.user,


role:
normalizeRole(
data.user.role
),


name:
data.user.full_name,


};



saveToken(
data.access_token
);



return {


access_token:
data.access_token,


token_type:
data.token_type,


user:
normalizedUser,


};


}





// =====================================================
// Register
// =====================================================


export async function registerUser(
payload:RegisterRequest
):Promise<RegisterResponse>{


const response =
await fetch(
`${API_BASE_URL}/auth/register`,
{


method:"POST",


headers:{

"Content-Type":
"application/json",

},


body:
JSON.stringify(payload),


}
);



const data =
await response.json();



if(!response.ok){


throw new Error(
getErrorMessage(
data,
"Registration failed."
)
);


}



return {

message:data.message,

email:data.email,

};


}





// =====================================================
// Verify Email
// =====================================================


export async function verifyEmail(
payload:VerifyEmailRequest
):Promise<VerifyEmailResponse>{


const response =
await fetch(
`${API_BASE_URL}/auth/verify-email`,
{


method:"POST",


headers:{

"Content-Type":
"application/json",

},


body:
JSON.stringify(payload),


}
);



const data =
await response.json();



if(!response.ok){


throw new Error(
getErrorMessage(
data,
"OTP verification failed."
)
);


}



return {

message:data.message,

};


}





// =====================================================
// Forgot Password
// =====================================================


export async function forgotPassword(
payload:ForgotPasswordRequest
){

return request(
"/auth/forgot-password",
{

method:"POST",

headers:{

"Content-Type":
"application/json",

},

body:
JSON.stringify(payload),

}
);


}





// =====================================================
// Reset Password
// =====================================================


export async function resetPassword(
payload:ResetPasswordRequest
){

return request(
"/auth/reset-password",
{

method:"POST",

headers:{

"Content-Type":
"application/json",

},


body:
JSON.stringify(payload),


}
);


}





// =====================================================
// Change Password
// =====================================================


export async function changePassword(
payload:ChangePasswordRequest
){

return request(
"/auth/change-password",
{


method:"POST",


token:
getToken() ?? undefined,


headers:{

"Content-Type":
"application/json",

},


body:
JSON.stringify(payload),


}
);


}

// =====================================================
// Current User
// =====================================================

export async function getCurrentUser(): Promise<AuthUser> {


const user = await request(
"/auth/me",
{

method:"GET",

token:
getToken() ?? undefined,

}
) as AuthUser;



return {

...user,


role:
normalizeRole(
user.role
),


name:
user.full_name,


};


}