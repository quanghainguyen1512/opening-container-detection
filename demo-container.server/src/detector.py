import keras

# import keras_retinanet
from keras_retinanet import models
from keras_retinanet.utils.image import read_image_bgr, preprocess_image, resize_image
from keras_retinanet.utils.visualization import draw_box, draw_caption
from keras_retinanet.utils.colors import label_color

# import miscellaneous modules
# import matplotlib.pyplot as plt
import cv2
import os
import numpy as np
import time
from threading import Thread

# set tf backend to allow memory to grow, instead of claiming everything
import tensorflow as tf

from .utils import get_dest_with_fname

def get_session():
    config = tf.ConfigProto()
    config.gpu_options.allow_growth = True
    return tf.Session(config=config)

# set the modified tf session as backend in keras
keras.backend.tensorflow_backend.set_session(get_session())

def detect(graph, model, image_paths):
    label_to_name = {0: 'open', 1: 'close'}
    saved = []
    for path in image_paths:
        img = read_image_bgr(path)
        draw = img.copy()
        draw = cv2.cvtColor(draw, cv2.COLOR_BGR2RGB)
        img = preprocess_image(img)
        img, scale = resize_image(img)
        with graph.as_default():
            bs, ss, ls = model.predict_on_batch(np.expand_dims(img, axis=0))
            bs /= scale
            
            for b, s, l in zip(bs[0], ss[0], ls[0]):
                if s < 0.5:
                    break
                color = label_color(l + 5)
                b = b.astype(int)
                # pred = gen_prediction(l, _b, s)
                # result.append(pred)
                caption = '{} {:.3f}'.format(label_to_name[l], s)
                draw_box(draw, b, color)
                draw_caption(draw, b, caption)
            dest = get_dest_with_fname(path)
            # thr = Thread(target=save_det, args=(draw, dest))
            # thr.start()
            cv2.imwrite(dest, cv2.cvtColor(draw, cv2.COLOR_RGB2BGR))
            saved.append(os.path.join('static', os.path.basename(path)))
    return saved
