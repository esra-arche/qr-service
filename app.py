from flask import Flask, request, redirect
import requests
from datetime import datetime

app = Flask(__name__)

LOGGING_URL = "https://webhook.site/31748e81-93df-4027-a93c-ff319b576fb2"

FINAL_URL_TEKNOSA = "https://www.teknosa.com/teknoclub"
FINAL_URL_MM = "https://www.mediamarkt.com.tr/tr/myaccount/loyalty-benefits"

@app.route("/track_mm")
def track_mm():  
    print("✅ /track called")

    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    user_agent = request.headers.get("User-Agent", "<not knowing>")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data = {
        "ip": ip,
        "user_agent": user_agent,
        "timestamp": timestamp
    }

    try:
        requests.post(LOGGING_URL, json=data, timeout=3)
        print("📨 Log sended:", data)
    except Exception as e:
        print("❌ Log error:", e)

    print("Redirect to final_url_mm:", FINAL_URL_MM)
    return redirect(FINAL_URL_MM)


@app.route("/track_teknosa")
def track_teknosa():  
    print("✅ /track called")

    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    user_agent = request.headers.get("User-Agent", "<not knowing>")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data = {
        "ip": ip,
        "user_agent": user_agent,
        "timestamp": timestamp
    }

    try:
        requests.post(LOGGING_URL, json=data, timeout=3)
        print("📨 Log sended:", data)
    except Exception as e:
        print("❌ Log error:", e)

    print("Redirect to final_url_teknosa:", FINAL_URL_TEKNOSA)
    return redirect(FINAL_URL_TEKNOSA)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

