from flask_restful import Api
from siphon.resources.queue import Enqueue


errors = {
    'QueueNotFound': {
        'message': "A queue with that given name does not exist",
        'status': 400,
    },
}


def get_error(error):
    pass

class QueueApi(Api):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def handle_error(self, e):
        description = getattr(e, 'description', None)
        if description is not None:
            if description in errors:
                return self.make_response({
                    'message': errors[description]['message'],
                }, errors[description]['status'])

        return super().handle_error(e)

api = QueueApi(errors=errors)

api.add_resource(Enqueue, '/api/enqueue/<string:queue_name>')
