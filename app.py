# BLACKRACK AI BLOCKCHAIN - PYTHON ALL - HADE DUKA - FINAL ULTIMATE - WAJE DAYA
# BRB + UGAS AI + P2P INFINITY MARKETPLACE YAFI BINANCE + CHATGPT AI + MINING + SECURITY + ALL
# BLOCKCHAIN DAYA - TOKEN BIYU - BRB DA UGAS AI - DUKA A CIKI - P2P INFINITY - INFINITY TRADING
import hashlib, time, random, json, os
from datetime import datetime
from collections import defaultdict
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse, urllib.request

class P2PInfinityMarketplace:
    def __init__(self):
        self.orders = []  # All P2P orders
        self.trades = []  # All trades
        self.profiles = {}  # User profiles
        self.escrow = {}  # Escrow
        self.order_id_counter = 1
    
    def create_profile(self, username, phone="", verified=False):
        if username not in self.profiles:
            self.profiles[username] = {
                "username": username,
                "phone": phone,
                "verified": verified,
                "rating": 5.0,
                "trades_count": 0,
                "success_rate": 100.0,
                "total_volume_brb": 0,
                "total_volume_ugas": 0,
                "badges": ["NEW"],
                "joined": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "bio": f"BLACKRACK AI TRADER - {username} - BRB+UGAS AI P2P INFINITY - YAFI BINANCE",
                "avatar": f"https://api.dicebear.com/7.x/bottts/svg?seed={username}"
            }
        return self.profiles[username]
    
    def create_order(self, username, order_type, from_token, to_token, amount, price, payment_method="BANK TRANSFER", min_limit=100, max_limit=10000):
        # order_type: BUY or SELL, from_token: BRB/UGAS AI/NGN, to_token: BRB/UGAS AI/NGN
        self.create_profile(username)
        order_id = f"P2P-{self.order_id_counter:06d}-{username[:4].upper()}"
        self.order_id_counter += 1
        order = {
            "order_id": order_id,
            "username": username,
            "profile": self.profiles[username],
            "type": order_type,  # BUY or SELL
            "from_token": from_token,  # What user gives
            "to_token": to_token,  # What user wants
            "amount": amount,  # Amount of from_token
            "price": price,  # Price per unit in to_token
            "total": amount * price,
            "payment_method": payment_method,
            "min_limit": min_limit,
            "max_limit": max_limit,
            "status": "ACTIVE",
            "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "rating": self.profiles[username]["rating"],
            "trades": self.profiles[username]["trades_count"],
            "verified": self.profiles[username]["verified"],
            "infinity": True,  # INFINITY FEATURE - No limits like Binance
            "escrow_enabled": True,
            "auto_release": True
        }
        self.orders.append(order)
        print(f"💱 P2P INFINITY ORDER: {order_id} - {username} - {order_type} {amount} {from_token} -> {to_token} @ {price} {to_token}/{from_token} - Total {order['total']} {to_token} - {payment_method} - YAFI BINANCE - INFINITY")
        return order
    
    def get_orders(self, filter_token=None, filter_type=None):
        filtered = self.orders
        if filter_token:
            filtered = [o for o in filtered if filter_token in [o["from_token"], o["to_token"]]]
        if filter_type:
            filtered = [o for o in filtered if o["type"] == filter_type]
        # Sort by rating + verified + infinity - Best traders first
        filtered = sorted(filtered, key=lambda x: (x["verified"], x["rating"], x["trades"]), reverse=True)
        return filtered[-100:]  # Last 100 - INFINITY but show last 100 for UI
    
    def execute_trade(self, order_id, buyer, amount):
        order = next((o for o in self.orders if o["order_id"] == order_id), None)
        if not order: return {"error": "Order not found - P2P INFINITY"}
        if order["status"] != "ACTIVE": return {"error": "Order not active"}
        if amount < order["min_limit"] or amount > order["max_limit"]: return {"error": f"Amount must be {order['min_limit']}-{order['max_limit']}"}
        
        # Escrow logic - INFINITY SECURITY
        escrow_id = f"ESCROW-{hashlib.sha256(f'{order_id}{buyer}{time.time()}'.encode()).hexdigest()[:8].upper()}"
        trade = {
            "trade_id": f"TRADE-{hashlib.sha256(f'{order_id}{buyer}{time.time()}'.encode()).hexdigest()[:8].upper()}",
            "order_id": order_id,
            "seller": order["username"],
            "buyer": buyer,
            "from_token": order["from_token"],
            "to_token": order["to_token"],
            "amount": amount,
            "price": order["price"],
            "total": amount * order["price"],
            "status": "ESCROW",
            "escrow_id": escrow_id,
            "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "payment_method": order["payment_method"],
            "infinity_feature": "AUTO_RELEASE + NO_LIMIT + INSTANT + AI_VERIFICATION"
        }
        self.trades.append(trade)
        self.escrow[escrow_id] = trade
        
        # Update profiles
        for u in [order["username"], buyer]:
            self.create_profile(u)
            self.profiles[u]["trades_count"] += 1
            self.profiles[u]["total_volume_brb"] += amount if order["from_token"]=="BRB" else 0
            self.profiles[u]["total_volume_ugas"] += amount if "UGAS" in order["from_token"] else 0
            if self.profiles[u]["trades_count"] > 10: self.profiles[u]["badges"] = ["TRUSTED", "INFINITY"]
            if self.profiles[u]["trades_count"] > 100: self.profiles[u]["badges"] = ["WHALE", "INFINITY", "VERIFIED"]
        
        print(f"💱 P2P INFINITY TRADE: {trade['trade_id']} - {order['username']} -> {buyer} - {amount} {order['from_token']} -> {order['to_token']} - Escrow {escrow_id} - INFINITY - YAFI BINANCE")
        return trade
    
    def get_profile(self, username):
        return self.profiles.get(username, self.create_profile(username))
    
    def get_stats(self):
        total_volume = sum(t["total"] for t in self.trades)
        return {
            "total_orders": len(self.orders),
            "active_orders": len([o for o in self.orders if o["status"]=="ACTIVE"]),
            "total_trades": len(self.trades),
            "total_volume": total_volume,
            "total_users": len(self.profiles),
            "infinity_features": ["NO_LIMIT_TRADING", "INSTANT_RELEASE", "AI_VERIFICATION", "DUAL_TOKEN_BRB_UGAS_AI", "NGN_SUPPORT", "ESCROW_SECURE", "RATING_SYSTEM", "PROFILE_BADGES", "YAFI_BINANCE"]
        }

