from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the prompt length calculator!"}

@app.get("/prompt-length/")
def get_prompt_length(prompt: str):
    return {"prompt": prompt, "length": len(prompt)}
