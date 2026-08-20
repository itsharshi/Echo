"use client";

import { useRef, useState } from "react";

const API_URL = process.env.NEXT_PUBLIC_API_URL;

export default function AudioRecorder({ personId }: { personId: string }) {
  const [recording, setRecording] = useState(false);
  const [audioUrl, setAudioUrl] = useState<string | null>(null);
  const [audioBlob, setAudioBlob] = useState<Blob | null>(null);
  const [uploading, setUploading] = useState(false);
  const [uploaded, setUploaded] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const mediaRecorderRef = useRef<MediaRecorder | null>(null);
  const chunksRef = useRef<Blob[]>([]);

  async function startRecording() {
    setError(null);
    setUploaded(false);
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      const mediaRecorder = new MediaRecorder(stream);
      chunksRef.current = [];

      mediaRecorder.ondataavailable = (e) => {
        if (e.data.size > 0) chunksRef.current.push(e.data);
      };

      mediaRecorder.onstop = () => {
        const blob = new Blob(chunksRef.current, { type: "audio/webm" });
        setAudioBlob(blob);
        setAudioUrl(URL.createObjectURL(blob));
        stream.getTracks().forEach((track) => track.stop());
      };

      mediaRecorder.start();
      mediaRecorderRef.current = mediaRecorder;
      setRecording(true);
    } catch {
      setError("Microphone access denied or unavailable");
    }
  }

  function stopRecording() {
    mediaRecorderRef.current?.stop();
    setRecording(false);
  }

  async function handleUpload() {
    if (!audioBlob) return;
    setUploading(true);
    setError(null);
    try {
      const formData = new FormData();
      formData.append("file", audioBlob, "recording.webm");
      const res = await fetch(`${API_URL}/people/${personId}/recordings`, {
        method: "POST",
        body: formData,
      });
      if (!res.ok) throw new Error("Failed to upload recording");
      setUploaded(true);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Something went wrong");
    } finally {
      setUploading(false);
    }
  }

  return (
    <div className="flex flex-col gap-4 rounded-md border border-black/10 p-4 dark:border-white/15">
      <p className="text-sm text-zinc-600 dark:text-zinc-400">
        Voice sample
      </p>

      <div className="flex gap-3">
        {!recording ? (
          <button
            onClick={startRecording}
            className="rounded-full bg-foreground px-5 py-2 text-sm text-background transition-colors hover:bg-[#383838] dark:hover:bg-[#ccc]"
          >
            Start Recording
          </button>
        ) : (
          <button
            onClick={stopRecording}
            className="rounded-full bg-red-600 px-5 py-2 text-sm text-white transition-colors hover:bg-red-700"
          >
            Stop Recording
          </button>
        )}
      </div>

      {audioUrl && (
        <div className="flex flex-col gap-3">
          <audio controls src={audioUrl} className="w-full" />
          <button
            onClick={handleUpload}
            disabled={uploading || uploaded}
            className="rounded-full border border-black/15 px-5 py-2 text-sm transition-colors hover:bg-black/[.04] disabled:opacity-50 dark:border-white/15 dark:hover:bg-[#1a1a1a]"
          >
            {uploaded ? "Uploaded" : uploading ? "Uploading..." : "Upload Recording"}
          </button>
        </div>
      )}

      {error && <p className="text-sm text-red-600">{error}</p>}
    </div>
  );
}
