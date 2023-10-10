from mongoengine import connect
import configparser


config = configparser.ConfigParser()
config.read('config.ini')

mongo_user = config.get('DB', 'user')
mongodb_pass = config.get('DB', 'pass')
db_name = config.get('DB', 'db_name')
domain = config.get('DB', 'domain')

# connect to cluster on AtlasDB with connection string
#connect(host='mongodb+srv://ivmv2007:EJvjkvc7pIaSWO5b@mimongo.uvxb1qp.mongodb.net/HW08_NoSQL')
connect(host=f"""mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/{db_name}?retryWrites=true&w=majority""", ssl=True)