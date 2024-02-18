# Express-Server

Express-Server is a lightweight and fast web server for Python, inspired by the simplicity  of Express.js.

![images](https://camo.githubusercontent.com/f6128b6a17c28ec054b7ab67e595d39f503a0e17b116901141c05e1a1016985a/68747470733a2f2f692e636c6f756475702e636f6d2f7a6659366c4c376546612d3330303078333030302e706e67)

**Simple Syntax**
```python
from express_server import express
app = express()

def home(req,res,next):
    return res.send("Hello World")

app.get("/",home)

app.listen(3000)
```

### Installation

This is a [Python](https://python.org/) library available through the pip registry.

Before installing, download and install [python](https://www.python.org/downloads/). Python 3.1 or higher is required.

Installation is done using the pip command:
```shell
$ pip install express-server
```

#### 🛠️ **This project is currently in development! Use For Fun**

We are actively working on improving and expanding this project. While many features are functional, there may be bugs or incomplete functionality. If you encounter any issues or have suggestions, feel free to open an issue or contribute to the development.

#### Security Notice

🔒 **This project is not intended for production use, and it may not be secure.**

As a work in progress, security considerations have not been fully addressed. Avoid using this project in a production environment or with sensitive data.

#### Links
* PyPI Releases: https://pypi.org/project/express-server/
* Github Code: https://github.com/avinashtare/express-server-python