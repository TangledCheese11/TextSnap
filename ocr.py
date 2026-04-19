from dotenv import load_dotenv
import os
import requests

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("API_KEY")

with open("test.jpg", "rb") as f:
    response = requests.post(
        "https://api.ocr.space/parse/image",
        files={"file": f},
        data={"apikey": API_KEY, "language": "eng"}
    )

data = response.json()

# Safe check to avoid crashes
if "ParsedResults" in data:
    text = data["ParsedResults"][0]["ParsedText"]
    print(text)
else:
    print("OCR Error:", data)
