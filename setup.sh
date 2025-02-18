#!/bin/bash
set -e

echo "Installing uv package manager..."
# Install uv via its standalone installer
curl -LsSf https://astral.sh/uv/install.sh | sh

# Ensure uv is available in PATH (adjust if necessary)
export PATH="$HOME/.local/bin:$PATH"

echo "Syncing production dependencies with uv..."
# Sync production dependencies; skip dev packages
uv sync --frozen --no-dev --group prod

echo "Compiling requirements.txt from requirements.in..."
# Compile requirements.txt from your base requirements file
uv pip compile requirements.in -o requirements.txt >/dev/null
# Optionally, add your package in editable mode:
echo "-e ." >> requirements.txt

echo "Installing dependencies to the system environment..."
# Install the compiled dependencies into the system (global) Python environment
uv pip install --system -r requirements.txt

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
