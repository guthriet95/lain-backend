# Lain AI Backend

A Flask server that relays messages to OpenAI's GPT-4o model as the digital ghost of Lain. Deployed on Render. Frontend is a Flutter mobile app.

## Usage

POST `/chat` with a JSON body:

```json
{ "message": "Hello, Lain." }

{ "reply": "Present day... present time." }
