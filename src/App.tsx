import { Routes, Route } from "react-router-dom";

import Overview from "./components/Overview";
import Login from "./components/Login";
import Register from "./components/Register";
import ForgotPassword from "./components/ForgotPassword";

import StudentDashboard from "./components/StudentDashboard";
import InstituteDashboard from "./components/InstituteDashboard";
import ProfessionalDashboard from "./components/ProfessionalDashboard";

function App() {
  return (
    <Routes>

      <Route
        path="/"
        element={<Overview />}
      />

      <Route
        path="/login"
        element={<Login />}
      />

      <Route
        path="/register"
        element={<Register />}
      />

      <Route
        path="/forgot-password"
        element={<ForgotPassword />}
      />

      <Route
        path="/student/dashboard"
        element={<StudentDashboard />}
      />

      <Route
        path="/institute/dashboard"
        element={<InstituteDashboard />}
      />

      <Route
        path="/professional/dashboard"
        element={<ProfessionalDashboard />}
      />

    </Routes>
  );
}

export default App;