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

import ProtectedRoute from "./components/ProtectedRoute";

 {/* import CollegeLayout from "./components/college/CollegeLayout";
import CollegeDashboard from "./components/college/CollegeDashboard";
import CollegeProfile from "./components/college/CollegeProfile";
import ResumeAnalyzer from "./components/college/ResumeAnalyzer";
import ResumeBuilder from "./components/college/ResumeBuilder";
import SkillAssessment from "./components/college/SkillAssessment";
import CodingAssessment from "./components/college/CodingAssessment";
import MockInterview from "./components/college/MockInterview";
import CareerRecommendation from "./components/college/CareerRecommendation";
import CollegeLearningRoadmap from "./components/college/LearningRoadmap";
import Certificates from "./components/college/Certificates";
import JobsInternships from "./components/college/JobsInternships";
import PlacementPreparation from "./components/college/PlacementPreparation";
import CollegeAchievements from "./components/college/Achievements"; */}


{/*import ProfessionalLayout from "./components/professional/ProfessionalLayout";
import ProfessionalDashboard from "./components/professional/ProfessionalDashboard";
import ProfessionalProfile from "./components/professional/ProfessionalProfile";
import CareerGrowth from "./components/professional/CareerGrowth";
import SkillUpgrade from "./components/professional/SkillUpgrade";
import ResumeManager from "./components/professional/ResumeManager";
import InterviewPreparation from "./components/professional/InterviewPreparation";
import JobSwitch from "./components/professional/JobSwitch";
import SalaryInsights from "./components/professional/SalaryInsights";
import LearningHub from "./components/professional/LearningHub";
import ProfessionalCertificates from "./components/professional/Certificates";
import ProfessionalAchievements from "./components/professional/Achievements"; */}

import Settings from "./components/common/Settings";

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
      <div className="flex min-h-screen items-center justify-center text-3xl font-bold">
        College Students Dashboard Coming Soon...
      </div>
      </ProtectedRoute>
  }
    />

      {/* College Student 
      <Route
        path="/college-student/login"
        element={<Login />}
      />

      <Route
        path="/college-student/register"
        element={<Register />}
      />

      <Route
        path="/college-student"
        element={
          <ProtectedRoute>
            <CollegeLayout />
          </ProtectedRoute>
        }
      >
        <Route
          index
          element={<Navigate to="dashboard" replace />}
        />

        <Route
          path="dashboard"
          element={<CollegeDashboard />}
        />

        <Route
          path="profile"
          element={<CollegeProfile />}
        />

        <Route
          path="resume-builder"
          element={<ResumeBuilder />}
        />

        <Route
          path="resume-analyzer"
          element={<ResumeAnalyzer />}
        />

        <Route
          path="skill-assessment"
          element={<SkillAssessment />}
        />

        <Route
          path="coding-assessment"
          element={<CodingAssessment />}
        />

        <Route
          path="mock-interview"
          element={<MockInterview />}
        />

        <Route
          path="career-recommendation"
          element={<CareerRecommendation />}
        />

        <Route
          path="learning-roadmap"
          element={<CollegeLearningRoadmap />}
        />

        <Route
          path="certificates"
          element={<Certificates />}
        />

        <Route
          path="jobs"
          element={<JobsInternships />}
        />

        <Route
          path="placement-preparation"
          element={<PlacementPreparation />}
        />

        <Route
          path="achievements"
          element={<CollegeAchievements />}
        />

        <Route
          path="settings"
          element={<Settings />}
        />  
        </route> 
                       */}


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
      <div className="flex min-h-screen items-center justify-center text-3xl font-bold">
         Working Professional Dashboard Coming Soon...
      </div>
      </ProtectedRoute>
  }
    />

    {/* Working Professional

<Route
  path="/working-professional/login"
  element={<Login />}
/>

<Route
  path="/working-professional/register"
  element={<Register />}
/>

<Route
  path="/working-professional"
  element={
    <ProtectedRoute>
      <ProfessionalLayout />
    </ProtectedRoute>
  }
>
  <Route
    index
    element={<Navigate to="dashboard" replace />}
  />

  <Route
    path="dashboard"
    element={<ProfessionalDashboard />}
  />

  <Route
    path="profile"
    element={<ProfessionalProfile />}
  />

  <Route
    path="career-growth"
    element={<CareerGrowth />}
  />

  <Route
    path="skill-upgrade"
    element={<SkillUpgrade />}
  />

  <Route
    path="resume-manager"
    element={<ResumeManager />}
  />

  <Route
    path="interview-preparation"
    element={<InterviewPreparation />}
  />

  <Route
    path="job-switch"
    element={<JobSwitch />}
  />

  <Route
    path="salary-insights"
    element={<SalaryInsights />}
  />

  <Route
    path="learning-hub"
    element={<LearningHub />}
  />

  <Route
    path="certificates"
    element={<ProfessionalCertificates />}
  />

  <Route
    path="achievements"
    element={<ProfessionalAchievements />}
  />

  <Route
    path="settings"
    element={<Settings />}
  />
</Route>    */}


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