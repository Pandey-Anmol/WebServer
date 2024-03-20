from flask import Flask, request, jsonify, json, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def showRequest():
    def reshowData():
        return render_template("show_request.html",
                               request_data = request_data,
                               req_header = req_header,
                               req_method = req_method)
    if (request.method == 'POST'):
        request_data = request.json
        reshowData()
        return jsonify(request_data)
    request_data = request.data
    req_header = request.headers
    req_method = request.method

    return render_template("show_request.html", 
                        request_data = request_data,
                        req_header = req_header,
                        req_method = req_method)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)