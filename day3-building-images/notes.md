# Docker - Day 3: Building Your Own Image

> **Goal of today:** write your first **Dockerfile**, build a custom image from your own app, run it, and publish it to Docker Hub.

---

## Objective of Day 3
By the end you'll be able to:
- Explain why we build custom images instead of only using public ones
- Write a **Dockerfile**
- Build an image and run it as a container
- Understand **image layers & build caching** (why instruction order matters)
- Use a **`.dockerignore`** file
- Tag and **push** an image to Docker Hub

---

## 1 Life Without Docker (the pain)

To run a React app the traditional way, every person must:
1. Install Node.js + npm
2. Clone the code
3. `npm install` the dependencies
4. Build and start it
```bash
npm install
npm start
```
Node version mismatches, dependency conflicts, OS differences, manual setup on every machine → *"works on my laptop, breaks on QA."*

---

## 2 The Dockerized Way

### Analogy
A Dockerfile is a **recipe**. The image is the **sealed meal kit** built from that recipe. Anyone can "cook" (run) it and get the identical result - no hunting for ingredients.

> **Dockerizing** = packaging your app + runtime + dependencies into an image that runs in a container anywhere.

```mermaid
flowchart LR
    DF["Dockerfile<br/>(the recipe)"] -->|docker build| IMG["Image<br/>(the meal kit)"]
    IMG -->|docker run| CT["Container<br/>(the served meal)"]
    style DF fill:#0277bd,color:#fff
    style IMG fill:#6a1b9a,color:#fff
    style CT fill:#2e7d32,color:#fff
```

| | Dockerfile | Image | Container |
|---|---|---|---|
| What | Instruction text file | Static template | Running app |
| Analogy | Recipe | Cake mix | Baked cake |

---

## 3 First, Install Node.js and npm

To create and run a React app on your own machine you need **Node.js** (the JavaScript runtime). Installing Node.js automatically installs **npm** (Node Package Manager) with it - they come together.

> Small irony worth noticing: we install Node.js here only so we can *create* a sample app to containerize. Once the app is in a Docker image, nobody else needs Node.js installed - that is exactly the "works on my machine" problem Docker solves. This is the last time you install a language runtime by hand in this course.

### Windows (recommended: winget)

Windows 10/11 ships with `winget`, the built-in package manager. Open **PowerShell** and run:
```powershell
winget install OpenJS.NodeJS.LTS
```
Close and reopen PowerShell, then verify:
```powershell
node --version    # e.g. v20.x.x
npm --version     # e.g. 10.x.x
```

