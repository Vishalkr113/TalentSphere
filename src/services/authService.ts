import type {
  User,
  LoginData,
  RegisterData,
  AuthResponse,
  SessionUser,
} from "../types";

import {
  addUser,
  findUserByEmail,
  saveSession,
  clearSession,
  getSession,
} from "./storage";

class AuthService {
  register(
    data: RegisterData
  ): AuthResponse {
    const existingUser =
      findUserByEmail(data.email);

    if (existingUser) {
      return {
        success: false,
        message: "Email already registered.",
      };
    }

    const user: User = {
      id: crypto.randomUUID(),

      fullName: data.fullName,

      email: data.email
        .trim()
        .toLowerCase(),

      phone: data.phone,

      password: data.password,

      role: data.role,

      college: data.college,

      course: data.course,

      semester: data.semester,

      instituteName:
        data.instituteName,

      companyName:
        data.companyName,

      designation:
        data.designation,

      createdAt:
        new Date().toISOString(),
    };

    addUser(user);

    return {
      success: true,
      message:
        "Registration Successful",
      user,
    };
  }

  login(
    data: LoginData
  ): AuthResponse {
    const user =
      findUserByEmail(data.email);

    if (!user) {
      return {
        success: false,
        message:
          "Account not found.",
      };
    }

    if (
      user.password !==
      data.password
    ) {
      return {
        success: false,
        message:
          "Invalid password.",
      };
    }

    if (
      user.role !== data.role
    ) {
      return {
        success: false,
        message: `This account belongs to ${user.role} portal.`,
      };
    }

    const session: SessionUser = {
      id: user.id,
      fullName: user.fullName,
      email: user.email,
      role: user.role,
    };

    saveSession(session);

    return {
      success: true,
      message:
        "Login Successful",
      user,
    };
  }

  logout() {
    clearSession();
  }

  currentUser() {
    return getSession();
  }

  isAuthenticated() {
    return getSession() !== null;
  }
}

export const authService =
  new AuthService();