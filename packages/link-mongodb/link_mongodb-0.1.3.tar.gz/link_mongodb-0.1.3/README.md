# install
```bash
pip install link-mongodb
```

## Usage
```python
import os
from link_mongodb import core
from typing import Optional, List, Dict, Any
from dotenv import load_dotenv
load_dotenv()

mongodb_uri = f'mongodb://{os.getenv("MONGODB_USER")}:{os.getenv("MONGODB_PASSWORD")}@{os.getenv("MONGODB_HOST")}:{os.getenv("MONGODB_PORT")}/?authMechanism=DEFAULT'
database_name = os.getenv("APP_NAME") + os.getenv("MONGODB_DATABASE_NAME")

def find_one(collection_name : str,filter : dict) -> Optional[Dict]:
    result = core.find_one(mongodb_uri,database_name,collection_name,filter)
    # None    
    # {'_id': ObjectId('654f49d2cc57188a2d539e72'), 'key': 'value'}
    return result

def find_all(collection_name : str,filter : dict) -> Optional[List]:
    result = core.find_all(mongodb_uri,database_name,collection_name,filter)
    # []
    # [{'_id': ObjectId('654f4beacc57188a2d539e74'), 'key': 'values'}]
    # [{'_id': ObjectId('654f49d2cc57188a2d539e72'), 'key': 'value'}, {'_id': ObjectId('654f4b1ecc57188a2d539e73'), 'key': 'value', 'key2': 'value2'}]
    return result
def insert_one(collection_name : str,filter : dict) -> Optional[Dict]:
    result = core.insert_one(mongodb_uri,database_name,collection_name,filter)
    # {'_id': ObjectId('654f51a59543b75c7cf4ca51'), 'key3': 'value1'}
    return result
def insert_many(collection_name : str,document : list) -> Optional[List]:
    result = core.insert_many(mongodb_uri,database_name,collection_name,document)
    # [ObjectId('654f58aad70e1f8cccc7e7ff'), ObjectId('654f58aad70e1f8cccc7e800')]
    return result

def update_one(collection_name : str,filter : dict,update : dict) -> Optional[Dict]:
    result = core.update_one(mongodb_uri,database_name,collection_name,filter,update)
    # {'n': 0, 'nModified': 0, 'ok': 1.0, 'updatedExisting': False}
    # {'n': 1, 'nModified': 1, 'ok': 1.0, 'updatedExisting': True}
    return result

def update_many(collection_name : str,filter : dict,update : dict) -> Optional[Dict]:
    result = core.update_many(mongodb_uri,database_name,collection_name,filter,update)
    # {'n': 3, 'nModified': 0, 'ok': 1.0, 'updatedExisting': True}
    # {'n': 3, 'nModified': 2, 'ok': 1.0, 'updatedExisting': True}
    return result

def delete_one(collection_name : str,filter : dict) -> Optional[Dict]:
    result = core.delete_one(mongodb_uri,database_name,collection_name,filter)
    # {'n': 0, 'ok': 1.0}
    # {'n': 1, 'ok': 1.0}
    return result

def delete_many(collection_name : str,filter : dict) -> Optional[Dict]:
    result = core.delete_many(mongodb_uri,database_name,collection_name,filter)
    # {'n': 0, 'ok': 1.0}
    # {'n': 3, 'ok': 1.0}
    return result

def count(collection_name : str,filter : dict) -> Optional[Any]:
    result = core.count(mongodb_uri,database_name,collection_name,filter)
    # 0
    # 2
    return result

def random_valuve(collection_name : str,key_name : str) -> Optional[Any]:
    result = core.random_valuve(mongodb_uri,database_name,collection_name,key_name)
    # 64ca01272ec39bc754bb202f
    return result

def download_file(file_id : str) -> Optional[Any]:
    result = core.download_file(mongodb_uri,database_name,file_id)
    return result
    
# if __name__ == "__main__":
    # collection = 'collection'
    # filter = {"key":"value"}
    # result = find_one(collection,filter)
    # print(result)

    # collection = 'collection'
    # filter = {"key":"values"}
    # find_all(collection,filter)

    # collection = 'collection'
    # document = {"key":"value"}
    # insert_one(collection,document)

    # collection = 'collection'
    # document = [{"key":"value"},{"key":"value2"},{"key":"value3"}]
    # result = insert_many(collection,document)
    # print(result)

    # collection = 'collection'
    # filter = {"key":"value"}
    # document = {"key":"value1"}
    # update_one(collection,filter,{'$set':document})

    # collection = 'collection'
    # filter = {"key":"value"}
    # document = {"ddd":"change"}
    # result = update_many(collection,filter,{'$set':document})
    # print(result)

    # collection = 'collection'
    # filter = {"key":"value2"}
    # result = delete_one(collection,filter)
    # print(result)

    # collection = 'collection'
    # filter = {"key":"value"}
    # result = delete_many(collection,filter)
    # print(result)

    # collection = 'collection'
    # result = count(collection,{"key":"value"})
    # print(result)
```