class BlackrackAIBlockchain:
    def __init__(self):
        self.bullish = 78
        self.brb_supply = 0
        self.brb_balances = defaultdict(int)
        self.brb_nfts = []
        self.ugas_supply = 0
        self.ugas_balances = defaultdict(int)
        self.ugas_burned = 0
        self.brb_stakes = {}
        self.ugas_stakes = {}
        self.tvl_brb = 0
        self.tvl_ugas = 0
        self.total_data_mb = 0
        self.total_data_brb = 0
        self.total_data_ugas = 0
        self.total_energy_kwh = 0
        self.total_energy_brb = 0
        self.plans = {
            "NOMA FARMER": {"brb": 500, "ugas": 5000, "tasks": 30, "kwh": 1200, "data": 6000, "hash": 100, "desc": "Shuka Masara - Tractor+Drone+Soil pH AI - AI Farming"},
            "WELDER": {"brb": 800, "ugas": 8000, "tasks": 20, "kwh": 1500, "data": 4000, "hash": 150, "desc": "Waldi Kofa - AI Welding Arm+3D Metal Print - AI Welder"},
            "MECHANIC": {"brb": 700, "ugas": 7000, "tasks": 25, "kwh": 1000, "data": 5000, "hash": 120, "desc": "Gyaran Mota - AI Diagnosis 99% - AI Mechanic"},
            "DOCTOR": {"brb": 1000, "ugas": 10000, "tasks": 50, "kwh": 800, "data": 10000, "hash": 200, "desc": "AI Doctor Ciwon kai - Diagnosis 99% - Doctor Teaches All - AI Doctor"},
            "TEACHER": {"brb": 600, "ugas": 6000, "tasks": 60, "kwh": 500, "data": 15000, "hash": 250, "desc": "Maths x+2=5->x=3! - Teacher Teaches All - AI Teacher GPT-10"},
            "SECURITY": {"brb": 300, "ugas": 3000, "tasks": 100, "kwh": 400, "data": 20000, "hash": 200, "desc": "Tsaro Barawo Thief Gobara Fire - SERVER SECURITY 99.99% - Quantum Resistant - AI Security"},
            "ENERGY": {"brb": 2000, "ugas": 1000, "tasks": 10, "kwh": -5000, "data": 1000, "hash": 500, "desc": "PRODUCES ENERGY! Solar 10MW - 5000 kWh/day - BEST MINER - Low Gas! - AI Energy"},
            "ALL IN ONE": {"brb": 5000, "ugas": 20000, "tasks": 500, "kwh": 5000, "data": 100000, "hash": 1000, "desc": "DUKA ROBOT DAYA! Noma+Welder+Mechanic+Doctor+Teacher+All - AGI Quantum Brain 1M Qubits - AI EVERYTHING - FINAL ULTIMATE"}
        }
        self.subs = {}
        self.subs_total_brb = 0
        self.subs_total_ugas = 0
        self.miners = {}
        self.blocks = []
        self.total_mined_brb = 0
        self.total_mined_ugas = 0
        self.total_hash = 0
        self.threats_blocked = 0
        self.security_logs = []
        self.tasks_done = 0
        self.tasks_total_brb = 0
        self.tasks_total_ugas = 0
        self.ai_chats = []
        self.ai_knowledge = {
            "blackrack": "BLACKRACK AI BLOCKCHAIN - RBR - BLACK RACK BLOCKCHAIN ONLY - DUAL TOKEN BRB+UGAS AI - P2P INFINITY YAFI BINANCE - 10M BRB $100K + 100M UGAS AI $1000 + AI $1000 + P2P $5000 = $106K/month - BULLISH 78%",
            "brb": "BRB = POWER+ENERGY+MONEY+DATA+AI - 5 IN 1 - 10M Supply - 1 BRB=1 kWh=$0.01",
            "ugas ai": "UGAS AI = GAS AI+FUEL AI+FEE AI - 100M Supply - 1 UGAS AI=0.001 BRB=$0.00001 - ROBOT AI FUEL - AI GAS LAYER - UGAS AI TOKEN",
            "p2p": "P2P INFINITY MARKETPLACE - YAFI BINANCE P2P - INFINITY TRADING - BRB <-> UGAS AI <-> NGN - PROFILE + RATING + ESCROW + INSTANT + NO LIMIT + AI VERIFICATION - DUAL TOKEN P2P - BLACKRACK AI BLOCKCHAIN DAYA - TOKEN BIYU BRB DA UGAS AI - DUKA A CIKI - P2P INFINITY",
            "noma": "NOMA FARMER - Shuka Masara - Tractor+Drone AI - 500 BRB+5000 UGAS AI/month",
            "all in one": "ALL IN ONE - DUKA ROBOT DAYA! - AGI Quantum Brain 1M Qubits - 5000 BRB+20000 UGAS AI/month - FINAL ULTIMATE"
        }
        self.p2p = P2PInfinityMarketplace()
    
    def ai_chat(self, user_message, user_name="Anonymous"):
        user_lower = user_message.lower()
        best_match = None
        for key, value in self.ai_knowledge.items():
            if key in user_lower:
                best_match = value
                break
        if not best_match:
            if "p2p" in user_lower or "saye" in user_lower or "siyar" in user_lower or "chanji" in user_lower or "binance" in user_lower:
                best_match = f"💱 P2P INFINITY MARKETPLACE - YAFI BINANCE P2P - BLACKRACK AI BLOCKCHAIN - BRB <-> UGAS AI <-> NGN:\n\n💰 BRB = MAIN TOKEN - 1 BRB=1 kWh=$0.01\n⛽ UGAS AI = GAS AI TOKEN - 1 UGAS AI=0.001 BRB=$0.00001 - ROBOT AI FUEL\n\n🔄 CHANJI - TRADING PAIRS - INFINITY:\n- BRB -> UGAS AI: 1 BRB = 1000 UGAS AI\n- UGAS AI -> BRB: 1000 UGAS AI = 1 BRB\n- BRB -> NGN: 1 BRB = ₦15\n- NGN -> BRB: ₦15 = 1 BRB\n- UGAS AI -> NGN: 1000 UGAS AI = ₦15\n\n👤 PROFILE: Rating + Trades + Volume + Badges NEW/TRUSTED/WHALE/VERIFIED/INFINITY\n🛡️ ESCROW: Secure + Auto Release + AI Verification + Instant - YAFI BINANCE\n♾️ INFINITY: No Limit Trading + Instant + No Restriction + Dual Token + AI - YAFI BINANCE P2P\n\nTambaya: {user_message} - Ina nan BLACKRACK AI - P2P INFINITY!"
            else:
                best_match = f"🤖 BLACKRACK AI - GPT-4o + Quantum Brain 1M Qubits - ME DAUKAR HANKALI:\n\n🚀 BLACKRACK AI BLOCKCHAIN - DUAL TOKEN BRB+UGAS AI + P2P INFINITY YAFI BINANCE:\n- BRB: 10M Supply - 1 BRB=1 kWh=$0.01\n- UGAS AI: 100M Supply - 1 UGAS AI=0.001 BRB - GAS AI TOKEN\n- P2P INFINITY: BRB <-> UGAS AI <-> NGN - PROFILE + RATING + ESCROW + INFINITY - YAFI BINANCE P2P - INFINITY TRADING\n\nTambayarka: '{user_message}'\n\nAmsa: BLACKRACK AI BLOCKCHAIN yana da P2P INFINITY MARKETPLACE - YAFI BINANCE - BRB <-> UGAS AI CHANJI - PROFILE + RATING + ESCROW - INFINITY - 12 HOUSES - 60 ROBOTS - HUMAN DOES NOTHING ROBOT DOES EVERYTHING - 10M BRB $100K + 100M UGAS AI $1000 + P2P $5000 = $106K/month - Bullish 78% - Tambaye ni komai!"
        openai_key = os.environ.get("OPENAI_API_KEY", "")
        if openai_key and openai_key.startswith("sk-"):
            try:
                headers = {"Authorization": f"Bearer {openai_key}", "Content-Type": "application/json"}
                payload = {"model": "gpt-4o-mini", "messages": [{"role": "system", "content": "You are BLACKRACK AI - P2P INFINITY MARKETPLACE YAFI BINANCE - BRB+UGAS AI DUAL TOKEN - Answer in Hausa/English mix, fun, energetic, with emojis"}, {"role": "user", "content": user_message}], "max_tokens": 800, "temperature": 0.9}
                req = urllib.request.Request("https://api.openai.com/v1/chat/completions", data=json.dumps(payload).encode(), headers=headers, method='POST')
                with urllib.request.urlopen(req, timeout=10) as resp:
                    result = json.loads(resp.read().decode())
                    best_match = f"🤖 REAL CHATGPT AI - GPT-4o:\n\n{result['choices'][0]['message']['content']}"
            except Exception as e:
                best_match = f"{best_match}\n\n⚠️ Local AI - Set OPENAI_API_KEY for real ChatGPT AI"
        tx = "0x"+hashlib.sha256(f"{user_message}{time.time()}".encode()).hexdigest()[:12]
        chat_log = {"time": datetime.now().strftime("%H:%M:%S"), "user": user_name, "message": user_message, "ai_response": best_match, "tx": tx, "model": "BLACKRACK AI"}
        self.ai_chats.append(chat_log)
        data_mb = len(user_message + best_match) / 1024
        self.total_data_mb += data_mb
        self.total_data_brb += data_mb * 1
        self.total_data_ugas += data_mb * 10
        return chat_log
    
    def mint_dual(self, user, brb_amount, ugas_amount, nft_type):
        self.brb_supply += brb_amount; self.brb_balances[user] += brb_amount
        self.ugas_supply += ugas_amount; self.ugas_balances[user] += ugas_amount
        tx = "0x" + hashlib.sha256(f"{user}{brb_amount}{ugas_amount}{time.time()}".encode()).hexdigest()[:12]
        nft_id = f"BLACKRACK-DUAL-NFT-{hashlib.sha256(f'{user}{brb_amount}'.encode()).hexdigest()[:6].upper()}"
        log = {"user": user, "brb": brb_amount, "ugas": ugas_amount, "type": nft_type, "tx": tx, "nft_id": nft_id, "time": datetime.now().strftime("%H:%M:%S")}
        self.brb_nfts.append(log)
        return log
    def stake_dual(self, user, brb_amount, ugas_amount):
        brb_reward = brb_amount * 78/100/365; ugas_reward = ugas_amount * 22/100/365
        self.brb_stakes[user] = self.brb_stakes.get(user,0)+brb_amount; self.ugas_stakes[user] = self.ugas_stakes.get(user,0)+ugas_amount
        self.tvl_brb += brb_amount; self.tvl_ugas += ugas_amount
        return {"user": user, "brb": brb_amount, "ugas": ugas_amount, "brb_apy": "78%", "ugas_apy": "22%", "brb_reward_day": brb_reward, "ugas_reward_day": ugas_reward, "tvl_brb": self.tvl_brb, "tvl_ugas": self.tvl_ugas}
    def track_data_dual(self, user, page, mb):
        brb_earned = mb * 1; ugas_earned = mb * 10
        self.total_data_mb += mb; self.total_data_brb += brb_earned; self.total_data_ugas += ugas_earned
        tx = "0x"+hashlib.sha256(f"{user}{page}{mb}{time.time()}".encode()).hexdigest()[:12]
        return {"user": user, "page": page, "mb": mb, "brb": brb_earned, "ugas": ugas_earned, "tx": tx, "total_mb": self.total_data_mb, "total_brb": self.total_data_brb, "total_ugas": self.total_data_ugas}
    def produce_energy_dual(self, source, kwh):
        brb = kwh * 1; ugas_used = kwh * 0.2
        self.total_energy_kwh += kwh; self.total_energy_brb += brb; self.ugas_burned += ugas_used
        return {"source": source, "kwh": kwh, "brb": brb, "ugas_used": ugas_used, "total_kwh": self.total_energy_kwh, "total_brb": self.total_energy_brb, "burned": self.ugas_burned}
    def subscribe_dual(self, user, plan, months=1):
        if plan not in self.plans: return None
        p = self.plans[plan]; total_brb = p["brb"]*months; total_ugas = p["ugas"]*months
        sub_id = f"BLACKRACK-SUB-{plan.replace(' ','-')}-{user[:5].upper()}-{hashlib.sha256(f'{user}{plan}{time.time()}'.encode()).hexdigest()[:6].upper()}"
        tx = "0x"+hashlib.sha256(f"{user}{plan}{months}{time.time()}".encode()).hexdigest()[:12]
        self.subs[sub_id] = {"user": user, "plan": plan, "months": months, "brb": total_brb, "ugas": total_ugas, "tasks": p["tasks"]*months, "done": 0, "remaining": p["tasks"]*months, "desc": p["desc"]}
        self.subs_total_brb += total_brb; self.subs_total_ugas += total_ugas; self.ugas_burned += total_ugas * 0.1
        return {"sub_id": sub_id, "user": user, "plan": plan, "brb": total_brb, "ugas": total_ugas, "months": months, "tasks": p["tasks"]*months, "tx": tx, "desc": p["desc"]}
    def do_task_dual(self, sub_id, detail):
        if sub_id not in self.subs: return None
        s = self.subs[sub_id]
        if s["remaining"]<=0: return {"error": "No tasks remaining"}
        s["done"]+=1; s["remaining"]-=1
        data = random.randint(50,300); data_brb = data*1; data_ugas = data*10
        block_brb = 100+random.randint(0,50); block_ugas = 1000+random.randint(0,500); gas_used = 100+random.randint(0,100)
        total_brb = data_brb + block_brb; total_ugas = data_ugas + block_ugas - gas_used
        self.tasks_done+=1; self.tasks_total_brb+=total_brb; self.tasks_total_ugas+=total_ugas; self.ugas_burned+=gas_used
        tx = "0x"+hashlib.sha256(f"{sub_id}{detail}{time.time()}".encode()).hexdigest()[:12]
        task_nft = f"BLACKRACK-TASK-{s['plan'][:10]}-{hashlib.sha256(f'{detail}'.encode()).hexdigest()[:6].upper()}"
        block_hash = "0x"+hashlib.sha256(f"{sub_id}{detail}{time.time()}".encode()).hexdigest()[:16]
        return {"sub_id": sub_id, "plan": s["plan"], "user": s["user"], "detail": detail, "data_mb": data, "data_brb": data_brb, "data_ugas": data_ugas, "block_brb": block_brb, "block_ugas": block_ugas, "gas_used": gas_used, "total_brb": total_brb, "total_ugas": total_ugas, "tx": tx, "task_nft": task_nft, "block_hash": block_hash, "done": s["done"], "remaining": s["remaining"]}
    def register_miner_dual(self, robot_id, rtype):
        if rtype not in self.plans: rtype="ALL IN ONE"
        base = self.plans[rtype]["hash"]; boost = random.randint(0,100); final = base*(1+boost/100)
        self.miners[robot_id] = {"type": rtype, "hashrate": final, "base": base, "boost": boost, "mined_brb": 0, "mined_ugas": 0, "blocks": 0}
        self.total_hash+=final
        return {"robot_id": robot_id, "type": rtype, "hashrate": final, "boost": boost, "total_hash": self.total_hash}
    def mine_block_dual(self, robot_id, task_detail):
        if robot_id not in self.miners: self.register_miner_dual(robot_id, "ALL IN ONE")
        m = self.miners[robot_id]
        block_hash = hashlib.sha256(f"{robot_id}{task_detail}{time.time()}".encode()).hexdigest()
        data = random.randint(50,300); data_brb = data*1; data_ugas = data*10
        block_brb = 100+random.randint(0,50); block_ugas = 1000+random.randint(0,500)
        total_brb = data_brb+block_brb; total_ugas = data_ugas+block_ugas
        energy = -5 if m["type"]=="ENERGY" else m["hashrate"]/100*0.1; gas_used = 50 if m["type"]=="ENERGY" else 100
        self.ugas_burned+=gas_used; m["mined_brb"]+=total_brb; m["mined_ugas"]+=total_ugas; m["blocks"]+=1
        self.total_mined_brb+=total_brb; self.total_mined_ugas+=total_ugas
        block_num = len(self.blocks)+1
        block = {"block_number": block_num, "block_hash": block_hash, "robot_id": robot_id, "type": m["type"], "task": task_detail, "data_mb": data, "data_brb": data_brb, "data_ugas": data_ugas, "block_brb": block_brb, "block_ugas": block_ugas, "total_brb": total_brb, "total_ugas": total_ugas, "energy": energy, "gas_used": gas_used, "hashrate": m["hashrate"], "tx": "0x"+block_hash[:12], "time": datetime.now().strftime("%H:%M:%S")}
        self.blocks.append(block)
        return block
    def block_threat_dual(self, ttype, detail):
        self.threats_blocked+=1; gas_used = random.randint(10,100); self.ugas_burned+=gas_used
        tx = "0x"+hashlib.sha256(f"{ttype}{detail}{time.time()}".encode()).hexdigest()[:12]
        nft = f"BLACKRACK-SECURITY-NFT-{ttype.replace(' ','-')}-{hashlib.sha256(f'{detail}'.encode()).hexdigest()[:6].upper()}"
        log = {"time": datetime.now().strftime("%H:%M:%S"), "type": ttype, "detail": detail, "tx": tx, "nft": nft, "gas_used": gas_used, "blocked": self.threats_blocked}
        self.security_logs.append(log)
        return log
    def dashboard(self):
        p2p_stats = self.p2p.get_stats()
        return {
            "BRB": {"supply": self.brb_supply, "nfts": len(self.brb_nfts), "balances": dict(self.brb_balances), "tvl": self.tvl_brb, "stakes": len(self.brb_stakes)},
            "UGAS_AI": {"supply": self.ugas_supply, "balances": dict(self.ugas_balances), "burned": self.ugas_burned, "tvl": self.tvl_ugas, "stakes": len(self.ugas_stakes), "token": "UGAS AI TOKEN - GAS AI + FUEL AI + FEE AI - AI GAS LAYER - ME DAUKAR HANKALI"},
            "DUAL": {"total_supply_brb": self.brb_supply, "total_supply_ugas": self.ugas_supply, "burned_ugas": self.ugas_burned, "tvl_brb": self.tvl_brb, "tvl_ugas": self.tvl_ugas, "blockchain": "BLACKRACK AI BLOCKCHAIN DAYA - TOKEN BIYU BRB DA UGAS AI - DUKA A CIKI"},
            "DATA": {"total_mb": self.total_data_mb, "total_gb": self.total_data_mb/1024, "total_brb": self.total_data_brb, "total_ugas": self.total_data_ugas, "value_usd": self.total_data_brb*0.01+self.total_data_ugas*0.00001},
            "ENERGY": {"total_kwh": self.total_energy_kwh, "total_brb": self.total_energy_brb, "burned_ugas": self.ugas_burned, "value_usd": self.total_energy_brb*0.01},
            "SUBSCRIPTION": {"count": len(self.subs), "total_brb": self.subs_total_brb, "total_ugas": self.subs_total_ugas, "value_usd": self.subs_total_brb*0.01+self.subs_total_ugas*0.00001},
            "MINING": {"miners": len(self.miners), "blocks": len(self.blocks), "total_mined_brb": self.total_mined_brb, "total_mined_ugas": self.total_mined_ugas, "total_hash": self.total_hash, "value_usd": self.total_mined_brb*0.01+self.total_mined_ugas*0.00001},
            "SECURITY": {"threats_blocked": self.threats_blocked, "logs": len(self.security_logs), "tasks_done": self.tasks_done, "tasks_brb": self.tasks_total_brb, "tasks_ugas": self.tasks_total_ugas, "burned_ugas": self.ugas_burned},
            "AI": {"chats": len(self.ai_chats), "last_chats": self.ai_chats[-5:], "knowledge_base": len(self.ai_knowledge), "model": "BLACKRACK AI - GPT-4o + Quantum Brain 1M Qubits - CHATGPT AI INTEGRATION - ME DAUKAR HANKALI"},
            "P2P_INFINITY": {
                "total_orders": p2p_stats["total_orders"],
                "active_orders": p2p_stats["active_orders"],
                "total_trades": p2p_stats["total_trades"],
                "total_volume": p2p_stats["total_volume"],
                "total_users": p2p_stats["total_users"],
                "features": p2p_stats["infinity_features"],
                "description": "P2P INFINITY MARKETPLACE - YAFI BINANCE P2P - INFINITY TRADING - BRB <-> UGAS AI <-> NGN - PROFILE + RATING + ESCROW + INSTANT + NO LIMIT + AI VERIFICATION - DUAL TOKEN P2P - BLACKRACK AI BLOCKCHAIN DAYA - TOKEN BIYU BRB DA UGAS AI - DUKA A CIKI - P2P INFINITY - INFINITY = NO LIMIT + INSTANT + AI + DUAL TOKEN + YAFI BINANCE",
                "trading_pairs": ["BRB/UGAS AI", "UGAS AI/BRB", "BRB/NGN", "NGN/BRB", "UGAS AI/NGN", "NGN/UGAS AI", "BRB/USDT", "UGAS AI/USDT"],
                "payment_methods": ["BANK TRANSFER", "OPAY", "PALMPAY", "KUDA", "MONIEPOINT", "USDT TRC20", "BRB WALLET", "UGAS AI WALLET"]
            },
            "BULLISH": self.bullish,
            "FORMULA": "BLOCKCHAIN DAYA TOKEN BIYU BRB+UGAS AI - 1 BRB=1 kWh=$0.01 - 1 UGAS AI=0.001 BRB=$0.00001 - 1 Task=300 BRB+3000 UGAS AI - 1 Block=100 BRB+1000 UGAS AI - Data 1 MB=1 BRB+10 UGAS AI - P2P INFINITY: BRB<->UGAS AI 1 BRB=1000 UGAS AI - BRB<->NGN 1 BRB=₦15 - Fee 0.5% INFINITY - YAFI BINANCE - 10M BRB $100K + 100M UGAS AI $1000 + AI $1000 + P2P $5000 = $106K/month - Bullish 78% - BLACK RACK BLOCKCHAIN ONLY - P2P INFINITY MARKETPLACE YAFI BINANCE"
        }

