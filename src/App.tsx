import {
  Navigate,
  Route,
  Routes,
} from "react-router-dom";

import Overview from "./components/Overview";
import PortalSelection from "./components/PortalSelection";

import Login from "./components/Login";
import Register from "./components/Register";
import ForgotPassword from "./components/ForgotPassword";

function App() {
  return (
    <Routes>

      {/* Landing Page */}

      <Route
        path="/"
        element={<Overview />}
      />

      {/* Portal Selection */}

      <Route
        path="/portal"
        element={<PortalSelection />}
      />

      {/* Student */}

      <Route
        path="/student/login"
        element={<Login />}
      />

      <Route
        path="/student/register"
        element={<Register />}
      />

      {/* Institute */}

      <Route
        path="/institute/login"
        element={<Login />}
      />

      <Route
        path="/institute/register"
        element={<Register />}
      />

      {/* Professional */}

      <Route
        path="/professional/login"
        element={<Login />}
      />

      <Route
        path="/professional/register"
        element={<Register />}
      />

      {/* Forgot Password */}

      <Route
        path="/forgot-password"
        element={<ForgotPassword />}
      />

      {/* Invalid Route */}

      <Route
        path="*"
        element={<Navigate to="/" replace />}
      />

    </Routes>
  );
}

export default App;