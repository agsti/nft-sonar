from sanic import Sanic, response
from base.milvus import Milvus
from base.hasher import Hasher

app = Sanic(name="NFT-Search")

@app.route("/")
async def index(request):
    return response.json(results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
