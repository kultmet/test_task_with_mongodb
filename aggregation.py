from pymongo import MongoClient
import datetime
from ast import literal_eval
from constants import *

client = MongoClient(
    (
    'mongodb://127.0.0.1:27017/?directConnection=true'
    '&serverSelectionTimeoutMS=2000&appName=mongosh+1.8.0'
    )
)
db = client.statistics_db
collection = db.statistics_collection

def read(input_data: str) -> dict:
    """Reads a message and converts it to a dict."""
    output_data = literal_eval(input_data)
    return output_data


def check_curent_fields(input_data: dict):
    for key, value in input_data.items():
        print(key)
        if key not in FIELDS:
            return False
        if not isinstance(value, str):
            return False
    if input_data['group_type'] not in periods.keys():
        return False
    return True


class Aggregator:
    """
    This class receives the time point and sequence step 
    by which the sample is grouped. To get the result of the selection, 
    you need to call the "get_result ()" method.
    """
    def __init__(self, dt_from: str, dt_upto: str, group_type: str) -> None:
        self.dt_from = datetime.datetime.fromisoformat(dt_from)
        self.dt_upto = datetime.datetime.fromisoformat(dt_upto)
        self.pipline = self._form_pipline(
            self.dt_from, self.dt_upto, group_type
        )
        self.aggregated_data = self._aggregate()
        self.line = {}
        self._generate_line(self.dt_from, self.dt_upto, group_type)
        self.result_data = {'dataset': [], 'labels': []}
        self._result_formation(self.aggregated_data)

    def _form_pipline(self, dt_from, dt_upto, group_type):
        """Sets the aggregation parameters for a query in MongoDB."""
        pipline = [
        {'$match': {'dt': {'$gte': dt_from, '$lte': dt_upto}}},
        {
        '$group': {
            '_id': GROUP_TIPES[group_type],
            'total': {'$sum': '$value'},},
        },
        {'$sort': {'_id': 1}},
        {'$project': {'_id': 1, 'total': 1, 'count': 1}}
        ]
        return pipline

    def _aggregate(self):
        """Returns the result of a query in MongaDB."""
        return collection.aggregate(pipeline=self.pipline)

    def _generate_line(self, dt_from, dt_upto, group_tipe):
        """Generates all datetime objects, between dt_from dt_upto, 
        and fixes it in keys, and in values writes int: 0."""
        if dt_from > dt_upto:
            return
        self.line[dt_from.isoformat()] = 0
        return self._generate_line(
            dt_from+periods[group_tipe], dt_upto, group_tipe
        )

    def out_date_formation(self, year=1, month=1, day=1, hour=0):
        return datetime.datetime(year, month, day, hour).isoformat()

    def _result_formation(self, aggregated_data):
        """At first, By keys, it fills with data from the database.
        After adding all the data to the resulting dictionary."""
        for entry in aggregated_data:
            self.line[self.out_date_formation(**entry['_id'])] = entry['total']
        for key, values in self.line.items():
            self.result_data['dataset'].append(values)
            self.result_data['labels'].append(key)

    def get_result(self):
        """Well ... everything is clear here."""
        return self.result_data
