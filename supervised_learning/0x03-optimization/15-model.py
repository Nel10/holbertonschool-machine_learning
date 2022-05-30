#!/usr/bin/env python3
"""
All together
"""
import tensorflow.compat.v1 as tf


def calculate_accuracy(y, y_pred):
    """Calculates accuracy of prediction"""
    pred = tf.math.argmax(y_pred, axis=1)
    ny = tf.math.argmax(y, axis=1)
    equality = tf.math.equal(pred, ny)
    accuracy = tf.math.reduce_mean(tf.cast(equality, tf.float32))
    return accuracy
