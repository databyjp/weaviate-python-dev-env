FROM python:3.11-slim-bullseye
WORKDIR /workspaces/app

# Install tools and utilities
RUN apt-get update && apt-get install -y \
    git \
    curl \
    vim \
    wget \
    && rm -rf /var/lib/apt/lists/*
