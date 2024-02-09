# Python FastAPI Microservice for Image Embeddings

This microservice is designed to handle image processing for a photo storage app, generating embeddings for images to enable semantic search capabilities. It uses the Sentence Transformers library to create embeddings from images and FastAPI for handling API requests. CORS (Cross-Origin Resource Sharing) is configured to allow communication between the microservice and the React client application.

## Features

- Image embedding generation using the `clip-ViT-B-32` model from Sentence Transformers.
- CORS configured for seamless integration with frontend applications.
- Utilizes FastAPI for efficient request handling and API development.


## Model Reference

The `clip-ViT-B-32` model is part of the Sentence Transformers library, which facilitates the creation of embeddings for images and text. This model is based on the CLIP architecture developed by OpenAI, combining the benefits of natural language understanding and computer vision. It's chosen for its ability to understand and process images in the context of semantic search, making it highly suitable for applications like photo storage apps where search functionality is enhanced through deep learning.

For more information on Sentence Transformers and the `clip-ViT-B-32` model:

- Sentence Transformers Documentation: `https://www.sbert.net/`
- CLIP by OpenAI: `https://openai.com/blog/clip/`

## Integration with Frontend

Ensure the React client sends image URLs here for embedding. Store embeddings as needed for search functionality.

## Contributing

Follow code style guidelines and document any changes or additions.


## Prerequisites

Before you start, ensure you have the following:

- Python 3.6 or later installed on your machine.
- Required Python packages installed.

## Installation

1. Clone the repository containing the microservice to your local machine.
2. Navigate to the project directory.
3. Install the required Python packages by running:

```
pip install fastapi uvicorn "python-multipart" pillow sentence-transformers requests
```


## Running the Microservice

To run the microservice, use the following command:

```
uvicorn main:app --reload
```


This command starts the FastAPI application with live reloading enabled. The service will be available at `http://localhost:8000`.

## Usage

### Uploading Images for Embedding Generation

- The microservice exposes a POST endpoint at `/upload` which accepts an image URL as form data.
- Upon receiving an image URL, it generates an embedding for the image and returns a JSON response containing the embedding.

### Example Request

To create an embedding for an image, send a POST request to `http://localhost:8000/upload` with the image URL as form data:

```
curl -X 'POST'
'http://localhost:8000/upload'
-H 'accept: application/json'
-H 'Content-Type: application/x-www-form-urlencoded'
-d 'imageUrl=YOUR_IMAGE_URL'
```

### Response

The response will be a JSON object containing a message and the generated image embedding:

```
{
"message": "Image processed successfully",
"embedding": [/* array of embedding values */]
}
```


## Integration with Frontend

- Ensure the React client application sends image URLs to this microservice for embedding generation.
- Store the received embeddings in your database or state management system as needed for semantic search functionality.

## Contributing

Contributions to the microservice are welcome. Please ensure to follow the code style guidelines and add comments where necessary for clarity.


