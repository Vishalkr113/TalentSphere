import { getAssessmentHistory, getAssessmentResult, type AssessmentResult } from "./assessmentService";

export interface SkillScore { skill: string; percentage: number; }
export interface StreamScore { stream: string; score: number; rank: number; fitLevel: string; reason: string; strengths: string[]; concerns: string[]; }
export interface StreamGuidanceResult { ready:boolean; recommendedStream:string; recommendationScore:number; confidenceLevel:string; improvementSkills:SkillScore[]; strongestSkills:SkillScore[]; streamScores:StreamScore[]; completedAssessments:number; requiredAssessments:number; summary:string; nextSteps:string[]; recommendationReason:string; results:AssessmentResult[]; }

export async function loadFinalStreamGuidance(): Promise<StreamGuidanceResult> {
  const history = await getAssessmentHistory();
  const done = history.filter(x=>x.status==="completed");
  const results = (await Promise.all(done.slice(0,50).map(x=>getAssessmentResult(x.id)))).filter(Boolean);
  const latest = new Map<string,AssessmentResult>();
  for(const r of results) if(!latest.has(r.assessment_type)) latest.set(r.assessment_type,r);
  const values=[...latest.values()];
  if(!values.length) return {ready:false,recommendedStream:"",recommendationScore:0,confidenceLevel:"Low",improvementSkills:[],strongestSkills:[],streamScores:[],completedAssessments:0,requiredAssessments:1,summary:"Complete at least one assessment to generate evidence-based guidance.",nextSteps:["Choose an assessment from the Assessment Center","Review your result after submission"],recommendationReason:"Guidance is generated from your latest saved assessment results.",results:[]};

  const by=(types:string[])=>values.filter(r=>types.includes(r.assessment_type));
  const streamDefs:[string,string[],string][]=[
    ["Science",["high_school_pcm","high_school_pcb"],"Strong academic performance in science-oriented assessments."],
    ["Commerce",["high_school_commerce"],"Strong performance in commerce-oriented assessment."],
    ["Arts / Humanities",["high_school_arts"],"Strong performance in humanities-oriented assessment."],
  ];
  const scores=streamDefs.map(([name,types,reason])=>{const rs=by(types);const score=rs.length?Math.round(rs.reduce((a,r)=>a+r.percentage,0)/rs.length):0;return {stream:name,score,rank:0,fitLevel:score>=80?"Strong Fit":score>=65?"Good Fit":score?"Developing":"Not assessed",reason,strengths:rs.flatMap(r=>r.strengths).slice(0,4),concerns:rs.flatMap(r=>r.weaknesses).slice(0,3)};}).filter(x=>x.score>0).sort((a,b)=>b.score-a.score).map((x,i)=>({...x,rank:i+1}));
  const fallback=values.reduce((a,r)=>a+r.percentage,0)/values.length;
  const top=scores[0];
  const strong=values.flatMap(r=>r.strengths).slice(0,6).map(skill=>({skill,percentage:Math.round(fallback)}));
  const weak=values.flatMap(r=>r.weaknesses).slice(0,6).map(skill=>({skill,percentage:Math.max(0,Math.round(fallback-20))}));
  return {ready:true,recommendedStream:top?.stream??"Evidence-based exploration",recommendationScore:top?.score??Math.round(fallback),confidenceLevel:values.length>=3?"High":values.length>=2?"Medium":"Early",improvementSkills:weak,strongestSkills:strong,streamScores:scores,completedAssessments:values.length,requiredAssessments:1,summary:`Guidance is based on ${values.length} completed assessment type${values.length===1?"":"s"}.`,nextSteps:["Review your strongest and weakest areas","Take another relevant assessment to improve confidence","Use the results to plan your next learning step"],recommendationReason:"Only completed, latest results are used. No fixed five-assessment requirement is applied.",results:values};
}

// Kept for legacy consumers. It intentionally does not invent results; callers that need authoritative guidance should use loadFinalStreamGuidance().
export function generateFinalStreamGuidance(_userId?: string): StreamGuidanceResult { return {ready:false,recommendedStream:"",recommendationScore:0,confidenceLevel:"Low",improvementSkills:[],strongestSkills:[],streamScores:[],completedAssessments:0,requiredAssessments:1,summary:"Load the latest saved assessment results to generate guidance.",nextSteps:["Complete an assessment"],recommendationReason:"Backend assessment results are authoritative.",results:[]}; }
