import json
import unittest
from api.routes import app

app.testing = True

class MNISTPredictTests(unittest.TestCase):

    def test_predict_three(self):
        with app.test_client() as client:
            with open('img/three.png', 'rb') as image:
                response = client.post('/predict', data={'file': image})
                prediction = json.loads(response.data)['prediction']
                self.assertEqual(prediction, 3)

    def test_predict_seven(self):
        with app.test_client() as client:
            with open('img/seven.png', 'rb') as image:
                response = client.post('/predict', data={'file': image})
                prediction = json.loads(response.data)['prediction']
                self.assertEqual(prediction, 7)

    def test_predict_eight(self):
        with app.test_client() as client:
            with open('img/eight.png', 'rb') as image:
                response = client.post('/predict', data={'file': image})
                prediction = json.loads(response.data)['prediction']
                self.assertEqual(prediction, 8)

if __name__ == '__main__':
    unittest.main()