import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { BrowserRouter } from "react-router-dom";

import App from "./App";
import { AuthProvider } from "./contexts/AuthContext";

import "./index.css";

const navigationEntry =
  performance.getEntriesByType(
    "navigation"
  )[0] as PerformanceNavigationTiming | undefined;

const isPageReload =
  navigationEntry?.type === "reload";

if (
  isPageReload &&
  window.location.pathname !== "/"
) {
  window.history.replaceState(
    null,
    "",
    "/"
  );
}

createRoot(
  document.getElementById("root")!
).render(
  <StrictMode>
    <BrowserRouter>
      <AuthProvider>
        <App />
      </AuthProvider>
    </BrowserRouter>
  </StrictMode>
);