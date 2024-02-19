from typing import Optional, List, Dict, Any
from pymongo import MongoClient, errors
import gridfs

def find_one(mongodb_uri: str, database_name: str, collection_name: str, filter: Dict) -> Optional[Any]:
    """
    Find a single document in a MongoDB collection based on the provided filter.
    Args:
        mongodb_uri (str): The URI of the MongoDB server.
        database_name (str): The name of the database containing the collection.
        collection_name (str): The name of the collection to search.
        filter (Dict): The filter used to match documents in the collection.
    Returns:
        Any | None: The matching document if found, otherwise None.
        
    Raises:
        Exception: If an error occurs while querying the MongoDB collection.
    """
    print(f"Connecting to MongoDB server... ")
    with MongoClient(mongodb_uri) as client:
        collection = client[database_name][collection_name]

        try:
            print(f"Executing find_one query with filter: {filter}")
            result = collection.find_one(filter=filter)
            return result

        except errors.PyMongoError as e:
            raise Exception(f"An error occurred while querying the MongoDB collection: {str(e)}")



def find_all(mongodb_uri: str, database_name: str, collection_name: str, filter: Dict) -> Optional[List[Dict]]:
    """
    Find multiple documents in the MongoDB collection that match the provided filter.

    Args:
        mongodb_uri (str): The URI for connecting to the MongoDB server.
        database_name (str): The name of the database in which the collection resides.
        collection_name (str): The name of the collection to search in.
        filter (Dict): A dictionary specifying the filter to apply when searching for documents.

    Returns:
        Optional[List[Dict]]: A list of dictionaries representing the matching documents if found, or None if not found.

    Raises:
        Exception: If an error occurs while querying the MongoDB collection.
    """
    print("Connecting to MongoDB server...")
    with MongoClient(mongodb_uri) as client:
        collection = client[database_name][collection_name]

        try:
            print(f"Executing find_all query with filter: {filter}")
            result = list(collection.find(filter=filter))
            print(f"result: {result}")
            return result
        except errors.PyMongoError as e:
            raise Exception(f"An error occurred while querying the MongoDB collection: {str(e)}")

def insert_one(mongodb_uri: str, database_name: str, collection_name: str, document: Dict) -> Optional[Dict]:
    """
    Inserts a single document into a MongoDB collection.

    Parameters:
        mongodb_uri (str): The URI of the MongoDB server.
        database_name (str): The name of the database.
        collection_name (str): The name of the collection.
        document (Dict): The document to be inserted.

    Returns:
        Optional[Dict]: The result of the insert operation as a dictionary, or None if an error occurred.

    Raises:
        Exception: If an error occurs while querying the MongoDB collection.
    """
    print("Connecting to MongoDB server...")
    with MongoClient(mongodb_uri) as client:
        collection = client[database_name][collection_name]

        try:
            print(f"Executing insert_one query with document: {document}")
            result = collection.insert_one(document)
            result_dict = collection.find_one({"_id": result.inserted_id})
            print(f"result: {result_dict}")
            return result_dict
        except errors.PyMongoError as e:
            raise Exception(f"An error occurred while querying the MongoDB collection: {str(e)}")
        
def insert_many(mongodb_uri: str, database_name: str, collection_name: str, documents: List[Dict]) -> Optional[List]:
    """
    Inserts multiple documents into a MongoDB collection.

    Parameters:
        mongodb_uri (str): The URI of the MongoDB server.
        database_name (str): The name of the database.
        collection_name (str): The name of the collection.
        documents (List[Dict]): The documents to be inserted.

    Returns:
        Optional[List]: The result of the insert operation as a list of dictionaries, or None if an error occurred.

    Raises:
        Exception: If an error occurs while querying the MongoDB collection.
    """
    print("Connecting to MongoDB server...")
    with MongoClient(mongodb_uri) as client:
        collection = client[database_name][collection_name]

        try:
            print(f"Executing insert_many query with documents: {documents}")
            result = collection.insert_many(documents)
            print(f"ids of the inserted document: {result.inserted_ids}")
            return result.inserted_ids
        except errors.PyMongoError as e:
            raise Exception(f"An error occurred while querying the MongoDB collection: {str(e)}")
        

def update_one(mongodb_uri: str, database_name: str, collection_name: str, filter: Dict, update: Dict) -> Optional[Dict]:
    """
    Updates a document in a MongoDB collection based on the provided filter and update parameters.

    Args:
        mongodb_uri (str): The URI of the MongoDB server.
        database_name (str): The name of the MongoDB database.
        collection_name (str): The name of the MongoDB collection.
        filter (Dict): The filter to select the document to be updated.
        update (Dict): The update to be applied to the selected document.

    Returns:
        Optional[Dict]: The result of the update operation. Returns None if no document was updated.
        
    Raises:
        Exception: An error occurred while querying the MongoDB collection.
    """
    print("Connecting to MongoDB server...")
    with MongoClient(mongodb_uri) as client:
        collection = client[database_name][collection_name]

        try:
            print(f"Executing update_one query with filter: {filter} and update: {update}")
            result = collection.update_one(filter=filter, update=update)
            result_dict = result.raw_result
            print(f"result: {result_dict}")
        except errors.PyMongoError as e:
            raise Exception(f"An error occurred while querying the MongoDB collection: {str(e)}")

