# Learn Docker
---

## **Day 1 — Foundations: Why Containers Exist**

Goal: Understand the problem Docker solves

We will learn:

* What virtualization means in computing
* How traditional servers evolved → Virtual Machines → Containers
* What a VM actually contains (hypervisor, guest OS, resources)
* What a container actually contains (process isolation, shared kernel)
* Difference between VM and container in:

  * startup time
  * resource usage
  * portability
  * scalability
* Real industry problems solved by containers (works on my machine issue)
* Basic terminology:

  * image
  * container
  * host
  * runtime

---

## **Day 2 — Running Containers & Accessing Applications**

Goal: Run our first container and access an app

We will learn:

* Networking basics needed for Docker:

  * IP address
  * ports
  * how browser reaches an application
* Docker architecture overview:

  * Docker CLI
  * Docker Engine
  * Docker Registry
* Installing Docker Desktop / Docker Engine
* Running containers using public images
* Basic Docker commands (run, ps, stop, rm, images)
* Understanding images vs containers
* Accessing an application via browser using ports
* Understanding: “application is running inside a container”

---

## **Day 3 — Building Our Own Image (React Application)**

Goal: Create our first custom Docker image

We will learn:

* Running React app without Docker (local setup problems)
* Why we build our own images instead of using public ones
* What a Dockerfile is and why it exists
* Build image → run container workflow
* Accessing our own application from browser
* Image tagging (versioning & naming)
* Docker Hub introduction
* Pushing image to Docker Hub

---

## **Day 4 — Backend Containers & Data Persistence**

Goal: Containerizing backend and managing runtime data

We will learn:

* Dockerizing a Python (FastAPI) application
* Inspecting running containers
* Viewing container logs
* Executing commands inside containers
* Why container data disappears
* Docker volumes concept
* Docker volume types
* Creating and attaching volumes
* Persisting application data

---

## **Day 5 — Docker Networking Concepts**

Goal: Understand how containers communicate

We will learn:

* What networking means in containers
* Bridge network concept
* Running multiple containers
* Container-to-container communication
* Accessing internet from container
* Different kinds of Docker networks
* Basic troubleshooting connectivity

---

## **Day 6 — Networking Practical Deep Dive**

Goal: Real hands-on networking behavior

We will do:

* Create custom networks
* Connect containers to same network
* Multi-container communication demo
* Network isolation demo
* Understanding internal vs external access

---

## **Day 7 — Dockerfile Deep Dive**

Goal: Understand how images are built internally

We will learn:

* All Dockerfile instructions explained
* Build vs runtime commands
* Entrypoint VS Cmd difference
* Best practices in writing Dockerfile
* Optimization strategies

---

## **Day 8 — Multi-Stage Builds & Image Optimization**

Goal: Production-ready images

We will learn:

* Why large images are bad
* Multi-stage builds concept
* Build stage vs runtime stage
* Creating lightweight production images
* Security improvements in containers

---

## **Day 9 — Docker Compose & Real Application**

Goal: Run complete application stack

We will learn:

* Docker Compose basics
* Running multiple services together
* Deploying a 3-tier application:

  * frontend
  * backend
  * database
* Container resource limits
* Introduction to orchestration (Docker Swarm concept overview)

---

# Course Outcome

By the end, students will be able to:

* Understand containers internally
* Build production-ready images
* Run multi-service applications
* Debug container issues
---
