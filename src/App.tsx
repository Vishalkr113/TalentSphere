import {
  Navigate,
  Route,
  Routes,
} from "react-router-dom";

import Overview from "./components/Overview";

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
import CollegeLayout from "./components/college/CollegeLayout";
import CollegeDashboard from "./components/college/CollegeDashboard";
import CollegeProfile from "./components/college/CollegeProfile";
import CollegeAssessment from "./components/college/SkillAssessment";
import CollegeAssessmentReports from "./components/college/AssessmentReports";
import SkillGapAnalysis from "./components/college/SkillGapAnalysis";
import CollegeCareerGuidance from "./components/college/CareerRecommendation";
import CollegeRoadmap from "./components/college/LearningRoadmap";
import ResumeBuilder from "./components/college/ResumeBuilder";
import ResumeAnalyzer from "./components/college/ResumeAnalyzer";
import CollegePractice from "./components/college/CodingAssessment";
import MockInterview from "./components/college/MockInterview";
import PlacementPreparation from "./components/college/PlacementPreparation";
import PlacementTracker from "./components/college/PlacementTracker";
import CollegeAchievements from "./components/college/Achievements";
import ProfessionalLayout from "./components/professional/ProfessionalLayout";
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
import ProfessionalAchievements from "./components/professional/Achievements";
import JobsInternships from "./components/college/JobsInternships";



function App() {
  return (
    <Routes>
      {/* Landing Page */}
      <Route
        path="/"
        element={<Overview />}
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

      {/* College Student Portal */}
      <Route path="/college-student" element={<ProtectedRoute><CollegeLayout /></ProtectedRoute>}>
        <Route index element={<Navigate to="dashboard" replace />} />
        <Route path="dashboard" element={<CollegeDashboard />} />
        <Route path="profile" element={<CollegeProfile />} />
        <Route path="assessment" element={<CollegeAssessment />} />
        <Route path="assessment-reports" element={<CollegeAssessmentReports />} />
        <Route path="skill-gap" element={<SkillGapAnalysis />} />
        <Route path="career-guidance" element={<CollegeCareerGuidance />} />
        <Route path="learning-roadmap" element={<CollegeRoadmap />} />
        <Route path="resume-builder" element={<ResumeBuilder />} />
        <Route path="resume-analyzer" element={<ResumeAnalyzer />} />
        <Route path="practice" element={<CollegePractice />} />
        <Route path="mock-interview" element={<MockInterview />} />
        <Route path="placement-readiness" element={<PlacementPreparation />} />
        <Route path="placement-tracker" element={<PlacementTracker />} />
        <Route path="jobs-internships" element={<JobsInternships />} />
        <Route path="achievements" element={<CollegeAchievements />} />
        <Route path="settings" element={<Settings />} />
      </Route>

      {/* Working Professional Authentication */}
      <Route
        path="/working-professional/login"
        element={<Login />}
      />

      <Route
        path="/working-professional/signup"
        element={<SignUp />}
      />

      {/* Working Professional Portal */}
      <Route path="/working-professional" element={<ProtectedRoute><ProfessionalLayout /></ProtectedRoute>}>
        <Route index element={<Navigate to="dashboard" replace />} />
        <Route path="dashboard" element={<ProfessionalDashboard />} />
        <Route path="profile" element={<ProfessionalProfile />} />
        <Route path="career-growth" element={<CareerGrowth />} />
        <Route path="skill-assessment" element={<SkillUpgrade />} />
        <Route path="skill-upgrade" element={<SkillUpgrade />} />
        <Route path="resume-manager" element={<ResumeManager />} />
        <Route path="interview-preparation" element={<InterviewPreparation />} />
        <Route path="job-switch" element={<JobSwitch />} />
        <Route path="salary-insights" element={<SalaryInsights />} />
        <Route path="learning-hub" element={<LearningHub />} />
        <Route path="certificates" element={<ProfessionalCertificates />} />
        <Route path="achievements" element={<ProfessionalAchievements />} />
        <Route path="settings" element={<Settings />} />
      </Route>

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