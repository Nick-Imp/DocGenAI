from fastapi import FastAPI, Request
import uvicorn
import json

app = FastAPI()

@app.post("/webhook")
async def github_webhook(request: Request):
    payload = await request.json()
    
    # Log basic PR info
    if payload.get("pull_request"):
        pr = payload["pull_request"]
        print("🔔 New PR Received:")
        print(f"Title: {pr['title']}")
        print(f"Body: {pr['body']}")
        print(f"URL: {pr['html_url']}")

    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)