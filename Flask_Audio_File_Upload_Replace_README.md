
# Flask Audio File Upload and Replace Web Application

This project is a simple **Flask** application that allows you to upload an audio file and replace an existing audio file on the **Webex Contact Center** using their API.

## Requirements

- Python 3.7+
- Flask
- Requests
- Your Webex Contact Center API credentials (organization ID and API token)

## Setup

1. **Install the required packages**:

   Use `pip` to install the required dependencies:
   ```bash
   pip install flask requests
   ```

2. **Set your Webex Contact Center credentials**:
   - Replace `{YOUR ORG ID}` with your Webex organization ID.
   - Replace `{YOUR TOKEN}` with your Webex API token.
   - Replace `{ID AUDIO TO REMPLACE}` with the audio file ID you want to replace.

3. **Create the upload folder**:
   The application saves uploaded files in a folder called `uploads`. The app will automatically create this folder if it doesn't exist.

## Application Structure

The Flask application provides a simple route (`/upload`) that accepts POST requests to upload an audio file. The uploaded file will replace an existing audio file on Webex.

### Key features:
- **Audio File Upload**: Users can upload an audio file (e.g., `aviso1.wav`).
- **File Replacement**: The uploaded file will replace an existing file on Webex with a specific audio file ID.
- **Webex API Integration**: The app sends the file and its metadata (like name and ID) to the Webex API.

## How It Works

### 1. File Upload
When a POST request is made to the `/upload` route, the app checks for a file named `aviso1.wav`. If the file is present and valid, it is saved to the `uploads` folder.

### 2. Preparing Audio Information
The application prepares the audio file's metadata (e.g., `blobId`, `contentType`, `createdTime`, `name`, etc.) in a JSON format that the Webex API expects.

### 3. Sending File to Webex
Using the **PUT** method, the app sends the uploaded audio file and its metadata to the Webex Contact Center API to replace the existing file identified by `audio_id`.

### 4. Response Handling
After sending the file, the app checks the response from the Webex API. If the status code is `200`, the file has been successfully uploaded and replaced. Otherwise, the app returns an error message.

## Example of a POST Request

To upload a file, make a **POST** request to `http://localhost:5000/upload` with the following parameters:

- `aviso1.wav`: The WAV file you wish to upload.

Here’s an example using `curl`:
```bash
curl -X POST -F "aviso1.wav=@path_to_your_audio_file/aviso1.wav" http://localhost:5000/upload
```

## Running the Application

To run the Flask application, use the following command:

```bash
python app.py
```

The application will start on `http://localhost:5000/`.

## Error Handling

- If no file is uploaded, the API returns a `400` error with a message saying "No file part."
- If an invalid file is uploaded (other than a WAV file), the API will return a `400` error stating "Invalid file type."
- If there’s an issue with the API response from Webex, a `500` error with the Webex API details will be returned.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
