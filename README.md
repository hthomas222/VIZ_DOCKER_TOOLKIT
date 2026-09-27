# Viz_Docker

Viz_Docker is a Python-based toolset designed to simplify Docker container and resource management. It offers two user interfaces depending on your workflow preference: an interactive **CLI tool** featuring formatted terminal output, and a lightweight **Web UI** built with Flask for browser-based operations.

---

## Repository Structure

```text
viz_docker/
├── README.md               <-- Primary Overview
├── cli/
│   ├── main.py             <-- Interactive Rich CLI application
│   └── README.md           <-- CLI-specific documentation
└── web/
    ├── app.py              <-- Flask Web dashboard application
    ├── templates/          <-- HTML templates for Web UI
    └── README.md           <-- Web app installation & setup guide