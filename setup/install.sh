#!/usr/bin/env bash
# Lending kit setup for macOS and Linux: Git, Node.js LTS (via nvm), PATH in your shell profile.
# Run in Terminal:
#   curl -fsSL https://monforje.github.io/lendingi-2026/setup/install.sh | bash
set -euo pipefail

say()  { printf '\n\033[1;36m== %s\033[0m\n' "$1"; }
ok()   { printf '   \033[32mOK\033[0m  %s\n' "$1"; }
warn() { printf '   \033[33m!!\033[0m  %s\n' "$1"; }
has()  { command -v "$1" >/dev/null 2>&1; }
ask()  { local a=""; if [ -r /dev/tty ]; then read -r -p "   $1" a </dev/tty || true; fi; printf '%s' "$a"; }

OS="$(uname -s)"
SUDO=""; if [ "$(id -u)" -ne 0 ] && has sudo; then SUDO="sudo"; fi

# Shell profile where PATH is written
case "${SHELL:-}" in
  */zsh)  RC="$HOME/.zshrc" ;;
  */bash) if [ "$OS" = "Darwin" ]; then RC="$HOME/.bash_profile"; else RC="$HOME/.bashrc"; fi ;;
  *)      RC="$HOME/.profile" ;;
esac
touch "$RC"
printf '\033[1;36mLending kit setup: Git + Node.js LTS. Profile: %s\033[0m\n' "$RC"

# 1. Git (+ curl)
say "Git"
if [ "$OS" = "Darwin" ]; then
  if xcode-select -p >/dev/null 2>&1; then ok "$(git --version)"; else
    warn "A window will open: press Install (Command Line Tools, 5-15 min)"
    xcode-select --install || true
    for _ in $(seq 1 180); do xcode-select -p >/dev/null 2>&1 && break; sleep 10; done
    xcode-select -p >/dev/null 2>&1 && ok "$(git --version)" || { warn "Finish Command Line Tools install and run this script again"; exit 1; }
  fi
else
  if has git && has curl; then ok "$(git --version)"; else
    if   has apt-get; then $SUDO apt-get update -y && $SUDO apt-get install -y git curl ca-certificates
    elif has dnf;     then $SUDO dnf install -y git curl
    elif has yum;     then $SUDO yum install -y git curl
    elif has pacman;  then $SUDO pacman -Sy --noconfirm git curl
    elif has zypper;  then $SUDO zypper --non-interactive install git curl
    elif has apk;     then $SUDO apk add git curl bash
    else warn "Unknown package manager: install git and curl manually"; exit 1; fi
    ok "$(git --version)"
  fi
fi

# 2. Node.js LTS through nvm (no sudo, easy to update)
say "Node.js LTS"
export NVM_DIR="$HOME/.nvm"
if [ ! -s "$NVM_DIR/nvm.sh" ]; then
  NVM_VER="$(curl -fsSL https://api.github.com/repos/nvm-sh/nvm/releases/latest 2>/dev/null | sed -n 's/.*"tag_name": *"\(v[^"]*\)".*/\1/p' | head -1 || true)"
  NVM_VER="${NVM_VER:-v0.40.3}"
  curl -fsSL "https://raw.githubusercontent.com/nvm-sh/nvm/$NVM_VER/install.sh" | PROFILE="$RC" bash >/dev/null
  ok "nvm $NVM_VER"
fi
# nvm.sh is not compatible with `set -u`
set +u
# shellcheck disable=SC1091
. "$NVM_DIR/nvm.sh"
nvm install --lts || { warn "Could not download Node.js from nodejs.org. Check internet/VPN and run the script again"; exit 1; }
nvm alias default 'lts/*' >/dev/null
nvm use default >/dev/null
set -u
ok "node $(node -v), npm $(npm -v)"

# PATH block in profile (nvm usually writes it, this makes sure)
if ! grep -q 'NVM_DIR' "$RC"; then
  {
    echo ''
    echo '# nvm + Node.js (lending kit)'
    echo 'export NVM_DIR="$HOME/.nvm"'
    echo '[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"'
  } >> "$RC"
fi
if ! grep -q '.local/bin' "$RC"; then
  echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$RC"
fi
ok "PATH written to $RC"

# 3. VS Code (macOS with Homebrew only; otherwise link)
say "VS Code"
if has code; then ok "VS Code found"
elif [ "$OS" = "Darwin" ] && has brew; then brew install --cask visual-studio-code && ok "VS Code installed"
else warn "Download VS Code: https://code.visualstudio.com/download"; fi

# 4. Git settings
say "Git settings"
git config --global init.defaultBranch main
git config --global core.autocrlf input
if [ -z "$(git config --global user.name || true)" ]; then
  n="$(ask 'Your name for commits (Enter = skip): ')"; [ -n "$n" ] && git config --global user.name "$n"
fi
if [ -z "$(git config --global user.email || true)" ]; then
  e="$(ask 'Email from GitHub (Enter = skip): ')"; [ -n "$e" ] && git config --global user.email "$e"
fi
ok "branch main, user: $(git config --global user.name || true) <$(git config --global user.email || true)>"

say "Done"
printf '\033[32mOpen a NEW terminal window (or run: source %s). Then check: node -v; npm -v; git --version\033[0m\n' "$RC"
