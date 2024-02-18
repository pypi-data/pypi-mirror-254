# A simple image resizing CLI - Package deployemnt test

### About
Just a test to see how distributing Python packages via Github would work. Feel free to use this if you think it would be useful though, but you're probably better off with [ImageMagick](https://github.com/ImageMagick/ImageMagick).

### Comands
- `img-resizer $IMG_PATH` Saves a new, resized image of the specified image path to the CWD, using the default size of 512x512px.
- `resizer $IMG_PATH small` Saves specified image as 512x512px in CWD   
- `resizer $IMG_PATH medium` Saves specified image as 1000x1000px in CWD
- `resizer $IMG_PATH big` Saves specified image as 2000x2000px in CWD
- `resizer $IMG_PATH custom <int> <int>` Saves specified image as <int>px<int>px in CWD
