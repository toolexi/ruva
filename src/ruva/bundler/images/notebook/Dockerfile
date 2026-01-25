FROM ghcr.io/astral-sh/uv:python3.10-bookworm

# System deps (optional)
RUN apt-get update && apt-get install -y \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set workdir
WORKDIR /app

# Install Jupyter with uv
RUN uv pip install --system \
    jupyterlab \
    notebook

# Expose Jupyter port
EXPOSE 8888

# Start Jupyter
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
