# WildTrack AI — Wildlife Detection System

---

## Project Title

WildTrack AI

---

## Course

EECE 490 — Introduction to Machine Learning

---

## Project Type

Option A: Application-Oriented Machine Learning System

---

## Developed By

Mamdouh El Zein

Lucien Daher

---

## Demo Video

[Click here to view files on Google Drive](https://drive.google.com/drive/folders/1O-9Wbvuy3f7lR71IX25wXVICt2VA-3G8?usp=drive_link)


## Project Overview

WildTrack AI is an artificial intelligence based wildlife detection system.

The project uses computer vision to detect animals from uploaded images and live camera frames.

The system is built around a trained YOLO object detection model.

The model identifies selected wildlife species.

The system also displays confidence scores for each detection.

The system returns bounding boxes around detected animals.

The system classifies each detected animal as legal or illegal.

This makes the project useful for wildlife monitoring and hunting regulation support.

WildTrack AI combines machine learning, backend development, frontend design, live detection, and model evaluation.

The final system includes a FastAPI backend.

The final system includes a web-based user interface.

The final system includes live camera detection logic.

The final system includes training and tuning scripts.

The final system includes model evaluation results.

The final system includes Docker support for the API.

---

## Project Motivation

Wildlife monitoring can require reviewing many images or video frames manually.

Manual review is slow.

Manual review can be repetitive.

Manual review can also be inaccurate when images are unclear.

Animals may appear at night.

Animals may be small in the frame.

Animals may be hidden by trees, grass, or shadows.

A person may miss detections in large camera-trap datasets.

WildTrack AI helps automate this process.

The system can detect animals faster than manual inspection.

The system can provide consistent detection results.

The system can help users focus on important frames.

---

## Real-World Problem

The real-world problem is the difficulty of monitoring wildlife efficiently.

Wildlife cameras can produce large amounts of image and video data.

Reviewing this data manually takes a lot of time.

A non-automated system does not scale well.

A simple rule-based system may only detect motion or brightness changes.

However, motion alone does not identify the animal species.

Brightness and sharpness rules cannot classify animals reliably.

WildTrack AI addresses this by using object detection.

The model detects the animal and identifies its species.

The system also provides useful metadata for each detection.

---

## Decision Being Automated

The system automates the decision of whether an animal is present in an image or frame.

The system also augments the decision of what species is present.

The system further augments the decision of whether the animal is legal or illegal.

The user still receives the final information clearly.

The system does not replace human judgment completely.

Instead, it supports the user by giving fast and organized detection results.

---

## Why a Non-AI Solution Is Insufficient

A non-AI solution could use simple motion detection.

A non-AI solution could use brightness thresholds.

A non-AI solution could use sharpness or texture heuristics.

These approaches may detect that something changed in the image.

However, they cannot reliably identify animal species.

They may fail in complex backgrounds.

They may fail when lighting changes.

They may fail when leaves or shadows move.

They may fail when animals are partially hidden.

They may also produce many false positives.

Machine learning is more appropriate because it learns visual patterns from data.

The YOLO model can detect animals and classify them into specific species.

It also returns bounding boxes and confidence scores.

---

## Who Could Use This System

Wildlife researchers could use this system.

Environmental monitoring teams could use this system.

Hunting regulation authorities could use this system.

Camera-trap users could use this system.

Farmers or landowners could use this system.

Conservation organizations could use this system.

Students and researchers could also use it as a computer vision prototype.

---

## Main Goal

The main goal of WildTrack AI is to build a practical wildlife detection platform.

The system should detect selected animals accurately.

The system should show results clearly.

The system should support uploaded image detection.

The system should support batch image detection.

The system should support live camera detection.

The system should include a baseline comparison.

The system should include reproducible experiments.

The system should include a running API.

The system should include a minimal but functional user interface.

---

## Animal Classes

The model focuses on five animal classes.

The classes are:

- Deer

- Boar

- Rabbit

- Pheasant

- Jackal

---

## Legal Classification

Each animal class is mapped to a legal status.

The legal status is returned by the backend.

The legal status is also displayed in the interface.

| Species | Legal Status |
|---|---|
| Deer | Legal |
| Boar | Legal |
| Rabbit | Legal |
| Pheasant | Legal |
| Jackal | Illegal |

---

## Main Features

Wildlife detection using YOLO.

Single image detection.

Batch image detection.

Live camera detection.

Motion-triggered detection.

Confidence score display.

Bounding box detection.

Legal and illegal animal classification.

Detection logging.

Frame saving.

FastAPI backend.

Web-based user interface.

Dataset preparation scripts.

Dataset tuning scripts.

Model training workflow.

Model evaluation results.

Dockerized API setup.

Organized GitHub repository.

---

## Repository Structure

```text
Final-EECE-490-Project/
│
├── README.md
├── Dockerfile
├── requirements.txt
├── best.pt
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
```

---

## Folder Explanation

The project is separated into folders for clarity.

Each folder has a specific role.

This makes the repository easier to read.

This also makes the project look more professional.

---

## README.md

The README file explains the project.

It describes the goal of the system.

It explains the repository structure.

It explains the API.

It explains the frontend.

It explains the model.

It explains the training process.

It explains the evaluation results.

It explains how to run the system.

---

## Dockerfile

The Dockerfile is used to containerize the API.

It defines the environment needed to run the FastAPI backend.

It installs the required dependencies.

It exposes the API port.

It runs the API using Uvicorn.

This supports the Dockerized API requirement.

---

## requirements.txt

The requirements file lists the Python packages needed by the project.

It allows another user to install the required dependencies.

It helps make the project easier to reproduce.

It is also used by the Dockerfile.

---

## best.pt

The best.pt file is the trained YOLO model weights file.

The API loads this file to perform detection.

The model file should be placed in the root of the repository if the API uses:

```python
MODEL_PATH = "best.pt"
```

If the model is placed somewhere else, the path in the code must be updated.

---

## api Folder

The api folder contains the backend application.

The backend is built using FastAPI.

The backend receives image uploads.

The backend preprocesses images.

The backend runs the YOLO model.

The backend returns detection results as JSON.

---

## api/main.py

The main.py file is the main backend file.

It creates the FastAPI application.

It loads the YOLO model at startup.

It defines the API endpoints.

It handles image upload detection.

It handles batch image detection.

It returns animal species, confidence score, bounding box, timestamp, and legal status.

---

## API Endpoints

The API includes several endpoints.

The main endpoints are:

- /health

- /classes

- /detect

- /detect/batch

---

## /health Endpoint

The /health endpoint checks whether the API is running.

It also confirms whether the model is loaded.

This endpoint is useful for testing the backend.

It can be opened in the browser.

It can also be tested using Postman or curl.

---

## /classes Endpoint

The /classes endpoint returns the animal classes.

It also returns the legal status mapping.

This helps explain which species the model can detect.

This endpoint can also support the frontend interface.

---

## /detect Endpoint

The /detect endpoint detects animals in one uploaded image.

The user sends one image file.

The backend preprocesses the image.

The YOLO model runs inference.

The backend returns the prediction results.

This is the main endpoint for image detection.

---

## /detect/batch Endpoint

The /detect/batch endpoint detects animals in multiple uploaded images.

The user can upload several images at once.

The backend processes each image.

The model runs inference on each image.

The response includes results for all uploaded images.

This is useful for testing many images quickly.

---

## Image Preprocessing

The backend preprocesses images before inference.

The image is decoded.

The image is resized.

The image is normalized.

CLAHE normalization is applied.

This helps make inference more consistent with the training pipeline.

Preprocessing is important because the model performs better when input images match the training conditions.

---

## Detection Output

The detection output includes the image name.

It includes whether an animal is present.

It includes the detected species.

It includes the confidence score.

It includes the bounding box coordinates.

It includes the legal status.

It includes the timestamp.

It includes the latency in milliseconds.

It includes whether the frame is empty.

---

## Example API Output

```json
{
  "image": "example.jpg",
  "animal_present": true,
  "detections": [
    {
      "species": "deer",
      "confidence": 0.91,
      "bbox": [120.5, 80.2, 430.8, 390.4],
      "legal": "legal"
    }
  ],
  "timestamp": "2026-04-30T12:00:00",
  "latency_ms": 45.2,
  "empty_frame": false
}
```

---

## frontend Folder

The frontend folder contains the user interface.

This folder holds the visual part of the system.

The main file is index.html.

The interface allows users to interact with the project without using command-line tools.

---

## frontend/index.html

The index.html file is the main interface of WildTrack AI.

It allows users to upload images.

It allows users to run detection.

It displays uploaded image previews.

It displays the detection results.

It shows the detected species.

It shows the confidence score.

It shows the legal or illegal status.

It uses a clean wildlife-themed design.

---

## Interface Purpose

The interface makes the project easier to use.

Users do not need to send API requests manually.

Users can upload images visually.

Users can see the results clearly.

The interface makes the system feel like a complete application.

---

## Interface Features

The interface includes a project title.

The interface includes an upload area.

The interface includes a detection button.

The interface includes image preview cards.

The interface includes result cards.

The interface includes confidence information.

The interface includes legal status badges.

The interface includes a clean forest-inspired visual theme.

---

## model Folder

The model folder contains model-related detection logic.

The main file inside this folder is detect.py.

This file is mainly used for live camera detection.

It is different from the API image upload detection.

---

## model/detect.py

The detect.py file handles live detection.

It uses camera input.

It waits for motion.

When motion is detected, it opens a live detection window.

During that window, YOLO runs continuously.

The system saves frames when detections occur.

The system logs detection events.

The system tracks whether the frame contains animals.

---

## Live Camera Detection

The live camera detection system supports real-time monitoring.

It is useful for a camera-based setup.

The camera stays active.

The system checks for motion.

Detection only becomes active when motion is detected.

This reduces unnecessary processing.

---

## Motion-Triggered Detection

Motion-triggered detection is a key feature.

The system compares frames to detect movement.

If movement passes a threshold, a detection window opens.

During that window, YOLO runs on the camera frames.

This makes the system more efficient.

This also makes the system more realistic for edge deployment.

---

## Event Counting

The live detection system avoids counting the same animal repeatedly.

A continuous animal appearance is counted once.

A new event is counted when an animal appears after an empty frame.

This produces more meaningful detection counts.

---

## Detection Logging

The system logs new detection events.

The log includes the timestamp.

The log includes the detected species.

The log includes the confidence score.

The log includes the legal status.

This creates a permanent record of wildlife activity.

---

## Frame Saving

The live detection system can save frames.

Saved frames can be reviewed later.

Saved frames can be used in reports.

Saved frames can be used in demonstrations.

This supports project explainability and validation.

---

## training Folder

The training folder contains the experiment scripts.

These scripts show how the model was trained.

They show how the dataset was prepared.

They show how the data was balanced.

They show how evaluation was performed.

This folder supports reproducible experiments.

---

## training/data_splits_training.py

This file contains the main training workflow.

It checks GPU availability.

It mounts Google Drive.

It installs Ultralytics.

It copies the dataset.

It updates the dataset configuration.

It trains the YOLO model.

It evaluates the model.

It compares YOLO with a non-AI baseline.

It saves evaluation results.

---

## training/model_tuning_training.py

This file contains dataset tuning logic.

It analyzes class distribution.

It balances the dataset.

It downsamples overrepresented classes.

It augments underrepresented classes.

It adds empty frames.

It applies image normalization.

It prepares the final balanced dataset.

---

## results Folder

The results folder contains evaluation outputs.

The main file is evaluation_results.json.

This file stores the final model evaluation numbers.

It includes overall model performance.

It includes per-class performance.

It helps make the results transparent.

---

## results/evaluation_results.json

The evaluation_results.json file contains the final evaluation data.

The model is named forest_lens_v2.

The model was evaluated on a balanced test set of 540 images.

The file includes precision, recall, mAP50, and mAP50-95.

It also includes separate results for each animal class.

---

## Final Model

The final model name is:

```text
forest_lens_v2
```

The test set used is:

```text
balanced test set with 540 images
```

---

## Overall Evaluation Results

| Metric | Score |
|---|---:|
| Precision | 0.915 |
| Recall | 0.921 |
| mAP50 | 0.948 |
| mAP50-95 | 0.747 |

---

## Meaning of Overall Results

The model achieved 91.5% precision.

This means that when the model predicted an animal, it was correct most of the time.

The model achieved 92.1% recall.

This means that the model detected most of the animals that were actually present.

The model achieved 94.8% mAP50.

This shows strong object detection performance at a 50% overlap threshold.

The model achieved 74.7% mAP50-95.

This is a stricter metric and is harder to score highly on.

---

## Per-Class Evaluation Results

| Class | Precision | Recall | mAP50 | mAP50-95 |
|---|---:|---:|---:|---:|
| Deer | 0.889 | 0.899 | 0.918 | 0.739 |
| Boar | 0.868 | 0.866 | 0.914 | 0.685 |
| Rabbit | 0.896 | 0.943 | 0.953 | 0.654 |
| Jackal | 0.971 | 0.903 | 0.966 | 0.824 |
| Pheasant | 0.950 | 0.991 | 0.988 | 0.834 |

---

## Results Discussion

The model performs strongly overall.

Pheasant is the strongest class based on mAP50.

Pheasant also has very high recall.

Jackal has the highest precision.

Boar is the most challenging class.

Boar has the lowest precision and recall among the five classes.

Rabbit has strong recall but lower mAP50-95 compared to some other classes.

The results show that the model works well but still has room for improvement.

---

## Evaluation Metrics

Precision measures how many predicted detections were correct.

Recall measures how many actual animals were detected.

mAP50 measures detection performance at a 50% bounding box overlap threshold.

mAP50-95 measures performance across stricter overlap thresholds.

mAP50-95 is harder than mAP50.

A strong model should have good precision and recall.

A strong model should also have a high mAP score.

---

## Non-AI Baseline

The project includes a non-AI baseline.

The baseline uses image processing methods.

It checks visual properties such as brightness and sharpness.

It can estimate whether a frame contains useful visual content.

However, it cannot reliably classify animal species.

It cannot provide accurate bounding boxes like YOLO.

It is less flexible than the ML-based approach.

The baseline is included to show why machine learning is useful.

---

## Machine Learning Approach

The main ML approach uses YOLO.

YOLO is an object detection model.

It detects objects in images quickly.

It returns bounding boxes.

It returns confidence scores.

It returns class labels.

This makes YOLO suitable for wildlife detection.

---

## Why YOLO Was Chosen

YOLO is fast.

YOLO is accurate for object detection.

YOLO can detect multiple objects in one image.

YOLO supports real-time use cases.

YOLO is widely used in computer vision projects.

YOLO works well with both images and video frames.

This makes it a good fit for WildTrack AI.

---

## Dataset Preparation

The dataset was organized for YOLO training.

The dataset was split into training, validation, and test sets.

Each image has a matching label file.

The labels follow YOLO format.

The dataset includes animal images.

The dataset also includes empty frames.

Empty frames help reduce false positives.

---

## Dataset Balancing

Class balancing was used to improve performance.

Some animal classes had more examples than others.

Overrepresented classes were reduced.

Underrepresented classes were increased.

This helps the model avoid bias toward common classes.

This improves fairness across species.

---

## Data Augmentation

Data augmentation was used to increase dataset variety.

The augmentation methods included brightness changes.

The augmentation methods included contrast changes.

The augmentation methods included noise addition.

The augmentation methods included rotation.

The augmentation methods included horizontal flipping.

These transformations help the model generalize better.

---

## Empty Frames

Empty frames are images with no animals.

They are important for real-world detection.

Without empty frames, the model may create false detections.

Adding empty frames teaches the model what no-animal images look like.

This improves the reliability of the system.

---

## Image Normalization

Image normalization was used during preparation.

CLAHE normalization was applied.

CLAHE helps improve lighting consistency.

This is useful because wildlife images can have different lighting conditions.

Some images may be too bright.

Some images may be too dark.

Normalization helps reduce this variation.

---

## System Workflow

The user opens the interface.

The user uploads an image.

The frontend sends the image to the backend.

The backend preprocesses the image.

The YOLO model runs inference.

The backend collects predictions.

The backend returns results.

The frontend displays the results.

The user sees the species, confidence score, bounding box, and legal status.

---

## Live Detection Workflow

The camera starts.

The system waits for motion.

Motion is detected.

A detection window opens.

YOLO runs on live frames.

Animals are detected.

Frames may be saved.

Detection events are logged.

The system returns to idle after the window ends.

---

## Responsible ML Considerations

The project considers privacy.

The project considers robustness.

The project considers bias.

The project considers explainability.

These are important for responsible machine learning systems.

---

## Privacy

Wildlife cameras may accidentally capture humans.

The system should avoid storing unnecessary human information.

If human detection is included, privacy alerts should be handled carefully.

The project should focus on wildlife and not personal surveillance.

---

## Robustness

The model may perform differently in new environments.

Different lighting can affect accuracy.

Different camera angles can affect accuracy.

Bad weather can affect accuracy.

Blurry images can affect accuracy.

The system should be tested on diverse real-world examples.

---

## Bias

A model can become biased if one class has more data than another.

Dataset balancing helps reduce this issue.

Augmentation also helps improve class coverage.

Per-class evaluation helps identify weaker classes.

Boar is currently the most challenging class.

This shows where future improvement should focus.

---

## Explainability

The system provides bounding boxes.

The system provides confidence scores.

The system provides class labels.

These outputs help users understand the model prediction.

The interface also displays the legal status clearly.

This makes the system easier to interpret.

---

## Technologies Used

Python

FastAPI

Uvicorn

YOLOv8

Ultralytics

OpenCV

NumPy

Pillow

HTML

CSS

JavaScript

Google Colab

Raspberry Pi Camera

Picamera2

Libcamera

Docker

GitHub

---

## Python Dependencies

The main Python dependencies include:

```text
fastapi
uvicorn[standard]
python-multipart
ultralytics
opencv-python-headless
numpy
pillow
```

These dependencies should be listed in requirements.txt.

---

## How to Run Locally

First, install the dependencies.

```bash
pip install -r requirements.txt
```

Then run the FastAPI backend.

```bash
uvicorn api.main:app --reload
```

The API should run at:

```text
http://127.0.0.1:8000
```

---

## How to Test the API

Open the health endpoint.

```text
http://127.0.0.1:8000/health
```

If the API is running correctly, it should return a status response.

You can also test the API using Postman.

You can also test it using curl.

You can also connect it to the frontend.

---

## How to Open the Interface

Open the frontend folder.

Open index.html in a browser.

Upload an image.

Run detection.

View the detected species.

View the confidence score.

View the legal status.

---

## Dockerized API

The project includes Docker support.

Docker packages the backend into a container.

This helps the project run in a consistent environment.

Docker also supports deployment to cloud platforms.

---

## Build the Docker Image

Run this command from the root of the repository.

```bash
docker build -t wildtrack-ai .
```

---

## Run the Docker Container

Run this command.

```bash
docker run -p 8000:8000 wildtrack-ai
```

Then open:

```text
http://localhost:8000/health
```

---

## Reproducible Experiments

The project includes reproducible experiment scripts.

These scripts are stored in the training folder.

They show how the dataset was prepared.

They show how the model was trained.

They show how the model was evaluated.

They also show the baseline comparison.

This supports the reproducibility requirement.

---

## Production Thinking

The project separates data processing, model logic, and serving.

The training folder handles experiments.

The model folder handles live detection logic.

The api folder handles serving.

The frontend folder handles user interaction.

The results folder stores evaluation outputs.

This separation makes the project easier to maintain.

---

## Failure Cases

The model may fail when the animal is too small.

The model may fail when the animal is blurry.

The model may fail when the animal is partially hidden.

The model may fail in very dark images.

The model may fail in unusual camera angles.

The model may confuse visually similar animals.

The model may create false positives in complex backgrounds.

---

## Limitations

The model only detects five animal classes.

The model cannot detect animals outside the trained classes.

The legal classification is fixed and predefined.

The live detection system depends on camera hardware.

The API depends on the trained model file.

Performance may change with new environments.

The system should not be used as the only source for legal decisions.

---

## Future Improvements

Add more animal classes.

Improve low-light detection.

Add night-vision support.

Add a database for detection history.

Add a dashboard for analytics.

Add user authentication.

Deploy the API to the cloud.

Add real-time alerts.

Add email or SMS notifications.

Add GPS location support.

Add automatic report generation.

Improve frontend responsiveness.

Improve model performance on boar.

Add more diverse training images.

Add more edge-device testing.

---

## Possible Dashboard Features

Total detection count.

Most detected species.

Legal versus illegal detections.

Detection history table.

Saved frame gallery.

Detection trends over time.

Species filters.

Date filters.

Legal status filters.

Downloadable reports.

---

## Practical Applications

Wildlife monitoring.

Camera-trap analysis.

Environmental observation.

Hunting regulation support.

Animal activity tracking.

Outdoor surveillance support.

Research assistance.

Automated image review.

Edge-based wildlife detection.

---

## Final Deliverables

This project includes a well-structured GitHub repository.

This project includes reproducible experiments.

This project includes a running API.

This project includes a final presentation.

The project also includes a Dockerized API setup.

The project includes a minimal functional user interface.

The project includes baseline and ML-based evaluation.

---

## Summary

WildTrack AI is a complete wildlife detection system.

It uses YOLO for animal detection.

It provides a FastAPI backend.

It includes a clean frontend interface.

It supports uploaded image detection.

It supports batch image detection.

It supports live camera detection.

It includes motion-triggered detection.

It logs detection events.

It classifies animals as legal or illegal.

It includes reproducible training and tuning scripts.

It includes final evaluation results.

The final model achieved strong performance on a balanced test set of 540 images.

The project demonstrates how machine learning can support practical wildlife monitoring.

---

## Authors

Mamdouh El Zein

Lucien Daher

---

## Final Note

This repository represents the full WildTrack AI workflow.

It includes data preparation.

It includes model training.

It includes model tuning.

It includes model evaluation.

It includes backend serving.

It includes frontend interaction.

It includes live detection support.

It includes Dockerized deployment support.

The organized structure makes the project easier to read, test, present, and improve.

WildTrack AI shows how artificial intelligence can be used to build useful real-world detection systems.
