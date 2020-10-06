import os
import boto3
import unittest

from tests.config import dynamodb


class TestDynamodbActions(unittest.TestCase):

    def setUp(self):
        """
        Cleans up previous state in DynamoDB
        """
        for table in dynamodb.list_tables()['TableNames']:
            dynamodb.delete_table(TableName=table)

    def should_create_table(self):
        # when
        dynamodb.create_table(TableName='TestTable',
                              AttributeDefinitions=[
                                  {
                                      'AttributeName': 'Key',
                                      'AttributeType': 'S'
                                  },
                              ],
                              KeySchema=[
                                  {
                                      'AttributeName': 'Key',
                                      'KeyType': 'HASH'
                                  }
                              ],
                              ProvisionedThroughput={
                                  'ReadCapacityUnits': 40_000,
                                  'WriteCapacityUnits': 40_000
                              })
        response = dynamodb.list_tables()

        # then
        self.assertEqual(['TestTable'], response['TableNames'])
