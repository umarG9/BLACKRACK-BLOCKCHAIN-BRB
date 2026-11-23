# app.py - BRB ALL IN ONE - PYTHON FILE ALL - DEPLOYMENT READY - FILE BIYU ONLY - PYTHON + HTML
# No pip install needed - Uses only built-in Python - Works on Pydroid, PC, Render, PythonAnywhere, VPS
import hashlib, time, random, json, os
from datetime import datetime, timedelta
from collections import defaultdict
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

# ==================== BRB CORE - ALL MODULES IN ONE FILE ====================
class BRBCore:
    def __init__(self):
        self.total_supply = 0
        self.balances = defaultdict(int)
        self.nfts = []
        self.stakes = {}
        self.tvl = 0
        self.total_data_mb = 0
        self.total_data_rbr = 0
        self.users_data = {}
        self.total_energy_kwh = 0
        self.total_energy_rbr = 0
        self.subs = {}
        self.subs_total_rbr = 0
        self.miners = {}
        self.blocks = []
        self.total_mined = 0
        self.total_hash = 0
        self.threats_blocked = 0
        self.security_logs = []
        self.tasks_done = 0
        self.tasks_total_rbr = 0
        self.bullish = 78
        self.plans = {
            "NOMA FARMER": {"price": 500, "tasks": 30, "kwh": 1200, "data": 6000, "hash": 100, "desc": "Shuka Masara Shinkafa - Tractor+Drone+Soil pH+Weather AI"},
            "WELDER": {"price": 800, "tasks": 20, "kwh": 1500, "data": 4000, "hash": 150, "desc": "Waldi Kofa Tagar - Welding+3D Metal Print"},
            "MECHANIC": {"price": 700, "tasks": 25, "kwh": 1000, "data": 5000, "hash": 120, "desc": "Gyaran Mota Babur Janareto Solar - AI Diagnosis 99%"},
            "DOCTOR": {"price": 1000, "tasks": 50, "kwh": 800, "data": 10000, "hash": 200, "desc": "AI Doctor Ciwon kai Zazzabi - Diagnosis 99% - Telemedicine VR - Doctor Teaches All"},
            "TEACHER": {"price": 600, "tasks": 60, "kwh": 500, "data": 15000, "hash": 250, "desc": "Maths x+2=5->x=3! English My name is Boko - 1000 Students - Metaverse VR - Teacher Teaches All"},
            "ENGINEER": {"price": 1200, "tasks": 15, "kwh": 2000, "data": 8000, "hash": 300, "desc": "Gini Building Tubali Block - 3D Printing House - 1 Day=1 House"},
            "SECURITY": {"price": 300, "tasks": 100, "kwh": 400, "data": 20000, "hash": 200, "desc": "Tsaro Barawo Thief Gobara Fire - Face Recognition - Quantum Resistant - SERVER SECURITY 99.99%"},
            "ENERGY": {"price": 2000, "tasks": 10, "kwh": -5000, "data": 1000, "hash": 500, "desc": "PRODUCES ENERGY! Solar 10MW - 5000 kWh/day - Sells to ETH BTC SOL - BEST MINER"},
            "ALL IN ONE": {"price": 5000, "tasks": 500, "kwh": 5000, "data": 100000, "hash": 1000, "desc": "DUKA A ROBOT DAYA! Noma+Welder+Mechanic+Doctor+Teacher+All - AGI Quantum Brain 1M Qubits - FINAL ULTIMATE - HUMAN DOES NOTHING ROBOT DOES EVERYTHING"}
        }
    
    def mint(self, user, amount, nft_type):
        self.total_supply += amount
        self.balances[user] += amount
        tx = "0x" + hashlib.sha256(f"{user}{amount}{time.time()}".encode()).hexdigest()[:10]
        nft_id = f"BRB-{nft_type[:20].replace(' ','-')}-{hashlib.sha256(f'{user}{amount}'.encode()).hexdigest()[:6].upper()}"
        self.nfts.append({"user": user, "amount": amount, "type": nft_type, "tx": tx, "nft_id": nft_id, "time": datetime.now().strftime("%H:%M:%S")})
        return {"user": user, "amount": amount, "type": nft_type, "tx": tx, "nft_id": nft_id}
    
    def stake(self, user, amount):
        reward = amount * 78/100/365
        self.stakes[user] = self.stakes.get(user, 0) + amount
        self.tvl += amount
        return {"user": user, "amount": amount, "apy": "78%", "reward": reward, "tvl": self.tvl}
    
    def track_data(self, user, page, mb):
        earned = mb * 1
        self.total_data_mb += mb
        self.total_data_rbr += earned
        if user not in self.users_data:
            self.users_data[user] = {"mb": 0, "rbr": 0}
        self.users_data[user]["mb"] += mb
        self.users_data[user]["rbr"] += earned
        tx = "0x" + hashlib.sha256(f"{user}{page}{mb}{time.time()}".encode()).hexdigest()[:10]
        return {"user": user, "page": page, "mb": mb, "rbr": earned, "tx": tx, "total_mb": self.total_data_mb, "total_rbr": self.total_data_rbr}
    
    def produce_energy(self, source, kwh):
        self.total_energy_kwh += kwh
        self.total_energy_rbr += kwh
        return {"source": source, "kwh": kwh, "rbr": kwh, "total_kwh": self.total_energy_kwh}
    
    def provide_energy(self, blockchain, kwh):
        tx = "0x" + hashlib.sha256(f"{blockchain}{kwh}{time.time()}".encode()).hexdigest()[:10]
        return {"blockchain": blockchain, "kwh": kwh, "rbr": kwh, "tx": tx}
    
    def subscribe(self, user, plan, months=1):
        if plan not in self.plans:
            return None
        p = self.plans[plan]
        total = p["price"] * months
        sub_id = f"BRB-SUB-{plan.replace(' ','-')}-{user[:5].upper()}-{hashlib.sha256(f'{user}{plan}{time.time()}'.encode()).hexdigest()[:6].upper()}"
        tx = "0x" + hashlib.sha256(f"{user}{plan}{months}{time.time()}".encode()).hexdigest()[:10]
        self.subs[sub_id] = {"user": user, "plan": plan, "months": months, "price": total, "tasks": p["tasks"]*months, "done": 0, "remaining": p["tasks"]*months, "desc": p["desc"], "kwh": p["kwh"], "data": p["data"], "hash": p["hash"]}
        self.subs_total_rbr += total
        return {"sub_id": sub_id, "user": user, "plan": plan, "price": total, "months": months, "tasks": p["tasks"]*months, "tx": tx, "desc": p["desc"]}
    
    def do_task(self, sub_id, detail):
        if sub_id not in self.subs:
            return None
        s = self.subs[sub_id]
        if s["remaining"] <= 0:
            return {"error": "No tasks remaining"}
        s["done"] += 1
        s["remaining"] -= 1
        data = random.randint(50, 300)
        data_rbr = data * 1
        block_rbr = 100 + random.randint(0, 50)
        energy_rbr = abs(s["kwh"]//s["tasks"]) if s["kwh"] < 0 else 0
        total_rbr = data_rbr + block_rbr + energy_rbr
        self.tasks_done += 1
        self.tasks_total_rbr += total_rbr
        tx = "0x" + hashlib.sha256(f"{sub_id}{detail}{time.time()}".encode()).hexdigest()[:10]
        task_nft = f"BRB-TASK-{s['plan'][:10]}-{hashlib.sha256(f'{detail}'.encode()).hexdigest()[:6].upper()}"
        block_hash = "0x" + hashlib.sha256(f"{sub_id}{detail}{time.time()}".encode()).hexdigest()[:16]
        return {"sub_id": sub_id, "plan": s["plan"], "user": s["user"], "detail": detail, "data_mb": data, "data_rbr": data_rbr, "block_rbr": block_rbr, "energy_rbr": energy_rbr, "total_rbr": total_rbr, "tx": tx, "task_nft": task_nft, "block_hash": block_hash, "done": s["done"], "remaining": s["remaining"]}
    
    def register_miner(self, robot_id, rtype):
        if rtype not in self.plans:
            rtype = "ALL IN ONE"
        base = self.plans[rtype]["hash"]
        boost = random.randint(0, 100)
        final = base * (1 + boost/100)
        self.miners[robot_id] = {"type": rtype, "hashrate": final, "base": base, "boost": boost, "mined": 0, "blocks": 0}
        self.total_hash += final
        return {"robot_id": robot_id, "type": rtype, "hashrate": final, "boost": boost, "total_hash": self.total_hash}
    
    def mine_block(self, robot_id, task_detail):
        if robot_id not in self.miners:
            self.register_miner(robot_id, "ALL IN ONE")
        m = self.miners[robot_id]
        block_hash = hashlib.sha256(f"{robot_id}{task_detail}{time.time()}".encode()).hexdigest()
        data = random.randint(50, 300)
        data_rbr = data * 1
        block_rbr = 100 + random.randint(0, 50)
        total = data_rbr + block_rbr
        energy = -5 if m["type"] == "ENERGY" else m["hashrate"]/100*0.1
        m["mined"] += total
        m["blocks"] += 1
        self.total_mined += total
        block_num = len(self.blocks) + 1
        block = {"block_number": block_num, "block_hash": block_hash, "robot_id": robot_id, "type": m["type"], "task": task_detail, "data_mb": data, "data_rbr": data_rbr, "block_rbr": block_rbr, "total_rbr": total, "energy": energy, "hashrate": m["hashrate"], "tx": "0x"+block_hash[:12], "time": datetime.now().strftime("%H:%M:%S")}
        self.blocks.append(block)
        return block
    
    def block_threat(self, ttype, detail):
        self.threats_blocked += 1
        tx = "0x" + hashlib.sha256(f"{ttype}{detail}{time.time()}".encode()).hexdigest()[:10]
        nft = f"BRB-SECURITY-NFT-{ttype.replace(' ','-')}-{hashlib.sha256(f'{detail}'.encode()).hexdigest()[:6].upper()}"
        responses = {
            "BARAWO THIEF": f"AI Camera → Face Recognition → Thief DB Match → Thief {detail} → Alarm+Lock+Police+NFT - BLOCKED - Server Secure 99.99%",
            "GOBARA FIRE": f"Smoke Sensor → AI → Fire {detail} → Water Sprinkler+Fire Service+Evacuate+NFT - BLOCKED",
            "CYBER HACK": f"Firewall → AI → Hack {detail} → Quantum Resistant Lattice+Dilithium → Block IP+Log+NFT - BLOCKED",
            "BLOCKCHAIN 51% ATTACK": f"Consensus → AI → 51% attack {detail} → Block attacker+Slash+Secure+NFT - BLOCKED",
            "SERVER DDOS": f"Monitor → AI → DDoS {detail} → AI Filter → Block malicious+Keep legit+Server online 99.99%+NFT - BLOCKED",
            "DATA BREACH": f"Monitor → AI → Data breach {detail} → Encrypt+Block+Alert+NFT - BLOCKED",
            "ENERGY THEFT": f"Monitor → AI → Energy theft {detail} → Detect+Block+Alert+NFT - BLOCKED - RBR=Energy Layer"
        }
        resp = responses.get(ttype, f"AI → {ttype}: {detail} → Block+NFT - BLOCKED - Server Secure 99.99%")
        log = {"time": datetime.now().strftime("%H:%M:%S"), "type": ttype, "detail": detail, "response": resp, "tx": tx, "nft": nft, "blocked": self.threats_blocked}
        self.security_logs.append(log)
        return log
    
    def dashboard(self):
        return {
            "total_supply": self.total_supply,
            "nfts": len(self.nfts),
            "balances": dict(self.balances),
            "tvl": self.tvl,
            "stakes": len(self.stakes),
            "total_data_mb": self.total_data_mb,
            "total_data_gb": self.total_data_mb/1024,
            "total_data_rbr": self.total_data_rbr,
            "users_data": len(self.users_data),
            "total_energy_kwh": self.total_energy_kwh,
            "total_energy_rbr": self.total_energy_rbr,
            "subs": len(self.subs),
            "subs_total_rbr": self.subs_total_rbr,
            "subs_total_usd": self.subs_total_rbr*0.01,
            "miners": len(self.miners),
            "blocks": len(self.blocks),
            "total_mined": self.total_mined,
            "total_hash": self.total_hash,
            "threats_blocked": self.threats_blocked,
            "security_logs": len(self.security_logs),
            "tasks_done": self.tasks_done,
            "tasks_total_rbr": self.tasks_total_rbr,
            "bullish": self.bullish
        }

core = BRBCore()

# ==================== HTTP SERVER - DEPLOYMENT READY ====================
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        
        if path == "/" or path == "/index.html":
            # Serve index.html if exists, else serve built-in
            if os.path.exists("index.html"):
                with open("index.html", "rb") as f:
                    content = f.read()
            else:
                content = b"<h1>BRB - Put index.html in same folder as app.py - 2 files only</h1><p>File 1: app.py (this file) - File 2: index.html (from second code) - Then run python app.py - Open http://localhost:8000</p>"
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(content)
        
        elif path == "/api/dashboard":
            self.send_json(core.dashboard())
        
        elif path == "/api/blocks":
            self.send_json({"blocks": core.blocks[-20:]})  # Last 20 blocks
        
        elif path == "/api/logs":
            self.send_json({"security_logs": core.security_logs[-20:], "nfts": core.nfts[-20:]})
        
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found - Use / , /api/dashboard , /api/blocks , /api/logs")
    
    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        length = int(self.headers.get('content-length', 0))
        body = self.rfile.read(length) if length > 0 else b"{}"
        try:
            data = json.loads(body.decode() if body else "{}")
        except:
            data = {}
        
        result = {}
        if path == "/api/mint":
            result = core.mint(data.get("user","Anonymous"), int(data.get("amount",1000)), data.get("type","BRB NFT"))
        elif path == "/api/stake":
            result = core.stake(data.get("user","Anonymous"), int(data.get("amount",1000)))
        elif path == "/api/data":
            result = core.track_data(data.get("user","Anonymous"), data.get("page","Page"), int(data.get("mb",100)))
        elif path == "/api/energy":
            result = core.produce_energy(data.get("source","Solar"), int(data.get("kwh",1000)))
        elif path == "/api/provide-energy":
            result = core.provide_energy(data.get("blockchain","ETH"), int(data.get("kwh",10000)))
        elif path == "/api/subscribe":
            result = core.subscribe(data.get("user","Anonymous"), data.get("plan","NOMA FARMER"), int(data.get("months",1)))
        elif path == "/api/task":
            result = core.do_task(data.get("sub_id",""), data.get("detail","Task"))
        elif path == "/api/register-miner":
            result = core.register_miner(data.get("robot_id",f"BRB-ROBOT-{random.randint(1,999):03d}"), data.get("type","ALL IN ONE"))
        elif path == "/api/mine":
            result = core.mine_block(data.get("robot_id",f"BRB-ROBOT-{random.randint(1,999):03d}"), data.get("task","Mining RBR"))
        elif path == "/api/security":
            result = core.block_threat(data.get("type","BARAWO THIEF"), data.get("detail","Threat"))
        else:
            result = {"error": "Unknown endpoint", "use": ["/api/mint","/api/stake","/api/data","/api/energy","/api/provide-energy","/api/subscribe","/api/task","/api/register-miner","/api/mine","/api/security","/api/dashboard"]}
        
        self.send_json(result)
    
    def send_json(self, obj):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
        self.wfile.write(json.dumps(obj, indent=2).encode())
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

def run_server():
    port = int(os.environ.get("PORT", 8000))  # For Render, Railway, etc - Uses PORT env
    server_address = ('', port)
    httpd = HTTPServer(server_address, Handler)
    print("="*110)
    print(f"🚀 BRB ALL IN ONE - PYTHON FILE ALL - DEPLOYMENT READY - RUNNING ON PORT {port}")
    print(f"📁 FILE 1: app.py (this file) - FILE 2: index.html (second file) - 2 FILES ONLY - WAJE DAYA")
    print(f"🌐 LOCAL: http://localhost:{port} - Open in browser")
    print(f"🌐 NETWORK: http://YOUR_IP:{port}
