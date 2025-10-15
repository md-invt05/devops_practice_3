from flask import Flask, jsonify
from datetime import datetime
import os

app = Flask(__name__)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/payload")
def payload():
    student = os.getenv("STUDENT_NAME", "Degtyarev")
    group = os.getenv("STUDENT_GROUP", "EFBO-02-23")
    data = {
        "student": student,
        "group": group,
        "timestamp_utc": datetime.utcnow().isoformat(timespec="seconds") + "Z"
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
