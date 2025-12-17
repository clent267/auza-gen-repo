from flask import Flask
import os
import threading
import bot_main

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

# Start Discord bot in background thread
threading.Thread(target=bot_main.run_bot, daemon=True).start()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
