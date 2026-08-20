# Echo Frontend

Next.js web app for Echo's capture flow and voice playback UI.

Built with TypeScript, Tailwind CSS, and the App Router.

## Setup

```bash
npm install
```

Create `.env.local` pointing at the backend:

```
NEXT_PUBLIC_API_URL=http://localhost:8010
```

## Run locally

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000).

The home page lets you create a person profile, then record a voice sample from your browser mic, play it back, and upload it to the backend (saved to MinIO + Postgres). Browser mic access requires `localhost` or HTTPS.
