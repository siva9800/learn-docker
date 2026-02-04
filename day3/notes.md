# 🐳 **DOCKER TRAINING — DAY 3**

## Topic: Dockerizing Real Applications (React Frontend + Python Backend)

---

# 🎯 Day 3 Learning Objectives

By the end of Day 3, students will be able to:

✅ Understand how applications run WITHOUT Docker
✅ Understand why Dockerizing applications is needed
✅ Write Dockerfile
✅ Build Docker images
✅ Run custom containers
✅ Access containerized applications
✅ Push images to Docker Hub
✅ Dockerize frontend and backend applications

---

# 1️⃣ How Applications Run Without Docker (Traditional Approach)

Before Docker, applications are deployed manually.

---

## Example: Running React App Traditionally

Steps required:

1. Install Node.js ( https://nodejs.org/en/download )
2. Install npm (installed along with nodejs)
3. Clone project code
4. Install dependencies
5. Build application
6. Start server

Commands:

```bash
npm install
npm start
```

---

## Problems With Traditional Approach

* Node version mismatch
* Dependency conflicts
* OS differences
* Manual setup on every system
* Hard to reproduce same environment

---

### Common Problem:

> Works on developer laptop but fails on QA or Production.

---

# 2️⃣ Dockerized Approach (Modern Way)

Instead of installing software manually:

> We package application + dependencies + runtime into Docker image.

---

## Benefits:

✔ Same environment everywhere
✔ Easy deployment
✔ Portable
✔ Faster setup
✔ Production-ready packaging

---

# 3️⃣ What Is Dockerizing an Application?

### Definition:

> Dockerizing means creating a Docker image that contains application code, runtime environment and dependencies so that application can run inside a container.

---

# 4️⃣ Dockerfile → Image → Container Flow

Important concept to revise:

```
Dockerfile → Docker Image → Docker Container
```

---

### Dockerfile

* Instruction file
* Tells Docker how to build image

---

### Image

* Static template
* Built from Dockerfile

---

### Container

* Running instance of image
* Actual application execution

---

# 🧩 PART 1 — Dockerizing a React Frontend Application

---

# 5️⃣ Create React Application (If Not Available)

Run:

```bash
npx create-react-app my-react-app
cd my-react-app
```

---

## Verify Application Runs Normally

```bash
npm start
```

Browser opens:

```
http://localhost:3000
```

Explain:

> This is traditional way without Docker.

Stop app:

```
CTRL + C
```

---

# 6️⃣ Create Dockerfile for React Application

Inside project folder:

Create file:

```
Dockerfile
```

---

## React Dockerfile (Single Stage – Beginner Friendly)

```Dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm config set registry https://registry.npmjs.org/ \
    && npm install --legacy-peer-deps --no-audit --no-fund
COPY . .
EXPOSE 3000
CMD ["npm", "start"]
```

---

# 7️⃣ Explain Dockerfile Instructions

---

### FROM

Specifies base image.

```
FROM node:18-alpine
```

Means:

✔ Node runtime installed
✔ Lightweight Linux base

---

### WORKDIR

Sets working directory inside container.

```
WORKDIR /app
```

---

### COPY

Copies files from host to container.

```
COPY package*.json ./
COPY . .
```

---

### RUN

Executes commands during image build.

```
RUN npm install
```

---

### CMD

Runs application when container starts.

```
CMD ["npm", "start"]
```

---

### EXPOSE

Informs which port app uses.

```
EXPOSE 3000
```

---

# 8️⃣ Build React Docker Image

Run:

```bash
docker build -t react-app .
```

---

## What Happens Internally?

* Docker reads Dockerfile
* Executes instructions
* Downloads dependencies
* Creates image

---

## Verify Image

```bash
docker images
```

You should see:

```
react-app
```

---

# 9️⃣ Run React Container

Run:

```bash
docker run -d -p 3000:3000 react-app
```

---

## Explain Port Mapping

```
Host Port 3000 → Container Port 3000
```

---

# 🔍 Access React App in Browser

Open:

```
http://localhost:3000
```

---

Explain:

> React app is now running inside Docker container.

---

# 1️⃣0️⃣ Verify Running Container

```bash
docker ps
```

Shows:

✔ Container ID
✔ Image name
✔ Port mapping
✔ Running status

---

# 🧩 PART 2 — Push React Image to Docker Hub

---

# 1️⃣1️⃣ Login to Docker Hub

```bash
docker login
```

Enter:

✔ Username
✔ Password

---

# 1️⃣2️⃣ Tag Image

Docker registry requires naming format:

```
username/image-name
```

Example:

```bash
docker tag react-app yourname/react-app
```

---

# 1️⃣3️⃣ Push Image

```bash
docker push yourname/react-app
```

---

## Verify On Docker Hub Website

Login to:

👉 [https://hub.docker.com](https://hub.docker.com)

You will see:

✔ Repository created
✔ Image uploaded

---
