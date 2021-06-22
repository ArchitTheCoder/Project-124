from flask import Flask, request, jsonify

app = Flask(__name__)

contacts = [
    {
        'id': 1,
        'contact': "1234567890",
        'name': 'John Doe',
        'done': False
    },
    {
        'id': 2,
        'contact': "0987654321",
        'name': 'Bob',
        'done': False 
    }
]

@app.route("/")

@app.route('/add-data', methods=["POST"])
def Add_Data():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "Please provide the data"
        }, 400)
    contact = {
        'id': contacts[-1]["id"] + 1,
        "name": request.json['name'],
        "contact": request.json.get('contact', ""),
        "done": False
    }
    contacts.append(contact)
    return jsonify({
        "status": "success",
        "message": "Task added successfully"
    })

@app.route("/get-data")
def Get_Contact():
    return jsonify({
        "data": contacts
    })
    

if __name__ == '__main__':
    app.run()