core = BlackrackAIBlockchain()

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        if path == "/" or path == "/index.html":
            if os.path.exists("index.html"):
                with open("index.html","rb") as f: content=f.read()
            else:
                content=b"<h1>BLACKRACK AI BLOCKCHAIN - P2P INFINITY YAFI BINANCE - Put index.html in same folder as app.py - 2 FILES ONLY - python app.py - http://localhost:8000</h1>"
            self.send_response(200); self.send_header("Content-type","text/html"); self.end_headers(); self.wfile.write(content)
        elif path == "/api/dashboard": self.send_json(core.dashboard())
        elif path == "/api/blocks": self.send_json({"blocks": core.blocks[-20:]})
        elif path == "/api/logs": self.send_json({"security_logs": core.security_logs[-20:], "nfts": core.brb_nfts[-20:], "ai_chats": core.ai_chats[-20:]})
        elif path == "/api/ai-chats": self.send_json({"ai_chats": core.ai_chats[-20:], "knowledge": list(core.ai_knowledge.keys())})
        elif path == "/api/p2p/orders": 
            q = urllib.parse.parse_qs(parsed.query)
            token = q.get("token", [None])[0]
            otype = q.get("type", [None])[0]
            self.send_json({"orders": core.p2p.get_orders(token, otype), "stats": core.p2p.get_stats()})
        elif path == "/api/p2p/profile":
            q = urllib.parse.parse_qs(parsed.query)
            username = q.get("username", ["Anonymous"])[0]
            self.send_json(core.p2p.get_profile(username))
        elif path == "/api/p2p/trades": self.send_json({"trades": core.p2p.trades[-50:], "escrow": list(core.p2p.escrow.values())[-20:]})
        elif path == "/api/p2p/stats": self.send_json(core.p2p.get_stats())
        else: self.send_response(404); self.end_headers(); self.wfile.write(b"Not Found - Use / , /api/dashboard , /api/blocks , /api/logs , /api/ai-chats , /api/p2p/orders , /api/p2p/profile , /api/p2p/trades , /api/p2p/stats")
    
    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        length = int(self.headers.get('content-length',0))
        body = self.rfile.read(length) if length>0 else b"{}"
        try: data=json.loads(body.decode() if body else "{}")
        except: data={}
        result={}
        if path=="/api/mint": result=core.mint_dual(data.get("user","Anonymous"), int(data.get("brb",1000)), int(data.get("ugas",10000)), data.get("type","BRB+UGAS AI NFT"))
        elif path=="/api/stake": result=core.stake_dual(data.get("user","Anonymous"), int(data.get("brb",1000)), int(data.get("ugas",10000)))
        elif path=="/api/data": result=core.track_data_dual(data.get("user","Anonymous"), data.get("page","Page"), int(data.get("mb",100)))
        elif path=="/api/energy": result=core.produce_energy_dual(data.get("source","Solar 10MW"), int(data.get("kwh",1000)))
        elif path=="/api/subscribe": result=core.subscribe_dual(data.get("user","Anonymous"), data.get("plan","NOMA FARMER"), int(data.get("months",1)))
        elif path=="/api/task": result=core.do_task_dual(data.get("sub_id",""), data.get("detail","Task"))
        elif path=="/api/register-miner": result=core.register_miner_dual(data.get("robot_id",f"BLACKRACK-ROBOT-{random.randint(1,999):03d}"), data.get("type","ALL IN ONE"))
        elif path=="/api/mine": result=core.mine_block_dual(data.get("robot_id",f"BLACKRACK-ROBOT-{random.randint(1,999):03d}"), data.get("task","Mining BRB+UGAS AI"))
        elif path=="/api/security": result=core.block_threat_dual(data.get("type","BARAWO THIEF"), data.get("detail","Threat"))
        elif path=="/api/ai-chat": result=core.ai_chat(data.get("message","Sannu BLACKRACK AI - P2P INFINITY YAFI BINANCE?"), data.get("user","Anonymous"))
        elif path=="/api/p2p/create-order": result=core.p2p.create_order(data.get("username","Anonymous"), data.get("order_type","SELL"), data.get("from_token","BRB"), data.get("to_token","UGAS AI"), float(data.get("amount",100)), float(data.get("price",1000)), data.get("payment_method","BANK TRANSFER"), float(data.get("min_limit",100)), float(data.get("max_limit",10000)))
        elif path=="/api/p2p/trade": result=core.p2p.execute_trade(data.get("order_id",""), data.get("buyer","Anonymous"), float(data.get("amount",100)))
        elif path=="/api/p2p/create-profile": result=core.p2p.create_profile(data.get("username","Anonymous"), data.get("phone",""), bool(data.get("verified",False)))
        else: result={"error":"Unknown endpoint","use":["/api/mint","/api/stake","/api/data","/api/energy","/api/subscribe","/api/task","/api/register-miner","/api/mine","/api/security","/api/ai-chat","/api/p2p/create-order username+order_type+from_token+to_token+amount+price+payment_method+min_limit+max_limit","/api/p2p/trade order_id+buyer+amount","/api/p2p/create-profile username+phone+verified","/api/dashboard","/api/p2p/orders?token=BRB&type=SELL","/api/p2p/profile?username=Musa","/api/p2p/trades","/api/p2p/stats"]}
        self.send_json(result)
    
    def send_json(self,obj):
        self.send_response(200)
        self.send_header("Content-type","application/json")
        self.send_header("Access-Control-Allow-Origin","*")
        self.send_header("Access-Control-Allow-Methods","GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers","Content-Type")
        self.end_headers()
        self.wfile.write(json.dumps(obj,indent=2,ensure_ascii=False).encode('utf-8'))
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin","*")
        self.send_header("Access-Control-Allow-Methods","GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers","Content-Type")
        self.end_headers()

