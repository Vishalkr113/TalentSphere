import { useRef } from "react";
import {
  Camera,
  Trash2,
  RefreshCw,
} from "lucide-react";

type ProfilePhotoProps = {
  image: string | null;
  editable?: boolean;
  name?: string;
  onChange: (image: string | null) => void;
};

function ProfilePhoto({
  image,
  editable = false,
  name = "User",
  onChange,
}: ProfilePhotoProps) {
  const fileInputRef =
    useRef<HTMLInputElement>(null);

  const handleUpload = (
    e: React.ChangeEvent<HTMLInputElement>
  ) => {
    const file =
      e.target.files?.[0];

    if (!file) return;

    const reader =
      new FileReader();

    reader.onload = () => {
      onChange(
        reader.result as string
      );
    };

    reader.readAsDataURL(file);
  };

  const handleRemove = () => {
    onChange(null);

    if (fileInputRef.current) {
      fileInputRef.current.value =
        "";
    }
  };

  const handleBrowse = () => {
    fileInputRef.current?.click();
  };

  return (
    <div className="rounded-3xl border border-slate-200 bg-white p-8 shadow-sm">

      <div className="flex flex-col items-center">

        <div className="relative">

          <img
            src={
              image ??
              `https://ui-avatars.com/api/?name=${encodeURIComponent(
                name
              )}&background=0891b2&color=ffffff&size=256`
            }
            alt="Profile"
            className="h-44 w-44 rounded-full border-4 border-cyan-100 object-cover shadow-lg"
          />

          {editable && (
            <button
              type="button"
              onClick={handleBrowse}
              className="absolute bottom-2 right-2 rounded-full bg-cyan-600 p-3 text-white shadow-lg transition hover:bg-cyan-700"
            >
              <Camera size={20} />
            </button>
          )}

        </div>

        <h2 className="mt-6 text-2xl font-bold text-slate-900">
          {name}
        </h2>

        <p className="mt-2 text-slate-500">
          Profile Photo
        </p>

        {editable && (
          <div className="mt-8 flex flex-wrap justify-center gap-4">

            <button
              type="button"
              onClick={handleBrowse}
              className="flex items-center gap-2 rounded-xl bg-cyan-600 px-5 py-3 font-semibold text-white transition hover:bg-cyan-700"
            >
              <Camera size={18} />

              Upload
            </button>

            <button
              type="button"
              onClick={handleBrowse}
              className="flex items-center gap-2 rounded-xl bg-blue-600 px-5 py-3 font-semibold text-white transition hover:bg-blue-700"
            >
              <RefreshCw size={18} />

              Change
            </button>

            <button
              type="button"
              onClick={handleRemove}
              className="flex items-center gap-2 rounded-xl bg-red-600 px-5 py-3 font-semibold text-white transition hover:bg-red-700"
            >
              <Trash2 size={18} />

              Remove
            </button>

          </div>
        )}

        <input
          ref={fileInputRef}
          type="file"
          accept="image/*"
          hidden
          onChange={handleUpload}
        />

      </div>

    </div>
  );
}

export default ProfilePhoto;