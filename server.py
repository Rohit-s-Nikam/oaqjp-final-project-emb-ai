"""Flask server for the emotion detection application."""

from flask import Flask, jsonify, render_template, request

from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def render_index_page():
    """Render the main application page."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """Detect emotions from the supplied text."""
    text_to_analyse = request.args.get("textToAnalyze")

    if not text_to_analyse or not text_to_analyse.strip():
        return jsonify({
            "error": "Invalid text! Please try again!"
        }), 400

    response = emotion_detector(text_to_analyse)

    if response is None or response.get("dominant_emotion") is None:
        return jsonify({
            "error": "Invalid text! Please try again!"
        }), 400

    return jsonify(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
