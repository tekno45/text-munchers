import boto3
from textshit import TextInput
import argparse
from Munch.Munchers import Muncher
import pickle
from botocore.exceptions import ClientError

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--name" )
args = parser.parse_args()

bonuswords = ["red","blue","row","car","sit","ass","pass","yes","no"]
dynamodb = boto3.client("dynamodb", endpoint_url='http://localhost:8000')
def db_setup(dynamodb):
    table = dynamodb
    try:
        table.create_table(TableName="plants",
KeySchema=
[{"AttributeName":"plant_name", "KeyType": "HASH"}],
AttributeDefinitions=[{"AttributeName":"plant_name", "AttributeType": "S"}],
BillingMode="PROVISIONED",
ProvisionedThroughput={"ReadCapacityUnits":5,
                       "WriteCapacityUnits":5}

)
    except:
        print("Table Found")
    return table

def save_mon(mon, db_client):
    db_client.put_item(mon.export)
    return True


def feed_mon(mon):
    choice = True
    while choice:
        if input("Feed him? Y/N").lower() == "y":
            x = input("Enter your words: ")
            x = x.strip()
            mon.feed(TextInput.points4words(x, bonuswords))
        else:
            choice = False
    return True

def new_mon():
    monName = input("Name your monster:")
    Mon1 = Muncher(monName)
    feed_mon(Mon1)


selections = ["1: Create Plant", "2: Get Plant"]
print(*selections, sep="\n")

pick = input("Pick 1 or 2:")
if(str(pick) == "1"):
    new_mon()

if(str(pick) == "2"):

    
    plants = dynamodb.query(TableName="plants")




# opening file for bonuswords










