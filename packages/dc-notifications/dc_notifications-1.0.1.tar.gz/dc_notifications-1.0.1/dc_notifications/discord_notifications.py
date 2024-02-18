import requests
import os
import json


def send_notification(notification):
    EXTERNAL_DB = os.getenv("NOTIFICATION_URL")
    data = json.dumps({"notification": notification})
    try:
        requests.post(f"{EXTERNAL_DB}/notifications", data=json.dumps(data))
        return True, "La notificacion se envio correctamente"
    except Exception as e:
        return False, f"Error al enviar la notificacion: {e}"