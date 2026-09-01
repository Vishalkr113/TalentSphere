# TalentSphere

## AI-Based Student Skill Assessment and Career Recommendation System

TalentSphere is a full-stack career development platform designed to assess skills, identify strengths and skill gaps, and provide personalized career guidance for High School Students, College Students, and Working Professionals.

The platform combines structured assessments, profile information, career intelligence, learning recommendations, interview preparation, resume readiness, and progress tracking into a single system.

---

## Project Overview

Students and professionals often have skills and interests but may not know their actual strengths, weaknesses, suitable career paths, or the skills they need to develop next.

TalentSphere addresses this problem by creating a structured profile for each user and combining profile information with assessment performance and career-related data.

The platform provides:

- Stage-specific assessments
- Skill and aptitude evaluation
- Career recommendations
- Skill-gap identification
- Learning roadmap
- Resume and profile readiness
- Interview preparation
- Career progress tracking
- Assessment reports
- Final career reports

---

## User Stages

TalentSphere supports three primary user stages.

### 1. High School Student

Designed for students who are exploring academic streams and future career options.

Supported areas include:

- Foundation Assessment
- Science and stream-specific assessments
- Commerce
- Arts and Humanities
- Aptitude
- Logical Reasoning
- Career Exploration
- Learning Progress
- Achievements
- Assessment Reports
- Final Guidance

### 2. College Student

Designed for undergraduate students preparing for skills development, internships, placements, and career opportunities.

Supported areas include:

- Common Assessment
- Aptitude
- Coding
- DSA
- Technical Assessment
- Career Assessment
- Skill Gap Analysis
- Career Guidance
- Learning Roadmap
- Resume
- Interview Preparation
- Assessment Reports
- Final Career Report

### 3. Working Professional

Designed for professionals who want to improve their skills, prepare for career growth, or transition to new roles.

Supported areas include:

- Common Assessment
- Technical Assessment
- DSA
- Situational Assessment
- Skill Growth
- Promotion Readiness
- Career Growth
- Interview Preparation
- Job Switch Preparation
- Resume and Profile Readiness
- Assessment Reports
- Final Career Report

---

## Core Features

### Authentication

- User registration
- Email verification
- OTP-based verification
- Login
- Password reset
- Role-based user experience

### Profile Management

Users can maintain stage-specific profile information including:

- Personal information
- Academic information
- Professional information
- Skills
- Career goals
- Target role
- Profile photo
- Resume

### Assessment System

TalentSphere uses a centralized question-bank architecture.

Each individual assessment attempt is designed around a fixed set of questions.

The assessment system supports:

- Random question selection
- Active question filtering
- Assessment-specific question banks
- Question validation
- Difficulty metadata
- Topic and skill metadata
- Answer evaluation
- Score calculation
- Assessment history
- Result generation

### Career Intelligence

The platform uses assessment and profile information to support:

- Career recommendations
- Strength identification
- Skill-gap identification
- Learning recommendations
- Career readiness
- Career progression

### Assessment Reports

Users can review:

- Assessment score
- Percentage
- Correct answers
- Total questions
- Grade
- Strengths
- Improvement areas
- Assessment history

### Interview Preparation

Working professionals can use structured interview preparation and evidence-based evaluation.

The interview evidence system supports explicit evidence levels and prevents unrelated page interactions from modifying the evaluation.

### Resume and Career Readiness

The platform considers profile and resume readiness as part of the broader career-development workflow.

---

## Question Bank Architecture

TalentSphere uses a centralized assessment question-bank system.

The question banks are organized according to user stage and assessment purpose.

### High School Question Banks

- Common/Foundation
- PCM
- PCB
- Commerce
- Arts

### College Question Banks

- Common
- Aptitude
- Coding
- DSA
- Technical
- Career

### Working Professional Question Banks

- Common
- Technical
- DSA
- Situational

### Shared Question Banks

The system also contains shared assessment banks for areas such as:

- Aptitude
- Logical Reasoning
- Coding
- DSA

DSA is designed as a language-neutral problem-solving assessment rather than separate Python, Java, C++, or JavaScript assessments.

---

## Question Metadata

Assessment questions support structured metadata such as:

- Question code
- Question text
- Options
- Correct answer
- Explanation
- Difficulty
- Category
- Skill
- Topic
- Sub-topic
- User role
- Student class
- Stream
- Degree
- Branch
- Experience level
- Domain
- Question type
- Language

This structure allows the application to select and manage questions according to assessment context.

---

## Assessment Flow

The general assessment workflow is:

```text
User Profile
     |
     v
Assessment Selection
     |
     v
Question Selection
     |
     v
Randomized Question Set
     |
     v
User Answers
     |
     v
Answer Evaluation
     |
     v
Score Calculation
     |
     v
Assessment Result
     |
     v
Assessment Report
     |
     v
Career Intelligence
     |
     v
Learning and Career Recommendations