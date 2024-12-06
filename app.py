from flask import Flask, render_template, request, jsonify, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        expression = data['expression']
        result = eval(expression)  # Note: eval() is used for simplicity, but it's not secure for production
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) 