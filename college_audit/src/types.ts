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

/* ================= Landing Page ================= */

export interface Portal {
  title: string;
  description: string;
  color: string;
  route: string;
}

export interface Feature {
  title: string;
  description: string;
  color: string;
}

export interface AIModule {
  title: string;
  description: string;
}

export interface HowItWorksStep {
  title: string;
  description: string;
}

export interface Testimonial {
  id: number;
  name: string;
  role: string;
  message: string;
}

export interface FAQItem {
  id: number;
  question: string;
  answer: string;
}