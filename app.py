from flask import Flask, request, jsonify
import os
import requests
import time
import json

app = Flask(__name__)

# Carpeta donde se guardarán los archivos subidos
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

org_id = "d9cd7ecf-e6e1-49fb-ab07-a69cb49ea081"  # Coloca tu Organization ID
audio_id = "ce273f0f-5d95-4ffc-a395-a5bfd1aa30b9"  # ID del archivo de audio a actualizar
url = f"https://api.wxcc-us1.cisco.com/organization/{org_id}/audio-file/{audio_id}"

token = "eyJhbGciOiJSUzI1NiJ9.eyJjbHVzdGVyIjoiUDBBMSIsInByaXZhdGUiOiJleUpqZEhraU9pSktWMVFpTENKbGJtTWlPaUpCTVRJNFEwSkRMVWhUTWpVMklpd2lZV3huSWpvaVpHbHlJbjAuLndnUlRNMzNNelY0cVpJM08zYWc1b2cueldmS294WkJkRFppQWhjRy10TGI5N2U4eldOQV9ZTEVmQVpRT0tyNlVJUDJHR3kwTl8yYTJWU0w2QXpwTWxkNTVaVDJGQy1XcUNINGN4UjlVWEVtbWQ5T21JMDZRTmJiTnZaeDNnUDVkMk9Ic0tJUWw4ZTJaR2hRN0kyblF4aElocjFOckJBWWNuWWtXTWlUY0IzcVppVDVpNFdaR0doWEk5YS1LMWtFRlNPMklDZk1rU1ExWWxVR2g2VXgtaTBxdmltdnA4Yl9venByYzRwa21Ra2JuOTdrVVk5RTM5TEVuemMxR0Y0ZlJZOUEycXhWRTRVeUNkZHFqRC1kaXVPd1drYVBwRGhnbWNnNDl0NVJMbGZyNUY2N3UxSWtkaGxEck5lamt1QnlqU0QzOVF4d0pSRjdGNnBQYzVOMFN4c1Q0SVhZQ1dQVFZHVEtWMFJqUXQwcUVxelFYSTdPai1YSzR3RmtDVFdrRHo3SWM3c2JsSGhWR3BLSnhIVEpvX3ZiQ1RpeUkwUHI5R3U5WUNHeWlFNjJra3dzTElBUFNFTmJDdy1lU1p0bVBlX1ByZThtLTJsQUNYbWFHZ1RRVW01ZjFXcERkRnRuT2M2SGNna0RHaEE5ckEtV0Fra1B5TzdrOVBOUG13Y2RrYmJkUXVUekZfbU1mUzQ4VG13TW1GeHJQX1hjT0RlY2R0d3NjblRTcjZvdU1uZzJDS2NSRlJRS1U3eFd2U3lGcnNrRnRKUG9LMFpfY3VHMkRVMFF1QUJRMkhqN1RGeVdCRENDTHJKdk52WnZHa2xBQTl4bzJpZ3AxVTBJaVJWaWpOSDA5YUlPZVJrWmNpMlp4ajNXMTRPVlRJaTBydXl5OUdpVVlPTG52aVRkYUtRY1NPS25lUXJFUXo1N2FlQk4tOGh3RU11cGQzVnY2LUN2dGM2TDJaaE0tdXVfSjlncDdCeTYyM0RDMzRyVFNlZDRXd04yRFZLZWctOWMxUjR4N1lLekRKekw5aHBtSVpQOW9CTWlueF9FdVBtNHhWN3JHV2lOUl85N3Z5Mm5yNWg1Z2Q4LW1xYmNFWFZ5Wng3bFdmMFNXdE1Val82TXdSV2VzZjlNaTdKa3RSYjFRXzdTV2dxUkN4MjJ0QUxKa3ZOeFBXYnJlZXgzc243ZEQ0blNuU1RUckd3S2J6OFg0bmY3WldjQUdHRHRzMkMzdXFBellnajRsZzNDRUtJTFR5VXdJa3dWMjBrZFhrbE83bXBJdEJPdXhDYnBqV1pCOHhRWDFFLXZ2a0RsdGNqaTJpT3pMNUs1b185NGE0T0FvUTJMMHpCNmZfRkxUVEhycjNGSXh4MjQ0MTRkR2hlZEJvZEQzMGRCUXlhY1Y1cE9SYksxamdDVkFuUVhMNFlTVkxpUFYyN3VzVEg5dEp5M2VGTXJkV28tM3ZxX0xrd0Q0cW9QOFlXNUdJSmhSeDdxbjNydTAzSUZ5VGhUYU01R1RxazlwOG54MGJ3bHZhS1J0SUs1S014OUlZNkFRQmFpR1Q2Q3JKaXVSczNiTWViWEdpeWJSbkp0UGR5ekY2WWRkMXZ2cGw1SnhYVW9TMWxfWnFXLTB0V0hXMUVqMjFzRTZaSk80Wjk5TlNxay5GUnd1WlNnSVpkeWVnbG4xNmI5c3BnIiwidXNlcl90eXBlIjoidXNlciIsInRva2VuX2lkIjoiQWFaM3IwTW1aaE9UWXpNamN0TURjelppMDBaRFUwTFRrNU1URXRaamN6TTJVeVpXRTFOamt3TjJZd1lqZzJZekl0TVRKaSIsInJlZmVyZW5jZV9pZCI6IjQ5MDQxY2UwLTQ0YWUtNDgyYS04YWIyLTZjNTU3YzZlYjc0MiIsImlzcyI6Imh0dHBzOlwvXC9pZGJyb2tlci1iLXVzLndlYmV4LmNvbVwvaWRiIiwidXNlcl9tb2RpZnlfdGltZXN0YW1wIjoiMjAyNDExMTkyMTI0MTIuNzY0WiIsInJlYWxtIjoiZDljZDdlY2YtZTZlMS00OWZiLWFiMDctYTY5Y2I0OWVhMDgxIiwiY2lzX3V1aWQiOiI5ZGI1ZjlhYy00MmUwLTRlMTItOGZjZC1hNGRjMWNjNzFiMDQiLCJ0b2tlbl90eXBlIjoiQmVhcmVyIiwiZXhwaXJ5X3RpbWUiOjE3MzIxMjIyNDM5MjQsImNsaWVudF9pZCI6IkM1ODI1NGYzOGNlMDBlYzdhZmQxYjYwNjZmOTdlM2MyNjgwZjgxOWZhZWZlNjhhOTY1MjE5N2EzYTllMTg4N2M0In0.iFP1MKazny4jyiF1gdaBCQvwa0pydU-v7wCL30adrgzVy4kHOiiT3mA7W2XHxpVghVDrCS24gWeD6uyc6LVdh8qxVn6oWGhDavogB9YG9_at7yj2MZbo6jKlVa5h_dIZWT0HqROrrgmJVA4JFsC7tzlB7Shpg2dPJ_pwdtzcrYqM11On-PWvBquT9N33MbBfohCxXcihMYuNy4IOWqm8gc1dXVOekozIcflYliVntc5iiiS3kxoOQXc0q_RfUlfKN36FUMLVbI9MDla44lZzuX9f4f4I_xgu_AvGN888E2jrVeWsnEjrgoHUi-3VMDfCXJBzg9Zb17Y432adibZl1g"  # Reemplaza con tu token de acceso

