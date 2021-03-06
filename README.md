<p align="center">
  <img src="https://raw.githubusercontent.com/brianbianchi/mnist/master/img/label.png" width="50%">
</p>

---

![Tests](https://github.com/brianbianchi/mnist/workflows/Tests/badge.svg)

> An example of how you can deploy a prediction neural net using a rest API.

> The [MNIST database](https://en.wikipedia.org/wiki/MNIST_database) (Modified National Institute of Standards and Technology database) is a large database of handwritten digits that is commonly used for training various image processing systems. I use this dataset to train a net and pedict the number in an image.

## Endpoints

| Request method | Endpoint   | Body                           | Reponse                                | Description                     |
| :------------- | :--------- | :----------------------------- | :------------------------------------- | :------------------------------ |
| POST           | `/predict` | `image[.png \| .jpg \| .jpeg]` | `{'prediction': 8, 'class_name': '8'}` | Predicts number in given image. |

## Usage

```console
$ python3 -m venv venv
$ . venv/bin/activate
$ (venv) flask run
$ (venv) python -m unittest discover tests
```
