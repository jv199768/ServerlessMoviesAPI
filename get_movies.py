import json
import boto3
from decimal import Decimal
from boto3.dynamodb.conditions import Key, Attr


client = boto3.client("dynamodb")
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Movies")
tableName = "Movies"


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return str(o)
        return super(DecimalEncoder, self).default(o)


def lambda_handler(event, context):
    print(GetMovies(event))
    print(event)
    body = {}
    statusCode = 200
    headers = {"Content-Type": "application/json"}
    response = table.scan()
    print(response)
    for i in response["Items"]:
        print(json.dumps(i, cls=DecimalEncoder))


def GetMovies(event):
    try:
        if event["routeKey"] == "GET /getmovies":
            response = table.scan()
            print(response)
            for i in response["Items"]:
                print(json.dumps(i, cls=DecimalEncoder))

    except KeyError:
        statusCode = 400
