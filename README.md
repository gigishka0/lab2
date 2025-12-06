Завдання 1

У першому завданні необхідно запустити веб сервер на порту 8000 у Python.
```python
from flask import Flask
app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=8000, debug=True)
```

Завднання 2

У другому завданні потрібно обробити медот GET.
```python
from flask import Flask
app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello_world():
    return "Hello World"

if __name__ == '__main__':
    app.run(port=8000)
```

<img width="334" height="120" alt="image" src="https://github.com/user-attachments/assets/46f3259f-96cd-4020-81df-58898ad522fa" />

Завдання 3 

У третьому завданні потрібно обробити GET запит із параметрами в URL та повернути статичне значення курсу валют.

```python
from flask import Flask, request

app = Flask(__name__)

@app.get("/currency")
def currency():
    today = request.args.get("today")
    key = request.args.get("key")

    return "USD - 41.5"

if __name__ == "__main__":
    app.run(port=8000)
```

<img width="269" height="119" alt="image" src="https://github.com/user-attachments/assets/e19c47f3-1297-414c-9348-194a99e76262" />

Завдання 4

У четвертому завданні потрібно повернути різні типи даних в залежності від заголовку Content-Type.
Сервер має видати JSON, XML або звичайний текст.

```python
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

```

<img width="277" height="138" alt="image" src="https://github.com/user-attachments/assets/ad4c2098-8f62-488d-ad06-9cd39b848272" />

