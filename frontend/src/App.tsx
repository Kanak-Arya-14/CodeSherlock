import { useState } from "react";
import "./styles/tailwind.css";
import Loading from "./components/Loading";
import { analyzeRepository } from "./api";
import type { RepositoryResponse } from "./types";
import ChatSection from "./components/ChatSection";
import RepositoryInfo from "./components/RepositoryInfo";

function App() {
  const [repoUrl, setRepoUrl] = useState("");

  const [loading, setLoading] = useState(false);

  const [repository, setRepository] =
    useState<RepositoryResponse | null>(null);

  const [error, setError] = useState("");

  async function handleAnalyze() {
    if (!repoUrl.trim()) return;

    setLoading(true);
    setError("");

    try {
      const result = await analyzeRepository(repoUrl);

      console.log(result);

      setRepository(result);
    } catch (err) {
      console.log(err);

      setError("Failed to analyze repository.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="min-h-screen bg-slate-950 text-white">

      <section className="max-w-6xl mx-auto px-6 py-16">

        {/* Hero */}

        <div className="text-center">

          <h1 className="text-6xl font-black">
            🔍 CodeSherlock
          </h1>

          <p className="text-slate-400 mt-5 text-xl">
            AI-Powered GitHub Repository Intelligence
          </p>

          <p className="text-slate-500 mt-2">
            Analyze • Explain • Learn • Visualize
          </p>

        </div>

        {/* Search */}

        <div className="mt-16 bg-slate-900 rounded-3xl p-6 shadow-2xl border border-slate-800">

          <div className="flex gap-4">

            <input
              value={repoUrl}
              onChange={(e) => setRepoUrl(e.target.value)}
              placeholder="Paste any GitHub Repository URL..."
              className="flex-1 rounded-xl bg-slate-800 px-5 py-4 outline-none border border-slate-700 focus:border-blue-500"
            />

            <button
              onClick={handleAnalyze}
              className="bg-blue-600 hover:bg-blue-700 transition px-8 rounded-xl font-semibold"
            >
              {loading ? "Analyzing..." : "Analyze →"}
            </button>

          </div>

        </div>

        {/* Error */}

        {error && (

          <div className="mt-6 bg-red-500/20 border border-red-500 rounded-xl p-4">

            {error}

          </div>

        )}

        {/* Loading */}

        {loading && <Loading />}

        {/* Repository */}

        {repository && !loading && (

          <div className="mt-12">

            <RepositoryInfo repository={repository} />
            <ChatSection repoUrl={repoUrl} />

          </div>

        )}

      </section>

    </div>
  );
}

export default App;