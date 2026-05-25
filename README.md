# Cloud-Native System Metrics API

A lightweight, high-performance REST API built to monitor server hardware metrics in real-time. Containerized with Docker and deployed to AWS EC2 using a fully automated CI/CD pipeline via GitHub Actions.

##  Architecture & Tech Stack
* **Backend:** Python 3.12, FastAPI, Uvicorn, psutil
* **Package Management:** uv (Rust-based)
* **Containerization:** Docker
* **Cloud Infrastructure:** AWS EC2 (Ubuntu Linux)
* **CI/CD:** GitHub Actions (Automated SSH deployments)

##  Core Features
* **Live Hardware Telemetry:** Endpoints to read real-time CPU and RAM utilization.
* **Fully Containerized:** Environment isolation guaranteed via Docker.
* **Zero-Downtime Deployment Pipeline:** Pushing to the `main` branch automatically rebuilds the Docker image and restarts the container on the live AWS server without manual intervention.

##  Local Development

1. **Clone the repository:**
   `git clone https://github.com/YOUR_USERNAME/system-metrics-api.git`
2. **Build the Docker Image:**
   `docker build -t system-metrics-api .`
3. **Run the Container:**
   `docker run -d -p 8000:8000 system-metrics-api`
4. **Access the API:** Navigate to `http://localhost:8000/docs` to view the interactive Swagger documentation.

##  CI/CD Pipeline (GitHub Actions)
This repository contains a `deploy.yml` workflow. Upon pushing to `main`, the pipeline:
1. Authenticates securely with the AWS EC2 instance via SSH.
2. Pulls the latest code.
3. Rebuilds the Docker image dynamically.
4. Gracefully shuts down the old container and boots the new instance on port 8000.
