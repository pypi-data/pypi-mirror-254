---
license: apache-2.0
tags:
- RyzenAI
- object-detection
- vision
- YOLO
- Pytorch
datasets:
- COCO
metrics:
- mAP
---
# YOLOv8m model trained on COCO

YOLOv8m is the medium version of YOLOv8 model trained on COCO object detection (118k annotated images) at resolution 640x640. It was released in [https://github.com/ultralytics/ultralytics](https://github.com/ultralytics/ultralytics).

We develop a modified version that could be supported by [AMD Ryzen AI](https://onnxruntime.ai/docs/execution-providers/Vitis-AI-ExecutionProvider.html).


## Model description

Ultralytics YOLOv8 is a cutting-edge, state-of-the-art (SOTA) model that builds upon the success of previous YOLO versions and introduces new features and improvements to further boost performance and flexibility. YOLOv8 is designed to be fast, accurate, and easy to use, making it an excellent choice for a wide range of object detection and tracking, instance segmentation, image classification and pose estimation tasks.


## Intended uses & limitations

You can use the raw model for object detection. See the [model hub](https://huggingface.co/models?search=amd/yolov8) to look for all available YOLOv8 models.


## How to use

### Installation

   Follow [Ryzen AI Installation](https://ryzenai.docs.amd.com/en/latest/inst.html) to prepare the environment for Ryzen AI.
   Run the following script to install pre-requisites for this model.
   ```bash
   pip install -r requirements.txt 
   ```


### Data Preparation (optional: for accuracy evaluation)

The dataset MSCOCO2017 contains 118287 images for training and 5000 images for validation.

Download COCO dataset and create/mount directories in your code like this:
  ```plain
  └── yolov8m
      └── datasets
          └── coco
                ├── annotations
                |   ├── instances_val2017.json
                |   └── ...
                ├── labels
                |   ├── val2017
                |   |   ├── 000000000139.txt
                |       ├── 000000000285.txt
                |       └── ...
                ├── images
                |   ├── val2017
                |   |   ├── 000000000139.jpg
                |       ├── 000000000285.jpg
                └── val2017.txt
  ```
1. put the val2017 image folder under images directory or use a softlink
2. the labels folder and val2017.txt above are generate by **general_json2yolo.py**
3. modify the coco.yaml like this:
```markdown
path: /path/to/your/datasets/coco  # dataset root dir
train: train2017.txt  # train images (relative to 'path') 118287 images
val: val2017.txt  # val images (relative to 'path') 5000 images
```


### Test & Evaluation

 - Code snippet from [`infer_onnx.py`](./infer_onnx.py) on how to use
```python
args = make_parser().parse_args()
source = args.image_path 
dataset = LoadImages(
    source, imgsz=imgsz, stride=32, auto=False, transforms=None, vid_stride=1
)
onnx_weight = args.model
onnx_model = onnxruntime.InferenceSession(onnx_weight)
for batch in dataset:
    path, im, im0s, vid_cap, s = batch
    im = preprocess(im)
    if len(im.shape) == 3:
        im = im[None]
    outputs = onnx_model.run(None, {onnx_model.get_inputs()[0].name: im.permute(0, 2, 3, 1).cpu().numpy()})
    outputs = [torch.tensor(item).permute(0, 3, 1, 2) for item in outputs]
    preds = post_process(outputs)
    preds = non_max_suppression(
        preds, 0.25, 0.7, agnostic=False, max_det=300, classes=None
    )
    plot_images(
        im,
        *output_to_target(preds, max_det=15),
        source,
        fname=args.output_path,
        names=names,
    )

```

 - Run inference for a single image
  ```python
  python infer_onnx.py --onnx_model ./yolov8m.onnx -i /Path/To/Your/Image --ipu --provider_config /Path/To/Your/Provider_config
  ```
*Note: __vaip_config.json__ is located at the setup package of Ryzen AI (refer to [Installation](#installation))*
 - Test accuracy of the quantized model
  ```python
  python eval_onnx.py --onnx_model ./yolov8m.onnx --ipu --provider_config /Path/To/Your/Provider_config
  ```

### Performance

|Metric |Accuracy on IPU|
| :----:  | :----: |
|AP\@0.50:0.95|0.486|


```bibtex
@software{yolov8_ultralytics,
  author = {Glenn Jocher and Ayush Chaurasia and Jing Qiu},
  title = {Ultralytics YOLOv8},
  version = {8.0.0},
  year = {2023},
  url = {https://github.com/ultralytics/ultralytics},
  orcid = {0000-0001-5950-6979, 0000-0002-7603-6750, 0000-0003-3783-7069},
  license = {AGPL-3.0}
}
```
