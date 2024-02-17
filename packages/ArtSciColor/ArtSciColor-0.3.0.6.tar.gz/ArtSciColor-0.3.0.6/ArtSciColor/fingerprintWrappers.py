#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from PIL import Image
from sklearn.cluster import KMeans
import ArtSciColor.image as amg
import ArtSciColor.swatches as swt
import ArtSciColor.fingerprint as fng
import warnings
warnings.filterwarnings("ignore")


def getSwatchedImage(
        img, maxSide=150,
        cFun=KMeans, cArgs={'n_clusters': 10, 'max_iter': 1000, 'n_init': 10},
        grpFun=np.median, round=True, 
        HSVSort=False, hueClasses=10, grayThreshold=25,
        barHeight=0.15, barProportional=True,
        font='Arial', fontSize=50
    ):
    resized = amg.resizeCV2BySide(img, maxSide)
    (pixels, labels, model) = fng.calcDominantColors(
        resized, cFun=cFun, cArgs=cArgs
    )
    swatch = fng.getDominantSwatch(pixels, labels, grpFun=grpFun, round=round)
    swatchHex = (
        swt.sortSwatchHSV(swatch, hue_classes=hueClasses, gray_thresh=grayThreshold)
        if HSVSort else
        swt.sortSwatchByFrequency(swatch)
    )
    bars = fng.genColorSwatchFromImg(
        img, barHeight, swatchHex, 
        proportionalHeight=barProportional
    )
    barsImg = fng.addHexColorText(
        Image.fromarray(bars.astype('uint8'), 'RGB'), 
        swatchHex, font=font, fontSize=fontSize
    )
    newIMG = np.row_stack([img, barsImg])
    imgOut = Image.fromarray(newIMG.astype('uint8'), 'RGB')
    return {'image': imgOut, 'swatch': swatchHex, 'model': model}