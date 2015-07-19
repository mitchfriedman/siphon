from tests.resources.api_test_case import ApiTestCase


class TestCreateQueue(ApiTestCase):

    def test_create_queue(self):
        response = self.post('/api/create', data={
            'queue_name': 'foobar'
        })



