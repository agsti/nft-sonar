import os

pinecone_api_key = os.getenv("PINECONE_API_KEY") or "3464d78c-e7f1-4f24-85bd-7357fa71720f"
pinecone_index_name = "nftsearch"


db_url= "postgres://nftsearch:nftsearch@localhost/nftsearch"