def update_many(mongodb_uri: str, database_name: str, collection_name: str, filter: Dict, update: Dict) -> Optional[Dict]:
    """
    Updates multiple documents in a MongoDB collection that match the specified filter with the given update.

    Args:
        mongodb_uri (str): The URI of the MongoDB server.
        database_name (str): The name of the database containing the collection.
        collection_name (str): The name of the collection to update.
        filter (Dict): The filter used to select the documents to update.
        update (Dict): The update to apply to the selected documents.

    Returns:
        Optional[Dict]: The result of the update operation, or None if an error occurred.

    Raises:
        Exception: If an error occurs while querying the MongoDB collection.
    """
    print("Connecting to MongoDB server...")
    with MongoClient(mongodb_uri) as client:
        collection = client[database_name][collection_name]

        try:
            print(f"Executing update_many query with filter: {filter} and update: {update}")
            result = collection.update_many(filter=filter, update=update)
            print(f"matched count: {result.matched_count} modified count: {result.modified_count}")
            return result.raw_result
        except errors.PyMongoError as e:
            raise Exception(f"An error occurred while querying the MongoDB collection: {str(e)}")
        
def delete_one(mongodb_uri: str, database_name: str, collection_name: str, filter: Dict) -> Optional[Dict]:
    """
    Deletes a single document from a MongoDB collection that matches the specified filter.

    Args:
        mongodb_uri (str): The URI of the MongoDB server.
        database_name (str): The name of the database containing the collection.
        collection_name (str): The name of the collection to delete from.
        filter (Dict): The filter used to select the document to delete.

    Returns:
        Optional[Dict]: The result of the delete operation, or None if an error occurred.

    Raises:
        Exception: If an error occurs while querying the MongoDB collection.
    """
    print("Connecting to MongoDB server...")
    with MongoClient(mongodb_uri) as client:
        collection = client[database_name][collection_name]

        try:
            print(f"Executing delete_one query with filter: {filter}")
            result = collection.delete_one(filter=filter)
            print(f"Query result: {result.raw_result}")
            return result.raw_result
        except errors.PyMongoError as e:
            raise Exception(f"An error occurred while querying the MongoDB collection: {str(e)}")
        
def delete_many(mongodb_uri: str, database_name: str, collection_name: str, filter: Dict) -> Optional[Dict]:
    """
    Deletes multiple documents from a MongoDB collection based on the provided filter.
    
    Args:
        mongodb_uri (str): The URI to connect to the MongoDB server.
        database_name (str): The name of the database.
        collection_name (str): The name of the collection.
        filter (Dict): A dictionary representing the filter criteria for selecting documents to delete.
        
    Returns:
        Optional[Dict]: The result of the delete operation, including the number of deleted documents.
        
    Raises:
        Exception: If an error occurs during the delete operation.
    """
    print("Connecting to MongoDB server...")
    with MongoClient(mongodb_uri) as client:
        collection = client[database_name][collection_name]

        try:
            print(f"Executing delete_many query with filter: {filter}")
            result = collection.delete_many(filter=filter)
            print(f"Query result: {result.raw_result}")
            return result.raw_result
        except errors.PyMongoError as e:
            raise Exception(f"An error occurred while querying the MongoDB collection: {str(e)}")
        
def count(mongodb_uri: str, database_name: str, collection_name: str, filter: Dict) -> Optional[Dict]:
    """
    Counts the number of documents in a MongoDB collection that match the specified filter.

    Args:
        mongodb_uri (str): The URI to connect to the MongoDB server.
        database_name (str): The name of the database.
        collection_name (str): The name of the collection.
        filter (Dict): A dictionary representing the filter criteria for selecting documents.

    Returns:
        Optional[Dict]: The result of the count operation, including the count of matching documents.
        
    Raises:
        Exception: If an error occurs during the count operation.
    """
    print("Connecting to MongoDB server...")
    with MongoClient(mongodb_uri) as client:
        collection = client[database_name][collection_name]

        try:
            print(f"Executing count query with filter: {filter}")
            result = collection.count_documents(filter=filter)
            print(f"Query result: {result}")
            return result
        except errors.PyMongoError as e:
            raise Exception(f"An error occurred while querying the MongoDB collection: {str(e)}")
        
def drop(mongodb_uri: str, database_name: str, collection_name: str) -> Optional[Dict]:
    """
    Drops a collection from a MongoDB database.

    Args:
        mongodb_uri (str): The URI to connect to the MongoDB server.
        database_name (str): The name of the database.
        collection_name (str): The name of the collection to drop.

    Returns:
        Optional[Dict]: The result of the drop operation.
        
    Raises:
        Exception: If an error occurs during the drop operation.
    """
    print("Connecting to MongoDB server...")
    with MongoClient(mongodb_uri) as client:
        try:
            print(f"Executing drop query with collection name: {collection_name}")
            result = client[database_name].drop_collection(collection_name)
            print(f"Query result: {result}")
            return result
        except errors.PyMongoError as e:
            raise Exception(f"An error occurred while querying the MongoDB collection: {str(e)}")
        
