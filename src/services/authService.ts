export type UserRole =
  | "high-school-student"
  | "college-student"
  | "working-professional";

export interface User {
  id: string;
  name: string;
  email: string;
  password: string;
  role: UserRole;
}

const STORAGE_KEY = "talentsphere_users";

const getUsers = (): User[] => {
  const users = localStorage.getItem(STORAGE_KEY);

  if (!users) return [];

  return JSON.parse(users);
};

const saveUsers = (users: User[]) => {
  localStorage.setItem(
    STORAGE_KEY,
    JSON.stringify(users)
  );
};

export const isValidEmail = (
  email: string
) => {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(
    email
  );
};

export const isValidPassword = (
  password: string
) => {
  return /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$/.test(
    password
  );
};

export const registerUser = ({
  name,
  email,
  password,
  role,
}: {
  name: string;
  email: string;
  password: string;
  role: UserRole;
}) => {
  const users = getUsers();

  const exists = users.find(
  (user) =>
    user.email.toLowerCase() === email.toLowerCase() &&
    user.role === role
);

  if (exists) {
    return {
      success: false,
      message:
        "Account already exists.",
    };
  }

  const newUser: User = {
    id: crypto.randomUUID(),
    name,
    email,
    password,
    role,
  };

  users.push(newUser);

  saveUsers(users);

  return {
    success: true,
    message:
      "Account created successfully.",
    user: newUser,
  };
};

export const loginUser = (
  email: string,
  password: string,
  role: UserRole
) => {
  const users = getUsers();

  const user = users.find(
    (item) =>
      item.email.toLowerCase() === email.toLowerCase()
     &&
      item.password === password &&
      item.role === role
  );

  if (!user) {
    return {
      success: false,
      message:
        "Invalid email or password.",
    };
  }

  localStorage.setItem(
    "currentUser",
    JSON.stringify(user)
  );

  return {
    success: true,
    user,
  };
};

export const logoutUser = () => {
  localStorage.removeItem(
    "currentUser"
  );
};

export const getCurrentUser = () => {
  const user =
    localStorage.getItem("currentUser");

  if (!user) return null;

  return JSON.parse(user);
};