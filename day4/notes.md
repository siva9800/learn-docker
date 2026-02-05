python -m venv myenv
myenv\Scripts\activate.ps1  # Windows PowerShell

pip install fastapi uvicorn

uvicorn main:app --reload


#how to login to a container

```bash
docker exec -it <container-name/id> bin/bash or -- sh
```



### docker volumes
> Container storage is NOT permanent.

---

# 2️⃣ Why Container Data Is Lost?

Let’s understand this with real behavior.

---

## Scenario

You run a container:

```bash
docker run -it ubuntu bash
```

Inside container:

```bash
echo "Hello Docker" > test.txt
```

Now exit container:

```bash
exit
```

Remove container:

```bash
docker rm <container-id>
```

---

### What Happens?

❌ `test.txt` is gone
❌ Data is deleted

---

## Why?

Because:

> Container writable layer is destroyed when container is removed.

---

# 🔥 Important Rule

```
Container = Temporary
```

So:

❌ Do NOT store important data inside container filesystem.

---

# 3️⃣ Why Is This a Big Problem?

Real applications store:

* Database data
* Uploaded files
* Logs
* Reports
* User content

If container restarts:

❌ Data loss = Disaster

---

# 4️⃣ Solution — Docker Volumes

---

## What Is a Docker Volume?

### Definition:

> **Docker Volume is a persistent storage location outside the container filesystem that is managed by Docker and used to store container data permanently.**

---

## Where Volume Is Stored?

Volume data is stored on:

👉 Host machine disk
NOT inside container.

---

## Visual Architecture

![Image](https://docs.docker.com/engine/storage/images/volumes-shared-storage.webp)

![Image](https://miro.medium.com/0%2A3WbZgnc5484HqKks.png)

![Image](https://i.sstatic.net/PmcBY.png)

---

### Data Flow

```
Application
↓
Container
↓
Docker Volume
↓
Host Disk
```

---

# 5️⃣ Difference: Container Filesystem vs Volume

| Feature                        | Container FS | Docker Volume |
| ------------------------------ | ------------ | ------------- |
| Persistence                    | Temporary    | Permanent     |
| Deleted when container removed | Yes          | No            |
| Shared between containers      | No           | Yes           |
| Production safe                | ❌ No         | ✅ Yes         |
| Use case                       | App runtime  | Data storage  |

---

# 6️⃣ Types of Docker Volumes

Docker supports mainly:

---

## 🔹 1. Named Volumes (Recommended)

Docker manages storage location.

Example:

```
mydata
```

Stored internally by Docker.

---

### Advantages:

✔ Easy to manage
✔ Portable
✔ Safe
✔ Production ready

---

## 🔹 2. Bind Mounts

Maps host folder to container folder.

Example:

```
/home/user/data → /app/data
```

---

### Advantages:

✔ Direct access from host
✔ Useful for development

---

### Disadvantages:

❌ Depends on host path
❌ Less portable

---

# 🧩 Hands-On Section (VERY IMPORTANT)

---

# 1️⃣ Create Docker Volume

Create named volume:

```bash
docker volume create myvolume
```

---

## Check Volume List

```bash
docker volume ls
```

Output:

```
myvolume
```

---

# 2️⃣ Attach Volume To Container

Now run container with volume:

```bash
docker run -it -v myvolume:/data ubuntu bash
```

---

### Meaning:

```
myvolume  →  /data (inside container)
```

---

# 3️⃣ Write Data Inside Container

Inside container:

```bash
cd /data
echo "Docker Volume Test" > file.txt
ls
```

You will see:

```
file.txt
```

Exit container:

```bash
exit
```

---

# 4️⃣ Delete Container

```bash
docker ps -a
docker rm <container-id>
```

---

# 5️⃣ Start New Container Using Same Volume

```bash
docker run -it -v myvolume:/data ubuntu bash
```

---

Check:

```bash
cd /data
ls
```

---

### Output:

```
file.txt
```

🎉 DATA PERSISTED!

---

# 🧠 Teaching Point

Tell students:

> Volume lives independently from container.
> Container can die — data survives.

---

# 7️⃣ Bind Mount Example (Development Use)

---

## Run With Host Folder

Example:

```bash
docker run -it -v /c/users/siva/data:/app/data ubuntu bash
```

---

### Meaning:

```
Windows Folder → Container Folder
```

Now any file created inside container:

✔ Appears on host
✔ Real-time sync

---

# ⚠ Warning

Bind mounts:

✔ Good for dev
❌ Avoid in production

---

# 8️⃣ Using Volume With Database (REAL WORLD SCENARIO)

This is the **most important use case**.

---

## Example: MySQL Without Volume

Run:

```bash
docker run -d mysql
```

Store data → container deleted → ❌ DATA LOST.

---

## Correct Way (With Volume)

---

### Step 1: Create Volume

```bash
docker volume create mysqldata
```

---

### Step 2: Run MySQL With Volume

```bash
docker run -d \
  -v mysqldata:/var/lib/mysql \
  -e MYSQL_ROOT_PASSWORD=root \
  mysql
```

---

### Meaning:

```
Database data directory → Docker volume
```

---

Now:

✔ Restart container
✔ Delete container
✔ Recreate container

Data is still SAFE ✅

---

# 9️⃣ Important Production Rule (MUST TEACH)

---

## NEVER Store These Inside Container FS:

❌ Database files
❌ Uploaded files
❌ Logs
❌ User content

---

## ALWAYS Use Volume For:

✔ Databases
✔ Persistent storage
✔ Application state

---

# 🔥 Interview Level Questions (Explain To Students)

---

### Q: Why do containers lose data?

Because container filesystem is ephemeral and removed with container lifecycle.

---

### Q: Why volumes are preferred?

Because they persist data independently from containers.

---

### Q: Difference between bind mount and volume?

Bind mount maps host path directly. Volume is Docker-managed storage.

---

# 🏁 Summary 

---

### Container Storage:

Temporary ❌

---

### Docker Volume:

Persistent ✅
Production-ready ✅

---

### Named Volume:

Best for production

---

### Bind Mount:

Best for development

---

### Databases:

Always use volumes

---
