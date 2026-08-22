<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/MuhammadMoiz20/MuhammadMoiz20/main/assets/header-dark.svg?v=3">
  <img alt="whoami — Muhammad Moiz, Dartmouth CS '26, backend and distributed systems" src="https://raw.githubusercontent.com/MuhammadMoiz20/MuhammadMoiz20/main/assets/header-light.svg?v=3" width="100%">
</picture>

<p align="center">
  <a href="https://moizofficial.com"><b>moizofficial.com</b></a> &nbsp;·&nbsp;
  <a href="https://linkedin.com/in/moizofficial">LinkedIn</a> &nbsp;·&nbsp;
  <a href="mailto:moizzahid20@gmail.com">Email</a> &nbsp;·&nbsp;
  <i>open to new-grad backend / infrastructure roles</i>
</p>

---

### Currently running

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/MuhammadMoiz20/MuhammadMoiz20/main/assets/services-dark.svg?v=3">
  <img alt="Service status board of current projects" src="https://raw.githubusercontent.com/MuhammadMoiz20/MuhammadMoiz20/main/assets/services-light.svg?v=3" width="100%">
</picture>

---

### The shape of what I build

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/MuhammadMoiz20/MuhammadMoiz20/main/assets/dataplane-dark.svg?v=3">
  <img alt="A request traced through browser, edge, FastAPI, queue, and Postgres" src="https://raw.githubusercontent.com/MuhammadMoiz20/MuhammadMoiz20/main/assets/dataplane-light.svg?v=3" width="100%">
</picture>

Two years of backend work at **DALI Lab** across client products, plus internships in the UK
and Kuwait. The pattern is always the same: a boundary that needs to hold under load, tenants
that must not see each other's rows, and work that has to happen after the response is sent.

---

### Selected work

| | What it is | The part worth reading |
|---|---|---|
| **ishaq-dar** <sub>(private)</sub> | A single-user financial OS with a tool-grounded AI advisor | The model performs **no arithmetic and never sees raw minor units** — every figure comes back pre-formatted from a pure, clockless, I/O-free engine. It also cannot write to the database; it emits a Zod-validated command that server code executes and logs. A behavioural eval suite runs each case three times, because one pass proves nothing about a non-deterministic system. |
| **[moji-proctor](https://github.com/MuhammadMoiz20/moji-proctor)** | Tamper-evident provenance for student code | A VS Code extension writes coding activity into an **Ed25519-signed hash chain**, verified by a GitHub Action on PR. Online mode uploads metadata only, with per-device sequence numbers for replay protection and deterministic doc IDs for idempotency. The README says plainly how it can be defeated — these are signals, not proofs. |
| **[qss45-h1b-final](https://github.com/MuhammadMoiz20/qss45-h1b-final)** | Can USCIS H-1B denials be predicted? | Joined **374K USCIS petitions to 3.75M DOL LCA records** with no shared employer key, via canonicalised-name matching (86.0% of petitions matched). Within a policy regime, AUC ≈ 0.80. Train ≤FY2021, test FY2022: **R² = −0.618**. The finding is that the signal does not survive a policy change, and the paper reports that instead of burying it. |
| **[Dispatch](https://github.com/MuhammadMoiz20/Dispatch)** | Multi-tenant e-commerce logistics & returns engine | NestJS + Postgres row-level security + a GraphQL gateway + RabbitMQ, as a pnpm monorepo with Docker Compose and Playwright end-to-end coverage. |
| **[hirescript](https://github.com/MuhammadMoiz20/hirescript)** | An AI-first résumé builder that compiles LaTeX | FastAPI + Alembic behind a React/Vite front end, Voyage embeddings over a personal knowledge base, compiled PDFs in MinIO keyed by version id, and a live agent smoke test kept behind an explicit flag so the normal suite stays offline. Runs on a VPS behind Caddy. |
| **[coursera-autograder](https://github.com/MuhammadMoiz20/coursera-autograder)** | Grading that assumes the student controls the runtime | Tests run on the learner's machine, so trust moves to the artifact: results are **AES-256-CBC encrypted with a server-held key** and the container refuses anything it cannot decrypt. |
| **[md-to-pdf](https://github.com/MuhammadMoiz20/md-to-pdf)** | Markdown → PDF, self-hosted | Small, finished, documented. `POST /api/render` takes JSON or raw `text/markdown` and returns `application/pdf`. Sometimes the answer is a 200-line tool that works. |

---

### Before this

| Where | What shipped |
|---|---|
| **Dartmouth Rauner Library** | Distributed Python ingestion for **10K+ videos and 1K+ articles/month**; parallel pipelines and dedup cut average processing time by **~90%**. Used by **60+ partner institutions**. |
| **Muff Manufacturing (UK)** | Serverless digital-twin platform over **170+ warehouses** on Lambda + S3 + DynamoDB + SQS, with **400+ BI dashboards** behind an authenticated React shell. **99.95% uptime.** |
| **DALI Lab · Classmoji** | Led a **JS → TS migration across an 8-workspace, ~89k-line monorepo**, plus an auth overhaul. Found a cross-package path-alias leak that had been silently defeating type checking. |
| **DALI Lab · Evergreen** | Multi-account Google OAuth, deep Calendar integration, and an **MCP server** exposing the product as agent-callable tools. |
| **Man To-Go** | Co-founded a campus delivery platform: **450+ active users in six weeks**, real-time Mapbox tracking. |

---

### Stack

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/MuhammadMoiz20/MuhammadMoiz20/main/assets/stack-dark.svg?v=3">
  <img alt="Stack, grouped by how often I actually reach for it" src="https://raw.githubusercontent.com/MuhammadMoiz20/MuhammadMoiz20/main/assets/stack-light.svg?v=3" width="100%">
</picture>

<details>
<summary><b>telemetry</b> — the usual cards, tucked away where they belong</summary>
<br>
<p align="center">
  <img height="160" src="https://github-readme-stats.vercel.app/api?username=MuhammadMoiz20&show_icons=true&hide_border=true&count_private=true&include_all_commits=true&rank_icon=github&title_color=3fb950&icon_color=58a6ff&bg_color=00000000" alt="GitHub stats" />
  <img height="160" src="https://github-readme-stats.vercel.app/api/top-langs/?username=MuhammadMoiz20&layout=compact&hide_border=true&langs_count=8&hide=roff,tex,dockerfile,makefile,shell,jupyter%20notebook,batchfile,powershell,scss,less,mdx&title_color=3fb950&bg_color=00000000" alt="Top languages" />
</p>
</details>

---

<sub>
Every panel above is a hand-written SVG generated by
<a href="./assets/build.py"><code>assets/build.py</code></a> — no badge services, no third-party
image APIs, one theme dict as the only source of colour. <code>python3 assets/build.py</code> rebuilds them.
</sub>
