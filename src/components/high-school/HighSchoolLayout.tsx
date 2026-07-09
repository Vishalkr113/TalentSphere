import { Outlet } from "react-router-dom";

import HighSchoolSidebar from "./HighSchoolSidebar";
import HighSchoolTopbar from "./HighSchoolTopbar";

function HighSchoolLayout() {
  return (
    <div className="flex min-h-screen bg-slate-100">

      <HighSchoolSidebar />

      <div className="ml-72 flex-1">

        <HighSchoolTopbar />

        <main className="p-8">

          <Outlet />

        </main>

      </div>

    </div>
  );
}

export default HighSchoolLayout;