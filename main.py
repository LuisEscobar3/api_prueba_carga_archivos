from fastapi import FastAPI, UploadFile, File
from typing import Optional

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/process-case")
async def process_case(
    pdf: Optional[UploadFile] = File(None),
    audio: Optional[UploadFile] = File(None)
):
    result = {}

    if pdf:
        pdf_bytes = await pdf.read()
        result["pdf"] = {
            "filename": pdf.filename,
            "content_type": pdf.content_type,
            "size_bytes": len(pdf_bytes)
        }
    else:
        result["pdf"] = None

    if audio:
        audio_bytes = await audio.read()
        result["audio"] = {
            "filename": audio.filename,
            "content_type": audio.content_type,
            "size_bytes": len(audio_bytes)
        }
    else:
        result["audio"] = None

    return {
        "status": "received",
        "files": result
    }
