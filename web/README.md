# Docker Web Dashboard

A Flask-based web interface for running common Docker commands directly from your browser.

## Features

- **Container Status (`/`)**: View active and stopped containers (`docker ps -a`).
- **Images Overview (`/images`)**: List local Docker images (`docker images`).
- **Disk Usage (`/df`)**: Monitor space consumed by containers, images, and volumes (`docker system df`).
- **Container Management**:
  - **Start (`/start`)**: Spin up stopped containers using Container ID.
  - **Stop (`/stop`)**: Safely stop running containers.
- **System Maintenance (`/system`)**: Clean up unused containers, networks, and images (`docker system prune -f`).

## Prerequisites

- **Python 3.7+**
- **Flask**
- **Docker** installed and running locally.
- Permission to run `docker` commands without `sudo` (or run Flask as root/sudo).

## Directory Structure

Ensure your project templates are organized as follows:

```text
.
├── app.py
└── templates/
    ├── index.html
    ├── images.html
    ├── df.html
    ├── start.html
    ├── stop.html
    └── system.html
```