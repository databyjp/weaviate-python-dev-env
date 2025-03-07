FROM python:3.10

# Install tools and utilities
RUN apt-get update && apt-get install -y \
    git \
    curl \
    vim \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Set up Python environment
RUN mkdir -p /workspaces/app
WORKDIR /workspaces/app

# Only try to copy requirements if it exists in your build context
COPY requirements.txt* ./
RUN if [ -f "requirements.txt" ]; then pip install --no-cache-dir -r requirements.txt; fi

