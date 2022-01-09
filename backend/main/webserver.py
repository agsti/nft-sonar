from fastapi import FastAPI, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from base.hasher import Hasher
from base.pinecone import Pinecone
from model.asset import find_asset


def get_app():
    app = FastAPI(title="Nft search")
    origins = ["http://localhost:3000"]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app


app = get_app()
h = Hasher()
pinecone = Pinecone()


@app.post("/upload-file")
async def query(file: UploadFile = File(...)):
    # Get upload file
    # Hash it
    embedding = h.encode_file(file.file)
    # query pinecone
    top_k_matches = pinecone.query(embedding)

    def fetch_asset(m):
        m['asset'] = find_asset(m['asset_id'])
        print(dict(m['asset']))
        return m

    # Get asset per pinecone answer
    with_assets = [fetch_asset(m) for m in top_k_matches]

    # Return
    return with_assets


app.mount("/", StaticFiles(directory="static"), name="static")
