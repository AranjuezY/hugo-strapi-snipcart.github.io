from flask import Flask, request
import os
import subprocess

app = Flask(__name__)

# This is a Flask application for a Hugo website auto deployment.
# When Flask receives a webhook from Strapi, it should fetch remote resources from Strapi api.
# The fetched data should be a json file in Data folder of Hugo project.
# Then Flask will trigger a Hugo website rebuild action.

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.json
        print(f"Received Webhook: {data}")

        rebuild_result = subprocess.run(
            ["bash", "./build.sh"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        if rebuild_result.returncode == 0:
            return "Rebuild Successful", 200
        else:
            return f"Rebuild Failed: {rebuild_result.stderr.decode()}", 500

    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == "__main__":
    app.run(port=5001)

