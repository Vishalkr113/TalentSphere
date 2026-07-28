import {
  createContext,
  useContext,
  useEffect,
  useState,
} from "react";

export type User = {
  id: string;
  name: string;
  email: string;
  role: string;
};

type AuthContextType = {
  user: User | null;
  login: (user: User) => void;
  logout: () => void;
  isAuthenticated: boolean;
};

const AuthContext =
  createContext<AuthContextType | null>(
    null
  );

export function AuthProvider({
  children,
}: {
  children: React.ReactNode;
}) {
  const [user, setUser] =
    useState<User | null>(null);

  useEffect(() => {
    const savedUser =
      localStorage.getItem("currentUser");

    if (!savedUser) {
      return;
    }

    try {
      const parsedUser =
        JSON.parse(savedUser) as User;

      if (
        !parsedUser.id ||
        !parsedUser.name ||
        !parsedUser.email ||
        !parsedUser.role
      ) {
        localStorage.removeItem(
          "currentUser"
        );

        return;
      }

      setUser(parsedUser);
    } catch (error) {
      console.error(
        "Unable to restore authenticated user:",
        error
      );

      localStorage.removeItem(
        "currentUser"
      );
    }
  }, []);

  const login = (authenticatedUser: User) => {
    localStorage.setItem(
      "currentUser",
      JSON.stringify(authenticatedUser)
    );

    setUser(authenticatedUser);
  };

  const logout = () => {
    localStorage.removeItem(
      "currentUser"
    );

    setUser(null);
  };

  return (
    <AuthContext.Provider
      value={{
        user,
        login,
        logout,
        isAuthenticated: Boolean(user),
      }}
    >
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const context = useContext(AuthContext);

  if (!context) {
    throw new Error(
      "useAuth must be used inside AuthProvider."
    );
  }

  return context;
}