import { useNavigate } from "react-router-dom";
import { LogOut } from "lucide-react";

import Button from "./ui/Button";
import { useAuth } from "../contexts/AuthContext";

function LogoutButton() {
  const navigate = useNavigate();

  const { logout } = useAuth();

  const handleLogout = () => {
    logout();

    navigate("/", {
      replace: true,
    });
  };

  return (
    <Button
      onClick={handleLogout}
      className="w-full bg-red-600 hover:bg-red-700"
    >
      <LogOut size={18} />
      Logout
    </Button>
  );
}

export default LogoutButton;