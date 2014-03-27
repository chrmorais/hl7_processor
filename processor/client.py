from pymongo import MongoClient, ASCENDING

class Client(object):
    def __init__(self):
        # establish the connection
        self.client = MongoClient('localhost', 28947)
        
        # connect to the database
        self.db = self.client.results

        # connect to tdl collection
        self.tdl = self.db.tdl
        indices = [( 'id', ASCENDING )]                  
        self.tdl.ensure_index(indices)

    def insert_tdl_message(self, message):
        """
        Inserts a message from tdl into the tdl collection
        """        
        print message['id']
        mid = self.tdl.update({'id': message['id']}, message, True)
        cnt = self.tdl.count()
        print mid, " inserted into collection, count: ", cnt


#client = Client()