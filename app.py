from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Chester Trading Bot is Live 🚀'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    # Add logic to execute trade based on TradingView alert
    print(f"Received alert: {data}")
    return '', 200

if __name__ == '__main__':
    app.run()
