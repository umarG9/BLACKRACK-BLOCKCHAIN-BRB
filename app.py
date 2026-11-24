# BLACKRACK AI BLOCKCHAIN - FULL COMPLETE - WITH AI ROBOT - OWNER: Golden diamond 9
# BRB + UGAS AI DUAL TOKEN + P2P INFINITY + AI ROBOT FLEET
# BLOCKCHAIN ONE - TWO TOKENS INSIDE - BRB DA UGAS AI DUKA A CIKI
# Owner: Golden diamond 9 - 100% Owner - All rights reserved - Final Clean Version
import hashlib
import time
import random
import json
import os
from collections import defaultdict
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

# ==================== AI ROBOT CLASS - OWNER GOLDEN DIAMOND 9 ====================
class AIRobot:
    def __init__(self, robot_id, robot_type="General"):
        self.robot_id = robot_id
        self.type = robot_type
        self.status = "IDLE"
        self.battery = 100
        self.tasks_completed = 0
        self.brb_earned = 0
        self.ugas_earned = 0
        self.hashrate = random.randint(100, 1000)
        self.ai_brain = "GPT-4o + Quantum 1M Qubits"
        self.sensors = ["Vision", "Lidar", "Thermal", "Audio"]
        self.capabilities = {
            "NOMA": ["Planting", "Watering", "Harvesting", "Soil Analysis", "Drone Spray"],
            "WELDER": ["Welding", "Cutting", "Metal Print", "Quality Check", "Laser"],
            "MECHANIC": ["Diagnosis 99%", "Repair", "Engine Scan", "Test Drive", "Parts Order"],
            "DOCTOR": ["Diagnosis 99%", "Scan", "Prescription", "Telemedicine", "VR Surgery"],
            "TEACHER": ["Math", "English", "Science", "Coding", "Hausa", "VR Class"],
            "SECURITY": ["Face Recognition", "Thief Detection", "Fire Detection", "Patrol", "Quantum Encryption"],
            "ENERGY": ["Solar Control", "Battery Management", "Energy Trading", "Power Distribution", "Grid Optimization"],
            "P2P_TRADER": ["Order Matching", "Escrow Management", "Price Prediction", "Auto Trading", "Risk Analysis"],
            "GENERAL": ["All Tasks", "AI Chat", "Mining", "P2P Trading", "Data Mining"]
        }
    
    def execute_task(self, task_description):
        self.status = "WORKING"
        data_mb = random.randint(50, 300)
        reward_brb = 10 + random.randint(0, 50)
        reward_ugas = 100 + random.randint(0, 500)
        self.battery -= random.randint(1, 5)
        if self.battery < 20:
            self.battery = 100
        self.tasks_completed += 1
        self.brb_earned += reward_brb + data_mb
        self.ugas_earned += reward_ugas + data_mb * 10
        self.status = "IDLE"
        block_hash = hashlib.sha256(f"{self.robot_id}{task_description}{time.time()}".encode()).hexdigest()
        return {
            "robot_id": self.robot_id,
            "type": self.type,
            "task": task_description,
            "status": self.status,
            "battery": self.battery,
            "data_mb": data_mb,
            "reward_brb": reward_brb + data_mb,
            "reward_ugas": reward_ugas + data_mb * 10,
            "total_brb": reward_brb + data_mb,
            "total_ugas": reward_ugas + data_mb * 10,
            "block_hash": block_hash[:16],
            "tx": "0x" + block_hash[:12],
            "tasks_completed": self.tasks_completed,
            "hashrate": self.hashrate,
            "ai_brain": self.ai_brain,
            "capabilities": self.capabilities.get(self.type, self.capabilities["GENERAL"]),
            "sensors": self.sensors,
            "time": time.strftime("%H:%M:%S")
        }
    
    def chat(self, message):
        lower = message.lower()
        if "hello" in lower or "hi" in lower or "sannu" in lower:
            return f"Hello, I am {self.robot_id} - {self.type} Robot - Owner Golden diamond 9 - Battery {self.battery}% - Tasks {self.tasks_completed} - Hashrate {self.hashrate} H/s - Ready to work - Capabilities: {', '.join(self.capabilities.get(self.type, self.capabilities['GENERAL'])[:3])}"
        if "status" in lower:
            return f"Status: {self.status} - Battery: {self.battery}% - Tasks Completed: {self.tasks_completed} - Earned: {self.brb_earned} BRB + {self.ugas_earned} UGAS AI - Hashrate: {self.hashrate} H/s - Brain: {self.ai_brain} - Type: {self.type} - Sensors: {', '.join(self.sensors)}"
        if "work" in lower or "task" in lower:
            return f"I am working - Type: {self.type} - Capabilities: {', '.join(self.capabilities.get(self.type, []))} - Owner: Golden diamond 9 - Give me a task to execute - I can do planting, welding, repair, diagnosis, teaching, security, energy, trading"
        return f"I am {self.robot_id} - {self.type} AI Robot - Owner Golden diamond 9 - I can do: {', '.join(self.capabilities.get(self.type, self.capabilities['GENERAL']))} - Ask me about status, hello, work - Battery {self.battery}% - AI Brain {self.ai_brain} - Hashrate {self.hashrate} H/s"

