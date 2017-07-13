import twice_input
import twice

from scipy.misc import imread
import numpy as np
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


if __name__ == '__main__':
    path = 'D:/Data/cnn/faces'
    data = twice_input.read_data_sets(path, 100)

    BATCH_SIZE = 15
    before_epoch = 0

    with tf.Session() as sess:
        m = twice.Twice(sess, 0.001)
        m.saver.restore(sess, 'save/capture.ckpt')

        array = np.array(imread('C:/Users/dsm2016/Desktop/me.jpg')).reshape((1, 32, 32, 3))
        c, = m.predict(array)
        print(c)
        # for i in range(100):
        #     x, y = data.test.next_batch(BATCH_SIZE)
        #     x.reshape(BATCH_SIZE, twice_input.IMAGE_SIZE)
        #
        #     c = m.predict(x)
        #     print("label : ", c, 'answer : ', np.argmax(y, axis=1))

