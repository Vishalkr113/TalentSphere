function Divider() {
  return (
    <div className="my-6 flex items-center">

      <div className="h-px flex-1 bg-slate-300" />

      <span className="px-4 text-sm text-slate-500">
        OR
      </span>

      <div className="h-px flex-1 bg-slate-300" />

    </div>
  );
}

export default Divider;