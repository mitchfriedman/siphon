from flask_restful import Api
from siphon.resources.errors import get_error
from siphon.resources.queue import Enqueue, CreateQueue, Dequeue


class QueueApi(Api):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def handle_error(self, e):
        description = getattr(e, 'description', None)
        error = get_error(description)

        if error is not None:
            error_code = error.pop('error', 500)
            return self.make_response(error, error_code)

        return super().handle_error(e)

api = QueueApi()

api.add_resource(Enqueue, '/api/enqueue/<string:queue_name>')
api.add_resource(CreateQueue, '/api/create')
api.add_resource(Dequeue, '/api/dequeue/<string:queue_name>')
