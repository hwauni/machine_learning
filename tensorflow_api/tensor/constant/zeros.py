# -*- coding: utf-8 -*-
#!/usr/bin/python

import tensorflow as tf
import tfutil

if __name__ == '__main__':
    const = tf.zeros([3, 4], tf.int32)
    tfutil.print_constant(const)

