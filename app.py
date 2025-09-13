from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample in-memory data storage
items = []

@app.route('/')
def home():
    return jsonify({'message': 'Welcome to the API'}), 200

@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify({'items': items}), 200

@app.route('/api/items', methods=['POST'])
def add_item():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'error': 'Name is required'}), 400
    
    item = {
        'id': len(items) + 1,
        'name': data['name']
    }
    items.append(item)
    return jsonify({'message': 'Item added', 'item': item}), 201

@app.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    item = next((item for item in items if item['id'] == item_id), None)
    if not item:
        return jsonify({'error': 'Item not found'}), 404
    
    items = [item for item in items if item['id'] != item_id]
    return jsonify({'message': 'Item deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)