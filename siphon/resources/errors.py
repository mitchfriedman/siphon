errors = {
    'QueueNotFound': {
        'message': "A queue with that given name does not exist",
        'status': 400,
    },
}


def get_error(error):
    if error in errors:
        error = errors[error]
        return {
            'message': error['message'],
            'error': error['status'],
        }
    return None

