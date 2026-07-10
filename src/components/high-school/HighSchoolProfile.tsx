import { useEffect, useState } from "react";

import { useAuth } from "../../contexts/AuthContext";

import ProfileView from "../common/Profile/ProfileView";
import HighSchoolProfileForm from "./HighSchoolProfileForm";

import type { HighSchoolProfile as HighSchoolProfileType } from "../../types/profile";

function HighSchoolProfile() {

  const { user } = useAuth();

  const [isEditing, setIsEditing] =
    useState(false);

  const [profile, setProfile] =
    useState<HighSchoolProfileType>({
      profileImage: null,

      fullName: user?.name || "",

      email: user?.email || "",

      mobile: "",

      dob: "",

      gender: null,

      bloodGroup: null,

      school: "",

      class: null,

      board: null,

      medium: "",

      rollNumber: "",

      admissionYear: "",

      percentage: "",

      parent: {

        parentName: "",

        parentMobile: "",

        parentEmail: "",

        occupation: "",

      },

      address: {

        country: "IN",

        state: "",

        district: "",

        city: "",

        pinCode: "",

      },

      careerGoal: null,

      stream: null,

      favoriteSubject: null,

      weakSubject: null,

      skills: [],

      hobbies: [],

      languages: [],

      lastUpdated: "",

    });

  useEffect(() => {

    const savedProfile =
      localStorage.getItem(
        "highSchoolProfile"
      );

    if (savedProfile) {

      setProfile(
        JSON.parse(savedProfile)
      );

    }

  }, []);

  const handleSave = (
    data: HighSchoolProfileType
  ) => {

    const updatedProfile = {

      ...data,

      lastUpdated:
        new Date().toLocaleString(),

    };

    setProfile(updatedProfile);

    localStorage.setItem(

      "highSchoolProfile",

      JSON.stringify(updatedProfile)

    );

    setIsEditing(false);

  };

  const handleCancel = () => {

    setIsEditing(false);

  };

  if (isEditing) {

    return (

      <HighSchoolProfileForm

        initialData={profile}

        onSave={handleSave}

        onCancel={handleCancel}

      />

    );

  }

  return (

    <ProfileView

      profileImage={
        profile.profileImage
      }

      name={profile.fullName}

      email={profile.email}

      phone={profile.mobile}

      role="High School Student"

      completion={85}

      lastUpdated={
        profile.lastUpdated
      }

      dob={profile.dob}

      address={`${profile.address.city}, ${profile.address.state}, ${profile.address.country}`}

      organization={
        profile.school
      }

      designation={`Class ${profile.class}`}

      onEdit={() =>
        setIsEditing(true)
      }

    >

      <div className="grid gap-8 md:grid-cols-2">

        <div>

          <h3 className="mb-4 text-xl font-bold">

            Academic Information

          </h3>

          <div className="space-y-3">

            <p>

              <strong>

                School :

              </strong>{" "}

              {profile.school ||
                "-"}

            </p>

            <p>

              <strong>

                Board :

              </strong>{" "}

              {profile.board?.label || "-"}
            </p>

            <p>

              <strong>

                Medium :

              </strong>{" "}

              {profile.medium ||
                "-"}

            </p>

            <p>

              <strong>

                Percentage :

              </strong>{" "}

              {profile.percentage ||
                "-"}

            </p>

          </div>

        </div>

        <div>

          <h3 className="mb-4 text-xl font-bold">

            Career Details

          </h3>

          <div className="space-y-3">

            <p>

              <strong>

                Dream Career :

              </strong>{" "}

              {profile.careerGoal?.label || "-"}
            </p>

            <p>

              <strong>

                Stream :

              </strong>{" "}

              {profile.stream?.label || "-"}

            </p>

            <p>

              <strong>

                Favorite Subject :

              </strong>{" "}

              {profile.favoriteSubject?.label || "-"}

            </p>

            <p>

              <strong>

                Weak Subject :

              </strong>{" "}

              {profile.weakSubject?.label || "-"}

            </p>

          </div>

        </div>

        <div>

          <h3 className="mb-4 text-xl font-bold">

            Parent Details

          </h3>

          <div className="space-y-3">

            <p>

              <strong>

                Parent Name :

              </strong>{" "}

              {profile.parent
                .parentName ||
                "-"}

            </p>

            <p>

              <strong>

                Mobile :

              </strong>{" "}

              {profile.parent
                .parentMobile ||
                "-"}

            </p>

            <p>

              <strong>

                Occupation :

              </strong>{" "}

              {profile.parent
                .occupation ||
                "-"}

            </p>

          </div>

        </div>

        <div>

          <h3 className="mb-4 text-xl font-bold">

            Skills

          </h3>

          <div className="flex flex-wrap gap-3">

            {profile.skills.length >

            0 ? (

              profile.skills.map(

                (skill) => (

                  <span
                    key={skill.value}
                    className="rounded-full bg-cyan-100 px-4 py-2 text-sm font-medium text-cyan-700"
                  >

                    {skill.label}
                  </span>

                )

              )

            ) : (

              <p>

                No Skills Added

              </p>

            )}

          </div>

        </div>

      </div>

    </ProfileView>

  );

}

export default HighSchoolProfile;