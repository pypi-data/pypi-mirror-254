from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Layer, BatchNormalization, MaxPool1D, Conv1D, ReLU, MaxPooling1D, Flatten, Bidirectional, GRU, LeakyReLU, Lambda, Dense, MaxPool2D, Conv2D, LSTM, Concatenate, Dropout
from tensorflow.keras.constraints import max_norm 
from tensorflow import expand_dims
from tensorflow.keras import activations
import tensorflow as tf
from . import CustomDistiller




class Hybrid(CustomDistiller):
    def __init__(self, payload_size=784, header_fields_packets=32, n_classes=[],merging_method='feat_concat') -> None:
        super(Hybrid, self).__init__(  
            modalities=[
                wang_payload_modality(payload_size),
                lopez_protocol_header_fields_extended_modality(header_fields_packets),
                stnn_inspired_image_extended_modality(),
                graphdapp_modality()
            ],
            adapter_size=128, 
            n_classes=n_classes,
            merging_method=merging_method
        )



def wang_payload_modality(payload_size=784):
    input_layer_payload_modality = Input(shape=(payload_size,1), name='input_payload')
    return Model(
        name='Wang payload modality - nbytes',
        inputs=input_layer_payload_modality,
        outputs=stack([
            input_layer_payload_modality,
            Conv1D(16, 25, name='Conv1D_payload_1'),
            ReLU(),
            MaxPooling1D(3, name='MaxPooling1D_payload_1'),
            Conv1D(32, 35, name='Conv1D_payload_2'),
            ReLU(),
            MaxPooling1D(3, name='MaxPooling1D_payload_2'),
            Flatten(), 
        ])
    )


def lopez_protocol_header_fields_modality(packet_count=32):
    input_layer_protocol_fields_modality = Input(shape=(packet_count,4), name='input_protocol_fields')
    return Model(
        name='Lopez protocol header fields modality',
        inputs=input_layer_protocol_fields_modality,
        outputs=stack([
            input_layer_protocol_fields_modality,
            Bidirectional(GRU(64, return_sequences=True, kernel_constraint=max_norm(3))),
            ReLU(),
            Flatten(),
        ])
    )

def lopez_protocol_header_fields_extended_modality(packet_count=32):
    input_layer_protocol_fields_modality = Input(shape=(packet_count,6), name='input_protocol_fields')
    return Model(
        name='Lopez protocol header fields extended modality',
        inputs=input_layer_protocol_fields_modality,
        outputs=stack([
            input_layer_protocol_fields_modality,
            Bidirectional(GRU(64, return_sequences=True, kernel_constraint=max_norm(3))),
            ReLU(),
            Flatten(),
        ])
    )

def stnn_inspired_image_modality():
    input_layer_stnn_modality = Input(shape=(5,14), name='input_stnn')
    return Model(
        name='STNN-inspired image modality',
        inputs=input_layer_stnn_modality,
        outputs=stack([
            input_layer_stnn_modality,
            Bidirectional(LSTM(65,return_sequences=True)),
            Lambda(lambda x: expand_dims(x, axis=3)),
            Conv2D(32,3,padding='same'),
            LeakyReLU(),
            Conv2D(32,3,padding='same'),
            LeakyReLU(),
            MaxPool2D(2),
            Conv2D(64,3,padding='same'),
            LeakyReLU(),
            Conv2D(128,3,padding='same'),
            LeakyReLU(),
            MaxPool2D(2),
            Flatten(),
            Dense(512),
        ])
    )

def stnn_inspired_image_extended_modality():
    input_size = 177-42
    input_layer_stnn_modality = Input(shape=(input_size,1), name='input_stnn')
    return Model(
        name='STNN-inspired image extended modality',
        inputs=input_layer_stnn_modality,
        outputs=stack([
            input_layer_stnn_modality,
            Bidirectional(LSTM(64,return_sequences=True)), #128
            Conv1D(32,3,padding='same'),
            LeakyReLU(),
            #Conv1D(32,3,padding='same'),
            #LeakyReLU(),
            #MaxPool1D(2),
            Conv1D(64,3,padding='same'),
            LeakyReLU(),
            #Conv1D(128,3,padding='same'),
            #LeakyReLU(),
            MaxPool1D(2),
            Flatten(),
            Dense(512),
        ])
    )


