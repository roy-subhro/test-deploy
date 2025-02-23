
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/accept',methods=['POST'])
def anyfunc():
    data = request.get_json()
    num1 = data.get('a')
    num2 = data.get('b')
    return jsonify({'sum': num1+num2})

if __name__ == '__main__':
    app.run(debug=True, host='13.233.131.202', port=80)