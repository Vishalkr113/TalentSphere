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

import HighSchoolLayout from "./components/high-school/HighSchoolLayout";
import HighSchoolDashboard from "./components/high-school/HighSchoolDashboard";
import HighSchoolProfile from "./components/high-school/HighSchoolProfile";
import SubjectGuidance from "./components/high-school/SubjectGuidance";
import CareerExplorer from "./components/high-school/CareerExplorer";
import LearningRoadmap from "./components/high-school/LearningRoadmap";
import AILearningSupport from "./components/high-school/AILearningSupport";
import AcademicProgress from "./components/high-school/AcademicProgress";
import UpcomingExams from "./components/high-school/UpcomingExams";
import Assignments from "./components/high-school/Assignments";
import DailyGoal from "./components/high-school/DailyGoal";
import Achievements from "./components/high-school/Achievements";
import Settings from "./components/high-school/Settings";

import StudentDashboard from "./components/StudentDashboard";
import ProtectedRoute from "./components/ProtectedRoute";
import ProfessionalDashboard from "./components/ProfessionalDashboard";



import ResumeHome from "./components/ResumeHome";
import ResumeBuilder from "./components/ResumeBuilder";

import SkillAssessment from "./components/SkillAssessment";
import CodingAssessment from "./components/CodingAssessment";


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
      
      
{/* High School Student */}

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
    element={<Navigate to="dashboard" replace />}
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
    path="settings"
    element={<Settings />}
  />
</Route>

<Route
  path="/high-school-student/login"
  element={<Login />}
/>

<Route
  path="/high-school-student/register"
  element={<Register />}
/>

{/* College Student */}

<Route
  path="/college-student/login"
  element={<Login />}
/>

<Route
  path="/college-student/register"
  element={<Register />}
/>

<Route
  path="/college-student/dashboard"
  element={
    <ProtectedRoute>
      <StudentDashboard />
    </ProtectedRoute>
  }
/>

<Route
  path="/college-student/resume"
  element={
    <ProtectedRoute>
      <ResumeHome />
    </ProtectedRoute>
  }
/>

<Route
  path="/college-student/resume-builder"
  element={
    <ProtectedRoute>
      <ResumeBuilder />
    </ProtectedRoute>
  }
/>

<Route
  path="/college-student/skill-assessment"
  element={
    <ProtectedRoute>
      <SkillAssessment />
    </ProtectedRoute>
  }
/>

<Route
  path="/college-student/coding-assessment"
  element={
    <ProtectedRoute>
      <CodingAssessment />
    </ProtectedRoute>
  }
/>

{/* Working Professional */}

<Route
  path="/working-professional/login"
  element={<Login />}
/>

<Route
  path="/working-professional/register"
  element={<Register />}
/>

<Route
  path="/working-professional/dashboard"
  element={
    <ProtectedRoute>
      <ProfessionalDashboard />
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
        element={<Navigate to="/" replace />}
      />

    </Routes>
  );
}

export default App;