import type { SelectOption } from "../components/common/Select/SearchSelect";

export interface ParentDetails {
  parentName: string;
  parentMobile: string;
  parentEmail: string;
  occupation: string;
}

export interface Address {
  country: string;
  state: string;
  district: string;
  city: string;
  pinCode: string;
}

export interface HighSchoolProfile {
  profileImage: string | null;

  fullName: string;
  email: string;
  mobile: string;

  dob: string;
  gender: SelectOption | null;
  bloodGroup: SelectOption | null;

  school: string;
  class: SelectOption | null;
  board: SelectOption | null;
  medium: string;
  rollNumber: string;
  admissionYear: string;
  percentage: string;

  parent: ParentDetails;

  address: Address;

  careerGoal: SelectOption | null;
  stream: SelectOption | null;
  favoriteSubject: SelectOption | null;
  weakSubject: SelectOption | null;

  skills: SelectOption[];
  hobbies: SelectOption[];
  languages: SelectOption[];

  lastUpdated: string;
}