Завдання 1

У першому завданні необхідно запустити веб сервер на порту 8000 у Python.
```python
from flask import Flask
app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=8000, debug=True)
```

waww
