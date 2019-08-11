import tensorflow as tf
import numpy as np
import matplotlib as mil
#mil.use('svg')
mil.use("nbagg")
from matplotlib import pyplot


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

# Rank 3 tensor in format:
# [batch_size, image_height, image_width, channels]
sess.run(image)

pyplot.imshow(sess.run(image), interpolation='nearest')
pyplot.show()
filename_queue.close(cancel_pending_enqueues=True)
coord.request_stop()
coord.join(threads)