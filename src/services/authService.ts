export type UserRole =
  | "student"
  | "professional"
  | "institute";

export interface User {
  id: string;
  name: string;
  email: string;
  password: string;
  role: UserRole;
  createdAt: string;
}

const STORAGE_KEY = "talentsphere-users";

/* =========================
   Get All Users
========================= */

export function getUsers(): User[] {
  const data = localStorage.getItem(STORAGE_KEY);

  return data ? JSON.parse(data) : [];
}

/* =========================
   Save Users
========================= */

export function saveUsers(users: User[]) {
  localStorage.setItem(
    STORAGE_KEY,
    JSON.stringify(users)
  );
}

/* =========================
   Email Validation
========================= */

export function isValidEmail(
  email: string
) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(
    email
  );
}

/* =========================
   Password Validation
========================= */

export function isValidPassword(
  password: string
) {
  return /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$/.test(
    password
  );
}

/* =========================
   Register User
========================= */

export function registerUser(
  user: Omit<User, "id" | "createdAt">
) {
  const users = getUsers();

  /* Same Role Duplicate */

  const duplicate = users.find(
    (u) =>
      u.email.toLowerCase() ===
        user.email.toLowerCase() &&
      u.role === user.role
  );

  if (duplicate) {
    return {
      success: false,
      message:
        `${user.role} account already exists.`,
    };
  }

  /* Institute Rule */

  if (user.role === "institute") {
    const personal = users.find(
      (u) =>
        u.email.toLowerCase() ===
          user.email.toLowerCase() &&
        (u.role === "student" ||
          u.role ===
            "professional")
    );

    if (personal) {
      return {
        success: false,
        message:
          "Please use an official institute email.",
      };
    }
  }

  const newUser: User = {
    ...user,

    id: crypto.randomUUID(),

    createdAt:
      new Date().toISOString(),
  };

  users.push(newUser);

  saveUsers(users);

  return {
    success: true,
    message:
      "Account created successfully.",
  };
}

/* =========================
   Login
========================= */

export function loginUser(
  email: string,
  password: string,
  role: UserRole
) {
  const users = getUsers();

  const user = users.find(
    (u) =>
      u.email.toLowerCase() ===
        email.toLowerCase() &&
      u.role === role
  );

  if (!user) {
    return {
      success: false,
      message:
        "No account found.",
    };
  }

  if (user.password !== password) {
    return {
      success: false,
      message:
        "Incorrect password.",
    };
  }

  return {
    success: true,
    user,
  };
}