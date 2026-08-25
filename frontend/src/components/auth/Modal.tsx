import { type ReactNode, useEffect } from "react";
import { X } from "lucide-react";

interface ModalProps {
  isOpen: boolean;
  onClose: () => void;
  children: ReactNode;
}

function Modal({
  isOpen,
  onClose,
  children,
}: ModalProps) {
  useEffect(() => {
    const handleEscape = (e: KeyboardEvent) => {
      if (e.key === "Escape") {
        onClose();
      }
    };

    window.addEventListener("keydown", handleEscape);

    return () =>
      window.removeEventListener(
        "keydown",
        handleEscape
      );
  }, [onClose]);

  if (!isOpen) return null;

  return (
    <div
      onClick={onClose}
      className="fixed inset-0 z-50 flex items-center justify-center bg-black/50 backdrop-blur-sm p-4"
    >
      <div
        onClick={(e) => e.stopPropagation()}
        className="relative w-full max-w-md rounded-3xl bg-white shadow-2xl animate-in fade-in zoom-in duration-300"
      >
        <button
          onClick={onClose}
          className="absolute right-5 top-5 rounded-full p-2 transition hover:bg-slate-100"
        >
          <X size={22} />
        </button>

        {children}
      </div>
    </div>
  );
}

export default Modal;