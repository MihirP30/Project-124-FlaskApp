from flask import Flask,jsonify, request

app = Flask(__name__)

contacts = [
    {
        'id': 1,
        'Name': u'Contact1',
        'Contact': u'1111111111', 
        'done': False
    },
    {
        'id': 2,
        'Name': u'Contact2',
        'Contact': u'2222222222', 
        'done': False
    }
]

@app.route("/add-data", methods=["POST"])
def add_contact():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please enter a contact's information"
        },400)

    contact = {
        'id': contacts[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ""),
        'done': False
    }
    contacts.append(contact)

    return jsonify({
        "status":"success",
        "message": "Contact was added"
    })
    

@app.route("/get-data")
def get_contact():
    return jsonify({
        "data" : contacts
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)