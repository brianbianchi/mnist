import json
import requests 
import unittest

# https://your-heroku-app-name.herokuapp.com/predict
# http://localhost:5000/predict

class MNISTPredictTests(unittest.TestCase):

    def test_predict_three(self):
        file = open('test/three.png', 'rb')
        resp = requests.post("http://127.0.0.1:5000/predict", files={'file': file})
        file.close()
        self.assertEqual(resp.json().get('prediction'), 3)

    def test_predict_seven(self):
        file = open('test/seven.png', 'rb')
        resp = requests.post("http://127.0.0.1:5000/predict", files={'file': file})
        file.close()
        self.assertEqual(resp.json().get('prediction'), 7)

    def test_predict_eight(self):
        file = open('test/eight.png', 'rb')
        resp = requests.post("http://127.0.0.1:5000/predict", files={'file': file})
        file.close()
        self.assertEqual(resp.json().get('prediction'), 8)

if __name__ == '__main__':
    unittest.main()