import type { ReactNode } from "react";
import {
  Navigate,
  useLocation,
} from "react-router-dom";

import { useAuth } from "../contexts/AuthContext";

type ProtectedRouteProps = {
  children: ReactNode;
};

function ProtectedRoute({
  children,
}: ProtectedRouteProps) {

  const {
    isAuthenticated,
  } = useAuth();

  const location =
    useLocation();

  if (!isAuthenticated) {

    const role = location.pathname.split("/")[1];

    const validRoles = [
      "high-school-student",
      "college-student",
      "working-professional",
    ];

    const loginRoute = validRoles.includes(role)
      ? `/${role}/login`
      : "/";

    return (
      <Navigate
        to={loginRoute}
        replace
      />
    );

  }

  return children;
}

export default ProtectedRoute;