from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods = ['GET'])

def ReturnJson():
  if(request.method == 'GET'):
      data = {
		"slackUsername": 'Lost-kode',
		"backend": True,
		"age": 25,
		"bio": "A backend developer with python and javascript skills"
	}
      return jsonify(data)
if __name__ == '__main__':
	app.run(debug=True)