# ==================== P2P MARKETPLACE - OWNER GOLDEN DIAMOND 9 ====================
class P2PMarketplace:
    def __init__(self):
        self.orders = []
        self.trades = []
        self.profiles = {}
        self.counter = 1
    
    def create_profile(self, username, verified=False):
        if username not in self.profiles:
            self.profiles[username] = {
                "username": username,
                "verified": verified,
                "rating": 5.0,
                "trades": 0,
                "volume_brb": 0,
                "volume_ugas": 0,
                "badges": ["NEW"],
                "joined": time.strftime("%Y-%m-%d")
            }
        return self.profiles[username]
    
    def create_order(self, username, order_type, from_token, to_token, amount, price, payment_method="Bank Transfer"):
        is_verified = True if username == "Golden diamond 9" else False
        self.create_profile(username, is_verified)
        order_id = f"P2P-{self.counter:06d}"
        self.counter += 1
        order = {
            "order_id": order_id,
            "username": username,
            "type": order_type,
            "from_token": from_token,
            "to_token": to_token,
            "amount": float(amount),
            "price": float(price),
            "total": float(amount) * float(price),
            "payment_method": payment_method,
            "status": "ACTIVE",
            "created": time.strftime("%Y-%m-%d %H:%M:%S"),
            "profile": self.profiles[username]
        }
        self.orders.append(order)
        return order
    
    def trade(self, order_id, buyer, amount):
        order = next((o for o in self.orders if o["order_id"] == order_id), None)
        if not order:
            return {"error": "Order not found - P2P Infinity"}
        trade = {
            "trade_id": f"TRADE-{hashlib.sha256(f'{order_id}{buyer}{time.time()}'.encode()).hexdigest()[:8].upper()}",
            "order_id": order_id,
            "seller": order["username"],
            "buyer": buyer,
            "from_token": order["from_token"],
            "to_token": order["to_token"],
            "amount": float(amount),
            "total": float(amount) * order["price"],
            "status": "COMPLETED",
            "created": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        self.trades.append(trade)
        for u in [order["username"], buyer]:
            self.create_profile(u)
            self.profiles[u]["trades"] += 1
            if self.profiles[u]["trades"] > 10:
                self.profiles[u]["badges"] = ["TRUSTED", "INFINITY"]
            if self.profiles[u]["trades"] > 50:
                self.profiles[u]["badges"] = ["WHALE", "VERIFIED", "INFINITY"]
        return trade

# ==================== BLOCKCHAIN CORE - OWNER GOLDEN DIAMOND 9 ====================
class BlockchainCore:
    def __init__(self):
        self.owner = "Golden diamond 9"
        self.brb_supply = 10000000
        self.ugas_supply = 100000000
        self.balances_brb = defaultdict(float)
        self.balances_ugas = defaultdict(float)
        self.balances_brb["Golden diamond 9"] = 10000000
        self.balances_ugas["Golden diamond 9"] = 100000000
        self.blocks = []
        self.robots = {}
        self.p2p = P2PMarketplace()
        robot_types = ["NOMA", "WELDER", "MECHANIC", "DOCTOR", "TEACHER", "SECURITY", "ENERGY", "P2P_TRADER", "GENERAL"]
        for i, rtype in enumerate(robot_types):
            rid = f"AI-ROBOT-{i+1:03d}-{rtype}"
            self.robots[rid] = AIRobot(rid, rtype)
    
    def get_robot(self, robot_id):
        if robot_id not in self.robots:
            self.robots[robot_id] = AIRobot(robot_id, "General")
        return self.robots[robot_id]
    
    def mint(self, user, brb, ugas):
        self.balances_brb[user] += brb
        self.balances_ugas[user] += ugas
        return {"user": user, "brb": brb, "ugas": ugas, "owner": self.owner}
    
    def mine_block(self, validator, task):
        block_hash = hashlib.sha256(f"{validator}{task}{time.time()}".encode()).hexdigest()
        block = {
            "number": len(self.blocks) + 1,
            "hash": block_hash,
            "validator": validator,
            "task": task,
            "reward_brb": 100,
            "reward_ugas": 1000,
            "time": time.strftime("%H:%M:%S")
        }
        self.blocks.append(block)
        return block
    
    def dashboard(self):
        total_tasks = sum(r.tasks_completed for r in self.robots.values())
        total_brb = sum(r.brb_earned for r in self.robots.values())
        total_ugas = sum(r.ugas_earned for r in self.robots.values())
        return {
            "owner": self.owner,
            "brb": {"supply": self.brb_supply, "owner_balance": self.balances_brb["Golden diamond 9"], "balances": dict(self.balances_brb)},
            "ugas_ai": {"supply": self.ugas_supply, "owner_balance": self.balances_ugas["Golden diamond 9"], "balances": dict(self.balances_ugas), "name": "UGAS AI TOKEN - GAS AI + FUEL AI + FEE AI"},
            "blockchain": {"blocks": len(self.blocks), "validators": 60, "chain_id": "BLACKRACK-AI-CHAIN-001", "owner": self.owner},
            "ai_robots": {
                "count": len(self.robots),
                "total_tasks": total_tasks,
                "total_brb": total_brb,
                "total_ugas": total_ugas,
                "owner": self.owner,
                "robots": [{"id": r.robot_id, "type": r.type, "status": r.status, "battery": r.battery, "tasks": r.tasks_completed, "brb": r.brb_earned, "ugas": r.ugas_earned, "hashrate": r.hashrate, "brain": r.ai_brain} for r in self.robots.values()]
            },
            "p2p": {"orders": len(self.p2p.orders), "trades": len(self.p2p.trades), "users": len(self.p2p.profiles), "description": "P2P Infinity Marketplace - Better than Binance P2P - BRB <-> UGAS AI <-> NGN - Owner Golden diamond 9"},
            "info": "BLACKRACK AI BLOCKCHAIN - Owner Golden diamond 9 - BRB + UGAS AI - AI ROBOT FLEET - P2P Infinity Better than Binance P2P - Blockchain One - Two Tokens Inside - Clean Version"
        }

core = BlockchainCore()

# ==================== HTTP HANDLER - OWNER GOLDEN DIAMOND 9 ====================
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        if path in ["/", "/index.html"]:
            if os.path.exists("index.html"):
                with open("index.html", "rb") as f:
                    content = f.read()
            else:
                content = b"<h1>BLACKRACK AI BLOCKCHAIN - Owner Golden diamond 9 - AI ROBOT - Put index.html in same folder as app.py - 2 FILES ONLY - python app.py</h1>"
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(content)
        elif path == "/api/dashboard":
            self.send_json(core.dashboard())
        elif path == "/api/p2p/orders":
            self.send_json({"orders": core.p2p.orders[-100:], "stats": {"total": len(core.p2p.orders), "active": len([o for o in core.p2p.orders if o["status"]=="ACTIVE"]), "trades": len(core.p2p.trades), "users": len(core.p2p.profiles)}})
        elif path == "/api/blocks":
            self.send_json({"blocks": core.blocks[-20:]})
        elif path == "/api/robots":
            self.send_json({"robots": [{"id": r.robot_id, "type": r.type, "status": r.status, "battery": r.battery, "tasks": r.tasks_completed, "brb": r.brb_earned, "ugas": r.ugas_earned, "hashrate": r.hashrate, "capabilities": r.capabilities.get(r.type, []), "sensors": r.sensors, "brain": r.ai_brain} for r in core.robots.values()], "owner": core.owner})
        elif path == "/api/p2p/trades":
            self.send_json({"trades": core.p2p.trades[-50:]})
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found - Use / , /api/dashboard , /api/p2p/orders , /api/blocks , /api/robots , /api/p2p/trades")
    
    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        length = int(self.headers.get('content-length', 0))
        body = self.rfile.read(length) if length > 0 else b"{}"
        try:
            data = json.loads(body.decode())
        except:
            data = {}
        result = {}
        if path == "/api/p2p/create-order":
            result = core.p2p.create_order(data.get("username", "Golden diamond 9"), data.get("type", "SELL"), data.get("from_token", "BRB"), data.get("to_token", "UGAS AI"), data.get("amount", 100), data.get("price", 1000), data.get("payment", "Bank Transfer"))
        elif path == "/api/p2p/trade":
            result = core.p2p.trade(data.get("order_id", ""), data.get("buyer", "Trader"), data.get("amount", 10))
        elif path == "/api/robot/task":
            robot = core.get_robot(data.get("robot_id", "AI-ROBOT-001-NOMA"))
            result = robot.execute_task(data.get("task", "General Task - Owner Golden diamond 9"))
        elif path == "/api/robot/chat":
            robot = core.get_robot(data.get("robot_id", "AI-ROBOT-001-NOMA"))
            msg = data.get("message", "hello")
            reply = robot.chat(msg)
            result = {"robot_id": robot.robot_id, "type": robot.type, "message": msg, "reply": reply, "battery": robot.battery, "status": robot.status, "tasks": robot.tasks_completed, "owner": core.owner}
        elif path == "/api/mine":
            result = core.mine_block(data.get("validator", "Validator-001"), data.get("task", "Validation - Owner Golden diamond 9"))
        elif path == "/api/mint":
            result = core.mint(data.get("user", "Golden diamond 9"), float(data.get("brb", 100)), float(data.get("ugas", 1000)))
        else:
            result = {"error": "Unknown endpoint", "use": ["/api/p2p/create-order", "/api/p2p/trade", "/api/robot/task", "/api/robot/chat", "/api/mine", "/api/mint", "/api/dashboard", "/api/robots"]}
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

def run():
    port = int(os.environ.get("PORT", 8000))
    httpd = HTTPServer(('', port), Handler)
    print("="*80)
    print(f"BLACKRACK AI BLOCKCHAIN - OWNER Golden diamond 9 - AI ROBOT FLEET")
    print(f"BRB + UGAS AI DUAL TOKEN - BLOCKCHAIN ONE - TWO TOKENS INSIDE")
    print(f"P2P INFINITY MARKETPLACE - BETTER THAN BINANCE P2P")
    print(f"PORT {port} - http://localhost:{port}")
    print(f"Owner: Golden diamond 9 - 100% Owner - 10M BRB + 100M UGAS AI")
    print("="*80)
    core.p2p.create_profile("Golden diamond 9", True)
    core.p2p.create_order("Golden diamond 9", "SELL", "BRB", "UGAS AI", 1000, 1000, "Bank Transfer")
    core.p2p.create_order("Golden diamond 9", "SELL", "BRB", "NGN", 500, 15, "Opay")
    core.p2p.create_order("Golden diamond 9", "SELL", "UGAS AI", "BRB", 50000, 0.001, "BRB Wallet")
    core.mine_block("Validator-001", "Genesis Block - Owner Golden diamond 9 - AI ROBOT FLEET")
    print(f"Demo: 3 P2P Orders Created - 9 AI Robots Active - Owner Golden diamond 9")
    print(f"Open: http://localhost:{port} - AI ROBOT - P2P INFINITY - BRB + UGAS AI")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
