# Data Notes

This file explains the dataset used for the WildTrack AI wildlife detection model.

---

## Dataset Overview

The model was trained to detect five wildlife classes:

- Deer
- Boar
- Rabbit
- Pheasant
- Jackal

The training dataset used approximately **1,000 images per species**.

The model was tested on a separate test set of **540 images**.

The dataset was prepared for YOLO object detection. Each image has a matching label file in YOLO format. The label files contain the class ID and bounding box coordinates for the animal in the image.

---

## Dataset Structure

The dataset follows a YOLO-style structure:

```text
dataset/
  train/
    images/
    labels/
  valid/
    images/
    labels/
  test/
    images/
    labels/
