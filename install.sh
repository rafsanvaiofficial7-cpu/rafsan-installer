
#!/data/data/com.termux/files/usr/bin/bash

set -e

clear
echo "================================"
echo "       RAFSAN INSTALLER"
echo "       Developer: RAFSAN VAI"
echo "       Version: 1.0.0"
echo "================================"
echo

if ! command -v pkg >/dev/null 2>&1; then
    echo "ERROR: This installer requires Termux."
    exit 1
fi

echo "[1/3] Updating package list..."
pkg update -y

echo
echo "[2/3] Installing basic tools..."
pkg install -y python git curl

echo
echo "[3/3] Creating rafsan command..."

mkdir -p "$PREFIX/bin"

cat > "$PREFIX/bin/rafsan" <<'EOF'
#!/data/data/com.termux/files/usr/bin/bash

clear
echo "================================"
echo "       RAFSAN INSTALLER"
echo "       Developer: RAFSAN VAI"
echo "================================"
echo
echo "1. Check installation"
echo "2. About RAFSAN"
echo "3. Exit"
echo

read -r -p "Choose an option: " choice

case "$choice" in
  1)
    echo
    echo "Checking installed tools..."
    python --version
    git --version
    curl --version | head -n 1
    echo
    echo "RAFSAN base setup is ready!"
    ;;
  2)
    echo
    echo "RAFSAN INSTALLER"
    echo "Developer: RAFSAN VAI"
    echo "Version: 1.0.0"
    echo "Official repository:"
    echo "github.com/rafsanvaiofficial7-cpu/rafsan-installer"
    ;;
  3)
    exit 0
    ;;
  *)
    echo "Invalid option."
    ;;
esac
EOF

chmod +x "$PREFIX/bin/rafsan"

echo
echo "================================"
echo " RAFSAN BASE SETUP COMPLETED!"
echo " Now type: rafsan"
echo "================================"