**Alternative for Windows (manual installer):** download the **LTS** installer from [nodejs.org](https://nodejs.org/), run the `.msi`, keep clicking Next (accept the defaults), then reopen your terminal and run the same two verify commands.

> Always pick **LTS** (Long-Term Support), not "Current." LTS is the stable version companies actually use.

> [!IMPORTANT]
> **Windows: "npm cannot be loaded because running scripts is disabled on this system"**
> This is the single most common error Windows students hit. It is **not** an npm problem - it is a PowerShell security setting. On Windows, `npm` is a PowerShell script, and PowerShell blocks scripts by default.
>
> **Fix (run once, in PowerShell):**
> ```powershell
> Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
> ```
> Type **Y** to confirm. `-Scope CurrentUser` means it only affects your account (no admin needed), and `RemoteSigned` is the safe, standard developer setting: your own local scripts run, while scripts downloaded from the internet must be signed. After this, `npm` works normally in every new PowerShell window.
>
> **Prefer not to change the policy?** Any of these work without it:
> - Use `npm.cmd install` instead of `npm install`.
> - Run your commands in **Command Prompt (cmd)** or **Git Bash** instead of PowerShell - neither has this restriction.

### macOS
```bash
brew install node        # using Homebrew
node --version
npm --version
```

### Linux (Ubuntu/Debian)
```bash
# NodeSource gives you a current LTS (the distro's default is often old)
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y nodejs
node --version
npm --version
```

### The professional way: nvm (Node Version Manager)

On real teams, different projects need different Node versions. **nvm** lets you install and switch between versions instantly, instead of reinstalling Node each time.

- **Windows:** install [nvm-windows](https://github.com/coreybutler/nvm-windows/releases) (`nvm-setup.exe`), then:
  ```powershell
  nvm install lts
  nvm use lts
  ```
- **macOS/Linux:** install [nvm](https://github.com/nvm-sh/nvm), then:
  ```bash
  nvm install --lts
  nvm use --lts
  ```

> This is optional for today, but it is how professionals manage Node - worth knowing when an interviewer asks "how do you handle different Node versions across projects?"

---

## 4 Create a React App (if you don't have one)

Now that Node.js and npm are installed, create a starter app:
```bash
npx create-react-app my-react-app
cd my-react-app
npm start          # runs at http://localhost:3000 (traditional way)
# press CTRL + C to stop
```
`npx` is a tool that comes with npm; it runs a package (here, `create-react-app`) without permanently installing it.

> **Heads-up (modern alternative):** `create-react-app` is now considered outdated and is no longer actively maintained. The current standard is **Vite**, which is faster:
> ```bash
> npm create vite@latest my-react-app -- --template react
> cd my-react-app
> npm install
> npm run dev        # Vite dev server (default http://localhost:5173)
> ```
> Either works for this Docker lesson. If you use Vite, remember its build output goes to `dist/` (not `build/`) and its dev port is `5173` - adjust the `EXPOSE`/port numbers accordingly.

---

## 5 Write the Dockerfile

Create a file named exactly `Dockerfile` (no extension) in the project root:

```Dockerfile
# 1. Base image: Node.js on a tiny Alpine Linux
FROM node:20-alpine

# 2. Set the working folder inside the image
WORKDIR /app

# 3. Copy ONLY dependency files first (for better caching - see §6)
COPY package*.json ./

# 4. Install dependencies
RUN npm install

# 5. Now copy the rest of the source code
COPY . .

# 6. Document the port the app uses
EXPOSE 3000

# 7. Command to start the app when the container runs
CMD ["npm", "start"]
```

> **Use a real, current version tag** like `node:20-alpine` (LTS) or `node:22-alpine`. Avoid invented tags like `node:24-alpine` - if the tag doesn't exist, the build fails.

### What each instruction means
| Instruction | Purpose |
|---|---|
| `FROM` | The base image to start from |
| `WORKDIR` | Sets/creates the working directory inside the image |
| `COPY` | Copies files from your machine into the image |
| `RUN` | Runs a command **at build time** (e.g. install deps) |
| `EXPOSE` | Documents which port the app listens on |
| `CMD` | The command run **when the container starts** |

---

## 6 Add a `.dockerignore` (do this!)

Just like `.gitignore`, a **`.dockerignore`** keeps junk and secrets *out* of your image - making builds faster and smaller. Create `.dockerignore`:
```
node_modules
build
.git
.env
*.log
Dockerfile
```
> Never bake `node_modules` or secrets (`.env`) into an image. They bloat it and can leak credentials.

---

## 7 Image Layers & Build Caching (the pro concept)

### Analogy
An image is built in **stacked layers**, like sheets of a lasagna - **one layer per instruction**. Docker **caches** each layer. On the next build, if a layer's inputs haven't changed, Docker **reuses the cached layer instead of rebuilding it**.

```mermaid
flowchart TB
    L1["Layer 1: FROM node:20-alpine"]
    L2["Layer 2: COPY package*.json"]
    L3["Layer 3: RUN npm install   slow"]
    L4["Layer 4: COPY . ."]
    L1-->L2-->L3-->L4
```

**Why we `COPY package*.json` BEFORE `COPY . .`:**
- If you only change your *source code* (not dependencies), layers 1-3 are **reused from cache**, so `npm install` is **skipped** → builds in seconds.
- If you copied everything first, *any* code change would invalidate the cache and re-run the slow `npm install` every time.

> Inspect layers with: `docker history react-app`

---

## 8 Build the Image
```bash
docker build -t react-app .
```
- `-t react-app` → tag (name) the image
- `.` → build context (the current folder)

Docker reads the Dockerfile top-to-bottom, executing each instruction into a layer.
```bash
docker images          # see 'react-app' listed
```

---

## 9 Run Your Container
```bash
docker run -d -p 3000:3000 react-app
```
Open `http://localhost:3000` → your React app, now running inside Docker!
```bash
docker ps              # confirm it's running
```

---

## 10 Push to Docker Hub (share your image)

### Analogy
Docker Hub is like **GitHub, but for images**. You tag your image with your username, then push.

```bash
docker login                                   # enter Docker Hub username + password/token

docker tag react-app yourname/react-app:v1     # registry naming: username/image:tag

docker push yourname/react-app:v1              # upload
```
Now anyone can run it with `docker run yourname/react-app:v1`. Verify at [hub.docker.com](https://hub.docker.com).

```mermaid
flowchart LR
    Local["local image<br/>react-app"] -->|docker tag| Tagged["yourname/react-app:v1"]
    Tagged -->|docker push| Hub["Docker Hub"]
    Hub -->|docker pull| Anyone["anyone, anywhere"]
```

> **Tip:** use an **access token** (Docker Hub → Account Settings → Security) instead of your password - safer, just like a GitHub PAT.

---

## Common Beginner Mistakes
1. **Invalid base image tag** (e.g. `node:24-alpine` when it doesn't exist) → build fails. Check tags on Docker Hub.
2. **No `.dockerignore`** → `node_modules` copied in, giant slow image.
3. **`COPY . .` before installing deps** → cache busted on every code change (slow builds).
4. **Forgetting to tag with your username** before push → push rejected.

---

## Quick Self-Check
1. What's the difference between a Dockerfile, an image, and a container?
2. Why copy `package*.json` *before* the rest of the source?
3. What does `.dockerignore` do, and why exclude `.env`?
4. What does `-t` do in `docker build -t react-app .`?
5. What naming format does Docker Hub require before pushing?

---

## Hands-On Lab
```bash
# from your React project folder containing the Dockerfile + .dockerignore
docker build -t react-app .
docker images
docker run -d -p 3000:3000 react-app
# open http://localhost:3000

# rebuild after a small code change - notice npm install is CACHED (fast!)
docker build -t react-app .
docker history react-app          # inspect the layers

# publish
docker login
docker tag react-app <yourname>/react-app:v1
docker push <yourname>/react-app:v1
```

---

## End of Day 3 Summary
- Wrote a Dockerfile and built a custom image
- Understood layers & caching (and why instruction order matters)
- Used `.dockerignore` to keep images clean
- Tagged and pushed an image to Docker Hub

Next up → [**Day 4: Backend Containers & Data Persistence (Volumes)**](../day4-volumes/notes.md)
