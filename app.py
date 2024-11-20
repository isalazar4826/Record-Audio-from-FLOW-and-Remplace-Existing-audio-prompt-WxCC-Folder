from flask import Flask, request, jsonify
import os
import requests
import time
import json

app = Flask(__name__)

# Carpeta donde se guardarán los archivos subidos
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

org_id = "{YOUR ORG ID}"  # Your ORG ID
audio_id = "{ID AUDIO TO REMPLACE}"  # ID FROM FILE TO REMPLACE
url = f"https://api.wxcc-us1.cisco.com/organization/{org_id}/audio-file/{audio_id}"

token = "{YOUR TOKEN}"  # YOUR TOKEN

@app.route('/upload', methods=['POST'])
def upload_file():
    # Verificar si la solicitud contiene archivos 
    if 'aviso1.wav' not in request.files:  # avisio1.wax is the name of the existing file to remplace
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['aviso1.wav']
    
    # Verificar si se seleccionó un archivo
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Guardar el archivo
    file_path = os.path.join(UPLOAD_FOLDER, 'aviso1.wav') # avisio1.wav is the name of the existing file to remplace
    file.save(file_path)

    # Preparar información del archivo de audio para la API
    audio_name = "aviso1.wav"  # avisio1.wav is the name of the existing file to remplace
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
