import numpy as np
import neurolab as nl
## import pylab as pl
from matplotlib import pyplot as pl

net = nl.net.newff([[-10, 10]], [15, 1])
x = np.linspace(-10, 10, 100)
y = 0.75*np.cos(x)
size = len(x)
inp = x.reshape(size,1)
inp
trg = y.reshape(size,1)
#error = net.train(inp, trg, epochs=300, show=100, goal=0.01)
trg
net.trainf = nl.train.train_gdx
error = net.train(inp, trg, epochs=300, show=100, goal=0.01,mc=0.2)
print(net.trainf)
out = net.sim(inp)

pl.subplot(211)
pl.plot(error)
pl.xlabel('Epoch number')
pl.ylabel('error (default SSE)')

pl.subplot(212)
pl.plot(inp, trg, '-',inp , out, '.', inp, trg, 'p')
pl.legend(['train target', 'net output'])
pl.show()



