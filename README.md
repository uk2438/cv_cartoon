# cv_cartoon
convert image to cartoon using OpenCV

## Best Image
'cartoon_best' is the best one of image converted an image to cartoon.
The colors in the photo are vivid, so I think the conversion went well.

## Worse Image
'cartoon_worse' is worse one of my converted photo sample.
There are a lot of blurry parts, so I think it couldn't find the outline properly.

## Limitations of my algorithm
first, the more blurry the photo is, the harder it is to find the outlines, so it doesn't look like a cartoon.
second, if the object and background in the image are similar colors, it is difficult to convert.
Third, images with many gradients cannot be converted accurately.
