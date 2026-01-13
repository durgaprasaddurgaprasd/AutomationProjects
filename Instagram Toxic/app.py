from fastapi import FastAPI
from pydantic import BaseModel
from googleapiclient import discovery
import json

# FastAPI instance
app = FastAPI(title="Perspective API FastAPI Wrapper")

# Input schema
class Comment(BaseModel):
    text: str
    comment_id: str

# Perspective API key
API_KEY = "AIzaSyCEoFNfB1yVVYIqKDkAgEJeyjabC6OmraI"

# Build the Google API client
client = discovery.build(
    "commentanalyzer",
    "v1alpha1",
    developerKey=API_KEY,
    discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
    static_discovery=False,
)

@app.get("/")
def root():
    return {"message": "Perspective API FastAPI running!"}

from fastapi import FastAPI
from pydantic import BaseModel
from googleapiclient import discovery

# FastAPI instance
app = FastAPI(title="Perspective API FastAPI Wrapper")

# Input schema
class Comment(BaseModel):
    comment_id: str
    username:str 
    user_id:str # new field for comment ID
    text: str

# Perspective API key
API_KEY = "AIzaSyCEoFNfB1yVVYIqKDkAgEJeyjabC6OmraI"

# Build the Google API client
client = discovery.build(
    "commentanalyzer",
    "v1alpha1",
    developerKey=API_KEY,
    discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
    static_discovery=False,
)

@app.get("/")
def root():
    return {"message": "Perspective API FastAPI running!"}

@app.post("/analyze")
def analyze_comment(comment: Comment):
    try:
        analyze_request = {
            "comment": {"text": comment.text},
            "requestedAttributes": {"TOXICITY": {}}
        }
        response = client.comments().analyze(body=analyze_request).execute()
        score = response["attributeScores"]["TOXICITY"]["summaryScore"]["value"]
        return {
            "comment_id": comment.comment_id,        # include comment ID in response
            "text": comment.text,
            "user_id": comment.user_id,              # include user ID in response
            "username": comment.username,            # include username in response
            "language": "English",
            "toxicity_score": round(score, 4)
        }
    except Exception as e:
        return {"error": str(e)}
