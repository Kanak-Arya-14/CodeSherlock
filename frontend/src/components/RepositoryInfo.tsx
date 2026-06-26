import type { RepositoryResponse } from "../types";

interface Props {
  repository: RepositoryResponse;
}

export default function RepositoryInfo({ repository }: Props) {
  return (
    <div className="space-y-10 animate-fade-in">

      {/* Top Stats */}

      <div className="grid grid-cols-2 md:grid-cols-4 gap-6">

        <div className="bg-slate-900 rounded-2xl p-6 border border-slate-800">
          <p className="text-slate-400">⭐ Stars</p>
          <h2 className="text-4xl font-bold mt-2">
            {repository.stars.toLocaleString()}
          </h2>
        </div>

        <div className="bg-slate-900 rounded-2xl p-6 border border-slate-800">
          <p className="text-slate-400">💻 Language</p>
          <h2 className="text-4xl font-bold mt-2">
            {repository.language}
          </h2>
        </div>

        <div className="bg-slate-900 rounded-2xl p-6 border border-slate-800">
          <p className="text-slate-400">👤 Owner</p>
          <h2 className="text-3xl font-bold mt-2">
            {repository.owner}
          </h2>
        </div>

        <div className="bg-slate-900 rounded-2xl p-6 border border-slate-800">
          <p className="text-slate-400">📦 Repository</p>
          <h2 className="text-3xl font-bold mt-2">
            {repository.repository}
          </h2>
        </div>

      </div>

      {/* Description */}

      <div className="bg-slate-900 rounded-2xl p-8 border border-slate-800">

        <h2 className="text-3xl font-bold mb-5">
          📖 Repository Description
        </h2>

        <p className="text-slate-300 text-lg leading-8">
          {repository.description}
        </p>

      </div>

      {/* AI Summary */}

      <div className="bg-slate-900 rounded-2xl p-8 border border-slate-800">

        <h2 className="text-3xl font-bold mb-5">
          🧠 AI Summary
        </h2>

        <p className="text-slate-300 text-lg leading-8">
          {repository.summary}
        </p>

      </div>

      {/* Tech Stack */}

      <div className="bg-slate-900 rounded-2xl p-8 border border-slate-800">

        <h2 className="text-3xl font-bold mb-6">
          ⚙️ Tech Stack
        </h2>

        <div className="flex flex-wrap gap-4">

          {repository.tech_stack.map((tech) => (

            <div
              key={tech.name}
              className="px-5 py-3 rounded-full bg-blue-600/20 border border-blue-500 text-blue-300 font-medium"
            >
              {tech.name}
            </div>

          ))}

        </div>

      </div>

    </div>
  );
}