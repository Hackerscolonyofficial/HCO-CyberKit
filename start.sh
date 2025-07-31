#!/data/data/com.termux/files/usr/bin/bash
clear
echo "This tool is not free!"
echo "Redirecting to our YouTube channel for access..."
termux-open-url https://youtube.com/@hackers_colony_tech?si=pvdCWZggTIuGb0ya
sleep 10
clear
echo -e "\e[1;32m[+] Welcome to \e[1;31mHCO-CyberKit by Azhar\e[0m"
sleep 2
echo "[*] Installing requirements..."
pip install flask pyngrok
pkg install cloudflared -y
echo "[*] Starting server..."
python main.py
