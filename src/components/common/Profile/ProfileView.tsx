import {
  Mail,
  Phone,
  MapPin,
  Calendar,
  GraduationCap,
  Briefcase,
  User,
  ShieldCheck,
  Clock3,
  Pencil,
} from "lucide-react";

type ProfileViewProps = {
  profileImage: string | null;

  name: string;

  email: string;

  phone?: string;

  role: string;

  completion: number;

  lastUpdated?: string;

  address?: string;

  dob?: string;

  organization?: string;

  designation?: string;

  onEdit?: () => void;

  children?: React.ReactNode;
};

function ProfileView({
  profileImage,

  name,

  email,

  phone,

  role,

  completion,

  lastUpdated,

  address,

  dob,

  organization,

  designation,

  onEdit,

  children,
}: ProfileViewProps) {

  return (

    <div className="overflow-hidden rounded-3xl bg-white shadow-sm">

      {/* Cover */}

      <div className="h-44 bg-gradient-to-r from-cyan-600 via-sky-600 to-indigo-600" />

      {/* Profile */}

      <div className="relative px-8 pb-8">

        <div className="-mt-24 flex flex-col gap-8 lg:flex-row lg:items-end lg:justify-between">

          <div className="flex flex-col items-center gap-6 lg:flex-row">

            <img
              src={
                profileImage ??
                `https://ui-avatars.com/api/?name=${encodeURIComponent(
                  name || "User"
                )}&background=0891b2&color=ffffff&size=256`
              }
              alt={name}
              className="h-44 w-44 rounded-full border-8 border-white object-cover shadow-xl"
            />

            <div>

              <div className="flex flex-wrap items-center gap-3">

                <h1 className="text-4xl font-bold text-slate-900">

                  {name}

                </h1>

                <span className="flex items-center gap-2 rounded-full bg-green-100 px-4 py-2 text-sm font-semibold text-green-700">

                  <ShieldCheck size={16} />

                  Verified

                </span>

              </div>

              <p className="mt-3 text-lg text-slate-600">

                {role}

              </p>

              <div className="mt-5 h-3 w-72 overflow-hidden rounded-full bg-slate-200">

                <div
                  className="h-full rounded-full bg-cyan-600 transition-all duration-500"
                  style={{
                    width: `${completion}%`,
                  }}
                />

              </div>

              <p className="mt-2 text-sm text-slate-500">

                Profile Completion : {completion}%

              </p>

            </div>

          </div>

          {onEdit && (

            <button
              onClick={onEdit}
              className="flex items-center gap-2 rounded-xl bg-cyan-600 px-6 py-3 font-semibold text-white transition hover:bg-cyan-700"
            >

              <Pencil size={18} />

              Edit Profile

            </button>

          )}

        </div>

                 {/* Information */}

        <div className="mt-12 grid gap-8 lg:grid-cols-3">

          {/* Contact */}

          <div className="rounded-2xl border border-slate-200 p-6">

            <h2 className="mb-6 text-xl font-bold text-slate-900">

              Contact Information

            </h2>

            <div className="space-y-5">

              <div className="flex items-center gap-3">

                <Mail
                  size={20}
                  className="text-cyan-600"
                />

                <div>

                  <p className="text-sm text-slate-500">

                    Email

                  </p>

                  <p className="font-medium">

                    {email || "-"}

                  </p>

                </div>

              </div>

              <div className="flex items-center gap-3">

                <Phone
                  size={20}
                  className="text-cyan-600"
                />

                <div>

                  <p className="text-sm text-slate-500">

                    Mobile

                  </p>

                  <p className="font-medium">

                    {phone || "-"}

                  </p>

                </div>

              </div>

              <div className="flex items-center gap-3">

                <MapPin
                  size={20}
                  className="text-cyan-600"
                />

                <div>

                  <p className="text-sm text-slate-500">

                    Address

                  </p>

                  <p className="font-medium">

                    {address || "-"}

                  </p>

                </div>

              </div>

              <div className="flex items-center gap-3">

                <Calendar
                  size={20}
                  className="text-cyan-600"
                />

                <div>

                  <p className="text-sm text-slate-500">

                    Date of Birth

                  </p>

                  <p className="font-medium">

                    {dob || "-"}

                  </p>

                </div>

              </div>

            </div>

          </div>

          {/* Profile */}

          <div className="rounded-2xl border border-slate-200 p-6">

            <h2 className="mb-6 text-xl font-bold text-slate-900">

              Profile Summary

            </h2>

            <div className="space-y-5">

              <div className="flex items-center gap-3">

                <User
                  size={20}
                  className="text-cyan-600"
                />

                <div>

                  <p className="text-sm text-slate-500">

                    Role

                  </p>

                  <p className="font-medium">

                    {role}

                  </p>

                </div>

              </div>

              <div className="flex items-center gap-3">

                <Clock3
                  size={20}
                  className="text-cyan-600"
                />

                <div>

                  <p className="text-sm text-slate-500">

                    Last Updated

                  </p>

                  <p className="font-medium">

                    {lastUpdated || "-"}

                  </p>

                </div>

              </div>

            </div>

          </div>

          {/* Organization */}

          <div className="rounded-2xl border border-slate-200 p-6">

            <h2 className="mb-6 text-xl font-bold text-slate-900">

              Academic / Professional

            </h2>

            <div className="space-y-5">

              <div className="flex items-center gap-3">

                <GraduationCap
                  size={20}
                  className="text-cyan-600"
                />

                <div>

                  <p className="text-sm text-slate-500">

                    School / College

                  </p>

                  <p className="font-medium">

                    {organization || "-"}

                  </p>

                </div>

              </div>

              <div className="flex items-center gap-3">

                <Briefcase
                  size={20}
                  className="text-cyan-600"
                />

                <div>

                  <p className="text-sm text-slate-500">

                    Designation

                  </p>

                  <p className="font-medium">

                    {designation || "-"}

                  </p>

                </div>

              </div>

            </div>

          </div>

        </div>  
           
                   {/* Dynamic Information */}

        {children && (

          <div className="mt-10 rounded-2xl border border-slate-200 p-8">

            <h2 className="mb-8 text-2xl font-bold text-slate-900">

              Additional Information

            </h2>

            {children}

          </div>

        )}

        {/* Footer */}

        <div className="mt-10 flex flex-col items-center justify-between gap-4 rounded-2xl bg-slate-50 px-8 py-6 lg:flex-row">

          <div>

            <h3 className="text-xl font-bold text-slate-900">

              TalentSphere Elevate

            </h3>

            <p className="mt-2 text-slate-600">

              Keep your profile updated to receive better
              AI recommendations, assessments and career
              opportunities.

            </p>

          </div>

          <div className="rounded-xl bg-cyan-100 px-5 py-3">

            <span className="font-semibold text-cyan-700">

              {completion}% Complete

            </span>

          </div>

        </div>

      </div>

    </div>

  );

}

export default ProfileView;