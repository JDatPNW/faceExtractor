# modified version of alexnet.py
""" AlexNet.
References:
    - Alex Krizhevsky, Ilya Sutskever & Geoffrey E. Hinton. ImageNet
    Classification with Deep Convolutional Neural Networks. NIPS, 2012.
"""

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.filterwarnings('ignore', category=DeprecationWarning)

import tflearn
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
from tflearn.layers.normalization import local_response_normalization


def dmnet(width, height, lr):
    network = input_data(shape=[None, width, height, 1], name='input')
    network = conv_2d(network, 32, 3, strides=2, activation='relu')
    network = max_pool_2d(network, 2, strides=2)
    network = conv_2d(network, 32, 3, activation='relu')
    network = max_pool_2d(network, 2, strides=2)
    network = conv_2d(network, 32, 3, activation='relu')
    network = max_pool_2d(network, 2, strides=2)
    network = fully_connected(network, 4, activation='linear')
    network = regression(network, optimizer='adam',
                         loss='mean_square',
                         learning_rate=lr, name='targets')

    model = tflearn.DNN(network, checkpoint_path='model_dmnet',
                        max_checkpoints=1, tensorboard_verbose=2, tensorboard_dir='log')

    return model
