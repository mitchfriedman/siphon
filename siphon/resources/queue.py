from flask.ext.restful import Resource, reqparse
from flask.ext.restful.representations import json
from siphon import queue_manager
from flask import make_response, request
from siphon.resources.util import get_args


class Enqueue(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('key', type=str, location='form', required=True, help='The unique key of your data')
    parser.add_argument('queue_name', type=str, location='view_args', required=True, help='The queue you wish to enqueue data in')

    def post(self, **_):
        args = get_args(self.parser, request)
        key = args.pop('key', None)
        queue_name = args.pop('queue_name', None)

        queue_manager.enqueue(queue_name, key, args)

        return make_response(json.dumps({
            'status': 'enqueued'
        }), 201)


class CreateQueue(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('queue_name', type=str, location='form', required=True, help='The name of the queue you wish to create')

    def post(self, **_):
        args = get_args(self.parser, request)
        queue_name = args.pop('queue_name')

        queue_manager.create_queue(queue_name)

        return make_response(json.dumps({
            'status': 'created',
            'id': queue_name,
            'queue': {
                'name': queue_name, 
            }
        }), 201)

class Dequeue(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('queue_name', type=str, location='view_args', required=True, help='The queue you wish to enqueue data in')

    def post(self, **_):
        args = get_args(self.parser, request)
        queue_name = args.pop('queue_name')

        data = queue_manager.dequeue(queue_name)
        status_code = 200

        print(data)

        if data is None:
            data, status_code = {'message': 'Queue does not exist'}, 400
        elif len(data) == 0:
            data = {'message': 'Queue is empty'}

        return make_response(json.dumps(data), status_code)
