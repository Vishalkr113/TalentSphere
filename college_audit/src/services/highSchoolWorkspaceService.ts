export type AssignmentStatus = "Pending" | "In Progress" | "Completed";
export type Assignment = { id:string; subject:string; title:string; dueDate:string; status:AssignmentStatus; notes:string };
export type Exam = { id:string; subject:string; title:string; date:string; time:string; room:string };
export type DailyGoalItem = { id:string; title:string; minutes:number; completed:boolean; date:string };
export type CareerVisit = { career:string; visitedAt:string };

const key=(userId:string,name:string)=>`talentsphere_hs_${name}_${userId}`;
const read=<T>(k:string,fallback:T):T=>{try{return JSON.parse(localStorage.getItem(k)||"") as T}catch{return fallback}};
const write=<T>(k:string,value:T)=>{localStorage.setItem(k,JSON.stringify(value)); window.dispatchEvent(new Event("talentsphere-hs-data"));};

export const getAssignments=(u:string)=>read<Assignment[]>(key(u,"assignments"),[]);
export const saveAssignments=(u:string,v:Assignment[])=>write(key(u,"assignments"),v);
export const getExams=(u:string)=>read<Exam[]>(key(u,"exams"),[]);
export const saveExams=(u:string,v:Exam[])=>write(key(u,"exams"),v);
export const getGoals=(u:string)=>read<DailyGoalItem[]>(key(u,"goals"),[]);
export const saveGoals=(u:string,v:DailyGoalItem[])=>write(key(u,"goals"),v);
export const getCareerVisits=(u:string)=>read<CareerVisit[]>(key(u,"career_visits"),[]);
export const markCareerVisited=(u:string,career:string)=>{
 const visits=getCareerVisits(u); if(!visits.some(v=>v.career===career)) visits.push({career,visitedAt:new Date().toISOString()});
 write(key(u,"career_visits"),visits); return visits;
};
export const getRoadmapCompleted=(u:string)=>read<string[]>(key(u,"roadmap"),[]);
export const saveRoadmapCompleted=(u:string,v:string[])=>write(key(u,"roadmap"),v);
export const getSubjectProgress=(u:string)=>read<Record<string,number>>(key(u,"subject_progress"),{});
export const saveSubjectProgress=(u:string,v:Record<string,number>)=>write(key(u,"subject_progress"),v);
export const todayKey=()=>new Date().toISOString().slice(0,10);

export function calculateWorkspaceStats(userId:string){
 const assignments=getAssignments(userId);
 const exams=getExams(userId);
 const goals=getGoals(userId).filter(g=>g.date===todayKey());
 const roadmap=getRoadmapCompleted(userId);
 const careers=getCareerVisits(userId);
 const subjectProgress=getSubjectProgress(userId);
 const completedAssignments=assignments.filter(a=>a.status==="Completed").length;
 const completedGoals=goals.filter(g=>g.completed).length;
 const progressValues=Object.values(subjectProgress);
 const subjectAverage=progressValues.length?Math.round(progressValues.reduce((a,b)=>a+b,0)/progressValues.length):0;
 const goalPercent=goals.length?Math.round(completedGoals/goals.length*100):0;
 const assignmentPercent=assignments.length?Math.round(completedAssignments/assignments.length*100):0;
 const overall=Math.round((subjectAverage+goalPercent+assignmentPercent)/3);
 return {assignments,exams,goals,roadmap,careers,subjectProgress,completedAssignments,completedGoals,subjectAverage,goalPercent,assignmentPercent,overall};
}
