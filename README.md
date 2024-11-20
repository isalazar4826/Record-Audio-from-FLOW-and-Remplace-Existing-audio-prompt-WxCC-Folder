
# Record Audio from WxCC FLOW and replace existing audio file in audio prompt folder WxCC 

This project is a simple **Flask** application that allows you to upload an audio file and replace an existing audio file on the **Webex Contact Center** using their API.

## Requirements

- Python 3.7+
- Flask
- Requests
- Your Webex Contact Center API credentials (organization ID and API token)
- Ngrok

## Setup

1. **Install the required packages**:

   Use `pip` to install the required dependencies:
   ```bash
   pip install flask requests
   ```

2. **Place the variables**:
   - Replace `{YOUR ORG ID}` with your Webex organization ID.
   - Replace `{YOUR TOKEN}` with your Webex API token.
   - Replace `{ID AUDIO TO REPLACE}` with the audio file ID you want to replace.
     
In WxCC Control Hub, From audio prompt find the audio file to replace
![image](https://github.com/user-attachments/assets/9420ed66-92aa-4c23-a4f4-bd6c411471dc)

In the code, replace the credentials and replace the name of the file you want to replace.
![image](https://github.com/user-attachments/assets/a2a52806-65cb-44c6-91d4-b455da84eeb8)


## Running the python code.

To run the Flask application, use the following command:

```
python app.py
```

The application will start on `http://localhost:5000/`.

![image](https://github.com/user-attachments/assets/26d17682-8762-40f8-a6b5-48bad5b5ae7b)

Use the ngrok application to expose our code on the internet.
run Ngrok
```
ngrok.exe http 5000
```

![image](https://github.com/user-attachments/assets/d88d52a4-cf9e-4f90-987a-bba7124b08d6)

this generates a temporary, test URL, for our code.
Now what we have to do is copy it and add the path (`/upload`)

it would look like this: https://f576-187-161-142-159.ngrok-free.app/upload 

Now in the Wxcc Flow , create a Record node and HTTP node to send the record to our code.
![image](https://github.com/user-attachments/assets/158dc002-3870-4120-91d5-c5973ab230f3)

## TEST

Now make a call and record an audio, when finished, you will see the result 200 OK and verify the file in the folder has been replaced correctly.

![image](https://github.com/user-attachments/assets/8ce88108-1c31-4245-9875-27e8f61beba1)

![image](https://github.com/user-attachments/assets/78b5ed0f-698b-41eb-8aee-83110b2ba6c5)

![image](https://github.com/user-attachments/assets/ca8fcbe6-1c22-4d9a-8c9b-8dafa4189a85)

