import tensorflow as tf
import numpy as np
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Layer
from tensorflow.keras.layers import (Reshape, Conv2DTranspose, Add, Conv2D, MaxPool2D, Dense, Flatten, InputLayer, BatchNormalization, Input)
from tensorflow.keras.optimizers import Adam
from mnist_data import LATENT_DIMS, dataset, BATCH_SIZE


latent_inputs = Input(shape=(LATENT_DIMS,))

