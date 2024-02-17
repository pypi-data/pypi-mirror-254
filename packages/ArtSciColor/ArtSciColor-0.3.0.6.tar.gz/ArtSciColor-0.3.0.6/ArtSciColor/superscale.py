#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image
from super_image import EdsrModel, ImageLoader


def superscale(img, model=EdsrModel, scale=2):
    mod = model.from_pretrained('eugenesiow/edsr-base', scale=scale)
    inputs = ImageLoader.load_image(Image.fromarray(img.astype('uint8'), 'RGB'))
    preds = mod(inputs)
    return preds