def graphdapp_modality():
    input_layer_graphdapp_adj_matrix_modality = Input(shape=(32,32),name='input_graphdapp_adj_matrix')
    input_layer_graphdapp_features_modality = Input(shape=(32,1),name='input_graphdapp_features')
    inputs_layer = [input_layer_graphdapp_adj_matrix_modality, input_layer_graphdapp_features_modality]
    mlp1 = MLPLayer(64)
    mlp2 = MLPLayer(64)
    mlp3 = MLPLayer(64)
    readout = Readout()
    concat = Concatenate()
    x1 = mlp1(inputs_layer)
    x2 = mlp2(x1)
    x3 = mlp3(x2)
    x4 = readout([x1, x2, x3])
    x4 = concat(x4)
    return Model(
        name='GraphDApp modality',
        inputs=inputs_layer,
        outputs= x4
    )

class Readout(Layer):
    def __init__(self):
        super(Readout, self).__init__()
    
    def call(self, inputs):
        FsBatch = []
        for i in range(len(inputs)):
            Fbatch = inputs[i][1]
            FsBatch.append(tf.reduce_sum(Fbatch, axis=-2))
        return FsBatch


class MLPLayer(Layer):
    def __init__(
            self, 
            output_size=5, 
            activation='relu', 
            use_bias=True, 
            neighbour_agg_method='sum', 
            dropout_rate=0.025):
        super(MLPLayer, self).__init__()
        self.output_size = output_size
        self.dense = Dense(self.output_size, use_bias=use_bias)
        self.activation = activations.get(activation)
        self.batch_norm = BatchNormalization()
        self.dropout = Dropout(dropout_rate)
    
    def build(self, input_shape):
        self.eps = self.add_weight(
            name='epsilon',
            shape=(1,),
            initializer="random_normal",
            dtype='float32',
            trainable=True,
        )
    
    def call(self, inputs, training=False):
        '''
        [A, F]
        '''
        A = inputs[0]
        F = inputs[1]
        outputs = tf.multiply(1.0+self.eps, F) + tf.matmul(A,F)
        outputs = self.dense(outputs)
        outputs = self.activation(outputs)
        outputs = self.batch_norm(outputs, training=training)
        outputs = self.dropout(outputs)
        return [A, outputs]



