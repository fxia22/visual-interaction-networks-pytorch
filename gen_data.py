from physics_engine import gen
import sys, os
import pickle as pkl
import numpy as np
import cv2
from PIL import Image

n_samples = 1000
n_body = 3
outf = sys.argv[1]
xx,yy = np.meshgrid(range(400), range(400))
resolution = (32,32)
colors = np.array([[0, 0, 255], [0, 255, 0], [255, 0, 0]]).astype(np.uint8)

for i in range(n_samples):
    data = gen(n_body, True)
    pkl.dump(data, open(os.path.join(outf, 'data_{}.pkl'.format(i)), 'wb'))

    xy = data[:, :, 1:3] + 200
    for j in range(xy.shape[0]):
        frame = np.zeros((400, 400, 3)).astype(np.uint8)
        for k in range(xy.shape[1]):
            mask = ((xx - xy[j, k, 1]) ** 2 + (yy - xy[j, k, 0]) ** 2) < 400
            # print(mask.shape)
            frame[mask, :] = colors[k]
        frame = cv2.resize(frame, resolution)
        Image.fromarray(frame).save(os.path.join(outf, 'img_{}_{}.png'.format(i,j)))

    if i%100 == 0: print(i)