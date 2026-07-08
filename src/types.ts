export type UserRole =
  | "student"
  | "institute"
  | "professional";

export interface User {
  id: string;
  fullName: string;
  email: string;
  phone: string;
  password: string;
  role: UserRole;

  college?: string;
  course?: string;
  semester?: string;

  instituteName?: string;

  companyName?: string;
  designation?: string;

  createdAt: string;
}

export interface SessionUser {
  id: string;
  fullName: string;
  email: string;
  role: UserRole;
}

export interface LoginData {
  email: string;
  password: string;
  role: UserRole;
}

export interface RegisterData {
  fullName: string;
  email: string;
  phone: string;
  password: string;
  role: UserRole;

  college?: string;
  course?: string;
  semester?: string;

  instituteName?: string;

  companyName?: string;
  designation?: string;
}

export interface AuthResponse {
  success: boolean;
  message: string;
  user?: User;
}