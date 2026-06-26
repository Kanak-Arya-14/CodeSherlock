export default function Loading() {
  return (
    <div className="flex flex-col items-center py-20">

      <div className="w-16 h-16 rounded-full border-4 border-blue-500 border-t-transparent animate-spin"></div>

      <h2 className="mt-8 text-2xl font-bold">
        AI is reading the repository...
      </h2>

      <p className="text-slate-400 mt-3">
        Detecting architecture • Tech Stack • Dependencies
      </p>

    </div>
  );
}