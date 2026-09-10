from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Welcome to GenAI Backend Training"
    }

@app.get("/msg")
def greetingMessage():
    return {"message":"Hi We are learning Fast API with AI"}


