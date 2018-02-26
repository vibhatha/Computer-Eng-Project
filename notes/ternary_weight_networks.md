# Ternary weight network Summary

* state-of-the-art DNN models cant be directly applied to real world applications like smart phones or embedded
devices requires due to limited storage, battery power, and computer capabilities of the small
embedded devices.
* Binary weight networks and model compression are possible solutions.
* Ternary weight network constrain the weights to be ternary-valued: +1, 0 and -1.
* stochastic gradient descent (SGD) method is used to train.

## Expressive ability

** most commonly used convolutional filter is of size 3*3.
** With binary precision, there is only 2^(3*3) = 512 templates where as  TWN 3^(3*3) = 19683.
** TWNs has expressive abilities than the binary counterpart(BPWNs).

## Model compression

** Compared to 32 bit float and 64 bit double, TWNs one unit only cost 2 bits.

## Computational requirement

** Compared with the BPWNs, TWNs own an extra 0 state.
** However, the 0 terms need not be accumulated for any multiple operations



