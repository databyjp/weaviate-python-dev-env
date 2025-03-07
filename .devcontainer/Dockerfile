FROM python:3.10

# Install tools and utilities
RUN apt-get update && apt-get install -y \
    git \
    curl \
    vim \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Set up Python environment
WORKDIR /workspaces/weaviatedev

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
