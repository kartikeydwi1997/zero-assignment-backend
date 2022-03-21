import pymongo
import urllib.parse


class MongoConnection:
    __client = None

    @classmethod
    def get_connection(cls, username, password, db_name):
        username = urllib.parse.quote_plus(username)
        password = urllib.parse.quote_plus(password)

        if not cls.__client:
            cls.__client = pymongo.MongoClient(
                f"mongodb+srv://{username}:{password}@cluster0.czzcv.mongodb.net/{db_name}?retryWrites=true&w=majority"
            )

        return cls.__client

    """
   Create a connection to the database.
   :collection_name: The name of the collection to connect to.
   The credentials represent the cluster credentials.
    """
def get_collection(collection_name):
    username = "kartikey"
    password = "12345"
    db_name = "zero_assignment"
    client = MongoConnection.get_connection(username=username, password=password, db_name=db_name)
    db = client[db_name]
    collection = db[collection_name]

    return collection
