from flask import Flask, render_template, request, jsonify
from cipher import cipher

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.get_json()
    message = data.get('message', '')
    mode = int(data.get('mode', 1))
    key = int(data.get('key', 1))
    
    try:
        result = cipher(message, mode, key)
        return jsonify({'success': True, 'result': result})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080) 