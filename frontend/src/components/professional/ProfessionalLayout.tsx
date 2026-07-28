import { Outlet } from "react-router-dom";

import ProfessionalSidebar from "./ProfessionalSidebar";
import ProfessionalTopbar from "./ProfessionalTopbar";
import AIChatbot from "../AIChatbot";

function ProfessionalLayout() {
  return (
    <div className="flex min-h-screen bg-slate-100">

      <ProfessionalSidebar />

      <div className="ml-72 flex-1">

        <ProfessionalTopbar />

        <main className="p-8">

          <Outlet />

        </main>

      </div>

      <AIChatbot />
    </div>
  );
}

export default ProfessionalLayout;