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
    print(GetMoviesByYear(event))
    print(event)
    body = {}
    statusCode = 200
    headers = {"Content-Type": "application/json"}

    # pe="title","releaseYear","coverUrl","genre"
    fe = Key("releaseYear").between(1900, 2030)
    response = table.scan(
        FilterExpression=fe,
        # ProjectionExpression=pe
    )
    print(response)
    for i in response["Items"]:
        print(json.dumps(i, cls=DecimalEncoder))


def GetMoviesByYear(event):
    movie_list = []
    try:
        if event["routeKey"] == "GET /getmovies/{year}":
            fe = Key("releaseYear").between(1900, 2030)
            response = table.scan(
                FilterExpression=fe,
        # ProjectionExpression=pe
            )
        print(response)
        for i in response["Items"]:
            print(json.dumps(i, cls=DecimalEncoder))

    except KeyError:
        statusCode = 400
