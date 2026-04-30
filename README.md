# WildTrack AI — Wildlife Detection System

---

## Project Overview

WildTrack AI is an AI-based wildlife detection system developed as a final EECE 490 machine learning project.

The project uses a trained YOLO object detection model to identify wildlife species from uploaded images or live camera frames.

The system detects animals, returns confidence scores, displays bounding boxes, and classifies the detected animal as legal or illegal.

WildTrack AI is designed as an application-oriented machine learning system.

The project focuses on solving a real-world wildlife monitoring problem using computer vision.

Instead of manually checking camera footage or image datasets, the system automates the detection process.

This makes the project useful for wildlife observation, camera-trap analysis, hunting regulation support, and environmental monitoring.

---

## Project Type

This project follows:

**Option A: Application-Oriented ML Systems**

The project includes:

- A real-world problem
- A non-AI baseline
- A machine learning model
- Model evaluation
- A backend API
- A user interface
- Reproducible experiments
- A Dockerized API setup
- A structured GitHub repository

---

## Developed By

- Mamdouh El Zein
- Lucien Daher

---

## Main Goal

The main goal of WildTrack AI is to create a practical wildlife detection platform.

The system allows users to upload wildlife images or use live camera input.

The model then detects the animal species.

The system also shows how confident the model is.

Finally, the system classifies the animal as legal or illegal based on a predefined mapping.

---

## Real-World Problem

Wildlife monitoring often requires reviewing many images or video frames manually.

This can be slow, repetitive, and error-prone.

A person may miss animals in low-quality images.

A person may also take too long to review large camera-trap datasets.

WildTrack AI helps solve this by using machine learning to detect animals automatically.

---

## Why Machine Learning Is Useful

A simple non-AI system may rely on brightness, motion, or image sharpness.

However, these rules cannot reliably identify the animal species.

They also struggle with complex backgrounds, lighting changes, and partial animal visibility.

Machine learning is more suitable because it can learn visual patterns from data.

The YOLO model can detect multiple animals and classify their species.

It can also return bounding boxes and confidence scores.

---

## Detected Animal Classes

The model focuses on five wildlife classes:

- Deer
- Boar
- Rabbit
- Pheasant
- Jackal

---

## Legal Classification

The system includes a legality classification for each detected species.

| Species | Legal Status |
|---|---|
| Deer | Legal |
| Boar | Legal |
| Rabbit | Legal |
| Pheasant | Legal |
| Jackal | Illegal |

This legal classification is displayed in the interface and returned by the API.

---

## Main Features

- Wildlife detection using YOLO
- Image upload detection
- Batch image detection
- Live camera detection
- Motion-triggered detection
- Confidence score display
- Bounding box detection
- Legal/illegal animal classification
- Detection logging
- Frame saving
- FastAPI backend
- Web-based user interface
- Dataset preparation scripts
- Model tuning scripts
- Evaluation results
- Dockerized API setup

---

## Repository Structure

```text
Final-EECE-490-Project/
│
├── README.md
├── Dockerfile
├── requirements.txt
│
├── api/
│   └── main.py
│
├── frontend/
│   └── index.html
│
├── model/
│   └── detect.py
│
├── training/
│   ├── data_splits_training.py
│   └── model_tuning_training.py
│
└── results/
    └── evaluation_results.json
