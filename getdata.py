import json
from elasticsearch import Elasticsearch
def getdata():
    es = Elasticsearch(['http://10.251.151.76:9200'])
    index_name = 'logstash-test-2024.02.28'

    scroll_size = 10000
    search_body = {
        "query": {
            "match_all": {}  # คิวรี่ทั้งหมด
        },
        "size": scroll_size,
    }

    response = es.search(index=index_name, body=search_body, scroll='100m')
    scroll_id = response['_scroll_id']
    results = []

    while True:
        hits = response['hits']['hits']
        if not hits:
            break
        results.extend([hit['_source'] for hit in hits])
        response = es.scroll(scroll_id=scroll_id, scroll='100m')

    # Save ลง JSON
    filename = f"data_all.json"

    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(results, json_file, ensure_ascii=False, indent=4)

    print(f"Data saved to '{filename}'")

    # Save ลง MongoDB
    # if results:
    #     mongo_client = MongoClient('mongodb://localhost:27017/')
    #     db = mongo_client[MONGO_DB_NAME]
    #     collection = db[MONGO_COLLECTION_NAME]

    #     # Inserting the retrieved data into MongoDB
    #     collection.insert_many(results)
    #     print("Data inserted into MongoDB")
    # else:
    #     print("No data found to insert into MongoDB")

# Call the function to get data, save to JSON, and then save to MongoDB
getdata()
