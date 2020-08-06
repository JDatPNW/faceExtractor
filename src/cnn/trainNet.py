import numpy as np
from dmnet import dmnet
from random import shuffle

WIDTH = 160
HEIGHT = 90
LR = 1e-3
EPOCHS = 100
MODEL_NAME = 'JD-dmnet-FaceX.model'


model = dmnet(WIDTH, HEIGHT, LR)

# model.load(MODEL_NAME)

train_data = np.load('data.npy', allow_pickle=True)

train_test_limit = int(len(train_data)/10)

for epoch in range(EPOCHS):

    shuffle(train_data)

    train = train_data[:-train_test_limit]
    test = train_data[-train_test_limit:]

    X = np.array([i[0] for i in train]).reshape(-1, WIDTH, HEIGHT, 1)
    Y = [i[1] for i in train]

    test_x = np.array([i[0] for i in test]).reshape(-1, WIDTH, HEIGHT, 1)
    test_y = [i[1] for i in test]

    model.fit({'input': X}, {'targets': Y}, n_epoch=1, validation_set=({'input': test_x}, {'targets': test_y}),
              snapshot_step=500, show_metric=True, run_id=MODEL_NAME)

    model.save(MODEL_NAME)
