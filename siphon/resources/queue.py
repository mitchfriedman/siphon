from flask.ext.restful import Resource, reqparse, abort
from flask.ext.restful.representations import json
from siphon import queue_manager
from flask import make_response, request

parser = reqparse.RequestParser()
parser.add_argument('key', type=str, location='form', required=True, help='The unique key of your data')
parser.add_argument('queue_name', type=str, location='view_args', required=True, help='The queue you wish to enqueue data in')

def get_extra_params(request):
    return request.form.to_dict()


class Enqueue(Resource):

    def post(self, **_):
        extra_args = get_extra_params(request)
        args = parser.parse_args(strict=False)
        args.update(extra_args)

        key = args.pop('key', None)
        queue_name = args.pop('queue_name', None)

        queue_manager.enqueue(queue_name, key, args)

        return make_response(json.dumps({
            'status': 'enqueued'
        }), 201)


class CreateQueue(Resource):
    def post(self, **kwargs):
        pass
