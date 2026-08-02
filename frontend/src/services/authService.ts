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
  email: string;
  otp: string;
}


export interface VerifyEmailResponse {
  message: string;
}


export interface ForgotPasswordRequest {
  email: string;
}


export interface ForgotPasswordResponse {
  message: string;
}


export interface ResetPasswordRequest {
  token: string;
  new_password: string;
}


export interface ResetPasswordResponse {
  message: string;
}


export interface ChangePasswordRequest {
  current_password: string;
  new_password: string;
}


export interface ChangePasswordResponse {
  message: string;
}



// =====================================================
// Token
// =====================================================

export const TOKEN_KEY = "access_token";


export function saveToken(
  token: string
): void {

  localStorage.setItem(
    TOKEN_KEY,
    token
  );

}


export function getToken(): string | null {

  return localStorage.getItem(
    TOKEN_KEY
  );

}


export function removeToken(): void {

  localStorage.removeItem(
    TOKEN_KEY
  );

}


export function logoutUser(): void {

  removeToken();

}



// =====================================================
// Validation
// =====================================================

export function isValidEmail(
  email: string
): boolean {

  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(
    email
  );

}



export function isValidPassword(
  password: string
): boolean {

  return /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$/.test(
    password
  );

}



// =====================================================
// Role Normalizer
// =====================================================

export function normalizeRole(
  role: string
): UserRole {

  switch (role) {

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
      return "college_student";

  }

}



// =====================================================
// Login
// =====================================================

export async function loginUser(
  email: string,
  password: string
): Promise<LoginResponse> {


  const formData =
    new URLSearchParams();


  formData.append(
    "username",
    email
  );


  formData.append(
    "password",
    password
  );



  const response =
    await fetch(
      `${API_BASE_URL}/auth/login`,
      {

        method: "POST",

        headers: {
          "Content-Type":
            "application/x-www-form-urlencoded",
        },

        body: formData,

      }
    );



  const data =
    await response.json();



  if (!response.ok) {

    throw new Error(
      data.detail ??
      "Login failed."
    );

  }



  saveToken(
    data.access_token
  );



  return {

    access_token:
      data.access_token,


    token_type:
      data.token_type,


    user: {
      ...data.user,

      role:
        normalizeRole(
          data.user.role
        ),

      name:
        data.user.full_name,
    }

  };

}



// =====================================================
// Register
// =====================================================

export async function registerUser(
  payload: RegisterRequest
): Promise<RegisterResponse> {


  const response =
    await fetch(
      `${API_BASE_URL}/auth/register`,
      {

        method: "POST",

        headers: {
          "Content-Type":
            "application/json",
        },


        body:
          JSON.stringify(payload),

      }
    );



  const data =
    await response.json();



  console.log(
    "REGISTER API RESPONSE:",
    data
  );



  if (!response.ok) {

    throw new Error(
      data.detail ||
      "Registration failed."
    );

  }



  return {

    message:
      data.message,


    email:
      data.email,

  };

}





// =====================================================
// Verify Email
// =====================================================

export async function verifyEmail(
  payload: VerifyEmailRequest
): Promise<VerifyEmailResponse> {


  const response =
    await fetch(
      `${API_BASE_URL}/auth/verify-email`,
      {

        method: "POST",


        headers: {
          "Content-Type":
            "application/json",
        },


        body:
          JSON.stringify(payload),

      }
    );



  const data =
    await response.json();



  console.log(
    "VERIFY OTP RESPONSE:",
    data
  );



  if (!response.ok) {

    throw new Error(
      data.detail ||
      "OTP verification failed."
    );

  }



  return {

    message:
      data.message,

  };


}


// =====================================================
// Forgot Password
// =====================================================

export async function forgotPassword(
  payload: ForgotPasswordRequest
): Promise<ForgotPasswordResponse> {


  return request<ForgotPasswordResponse>(
    "/auth/forgot-password",
    {

      method: "POST",

      headers: {
        "Content-Type":
          "application/json",
      },

      body:
        JSON.stringify(
          payload
        ),

    }
  );

}



// =====================================================
// Reset Password
// =====================================================

export async function resetPassword(
  payload: ResetPasswordRequest
): Promise<ResetPasswordResponse> {


  return request<ResetPasswordResponse>(
    "/auth/reset-password",
    {

      method: "POST",

      headers: {
        "Content-Type":
          "application/json",
      },

      body:
        JSON.stringify(
          payload
        ),

    }
  );

}



// =====================================================
// Change Password
// =====================================================

export async function changePassword(
  payload: ChangePasswordRequest
): Promise<ChangePasswordResponse> {


  return request<ChangePasswordResponse>(
    "/auth/change-password",
    {

      method: "POST",

      token:
        getToken() ?? undefined,


      headers: {
        "Content-Type":
          "application/json",
      },


      body:
        JSON.stringify(
          payload
        ),

    }
  );

}



// =====================================================
// Current User
// =====================================================

export async function getCurrentUser()
  : Promise<AuthUser> {


  const user =
    await request<AuthUser>(
      "/auth/me",
      {

        method: "GET",

        token:
          getToken() ?? undefined,

      }
    );

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