# Lain AI Backend

A Flask server that relays messages to OpenAI's GPT-4o model as the digital ghost of Lain. Deployed on Render. Frontend is a Flutter mobile app.

## Usage

POST `/chat` with a JSON body:

```json
{ "message": "Hello, Lain." }

{ "reply": "Present day... present time." }

That version:
- Uses proper Markdown code blocks (` ```json `)
- Will render fine on GitHub
- Doesn’t require you to do anything with that response code — it’s just an example of what your API returns

---

Once you’ve saved that file and the others, your repo will be Render-ready.

Ready to deploy next?