def drop_database(mongodb_uri: str, database_name: str) -> Optional[Dict]:
    """
    Drops a database from a MongoDB server.

    Args:
        mongodb_uri (str): The URI to connect to the MongoDB server.
        database_name (str): The name of the database to drop.

    Returns:
        Optional[Dict]: The result of the drop operation.
        
    Raises:
        Exception: If an error occurs during the drop operation.
    """
    print("Connecting to MongoDB server...")
    with MongoClient(mongodb_uri) as client:
        try:
            print(f"Executing drop_database query with database name: {database_name}")
            result = client.drop_database(database_name)
            print(f"Query result: {result}")
            return result
        except errors.PyMongoError as e:
            raise Exception(f"An error occurred while querying the MongoDB collection: {str(e)}")
        

def close_connection(mongodb_uri: str) -> None:
    """
    Closes the connection to a MongoDB server.

    Args:
        mongodb_uri (str): The URI to connect to the MongoDB server.
    """
    print("Closing connection to MongoDB server...")
    with MongoClient(mongodb_uri) as client:
        client.close()

def create_index(mongodb_uri: str, database_name: str, collection_name: str, index: Dict) -> Optional[Dict]:
    """
    Creates an index on a MongoDB collection.

    Args:
        mongodb_uri (str): The URI to connect to the MongoDB server.
        database_name (str): The name of the database.
        collection_name (str): The name of the collection.
        index (Dict): The index to create.

    Returns:
        Optional[Dict]: The result of the create_index operation.
        
    Raises:
        Exception: If an error occurs during the create_index operation.
    """
    print("Connecting to MongoDB server...")
    with MongoClient(mongodb_uri) as client:
        collection = client[database_name][collection_name]

        try:
            print(f"Executing create_index query with index: {index}")
            result = collection.create_index(index)
            print(f"Query result: {result}")
            return result
        except errors.PyMongoError as e:
            raise Exception(f"An error occurred while querying the MongoDB collection: {str(e)}")
        
def drop_index(mongodb_uri: str, database_name: str, collection_name: str, index_name: str) -> Optional[Dict]:
    """
    Drops an index from a MongoDB collection.

    Args:
        mongodb_uri (str): The URI to connect to the MongoDB server.
        database_name (str): The name of the database.
        collection_name (str): The name of the collection.
        index_name (str): The name of the index to drop.

    Returns:
        Optional[Dict]: The result of the drop_index operation.
        
    Raises:
        Exception: If an error occurs during the drop_index operation.
    """
    print("Connecting to MongoDB server...")
    with MongoClient(mongodb_uri) as client:
        collection = client[database_name][collection_name]

        try:
            print(f"Executing drop_index query with index name: {index_name}")
            result = collection.drop_index(index_name)
            print(f"Query result: {result}")
            return result
        except errors.PyMongoError as e:
            raise Exception(f"An error occurred while querying the MongoDB collection: {str(e)}")


def download_file(mongodb_uri: str, database_name: str, id: str):
    """
    Downloads a file from MongoDB using the provided MongoDB URI, database name, and file ID.

    Args:
        mongodb_uri (str): The URI of the MongoDB server.
        database_name (str): The name of the database.
        id (str): The ID of the file to download.

    Returns:
        str: The ID of the downloaded file.

    Raises:
        Exception: If an error occurs while querying the MongoDB collection.
    """
    print("Connecting to MongoDB server...")
    with MongoClient(mongodb_uri) as client:
        fs = gridfs.GridFS(client[database_name])
        try:
            file = fs.get(id)
            with open(f'{id}', 'wb') as f:
                f.write(file.read())
            return id
        except errors.PyMongoError as e:
            raise Exception(f"An error occurred while querying the MongoDB collection: {str(e)}")

def random_valuve(mongodb_uri: str, database_name: str, collection_name: str, key_name: str):
    """
    Retrieves a random value from a MongoDB collection.

    Args:
        mongodb_uri (str): The URI of the MongoDB server.
        database_name (str): The name of the MongoDB database.
        collection_name (str): The name of the MongoDB collection.
        key_name (str): The key name of the value to retrieve from the document.

    Returns:
        The value associated with the specified key in a randomly selected document.

    Raises:
        Exception: If an error occurs while querying the MongoDB collection.
    """
    print("Connecting to MongoDB server...")
    with MongoClient(mongodb_uri) as client:
        collection = client[database_name][collection_name]
        try:
            document = collection.aggregate([{"$sample": {"size": 1}}]).next()
            return document[key_name]
        except errors.PyMongoError as e:
            raise Exception(f"An error occurred while querying the MongoDB collection: {str(e)}")
