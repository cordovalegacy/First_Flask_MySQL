from mysqlconnection import connectToMySQL
#import the function that will return an instance of a connection
class Friend:
#model the class after the friend table we just created in MySQL workbench from our database
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    #make sure to indent here so that anything involving the Friend class sits inside the scope of the class
    @classmethod
    #now we will use class methods to query our database
    def get_all(cls):
        query = "SELECT * FROM friends;"
        results = connectToMySQL('first_flask').query_db(query)
        #make sure to call the connectToMySQL function/method with the schema you are targeting
        friends = []
        #create an empty list to append our instances of friends
        for friend in results:
            friends.append(cls(friend))
            #iterate over the database results and create instances of friends with cls
        return friends

    @classmethod
    def save(cls, data):
    #a function that allows us to save a user instance to the database
        query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES ( %(fname)s, %(lname)s, %(occ)s, NOW(), NOW() );"
        return connectToMySQL('first_flask').query_db(query, data)