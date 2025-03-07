import os
import weaviate
from weaviate.classes.config import Configure, Property, DataType
from weaviate.classes.query import MetadataQuery
from dotenv import load_dotenv

load_dotenv()

client = weaviate.connect_to_local(
    host="weaviate",
    headers={
        "X-Cohere-Api-Key": os.environ["COHERE_API_KEY"]
    }
)

collection_name = "DemoCollection"

client.collections.delete(collection_name)

client.collections.create(
    collection_name,
    properties=[
        Property(name="title", data_type=DataType.TEXT),
        Property(name="body", data_type=DataType.TEXT),
    ],
    vectorizer_config=[
        Configure.NamedVectors.text2vec_cohere(
            name="all_text",
            source_properties=["title", "body"],
        )
    ],
)

objs = [
    {"title": "The Matrix", "body": "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers."},
    {"title": "Iron Man", "body": "After being held captive in an Afghan cave, billionaire engineer Tony Stark creates a unique weaponized suit of armor to fight evil."},
    {"title": "Contact", "body": "Dr. Ellie Arroway, after years of searching, finds conclusive radio proof of extraterrestrial intelligence, sending plans for a mysterious machine."},
]

collection = client.collections.get(collection_name)

collection.data.insert_many(objs)

print(f"Collection created, with {len(collection)} objects.")

response = collection.query.near_text(
    query="virtual world metaverse movie",
    target_vector="all_text",
    return_metadata=MetadataQuery(distance=True)
)

for o in response.objects:
    print(f"Title: {o.properties['title']}")
    print(f"Distance: {o.metadata.distance}")

client.close()
