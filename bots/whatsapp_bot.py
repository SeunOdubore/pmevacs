# bots/whatsapp_bot.py
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=['POST'])
def whatsapp_reply():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()

    if 'hi' in incoming_msg:
        msg.body("🇳🇬 *VoteBoost NG*!\n1. QUIZ\n2. REGISTER\n3. POLL\n4. REFER")
    elif 'quiz' in incoming_msg:
        msg.body("🧠 Do you think your vote can change Nigeria? Reply YES/NO")
    else:
        msg.body("Send 'HI' to begin.")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)