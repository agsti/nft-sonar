from fastapi import FastAPI, UploadFile, File

from base.hasher import Hasher
from base.pinecone import Pinecone
from model.asset import find_asset


def get_app():
    app = FastAPI(title="Nft search")
    return app


app = get_app()
h = Hasher()
pinecone = Pinecone()


@app.post("/")
async def helloworld(file: UploadFile = File(...)):
    # Get upload file
    # Hash it
    embedding = h.encode_file(file.file)
    # query pinecone
    top_k_matches = pinecone.query(embedding)

    def fetch_asset(m):
        m['asset'] = find_asset(m['asset_id'])
        return m

    with_assets = [fetch_asset(m) for m in top_k_matches]

    # Get asset per pinecone answer
    # Return
    return with_assets
