from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Akshay's Flask app running in Docker and deployed via GitHub Actions to AWS ECS!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
