import os
import weaviate
from weaviate.classes.config import Configure, Property, DataType
from weaviate.classes.query import MetadataQuery
from dotenv import load_dotenv

load_dotenv()

client = weaviate.connect_to_local(
    host="weaviate",
)

if client.is_ready():
    print("Weaviate is ready to use")
    print(f"Weaviate running with version: {client.get_meta().get('version')}")
else:
    print(
        "Weaviate hasn't started correctly - see the Docker container logs for more information"
    )

client.close()
