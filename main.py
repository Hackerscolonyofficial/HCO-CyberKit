from flask import Flask, request, render_template from threading import Thread import os, time import pyngrok

app = Flask(name)

@app.route('/') def index(): return render_template('index.html')

@app.route('/submit', methods=['POST']) def submit(): number = request.form.get('number') print(f"[+] Call spoof sent to: {number}") print("[!] Simulating voice playback and fake alert...") print("\n[!!] ALERT: Your Aadhar card, PAN card, and social accounts have been hacked!\nYou are under surveillance by Cyber Cell.") return "<h2 style='color:red'>Voice alert sent successfully!</h2>"

def tunnel(): os.system("cloudflared tunnel --url http://localhost:5000")

def run(): app.run(host="0.0.0.0", port=5000)

if name == 'main': Thread(target=run).start() Thread(target=tunnel).start()

