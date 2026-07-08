import type { User, SessionUser } from "../types";

const USERS_KEY = "talentsphere_users";
const SESSION_KEY = "talentsphere_session";

/* ---------------- USERS ---------------- */

export function getUsers(): User[] {
  const users = localStorage.getItem(USERS_KEY);

  if (!users) return [];

  try {
    return JSON.parse(users);
  } catch {
    return [];
  }
}

export function saveUsers(users: User[]) {
  localStorage.setItem(
    USERS_KEY,
    JSON.stringify(users)
  );
}

export function addUser(user: User) {
  const users = getUsers();

  users.push(user);

  saveUsers(users);
}

export function findUserByEmail(email: string) {
  return getUsers().find(
    (user) =>
      user.email.toLowerCase() ===
      email.toLowerCase()
  );
}

export function findUserById(id: string) {
  return getUsers().find(
    (user) => user.id === id
  );
}

/* ---------------- SESSION ---------------- */

export function saveSession(
  session: SessionUser
) {
  localStorage.setItem(
    SESSION_KEY,
    JSON.stringify(session)
  );
}

export function getSession():
  | SessionUser
  | null {
  const session =
    localStorage.getItem(SESSION_KEY);

  if (!session) return null;

  try {
    return JSON.parse(session);
  } catch {
    return null;
  }
}

export function clearSession() {
  localStorage.removeItem(
    SESSION_KEY
  );
}

/* ---------------- CURRENT USER ---------------- */

export function getCurrentUser():
  | User
  | null {
  const session = getSession();

  if (!session) return null;

  return (
    findUserById(session.id) ?? null
  );
}

export function isAuthenticated() {
  return getSession() !== null;
}