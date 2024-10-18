import tensorflow as tf
import numpy as np
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Layer
from tensorflow.keras.layers import (Reshape, Conv2DTranspose, Add, Conv2D, MaxPool2D, Dense, Flatten, InputLayer, BatchNormalization, Input)
from tensorflow.keras.optimizers import Adam
from data_preparation import LATENT_DIMS, dataset, BATCH_SIZE



#Sampling Layer

class Sampling(Layer):
  def call(self, inputs):
    mean, log_var = inputs
    return mean + tf.math.exp(0.5*log_var)*tf.random.normal(shape=(BATCH_SIZE, LATENT_DIMS))

encoder_inputs = Input(shape=(28, 28, 1))

x = Conv2D(32, 3, activation = 'relu', stride = 2, padding = 'same')(encoder_inputs)
x = Conv2D(32, 3, activation = 'relu', stride = 2, padding = 'same')(x)

x = Flatten()(x)
x = Dense(16, activation='relu')(x)

mean = Dense(LATENT_DIMS,)(x)
log_var = Dense(LATENT_DIMS,)(x)

z = Sampling()([mean, log_var])

encoder_model = Model(encoder_inputs, [z, mean, log_var], name = 'encoder')
encoder_model.summary()


