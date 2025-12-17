from flask import Flask
import os
import threading
import bot_main  # your bot.py logic as module

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

# Run bot in a separate thread
threading.Thread(target=bot_main.run_bot).start()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
  
