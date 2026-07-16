import type { ReactNode } from "react";
import { Navigate, useLocation } from "react-router-dom";
import { useAuth } from "../contexts/AuthContext";

type Props = { children: ReactNode };
const roles = ["high-school-student", "college-student", "working-professional"];
export default function ProtectedRoute({ children }: Props) {
  const { isAuthenticated, user } = useAuth();
  const location = useLocation();
  const requestedRole = location.pathname.split("/")[1];
  if (!isAuthenticated) return <Navigate to={roles.includes(requestedRole) ? `/${requestedRole}/login` : "/"} replace />;
  if (roles.includes(requestedRole) && user?.role !== requestedRole) return <Navigate to={`/${user?.role}/dashboard`} replace />;
  return children;
}
