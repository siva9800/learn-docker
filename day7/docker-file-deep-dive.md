Below are **complete detailed notes on Dockerfile** — structured so students understand *what each instruction does, when it runs, and why we use it.*

---

# 🐳 Dockerfile — Complete Detailed Notes

---

# 1️⃣ What is a Dockerfile?

> A Dockerfile is a script containing instructions that Docker follows to build an image.

Flow:

```
Dockerfile → docker build → Docker Image → docker run → Container
```

So:

* Dockerfile = recipe
* Image = prepared software package
* Container = running application

---

# 2️⃣ How Docker Builds an Image (Important Concept)

Docker executes instructions **line by line**.

Each instruction creates a **layer**.

```
FROM python
RUN apt install
COPY code
RUN pip install
CMD start
```

Every step = one layer
Layers are cached → builds become faster

---

---

# 3️⃣ Dockerfile Instructions (All Important Ones)

---

## 🔹 FROM — Base Image

> Defines the starting OS/runtime

```dockerfile
FROM python:3.11-slim
```

Must be the **first instruction** (except ARG before it).

You can use multiple FROM → multi-stage build.

---

## 🔹 WORKDIR — Working Directory

> Sets current directory inside container

```dockerfile
WORKDIR /app
```

Equivalent to `cd /app`

All next commands run inside `/app`

---

## 🔹 COPY — Copy Files

> Copies files from host → image

```dockerfile
COPY . .
COPY requirements.txt /app/
```

Runs during build time.
---

## 🔹 RUN — Execute Command During Build

> Used to install dependencies

```dockerfile
RUN apt-get update && apt-get install -y curl
RUN pip install -r requirements.txt
```

Executed while building image
Result saved in image layer

---

## 🔹 CMD — Default Runtime Command

> Runs when container starts

```dockerfile
CMD ["python","app.py"]
```

Can be overridden:

```bash
docker run image bash
```

---

## 🔹 ENTRYPOINT — Fixed Main Command

> Makes container behave like an executable

```dockerfile
ENTRYPOINT ["python"]
CMD ["app.py"]
```

Final command:

```
python app.py
```

If user passes argument:

```
docker run image test.py
→ python test.py
```

---

### CMD vs ENTRYPOINT

| Feature     | CMD          | ENTRYPOINT      |
| ----------- | ------------ | --------------- |
| Purpose     | default args | main executable |
| Override    | replaced     | appended        |
| Flexibility | high         | fixed behavior  |

Rule:

```
ENTRYPOINT = fixed program
CMD = default parameters
```

---

## 🔹 EXPOSE — Documentation Port

```dockerfile
EXPOSE 8000
```

Does NOT publish port
Just indicates app listens on port

---

## 🔹 ENV — Runtime Environment Variable

> Available inside container

```dockerfile
ENV PORT=8000
ENV DB_HOST=database
```

Accessible in app:

```python
os.getenv("PORT")
```

---

## 🔹 ARG — Build Time Variable

> Used only while building image

```dockerfile
ARG VERSION=3.11
FROM python:${VERSION}
```

Not available in running container.

---

### ARG vs ENV

| Feature                | ARG               | ENV               |
| ---------------------- | ----------------- | ----------------- |
| Available in build     | Yes               | Yes               |
| Available in container | No                | Yes               |
| Use case               | version selection | app configuration |

---

## 🔹 USER — Run as Non-Root

Security best practice

```dockerfile
RUN adduser -S appuser
USER appuser
```

Prevents privilege escalation.

---

## 🔹 VOLUME — Persistent Storage Location

```dockerfile
VOLUME /data
```

Marks folder to store data outside container lifecycle.

---

## 🔹 LABEL — Metadata

```dockerfile
LABEL version="1.0"
LABEL maintainer="siva"
```

Used for documentation & automation.

---

## 🔹 HEALTHCHECK — Container Health Monitoring

```dockerfile
HEALTHCHECK CMD curl -f http://localhost:8000/health || exit 1
```

Docker marks container healthy/unhealthy.

---

## 🔹 SHELL — Change Default Shell

```dockerfile
SHELL ["/bin/bash","-c"]
```

Used when scripts require bash features.

---

---

# 4️⃣ Multi-Stage Dockerfile Concept

Use multiple build stages:

```dockerfile
FROM node AS build
RUN npm run build

FROM nginx
COPY --from=build /app/build /usr/share/nginx/html
```

Benefits:

* smaller image
* better security
* removes build tools

---

---

# 5️⃣ Dockerfile Best Practices

---

## Layer Optimization

Bad:

```dockerfile
RUN apt update
RUN apt install curl
```

Good:

```dockerfile
RUN apt update && apt install -y curl
```

---

## Cache Optimization

Copy dependencies first:

```dockerfile
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
```

So dependency layer reused.

---

## Use Minimal Base Images

```
python:slim
node:alpine
nginx:alpine
```

Reduces size & vulnerabilities.

---

## Run as Non-Root

Always add USER in final stage.

---

---

# 6️⃣ Build vs Run Time

| Instruction | When Executed |
| ----------- | ------------- |
| RUN         | build time    |
| COPY        | build time    |
| ARG         | build time    |
| CMD         | runtime       |
| ENTRYPOINT  | runtime       |
| ENV         | runtime       |

---

---

# 7️⃣ Dockerfile Execution Flow

```
docker build
   ↓
Docker reads instructions
   ↓
Creates layers
   ↓
Image ready
   ↓
docker run
   ↓
CMD/ENTRYPOINT executed
```

---

---

#  Final Key Understanding

Dockerfile prepares environment
Container runs application

---

#  One-Line Summary

Dockerfile defines how to build an application environment in a reproducible way.

---

These notes cover all core Dockerfile concepts students need before advanced orchestration.
