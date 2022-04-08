<p align="center">
  <img src="https://raw.githubusercontent.com/brianbianchi/mnist/master/img/label.png" width="50%">
</p>

--------------------------------------------------------------------

![Tests](https://github.com/brianbianchi/mnist/workflows/Tests/badge.svg)

> An example project to show how you can deploy a prediction neural net using a rest API.

> The [MNIST database](https://en.wikipedia.org/wiki/MNIST_database) (Modified National Institute of Standards and Technology database) is a large database of handwritten digits that is commonly used for training various image processing systems. I use this dataset to train a net and pedict the number in an image.

## Usage

```console
$ python3 -m venv venv
$ . venv/bin/activate 
$ (venv) flask run
$ (venv) python -m unittest discover tests
```