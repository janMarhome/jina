import unittest

import numpy as np

from . import NumericTestCase
from jina.executors.encoders.numeric.pca import IncrementalPCAEncoder


class MyTestCase(NumericTestCase):
    def _get_encoder(self):
        self.input_dim = 28
        self.target_output_dim = 2
        encoder = IncrementalPCAEncoder(
            output_dim=self.target_output_dim, whiten=True, num_features=self.input_dim)
        train_data = np.random.rand(1000, self.input_dim)
        encoder.train(train_data)
        return encoder


if __name__ == '__main__':
    unittest.main()
