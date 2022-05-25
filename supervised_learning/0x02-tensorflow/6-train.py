#!/usr/bin/env python3
"""builds, trains, and saves a neural network classifier"""
import tensorflow.compat.v1 as tf
calculate_accuracy = __import__('3-calculate_accuracy').calculate_accuracy
calculate_loss = __import__('4-calculate_loss').calculate_loss
create_placeholders = __import__('0-create_placeholders').create_placeholders
create_train_op = __import__('5-create_train_op').create_train_op
forward_prop = __import__('2-forward_prop').forward_prop


def train(X_train, Y_train, X_valid, Y_valid, layer_sizes,
          activations, alpha, iterations, save_path="/tmp/model.ckpt"):
    """Returns: the path where the model was saved"""
    create_placeholders(X_train.shape[1], Y_train.shape[1])
    tf.add_to_collection(name='x', value=x)
    tf.add_to_collection(name='y', value=y)
    prediction_total = forward_prop(x, layer_sizes, activations)
    tf.add_to_collection(name='prediction', value=prediction_total)
    loss_total = calculate_loss(y, prediction_total)
    tf.add_to_collection(name='loss', value=loss_total)
    accuracy = calculate_accuracy(y, prediction_total)
    tf.add_to_collection(name='accuracy', value=accuracy)
    train = create_train_op(loss_total, alpha)
    tf.add_to_collection(name='train', value=train)

    init = tf.global_variables_initializer()

    with tf.Session() as session:
        session.run(init)
        for i in range(iterations + 1):
            if i % 100 == 0 or i == iterations:
                print("After {} iterations:".format(i))
                tloss, taccuracy = session.run([loss_total, accuracy],
                                               feed_dict={x: X_train,
                                                          y: Y_train})
                print("\tTraining Cost: {}".format(tloss))
                print("\tTraining Accuracy: {}".format(taccuracy))
                vloss, vaccuracy = session.run([loss_total, accuracy],
                                               feed_dict={x: X_valid,
                                                          y: Y_valid})
                print("\tValidation Cost: {}".format(vloss))
                print("\tValidation Accuracy: {}".format(vaccuracy))
            if i < iterations:
                session.run(train_op, feed_dict={x: X_train, y: Y_train})
        saver = tf.train.Saver()
        return saver.save(session, save_path)
