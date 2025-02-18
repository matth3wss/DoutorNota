#!/bin/bash
set -e

echo "Installing uv package manager..."
# Install uv via its standalone installer
curl -LsSf https://astral.sh/uv/install.sh | sh

# Make sure uv is in your PATH (adjust if needed)
export PATH="$HOME/.local/bin:$PATH"

echo "Syncing production dependencies with uv..."
# Sync production dependencies (skip dev packages)
uv sync --frozen --no-dev --group prod

echo "Compiling requirements.txt from requirements.in..."
# This is your usual command
uv pip compile requirements.in -o requirements.txt >/dev/null
# Optionally, add your package in editable mode
echo "-e ." >> requirements.txt

echo "Installing dependencies to the system environment..."
# Install dependencies globally (Heroku does not use a virtualenv by default)
uv pip install --system -r requirements.txt

echo "Clearing requirements.txt to prevent Heroku's buildpack from re-installing packages..."
# Truncate the file so pip install -r requirements.txt is a no-op
: > requirements.txt

echo "Setting up Streamlit configuration..."
mkdir -p ~/.streamlit

cat <<EOF > ~/.streamlit/credentials.toml
[general]
email = "your-email@domain.com"
EOF

cat <<EOF > ~/.streamlit/config.toml
[server]
headless = true
enableCORS = false
port = \$PORT
EOF

echo "Build script completed successfully."
