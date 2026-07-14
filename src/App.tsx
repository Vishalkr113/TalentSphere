import {
  Navigate,
  Route,
  Routes,
} from "react-router-dom";

import Overview from "./components/Overview";
import PortalSelection from "./components/PortalSelection";

import Login from "./components/Login";
import SignUp from "./components/SignUp";
import ForgotPassword from "./components/ForgotPassword";

import HighSchoolLayout from "./components/high-school/HighSchoolLayout";
import HighSchoolDashboard from "./components/high-school/HighSchoolDashboard";
import HighSchoolProfile from "./components/high-school/HighSchoolProfile";
import Assessment from "./components/high-school/Assessment";
import AssessmentReports from "./components/high-school/AssessmentReports";
import SubjectGuidance from "./components/high-school/SubjectGuidance";
import CareerExplorer from "./components/high-school/CareerExplorer";
import LearningRoadmap from "./components/high-school/LearningRoadmap";
import AILearningSupport from "./components/high-school/AILearningSupport";
import AcademicProgress from "./components/high-school/AcademicProgress";
import UpcomingExams from "./components/high-school/UpcomingExams";
import Assignments from "./components/high-school/Assignments";
import DailyGoal from "./components/high-school/DailyGoal";
import Achievements from "./components/high-school/Achievements";
import FinalGuidanceReport from "./components/high-school/FinalGuidanceReport";

import ProtectedRoute from "./components/ProtectedRoute";
import Settings from "./components/common/Settings";

function App() {
  return (
    <Routes>
      {/* Landing Page */}
      <Route
        path="/"
        element={<Overview />}
      />

      {/* Category Selection */}
      <Route
        path="/portal"
        element={<PortalSelection />}
      />

      {/* High School Authentication */}
      <Route
        path="/high-school-student/login"
        element={<Login />}
      />

      <Route
        path="/high-school-student/signup"
        element={<SignUp />}
      />

      {/* High School Student Category */}
      <Route
        path="/high-school-student"
        element={
          <ProtectedRoute>
            <HighSchoolLayout />
          </ProtectedRoute>
        }
      >
        <Route
          index
          element={
            <Navigate
              to="dashboard"
              replace
            />
          }
        />

        <Route
          path="dashboard"
          element={<HighSchoolDashboard />}
        />

        <Route
          path="profile"
          element={<HighSchoolProfile />}
        />

        <Route
          path="subject-guidance"
          element={<SubjectGuidance />}
        />

        <Route
          path="assessment"
          element={<Assessment />}
        />

        <Route
          path="assessment-reports"
          element={<AssessmentReports />}
        />

        <Route
          path="career-explorer"
          element={<CareerExplorer />}
        />

        <Route
          path="learning-roadmap"
          element={<LearningRoadmap />}
        />

        <Route
          path="ai-learning-support"
          element={<AILearningSupport />}
        />

        <Route
          path="academic-progress"
          element={<AcademicProgress />}
        />

        <Route
          path="upcoming-exams"
          element={<UpcomingExams />}
        />

        <Route
          path="assignments"
          element={<Assignments />}
        />

        <Route
          path="daily-goal"
          element={<DailyGoal />}
        />

        <Route
          path="achievements"
          element={<Achievements />}
        />

        <Route
          path="final-guidance"
          element={<FinalGuidanceReport />}
        />

        <Route
          path="settings"
          element={<Settings />}
        />
      </Route>

      {/* College Student Authentication */}
      <Route
        path="/college-student/login"
        element={<Login />}
      />

      <Route
        path="/college-student/signup"
        element={<SignUp />}
      />

      {/* College Student Dashboard */}
      <Route
        path="/college-student/dashboard"
        element={
          <ProtectedRoute>
            <div className="flex min-h-screen items-center justify-center text-3xl font-bold">
              College Students Dashboard Coming Soon...
            </div>
          </ProtectedRoute>
        }
      />

      {/* Working Professional Authentication */}
      <Route
        path="/working-professional/login"
        element={<Login />}
      />

      <Route
        path="/working-professional/signup"
        element={<SignUp />}
      />

      {/* Working Professional Dashboard */}
      <Route
        path="/working-professional/dashboard"
        element={
          <ProtectedRoute>
            <div className="flex min-h-screen items-center justify-center text-3xl font-bold">
              Working Professional Dashboard Coming Soon...
            </div>
          </ProtectedRoute>
        }
      />

      {/* Forgot Password */}
      <Route
        path="/forgot-password"
        element={<ForgotPassword />}
      />

      {/* Invalid Route */}
      <Route
        path="*"
        element={
          <Navigate
            to="/"
            replace
          />
        }
      />
    </Routes>
  );
}

export default App;