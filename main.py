from sentence_transformers import SentenceTransformer, util
from PIL import Image
from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import requests

# initialize FastAPI
app = FastAPI()

# CORS middleware to help with communication between Python and React/JS
app.add_middleware(
    CORSMiddleware,
    # Startng with allow-all for testing
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#initialize AI model 
model = SentenceTransformer('clip-ViT-B-32')

# function to create an image embedding
def create_img_embedding(imageUrl):
    image = Image.open(requests.get(imageUrl, stream=True).raw)
    # create embedding 
    img_emb = model.encode(image).tolist()
    return img_emb
    

# POST HTTP requests
@app.post('/upload')
async def embed_upload(imageUrl: str = Form(...)):

    # create embedding 
    embedding = create_img_embedding(imageUrl)
    
    return JSONResponse(content={"message": "Image processed successfully", "embedding": embedding}, status_code=200)



  
### run with: 
# uvicorn main:app --reload