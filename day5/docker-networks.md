

---

# Docker Networking — Detailed Notes (Practical Understanding)

---

# What is Docker Networking?

> Docker networking allows containers to communicate with each other, the host machine, and the internet.

Containers behave like small computers.
To talk to another container or a browser → networking is required.

---

## Two Types of Communication

| Communication         | Example            |
| --------------------- | ------------------ |
| Container → Container | frontend → backend |
| Container → Internet  | download packages  |
| Host → Container      | browser access     |

---

---

# List Existing Networks

```bash
docker network ls
```

You will see:

```
bridge
host
none
```

Docker automatically creates these default networks.

---

---

# Bridge Network (Default)

## What it is

Private internal network created by Docker.

All containers automatically join this network if no network specified.

---

## Behavior

* Containers get private IP address
* Can access internet
* Cannot access each other using name (only IP)
* External access requires port mapping

---

## Example

Run container:

```bash
docker run -d --name web nginx
```

Check IP:

```bash
docker inspect web
```

Access in browser:

```
http://localhost:8080  (only if -p used)
```

---

## Key Learning

Default bridge provides connectivity but not service discovery.

---

---

# Custom Bridge Network (User Defined)

## Create Network

```bash
docker network create appnet
```

---

## Run Containers

```bash
docker run -d --name backend --network appnet nginx
docker run -it --network appnet alpine sh
```

Inside container:

```sh
ping backend
```

Works 

---

## Behavior

* Containers communicate using names
* Automatic DNS available
* Better isolation
* Recommended for applications

---

## Key Difference from Default Bridge

| Feature             | Default | Custom |
| ------------------- | ------- | ------ |
| DNS name resolution | No      | Yes    |
| Recommended         | No      | Yes    |
| Service discovery   | No      | Yes    |

---

---

# Port Mapping (Access From Browser)

Containers are private by default.

To expose app to host:

```bash
docker run -p 8080:80 nginx
```

Meaning:

```
Host Port 8080 → Container Port 80
```

Now browser can access container.

---

---

#  Host Network

## Run Container

```bash
docker run --network host nginx
```

---

## Behavior

* Container shares host network
* No separate IP
* No port mapping required
* Access directly using localhost

Open:

```
http://localhost
```

---

## Use Case

High performance apps

---

---

#  None Network

## Run Container

```bash
docker run --network none alpine
```

---

## Behavior

* No internet
* No container communication
* Only loopback (self)

---

## Use Case

Security or batch processing

---

---

#  Connecting Container to Multiple Networks

Create networks:

```bash
docker network create frontend
docker network create backend
```

Run container in one network:

```bash
docker run -d --name api --network frontend nginx
```

Attach another network:

```bash
docker network connect backend api
```

Now container communicates with both networks.

---

---

#  Disconnect Container from Network

```bash
docker network disconnect backend api
```

---

---

# Inspect Network Details

```bash
docker network inspect appnet
```

Shows:

* connected containers
* IP addresses
* subnet

---

---

# Remove Network

```bash
docker network rm appnet
```

(Only works if no container attached)

---

---

#  Practical Architecture Example

```
public-network:
   frontend

private-network:
   backend
   database

backend connected to both
```

Frontend cannot directly access database.

---

---

# Important Rules to Remember

1. Containers inside same network can communicate
2. Custom network allows name-based communication
3. Port mapping needed for browser access
4. Host network removes isolation
5. None network blocks communication
6. Networks provide isolation and organization

---


