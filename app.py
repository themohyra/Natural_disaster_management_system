from flask import Flask, render_template, request, jsonify
from supabase import create_client
import os

app = Flask(__name__)

# Supabase config
SUPABASE_URL = "https://bpjejgmgfuaukpyohqop.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJwamVqZ21nZnVhdWtweW9ocW9wIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDY5ODQxMzMsImV4cCI6MjA2MjU2MDEzM30.0mIQ6ma2To9bRaWlspMhwMG8nvxo-M2EHC8Ofi6KY8Y"
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/send-alert", methods=["POST"])
def send_alert():
    data = request.get_json()
    contact = data.get("contact")
    message = data.get("message")

    if not contact or not message:
        return jsonify({"status": "error", "message": "Contact and message required"}), 400

    try:
        # Insert into Supabase table
        supabase.table("alerts").insert({"contact": contact, "message": message}).execute()
        return jsonify({"status": "success", "message": "Alert sent and stored!"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
