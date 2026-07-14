export type HighSchoolClass =
    | "10"
    | "11"
    | "12";

export type SchoolBoard = string;

export type HighSchoolStream =
    | "Science - PCM"
    | "Science - PCB"
    | "Science - PCMB"
    | "Commerce with Mathematics"
    | "Commerce without Mathematics"
    | "Humanities / Arts";

export interface HighSchoolProfile {
    id: string;
    userId: string;
    fullName: string;
    email: string;
    studentClass: HighSchoolClass;
    board: SchoolBoard;
    currentStream: HighSchoolStream | null;
    careerGoal: string;
    schoolName: string;
    city: string;
    state?: string;
    district?: string;
    profilePhoto?: string | null;
    createdAt: string;
    updatedAt: string;
}

export type HighSchoolProfileInput = {
    userId: string;
    fullName: string;
    email: string;
    studentClass: HighSchoolClass;
    board: SchoolBoard;
    currentStream: HighSchoolStream | null;
    careerGoal: string;
    schoolName: string;
    city: string;
    state?: string;
    district?: string;
    profilePhoto?: string | null;
};

const STORAGE_KEY =
    "talentsphere_high_school_profiles";

function getAllProfiles(): HighSchoolProfile[] {
    const storedProfiles =
        localStorage.getItem(STORAGE_KEY);

    if (!storedProfiles) {
        return [];
    }

    try {
        const parsedProfiles =
            JSON.parse(storedProfiles);

        if (!Array.isArray(parsedProfiles)) {
            return [];
        }

        return parsedProfiles;
    } catch {
        return [];
    }
}

function saveAllProfiles(
    profiles: HighSchoolProfile[]
) {
    localStorage.setItem(
        STORAGE_KEY,
        JSON.stringify(profiles)
    );
}

export function getHighSchoolProfile(
    userId: string
): HighSchoolProfile | null {
    const profiles = getAllProfiles();

    return (
        profiles.find(
            (profile) =>
                profile.userId === userId
        ) ?? null
    );
}

export function saveHighSchoolProfile(
    input: HighSchoolProfileInput
): HighSchoolProfile {
    const profiles = getAllProfiles();

    const existingProfileIndex =
        profiles.findIndex(
            (profile) =>
                profile.userId === input.userId
        );

    const now = new Date().toISOString();

    if (existingProfileIndex >= 0) {
        const existingProfile =
            profiles[existingProfileIndex];

        const updatedProfile: HighSchoolProfile = {
            ...existingProfile,
            ...input,
            id: existingProfile.id,
            createdAt: existingProfile.createdAt,
            updatedAt: now,
        };

        profiles[existingProfileIndex] =
            updatedProfile;

        saveAllProfiles(profiles);

        return updatedProfile;
    }

    const newProfile: HighSchoolProfile = {
        id: crypto.randomUUID(),
        ...input,
        createdAt: now,
        updatedAt: now,
    };

    profiles.push(newProfile);

    saveAllProfiles(profiles);

    return newProfile;
}

export function getAssessmentPurpose(
    studentClass: HighSchoolClass
) {
    switch (studentClass) {
        case "10":
            return {
                title:
                    "Stream Guidance Assessment",
                description:
                    "Discover the most suitable academic stream based on your subject strengths, aptitude and reasoning ability.",
                reportTitle:
                    "Final Stream Guidance Report",
            };

        case "11":
            return {
                title:
                    "Stream Fit & Academic Direction Assessment",
                description:
                    "Evaluate how well your current stream matches your academic strengths and identify suitable future directions.",
                reportTitle:
                    "Stream Fit & Direction Report",
            };

        case "12":
            return {
                title:
                    "Post-12th Course & Career Guidance Assessment",
                description:
                    "Analyze your academic strengths and identify suitable courses and career directions after Class 12.",
                reportTitle:
                    "Post-12th Course & Career Guidance Report",
            };
    }
}

export function isStreamRequired(
    studentClass: HighSchoolClass
) {
    return (
        studentClass === "11" ||
        studentClass === "12"
    );
}

export function calculateProfileCompletion(
    profile: HighSchoolProfile | null
) {
    if (!profile) {
        return 0;
    }

    const requiredValues = [
        profile.fullName,
        profile.email,
        profile.studentClass,
        profile.board,
        profile.schoolName,
        profile.city,
        profile.state ?? "",
        profile.district ?? "",
    ];

    if (
        isStreamRequired(profile.studentClass)
    ) {
        requiredValues.push(
            profile.currentStream ?? ""
        );
    }

    const completedFields =
        requiredValues.filter(
            (value) => value.trim().length > 0
        ).length;

    return Math.round(
        (completedFields /
            requiredValues.length) *
        100
    );
}