export interface FinalCareerReport {

  profileCompletion: number;

  resumeScore: number;

  atsScore: number;

  assessmentScore: number;

  codingScore: number;

  interviewScore: number;

  placementScore: number;

  achievementScore: number;

  overallScore: number;

}

export function calculateOverallScore(report: Omit<FinalCareerReport, "overallScore">): number {

  const total =
    report.profileCompletion +
    report.resumeScore +
    report.atsScore +
    report.assessmentScore +
    report.codingScore +
    report.interviewScore +
    report.placementScore +
    report.achievementScore;

  return Math.round(total / 8);

}