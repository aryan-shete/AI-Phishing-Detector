from flask import Flask, render_template, request
from detector import detect

app = Flask(__name__)


def classify(score):
    """Map a 0-100 score to a risk bucket and gauge needle angle."""
    if score is None:
        return None, None

    if score > 60:
        risk = "high"
    elif score > 30:
        risk = "medium"
    else:
        risk = "low"

    # Gauge sweeps 270deg starting at 135deg (see index.html for the
    # matching arc geometry). 0 -> 135deg, 100 -> 45deg (405 % 360).
    needle_angle = (135 + 2.7 * score) % 360

    return risk, needle_angle


@app.route("/", methods=["GET", "POST"])
def home():

    score = None
    reasons = []
    risk = None
    needle_angle = None

    if request.method == "POST":
        email = request.form["email"]

        score, reasons = detect(email)
        risk, needle_angle = classify(score)

    return render_template(
        "index.html",
        score=score,
        reasons=reasons,
        risk=risk,
        needle_angle=needle_angle,
    )


if __name__ == "__main__":
    app.run(debug=True)