class GraphAttention(layers.Layer):
    def __init__(
        self,
        units,
        kernel_initializer="glorot_uniform",
        kernel_regularizer=None,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.units = units
        self.kernel_initializer = keras.initializers.get(kernel_initializer)
        self.kernel_regularizer = keras.regularizers.get(kernel_regularizer)

    def build(self, input_shape):

        self.kernel = self.add_weight(
            shape=(input_shape[0][-1], self.units),
            trainable=True,
            initializer=self.kernel_initializer,
            regularizer=self.kernel_regularizer,
            name="kernel",
        )
        self.kernel_attention = self.add_weight(
            shape=(self.units * 2, 1),
            trainable=True,
            initializer=self.kernel_initializer,
            regularizer=self.kernel_regularizer,
            name="kernel_attention",
        )
        self.built = True

    def call(self, inputs):
        node_states, edges = inputs

        # Linearly transform node states
        node_states_transformed = tf.matmul(node_states, self.kernel)

        # (1) Compute pair-wise attention scores
        node_states_expanded = tf.gather(node_states_transformed, edges)
        node_states_expanded = tf.reshape(
            node_states_expanded, (tf.shape(edges)[0], -1)
        )
        attention_scores = tf.nn.leaky_relu(
            tf.matmul(node_states_expanded, self.kernel_attention)
        )
        attention_scores = tf.squeeze(attention_scores, -1)

        # (2) Normalize attention scores
        attention_scores = tf.math.exp(tf.clip_by_value(attention_scores, -2, 2))
        attention_scores_sum = tf.math.unsorted_segment_sum(
            data=attention_scores,
            segment_ids=edges[:, 0],
            num_segments=tf.reduce_max(edges[:, 0]) + 1,
        )
        attention_scores_sum = tf.repeat(
            attention_scores_sum, tf.math.bincount(tf.cast(edges[:, 0], "int32"))
        )
        attention_scores_norm = attention_scores / attention_scores_sum

        # (3) Gather node states of neighbors, apply attention scores and aggregate
        node_states_neighbors = tf.gather(node_states_transformed, edges[:, 1])
        out = tf.math.unsorted_segment_sum(
            data=node_states_neighbors * attention_scores_norm[:, tf.newaxis],
            segment_ids=edges[:, 0],
            num_segments=tf.shape(node_states)[0],
        )
        return out


class MultiHeadGraphAttention(layers.Layer):
    def __init__(self, units, num_heads=8, merge_type="concat", **kwargs):
        super().__init__(**kwargs)
        self.num_heads = num_heads
        self.merge_type = merge_type
        self.attention_layers = [GraphAttention(units) for _ in range(num_heads)]

    def call(self, inputs):
        atom_features, pair_indices = inputs

        # Obtain outputs from each attention head
        outputs = [
            attention_layer([atom_features, pair_indices])
            for attention_layer in self.attention_layers
        ]
        # Concatenate or average the node states from each head
        if self.merge_type == "concat":
            outputs = tf.concat(outputs, axis=-1)
        else:
            outputs = tf.reduce_mean(tf.stack(outputs, axis=-1), axis=-1)
        # Activate and return node states
        return tf.nn.relu(outputs)


class GraphAttentionNetwork(keras.Model):
    def __init__(
        self,
        node_states,
        edges,
        hidden_units,
        num_heads,
        num_layers,
        output_dim,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.node_states = node_states
        self.edges = edges
        self.preprocess = layers.Dense(hidden_units * num_heads, activation="relu")
        self.attention_layers = [
            MultiHeadGraphAttention(hidden_units, num_heads) for _ in range(num_layers)
        ]
        self.output_layer = layers.Dense(output_dim)

    def call(self, inputs):
        node_states, edges = inputs
        x = self.preprocess(node_states)
        for attention_layer in self.attention_layers:
            x = attention_layer([x, edges]) + x
        outputs = self.output_layer(x)
        return outputs

    def train_step(self, data):
        indices, labels = data

        with tf.GradientTape() as tape:
            # Forward pass
            outputs = self([self.node_states, self.edges])
            # Compute loss
            loss = self.compiled_loss(labels, tf.gather(outputs, indices))
        # Compute gradients
        grads = tape.gradient(loss, self.trainable_weights)
        # Apply gradients (update weights)
        optimizer.apply_gradients(zip(grads, self.trainable_weights))
        # Update metric(s)
        self.compiled_metrics.update_state(labels, tf.gather(outputs, indices))

        return {m.name: m.result() for m in self.metrics}

    def predict_step(self, data):
        indices = data
        # Forward pass
        outputs = self([self.node_states, self.edges])
        # Compute probabilities
        return tf.nn.softmax(tf.gather(outputs, indices))

    def test_step(self, data):
        indices, labels = data
        # Forward pass
        outputs = self([self.node_states, self.edges])
        # Compute loss
        loss = self.compiled_loss(labels, tf.gather(outputs, indices))
        # Update metric(s)
        self.compiled_metrics.update_state(labels, tf.gather(outputs, indices))

        return {m.name: m.result() for m in self.metrics}
    
# TDL verions

def lopez_protocol_header_fields_TDL_modality(packet_count=32):
    input_layer_protocol_fields_modality = Input(shape=(packet_count,3), name='input_protocol_fields_TDL')
    return Model(
        name='Lopez protocol header fields modality',
        inputs=input_layer_protocol_fields_modality,
        outputs=stack([
            input_layer_protocol_fields_modality,
            Bidirectional(GRU(64, return_sequences=True, kernel_constraint=max_norm(3))),
            ReLU(),
            Flatten(),
        ])
    )

def stack(layers):
    '''
    Using the Functional-API of Tensorflow to build a sequential
    network (stacked layers) from list of layers.
    '''
    layer_stack = None
    for layer in layers:
        if layer_stack is None:
            layer_stack = layer
        else:
            layer_stack = layer(layer_stack)
    return layer_stack
