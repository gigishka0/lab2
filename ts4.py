from flask import Flask, request, jsonify
app = Flask(__name__)

@app.get("/")
@app.get("/info")
def info():
    ctype = request.headers.get("Content-Type")

    match ctype:
        case "application/json":
            return jsonify({"message": "JSON response"})

        case "application/xml":
            xml = "<response><message>XML response</message></response>"
            return app.response_class(xml, mimetype="application/xml")

        case _:
            return "lb2"

if __name__ == "__main__":
    app.run(port=8000)
