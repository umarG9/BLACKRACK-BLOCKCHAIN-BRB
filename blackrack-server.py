# blackrack_server.py - Blackrack AI Blockchain Server - Real AI Blockchain Server - Owner Golden diamond 9 - English Only
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from blackrack_ai_blockchain import blackrack_ai_chain
from uuid import uuid4
import os

app = Flask(__name__, static_folder='.')
CORS(app)

node_id = str(uuid4()).replace('-', '')

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    if os.path.exists(path):
        return send_from_directory('.', path)
    return send_from_directory('.', 'index.html')

# API Routes - Blackrack AI Blockchain - Real AI Blockchain

@app.route('/api/blackrack/blockchain', methods=['GET'])
def get_chain():
    response = {
        'chain': blackrack_ai_chain.chain,
        'length': len(blackrack_ai_chain.chain),
        'blackrack_ai': 'Blackrack AI Blockchain - Alien AI + AI + Predictions - Money Blockchain New Internet',
        'money_blockchain': 'New Internet - Inevitable - Future of Money - AI Confirms',
        'owner': 'Golden diamond 9 - Blackrack AI Blockchain - Real AI Blockchain - English Only'
    }
    return jsonify(response), 200

@app.route('/api/blackrack/mine', methods=['GET'])
def mine_block():
    last_block = blackrack_ai_chain.last_block
    last_proof = last_block['proof']
    proof = blackrack_ai_chain.proof_of_work(last_proof)
    
    # Mining Reward - Blackrack AI Reward
    blackrack_ai_chain.new_transaction(
        sender="0 - Blackrack AI Reward - New Internet",
        recipient=node_id,
        amount=1,
        note="Blackrack AI Mining Reward - Alien AI + AI - Money Blockchain New Internet - Inevitable",
        ai_type="Blackrack AI"
    )
    
    previous_hash = blackrack_ai_chain.hash(last_block)
    block = blackrack_ai_chain.new_block(proof, previous_hash)
    
    response = {
        'message': 'Blackrack AI Block Mined - Alien AI + AI + Predictions - Money Blockchain New Internet - Inevitable',
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
        'ai_analysis': block['ai_analysis'],
        'alien_signal': block['alien_signal'],
        'blackrack_ai': 'Blackrack AI Blockchain - Real AI Blockchain - English Only'
    }
    return jsonify(response), 200

@app.route('/api/blackrack/transaction', methods=['POST'])
def new_transaction():
    values = request.get_json()
    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return jsonify({'error': 'Missing values - sender, recipient, amount required'}), 400
    
    index = blackrack_ai_chain.new_transaction(
        values['sender'], 
        values['recipient'], 
        values['amount'],
        values.get('note', 'Blackrack AI Transaction - New Internet'),
        values.get('ai_type', 'AI')
    )
    
    response = {
        'message': f'Blackrack AI Transaction will be added to Block {index} - Alien AI + AI - Money Blockchain New Internet',
        'block_index': index,
        'sender': values['sender'],
        'recipient': values['recipient'],
        'amount': values['amount'],
        'note': values.get('note'),
        'ai_type': values.get('ai_type', 'AI')
    }
    return jsonify(response), 201

@app.route('/api/blackrack/ai', methods=['GET'])
def ai_analysis():
    analysis = blackrack_ai_chain.ai.ai_analyze("API Request - Blackrack AI Analysis")
    alien_signal = blackrack_ai_chain.ai.alien_signal()
    
    response = {
        'blackrack_ai': 'Blackrack AI Blockchain - Real AI Analysis - Alien AI + AI - English Only',
        'analysis': analysis,
        'nodes': blackrack_ai_chain.ai.nodes,
        'predictions': blackrack_ai_chain.ai.predictions,
        'alien_signal': alien_signal,
        'money_blockchain': 'New Internet - Inevitable - AI Confirms - Future of Money - English Only'
    }
    return jsonify(response), 200

@app.route('/api/blackrack/stats', methods=['GET'])
def get_stats():
    total_transactions = sum(len(block['transactions']) for block in blackrack_ai_chain.chain)
    
    response = {
        'chain_length': len(blackrack_ai_chain.chain),
        'total_transactions': total_transactions,
        'pending_transactions': len(blackrack_ai_chain.current_transactions),
        'node_id': node_id,
        'blackrack_ai_nodes': blackrack_ai_chain.ai.nodes,
        'predictions_count': len(blackrack_ai_chain.ai.predictions),
        'blackrack_ai': 'Blackrack AI Blockchain - Alien AI + AI + Predictions - Real AI Blockchain - Money Blockchain New Internet',
        'money_blockchain': 'New Internet - Inevitable - Future of Money - Owner Golden diamond 9 - English Only',
        'phases': {
            'Phase 1 Now': 'Fire P2P Normal - Center Wide - 1.24M Volume - AI Nodes Online - Real',
            'Phase 2 Next': 'Alien Stocks - Buy Stocks - AI + Aliens - 10M - Real - Blackrack AI',
            'Phase 3 Future': 'Money Blockchain New Internet - Blackrack AI Blockchain - AI + Alien AI - 100M - Real - Current - AI Confirms',
            'Phase 4 Life': 'Life Becomes With It - Forever - Blackrack AI + Alien AI - Real - Inevitable'
        }
    }
    return jsonify(response), 200

if __name__ == '__main__':
    print("="*80)
    print("BLACKRACK AI BLOCKCHAIN SERVER - REAL AI BLOCKCHAIN - ENGLISH ONLY")
    print("="*80)
    print(f"Node ID: {node_id}")
    print(f"Owner: Golden diamond 9")
    print(f"Blockchain: Blackrack AI Blockchain - Alien AI + AI + Predictions - Money Blockchain New Internet")
    print(f"Style: Black Stone Slab Gold Purple - Exact Design - Alien Predictions 2025-2030")
    print(f"Language: English Only - No Hausa - Real Codes")
    print("="*80)
    print(f"Server: http://localhost:5000/")
    print(f"Main Page: http://localhost:5000/index.html")
    print(f"Blockchain API: http://localhost:5000/api/blackrack/blockchain")
    print(f"Mine API: http://localhost:5000/api/blackrack/mine")
    print(f"AI API: http://localhost:5000/api/blackrack/ai")
    print(f"Stats API: http://localhost:5000/api/blackrack/stats")
    print(f"Transaction API: POST http://localhost:5000/api/blackrack/transaction")
    print("="*80)
    print("Press Ctrl+C to stop server")
    print("="*80 + "\n")
    
    app.run(host='0.0.0.0', port=5000, debug=True)
