import json
import unittest
from api.routes import app

app.testing = True

class MNISTPredictTests(unittest.TestCase):

    def test_predict_three(self):
        with app.test_client() as client:
            with open('img/three.png', 'rb') as image:
                response = client.post('/predict', data={'file': image})
                # print(json.loads(response))
                prediction = json.loads(response.data)['prediction']
                self.assertEqual(prediction, 3)
                self.assertEqual(response.status_code, 200)

    def test_predict_seven(self):
        with app.test_client() as client:
            with open('img/seven.png', 'rb') as image:
                response = client.post('/predict', data={'file': image})
                prediction = json.loads(response.data)['prediction']
                self.assertEqual(prediction, 7)
                self.assertEqual(response.status_code, 200)

    def test_predict_eight(self):
        with app.test_client() as client:
            with open('img/eight.png', 'rb') as image:
                response = client.post('/predict', data={'file': image})
                prediction = json.loads(response.data)['prediction']
                self.assertEqual(prediction, 8)
                self.assertEqual(response.status_code, 200)

    def test_predict_nofile(self):
        with app.test_client() as client:
            response = client.post('/predict', data={'file': ''})
            error = json.loads(response.data)['error']
            self.assertEqual(error, 'no file')
            self.assertEqual(response.status_code, 400)

    def test_predict_bad_file_type(self):
        with app.test_client() as client:
            with open('tests/notanimage.txt', 'rb') as file:
                response = client.post('/predict', data={'file': file})
                error = json.loads(response.data)['error']
                self.assertEqual(error, 'format not supported')
                self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()