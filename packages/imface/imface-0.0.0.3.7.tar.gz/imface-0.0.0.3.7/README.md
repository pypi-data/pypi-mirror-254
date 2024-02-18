# imface

this cli project is depended on serengil deepface project
https://github.com/serengil/deepface


install gdown first
```
pip install gdown
```

how to install
```
pip install imface
```

to uninstall

```
pip uninstall imface
```

how to use

```
imface represent -p image-path -d detector(ie yolov8 or retinaface)
```
to get the embedded vectors of an image

```
imface selfie -p image-path -d detector(ie yolov8 or retinaface)
```
to extract embedded vector of face in image, only just for one face per image
