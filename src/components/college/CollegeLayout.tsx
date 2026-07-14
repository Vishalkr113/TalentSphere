import { Outlet } from "react-router-dom";

import CollegeSidebar from "./CollegeSidebar";
import CollegeTopbar from "./CollegeTopbar";
import AIChatbot from "../AIChatbot";

function CollegeLayout() {
  return (
    <div className="flex min-h-screen bg-slate-100">

      <CollegeSidebar />

      <div className="ml-72 flex-1">

        <CollegeTopbar />

        <main className="p-8">

          <Outlet />

        </main>

      </div>

      <AIChatbot />
    </div>
  );
}

export default CollegeLayout;