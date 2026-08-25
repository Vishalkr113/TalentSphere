import { Navigate } from "react-router-dom";
import type { ReactNode } from "react";

import { useAuth } from "../contexts/AuthContext";
import type { UserRole } from "../services/authService";


interface ProtectedRouteProps {

  children: ReactNode;

  allowedRoles?: UserRole[];

}


function ProtectedRoute({

  children,

  allowedRoles,

}: ProtectedRouteProps) {


  const {
    user,
    loading,
  } = useAuth();



  if (loading) {

    return (
      <div className="flex min-h-screen items-center justify-center">

        <p className="text-slate-600">
          Loading...
        </p>

      </div>
    );

  }


  if (!user) {
    return (
      <Navigate
        to="/"
        replace
      />
    );
  }


  if (
    allowedRoles &&
    !allowedRoles.includes(user.role)
  ) {

    return (
      <Navigate
        to={`/${user.role}/dashboard`}
        replace
      />
    );

  }



  return (
    <>
      {children}
    </>
  );

}


export default ProtectedRoute;