@app.route('/upload', methods=['POST'])
def upload_file():
    # Verificar si la solicitud contiene archivos
    if 'aviso1.wav' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['aviso1.wav']
    
    # Verificar si se seleccionó un archivo
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Guardar el archivo
    file_path = os.path.join(UPLOAD_FOLDER, 'aviso1.wav')
    file.save(file_path)

    # Preparar información del archivo de audio para la API
    audio_name = "aviso1.wav"  # Nombre del archivo en el sistema
    audio_file_info = {
        "blobId": "audio-file_ad97c5bf-fe08-44a7-a707-85ce28cb305d",
        "contentType": "AUDIO_WAV",
        "createdTime": int(time.time() * 1000),
        "id": audio_id,
        "lastUpdatedTime": int(time.time() * 1000),
        "name": audio_name,
        "organizationId": org_id,
        "version": 1
    }

    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {token}"
    }

    # Realizar la solicitud PUT a la API para reemplazar el archivo de audio
    with open(file_path, "rb") as audio_file:
        files = {
            "audioFile": audio_file,
            "audioFileInfo": (None, json.dumps(audio_file_info), "application/json")
        }
        response = requests.put(url, headers=headers, files=files)

    # Retornar respuesta de la API
    if response.status_code == 200:
        return jsonify({'message': 'File uploaded and replaced successfully', 'file_path': file_path, 'api_response': response.json()}), 200
    else:
        return jsonify({'error': 'Failed to update audio file', 'api_response': response.json()}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
