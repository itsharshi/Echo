# Infra

Local dev infrastructure for Echo: Postgres (metadata) and MinIO (S3-compatible object storage for audio files).

## Usage

```
cd infra
docker compose up -d
```

- Postgres: `localhost:5432`, db/user/pass all `echo` (see `docker-compose.yml`)
- MinIO API: `localhost:9000`, console: `localhost:9001`, user `echo` / pass `echo12345`
- Bucket `echo-audio` must exist before uploads work. Create it once with:

```
docker exec echo-minio mc alias set local http://localhost:9000 echo echo12345
docker exec echo-minio mc mb local/echo-audio
```

Copy `backend/.env.example` to `backend/.env` to point the backend at these services.

Stop with `docker compose down` (add `-v` to also wipe the data volumes).
