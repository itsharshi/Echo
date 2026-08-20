"use client";

import { useState } from "react";

const API_URL = process.env.NEXT_PUBLIC_API_URL;

type Person = {
  id: string;
  name: string;
  status: string;
};

export default function Home() {
  const [name, setName] = useState("");
  const [person, setPerson] = useState<Person | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    setError(null);
    setLoading(true);
    try {
      const res = await fetch(`${API_URL}/people`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name }),
      });
      if (!res.ok) throw new Error("Failed to create person");
      const data: Person = await res.json();
      setPerson(data);
      setName("");
    } catch (err) {
      setError(err instanceof Error ? err.message : "Something went wrong");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="flex flex-col flex-1 items-center justify-center bg-zinc-50 font-sans dark:bg-black">
      <main className="flex w-full max-w-md flex-col gap-8 px-6 py-16">
        <h1 className="text-2xl font-semibold text-black dark:text-zinc-50">
          Person Profile
        </h1>

        <form onSubmit={handleSubmit} className="flex flex-col gap-4">
          <label className="flex flex-col gap-2 text-sm text-zinc-600 dark:text-zinc-400">
            Name
            <input
              className="rounded-md border border-black/10 bg-white px-3 py-2 text-black dark:border-white/15 dark:bg-zinc-900 dark:text-zinc-50"
              value={name}
              onChange={(e) => setName(e.target.value)}
              required
            />
          </label>
          <button
            type="submit"
            disabled={loading || !name.trim()}
            className="rounded-full bg-foreground px-5 py-2 text-background transition-colors hover:bg-[#383838] disabled:opacity-50 dark:hover:bg-[#ccc]"
          >
            {loading ? "Saving..." : "Save"}
          </button>
        </form>

        {error && <p className="text-sm text-red-600">{error}</p>}

        {person && (
          <div className="flex flex-col gap-1 rounded-md border border-black/10 p-4 text-sm dark:border-white/15">
            <p className="text-zinc-600 dark:text-zinc-400">
              Saved person:
            </p>
            <p className="text-black dark:text-zinc-50">
              <span className="font-medium">Name:</span> {person.name}
            </p>
            <p className="text-black dark:text-zinc-50">
              <span className="font-medium">Status:</span> {person.status}
            </p>
            <p className="text-zinc-500 dark:text-zinc-500 text-xs">
              ID: {person.id}
            </p>
          </div>
        )}
      </main>
    </div>
  );
}
