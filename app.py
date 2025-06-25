
from flask import Flask, request, jsonify
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse
from twilio.twiml.messaging_response import MessagingResponse
from reply_engine import generate_reply
from tts_engine import speak_reply
import os
import json

app = Flask(__name__)

# Environment variables
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH = os.getenv("TWILIO_AUTH")
TWILIO_WHATSAPP = os.getenv("TWILIO_WHATSAPP")
TWILIO_CALLER = os.getenv("TWILIO_CALLER")
MY_PHONE = os.getenv("MY_PHONE")

client = Client(TWILIO_SID, TWILIO_AUTH)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming = request.values.get("Body", "")
    print(f"Steve: {incoming}")
    reply = generate_reply(incoming)
    response = MessagingResponse()
    response.message(reply)
    return str(response)

@app.route("/voice", methods=["POST"])
def voice():
    resp = VoiceResponse()
    reply_text = "Hi Steve. Just calling to check in. How are you doing?"
    audio_url = speak_reply(reply_text)
    resp.play(audio_url)
    return str(resp)

@app.route("/")
def home():
    return "AI Best Friend running."

if __name__ == "__main__":
    app.run()
