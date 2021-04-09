from flask import Flask,jsonify, request
import json
app = Flask(__name__)

todos = [{ "label": "My first task", "done": False }]
  
@app.route('/todos', methods=['GET'])
def hello_world():
     json_text = jsonify(todos)
     return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    decoded_object  = json.loads(request.data)  
    todos.append(decoded_object) 
    print("Incoming request with the following body", request.data)
    return jsonify(todos)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)