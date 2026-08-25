import { useEffect, useState } from "react";
import { Outlet } from "react-router-dom";
import { Menu } from "lucide-react";

import HighSchoolSidebar from "./HighSchoolSidebar";
import HighSchoolTopbar from "./HighSchoolTopbar";
import AIChatbot from "../AIChatbot";

function HighSchoolLayout() {
  const [isSidebarOpen, setIsSidebarOpen] = useState(false);

  useEffect(() => {
    document.documentElement.classList.remove("dark");
  }, []);

  const openSidebar = () => {
    setIsSidebarOpen(true);
  };

  const closeSidebar = () => {
    setIsSidebarOpen(false);
  };

  return (
    <div className="min-h-screen overflow-x-hidden bg-slate-100 text-[14px]">
      {/* Mobile / Tablet Sidebar Overlay */}

      {isSidebarOpen && (
        <button
          type="button"
          aria-label="Close sidebar overlay"
          onClick={closeSidebar}
          className="fixed inset-0 z-40 bg-slate-950/50 lg:hidden"
        />
      )}

      {/* Sidebar */}

      <HighSchoolSidebar
        isOpen={isSidebarOpen}
        onClose={closeSidebar}
      />

      {/* Main Application Area */}

      <div className="min-w-0 lg:ml-64">
        {/* Mobile / Tablet Navigation Bar */}

        <div className="sticky top-0 z-30 flex h-16 items-center border-b border-slate-200 bg-white px-4 lg:hidden">
          <button
            type="button"
            onClick={openSidebar}
            aria-label="Open sidebar"
            className="flex h-10 w-10 items-center justify-center rounded-xl border border-slate-200 text-slate-700 transition hover:bg-slate-100"
          >
            <Menu size={22} />
          </button>

          <div className="ml-3 min-w-0">
            <p className="truncate text-base font-bold text-slate-900">
              TalentSphere
            </p>

            <p className="truncate text-xs text-slate-500">
              High School Portal
            </p>
          </div>
        </div>

        {/* Desktop Topbar */}

        <HighSchoolTopbar />

        {/* Page Content */}

        <main className="w-full min-w-0 px-3 py-4 sm:px-4 sm:py-5 md:px-5 lg:px-6">
          <div className="mx-auto w-full max-w-[1440px]">
            <Outlet />
          </div>
        </main>
      </div>

      <AIChatbot />
    </div>
  );
}

export default HighSchoolLayout;