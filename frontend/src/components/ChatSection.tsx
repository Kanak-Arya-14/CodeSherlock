import { useState } from "react";
import { askAI } from "../api";

interface Props {
  repoUrl: string;
}

export default function ChatSection({ repoUrl }: Props) {

  const [question, setQuestion] = useState("");

  const [answer, setAnswer] = useState("");

  const [loading, setLoading] = useState(false);

  async function handleAsk() {

    if (!question.trim()) return;

    setLoading(true);

    try {

      const result = await askAI(repoUrl, question);

      setAnswer(result.answer);

    }

    catch {

      setAnswer("Something went wrong.");

    }

    finally {

      setLoading(false);

    }

  }

  return (

    <div className="mt-12 bg-slate-900 rounded-2xl border border-slate-800 p-8">

      <h2 className="text-3xl font-bold mb-6">

        🤖 Ask CodeSherlock

      </h2>

      <textarea

        value={question}

        onChange={(e)=>setQuestion(e.target.value)}

        rows={4}

        placeholder="Ask anything about this repository..."

        className="w-full rounded-xl bg-slate-800 border border-slate-700 p-4 outline-none"

      />

      <button

        onClick={handleAsk}

        className="mt-5 bg-blue-600 hover:bg-blue-700 px-6 py-3 rounded-xl font-semibold"

      >

        {loading ? "Thinking..." : "Ask AI"}

      </button>

      {answer && (

        <div className="mt-8 bg-slate-800 rounded-xl p-5 whitespace-pre-wrap leading-8">

          {answer}

        </div>

      )}

    </div>

  );

}