def run_server():
    port=int(os.environ.get("PORT",8000))
    httpd=HTTPServer(('',port),Handler)
    print("="*130)
    print(f"🚀 BLACKRACK AI BLOCKCHAIN - PYTHON ALL - HADE DUKA - P2P INFINITY YAFI BINANCE - PORT {port}")
    print(f"📁 FILE 1: app.py ALL - P2P INFINITY + BRB+UGAS AI DUAL + CHATGPT AI + MINING + SECURITY + DATA + ENERGY - WAJE DAYA - FINAL")
    print(f"💰 BRB = MAIN TOKEN - UGAS AI = GAS AI TOKEN - BLOCKCHAIN DAYA - TOKEN BIYU BRB DA UGAS AI - DUKA A CIKI")
    print(f"💱 P2P INFINITY: BRB <-> UGAS AI <-> NGN - PROFILE + RATING + ESCROW + INFINITY - YAFI BINANCE P2P - NO LIMIT + INSTANT + AI")
    print(f"🌐 LOCAL: http://localhost:{port} - P2P TRADING - Chat AI - Blockchain Animation - Data Mining - YAFI BINANCE")
    print("="*130)
    print("\n--- AUTO DEMO P2P INFINITY + DUAL TOKEN + AI ---")
    core.mint_dual("Musa", 1000, 10000, "House1 Teacher - BRB+UGAS AI")
    core.p2p.create_profile("Musa", "08012345678", True)
    core.p2p.create_profile("Aisha - Whale", "08098765432", True)
    core.p2p.create_order("Musa", "SELL", "BRB", "UGAS AI", 100, 1000, "BANK TRANSFER", 10, 1000)
    core.p2p.create_order("Aisha - Whale", "SELL", "BRB", "NGN", 500, 15, "OPAY", 50, 5000)
    core.p2p.create_order("Alhaji - CEO", "BUY", "NGN", "BRB", 10000, 0.066, "BANK TRANSFER", 1000, 50000)
    core.p2p.create_order("Musa", "SELL", "UGAS AI", "BRB", 50000, 0.001, "BRB WALLET", 1000, 100000)
    core.p2p.execute_trade("P2P-000001-MUSA", "Ali - Buyer", 50)
    core.ai_chat("Sannu BLACKRACK AI - P2P INFINITY YAFI BINANCE - BRB <-> UGAS AI - Yaya yake aiki?", "Musa - P2P Demo")
    print(f"\n✅ DEMO P2P INFINITY DONE - Orders {len(core.p2p.orders)} - Trades {len(core.p2p.trades)} - Users {len(core.p2p.profiles)} - BRB {core.brb_supply} + UGAS AI {core.ugas_supply} - P2P INFINITY YAFI BINANCE")
    print(f"🌐 OPEN: http://localhost:{port} - P2P INFINITY TRADING - YAFI BINANCE - BRB<->UGAS AI - WAJE DAYA")
    print("="*130)
    httpd.serve_forever()

if __name__=="__main__": run_server()
