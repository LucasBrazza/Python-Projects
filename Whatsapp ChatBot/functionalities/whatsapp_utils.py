from email import message
from flask import current_app, jsonify
import json
import logging
import requests
import re

def logHttpResponse(response):
    logging.info(f"Status: {response.status_code}")
    logging.info(f"Content-type: {response.headers.get('content-type')}")
    logging.info(f"Body: {response.text}")


def getTextMessageInput(recipient, text):
    return json.dumps(
        {
            "messagin_product": "whatsapp",
            "recipient_type": "individual",
            "to": recipient,
            "type": "text",
            "text": {"preview_url": False, "body": text},
        }
    )


def generateResponse(response):
    return response.upper()


def sendMessage(data):
    headers = {
        "Content-type": "application/json",
        "Authorization": f"Beatrer {current_app.config['ACCESS_TOKEN']}/{current_app.config['PHONE_NUMBER_ID']}/messages",
    }
    
    url = f"https://graph.facebook.com/{current_app.config['VERSION']}/{current_app.config['PHONE_NUMBER_ID']}/messages"

    try:
        response = request.post(
            url, data=data, headers=headers, timeout=5
        )
        response.raise_for_status()
    
    except requests.Timeout:
        logging.error("Timeout occured while sending message")
        return jsonify({"status": "error", "message": "Timeout"}), 408
    
    except requests.RequestException as e:
        logging.error(f"Request exception occured: {e}")
        return jsonify({"status": "error", "message": "Failed to send message"}), 500
    
    else:
        logHttpResponse(response)
        return response
    

def processTextForWhatsapp(text):
    # Remove brackets
    pattern = r"\ [.*?\] "
    
    # Substitute the pattern with empty string
    text = re.sub(pattern, "", text).strip()
    
    # Pattern to find double asteriscks including the text inside
    pattern = r"\*\*(.*?)\*\*"
    
    #replacement pattern with single asterisks
    replacement = r"*\1*"
    
    # Substitute occurrences of the pattern with the repalcement pattern
    return re.sub(pattern, replacement, text)


def processWhatsappMessage(body):
    wa_id = body["entry"][0]["changes"][0]["value"]["contacts"][0]["wa_id"]
    name = body["entry"][0]["changes"][0]["value"]["contacts"][0]["profile"]["name"]

    message = body["entry"][0]["changes"][0]["value"]["messages"][0]
    message_body = message["text"]["body"]

    # TODO: custom logic to process the message
    response = generateResponse(message_body)
    
    data = getTextMessageInput(current_app.config["RECIPENT_WAID"], response)
    sendMessage(data)
    

def isValidWhatsappMessage(body):
    return (
        body.get("entry")
        and body["entry"][0].get("changes")
        and body["entry"][0]["changes"][0].get("value")
        and body["entry"][0]["changes"][0]["value"].get("messages")
        and body["entry"][0]["changes"][0]["value"]["messages"][0]
    )