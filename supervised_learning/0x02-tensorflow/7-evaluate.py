#!/usr/bin/env python3
"""evaluates the output of a neural network"""
import tensorflow.compat.v1 as tf


def evaluate(X, Y, save_path):
    """
    X is a numpy.ndarray containing the input data to evaluate
    Y is a numpy.ndarray containing the one-hot labels for X
    save_path is the location to load the model from
    """
    with tf.Session() as sess:
        saver = tf.train.import_meta_graph(save_path + '.meta')
        saver.restore(sess, save_path)
        x = tf.get_collection('x')[0]
        y = tf.get_collection("y")[0]
        y_pred = tf.get_collection("y_pred")[0]
        loss = tf.get_collection("loss")[0]
        acc = tf.get_collection("accuracy")[0]
        vars = sess.run([y_pred, acc, loss], feed_dict={x: X, y: Y})
        return vars[0], vars[1], vars[2]
