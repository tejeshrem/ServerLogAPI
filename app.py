from fastapi import FastAPI

app = FastAPI(title="Secure Log Analysis API")

@app.get("/health")
def health():
    return {"ok": True}
