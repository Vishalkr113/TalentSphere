export type CollegeQuestion={id:string;question:string;options:string[];answer:number;skill:string;topic:string};
export type AssessmentAttempt={id:string;userId:string;category:string;degree:string;branch:string;semester:string;targetRole:string;score:number;total:number;percentage:number;skillScores:Record<string,number>;topicScores:Record<string,number>;completedAt:string};
