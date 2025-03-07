FROM python:3.10
WORKDIR /workspaces/app

# Install tools and utilities
RUN apt-get update && apt-get install -y \
    git \
    curl \
    vim \
    wget \
    && rm -rf /var/lib/apt/lists/*
