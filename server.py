from flask import Flask, request, jsonify, render_template
from LANclient_rest_api import LANclient_Blueprint

app = Flask(__name__)

@app.route('/')
def swagger():
    print('sending root test api 2')
    return render_template('swaggerui.html')

#LANclients API
app.register_blueprint(LANclient_Blueprint)

app.run(debug=True,port=5001,host="0.0.0.0")