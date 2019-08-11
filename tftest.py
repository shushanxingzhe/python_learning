import matplotlib as mil
#mil.use('svg')
#mil.use("nbagg")

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
sess = tf.InteractiveSession()


image_filename = "dog.jpg"
filename_queue = tf.train.string_input_producer(tf.train.match_filenames_once(image_filename))

image_reader = tf.WholeFileReader()
init_op = tf.group(tf.initialize_all_variables(), tf.local_variables_initializer())
sess.run(init_op)
_, image_file = image_reader.read(filename_queue)
image = tf.image.decode_jpeg(image_file)


coord = tf.train.Coordinator()
threads = tf.train.start_queue_runners(coord=coord)

image_batch = tf.image.convert_image_dtype(tf.expand_dims(image, 0), tf.float32, saturate=False)

kernel1 = tf.constant([
        [
            [[ -1., 0., 0.], [ 0., -1., 0.], [ 0., 0., -1.]],
            [[ -1., 0., 0.], [ 0., -1., 0.], [ 0., 0., -1.]],
            [[ -1., 0., 0.], [ 0., -1., 0.], [ 0., 0., -1.]]
        ],
        [
            [[ -1., 0., 0.], [ 0., -1., 0.], [ 0., 0., -1.]],
            [[ 8., 0., 0.], [ 0., 8., 0.], [ 0., 0., 8.]],
            [[ -1., 0., 0.], [ 0., -1., 0.], [ 0., 0., -1.]]
        ],
        [
            [[ -1., 0., 0.], [ 0., -1., 0.], [ 0., 0., -1.]],
            [[ -1., 0., 0.], [ 0., -1., 0.], [ 0., 0., -1.]],
            [[ -1., 0., 0.], [ 0., -1., 0.], [ 0., 0., -1.]]
        ]
    ])

kernel2 = tf.constant([
        [
            [[ 0., 0., 0.], [ 0., 0., 0.], [ 0., 0., 0.]],
            [[ -1., 0., 0.], [ 0., -1., 0.], [ 0., 0., -1.]],
            [[ 0., 0., 0.], [ 0., 0., 0.], [ 0., 0., 0.]]
        ],
        [
            [[ -1., 0., 0.], [ 0., -1., 0.], [ 0., 0., -1.]],
            [[ 5., 0., 0.], [ 0., 5., 0.], [ 0., 0., 5.]],
            [[ -1., 0., 0.], [ 0., -1., 0.], [ 0., 0., -1.]]
        ],
        [
            [[ 0., 0., 0.], [ 0., 0., 0.], [ 0., 0., 0.]],
            [[ -1., 0., 0.], [ 0., -1., 0.], [ 0., 0., -1.]],
            [[ 0, 0., 0.], [ 0., 0., 0.], [ 0., 0., 0.]]
        ]
    ])


conv2d = tf.nn.conv2d(image_batch, kernel1, [1, 1, 1, 1], padding="SAME")
activation_map = sess.run(tf.minimum(tf.nn.relu(conv2d), 255))

fig = plt.gcf() #pyplot.figure()
ax1 = fig.add_subplot(121)
ax1.set_title("original")
ax1.set_xticks([])
ax1.set_yticks([])
ax1.imshow(image_batch[0].eval(), interpolation='nearest')
ax2 = fig.add_subplot(122)
ax2.imshow(activation_map[0], interpolation='nearest')
ax2.set_title("after")
ax2.set_xticks([])
ax2.set_yticks([])
# fig.set_size_inches(4, 4)
# fig.savefig("example-edge-detection.png")
plt.show()


filename_queue.close(cancel_pending_enqueues=True)
coord.request_stop()
coord.join(threads)
