from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'message': 'Hello from Flask!',
        'status': 'success',
        'version': '1.0.0'
    }), 200

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'service': 'flask-app'
    }), 200

@app.route('/test')
def test():
    return jsonify({
        'message': 'Jenkins pipeline test endpoint',
        'status': 'ok'
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

