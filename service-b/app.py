from flask import Flask, jsonify, request
import os, requests

SERVICE_A_URL = os.getenv("SERVICE_A_URL", "http://service-a:5000/payload")
PROJECT_URL = os.getenv("PROJECT_URL")  

app = Flask(__name__)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/forward")
def forward():
    # Pull data from service-a
    try:
        src = requests.get(SERVICE_A_URL, timeout=5)
        src.raise_for_status()
        payload = src.json()
    except Exception as e:
        return jsonify({"ok": False, "error": f"failed to fetch from service-a: {e}"}), 502

    result = {"fetched_from_service_a": payload, "project_post_status": "skipped (no PROJECT_URL set)"}

    if PROJECT_URL:
        try:
            r = requests.post(PROJECT_URL, json=payload, timeout=5)
            result["project_post_status"] = f"posted to {PROJECT_URL}, http {r.status_code}"
        except Exception as e:
            result["project_post_status"] = f"post failed: {e}"

    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
