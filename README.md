# WildTrack AI — Wildlife Detection System

---

## Project Title

WildTrack AI

---

## Project Type

Final EECE 490 Project

---

## Developed By

Mamdouh El Zein

Lucien Daher

---

## Project Overview

WildTrack AI is an artificial intelligence based wildlife detection system.

The system uses computer vision to detect animals from images and live camera frames.

The project is built around a trained YOLO object detection model.

The model identifies selected wildlife species.

The system also classifies the detected animal as legal or illegal.

This makes the project useful for wildlife monitoring and hunting regulation support.

The system combines machine learning, backend development, frontend design, and live camera detection.

The project includes an API, a user interface, live detection logic, and training scripts.

The main goal is to create a practical and organized wildlife detection platform.

---

## Purpose of the Project

The purpose of WildTrack AI is to automate wildlife detection.

In many monitoring systems, users must manually check camera footage or uploaded images.

This process can take a lot of time.

It can also be inaccurate if the user misses an animal in the frame.

WildTrack AI solves this problem by using AI to detect animals automatically.

The system receives an image or camera frame.

It processes the image.

It runs the YOLO model.

It returns the detected animal species.

It shows the confidence score.

It also shows whether the animal is legal or illegal.

This makes the system useful for real-world observation tasks.

---

## Main Idea

The main idea of the project is simple.

A user provides an image or camera input.

The system detects whether an animal is present.

If an animal is detected, the system identifies the species.

The system then displays the result clearly.

The result includes the animal name.

The result includes the confidence score.

The result includes the bounding box.

The result includes the timestamp.

The result includes the legal status.

This creates a full detection workflow from input to result.

---

## Detected Animal Classes

The model focuses on five animal classes.

These classes are:

- Deer

- Boar

- Rabbit

- Pheasant

- Jackal

---

## Legal Classification

The system includes a legal status for each animal.

Deer is classified as legal.

Boar is classified as legal.

Rabbit is classified as legal.

Pheasant is classified as legal.

Jackal is classified as illegal.

This legal classification is used in the output.

It helps the user quickly understand the status of the detected animal.

---

## Main Features

Wildlife detection using YOLO.

Image upload detection.

Batch image detection.

Live camera detection.

Motion-triggered detection.

Confidence score display.

Bounding box detection.

Legal and illegal animal classification.

Detection logging.

Frame saving.

Simple web-based user interface.

FastAPI backend.

Organized project folder structure.

Training and tuning scripts.

Dataset balancing.

Dataset augmentation.

Model evaluation.

---

## Project Structure

The project is organized into different folders.

Each folder has a clear purpose.

This makes the repository easier to understand.

It also makes the project look more professional.

---

## Repository Layout

Final-EECE-490-Project/

    README.md

    api/

        main.py

    frontend/

        index.html

    model/

        detect.py

    training/

        data_splits_training.py

        model_tuning_training.py

---

## README.md

The README file explains the project.

It describes the goal of the system.

It explains the repository structure.

It lists the main features.

It explains how the system works.

It also explains how to run the project.

This file helps anyone understand the project quickly.

---

## api Folder

The api folder contains the backend of the system.

The backend is built using FastAPI.

FastAPI receives requests from the frontend.

It processes uploaded images.

It runs the YOLO detection model.

It returns the detection results as structured data.

The main backend file is main.py.

---

## api/main.py

The main.py file is the main FastAPI application.

It defines the API routes.

It loads the YOLO model when the server starts.

It receives uploaded images from the user.

It preprocesses the images.

It runs the model on the processed image.

It returns the detection result.

It also supports batch detection.

This file is one of the most important files in the project.

---

## Backend Responsibilities

The backend handles the detection logic for uploaded images.

It checks if the model is loaded.

It receives image files.

It decodes the image.

It resizes the image.

It applies preprocessing.

It sends the processed image to the YOLO model.

It collects the model predictions.

It formats the output.

It sends the response back to the frontend.

---

## API Endpoints

The backend includes several useful endpoints.

The health endpoint checks if the API is working.

The classes endpoint returns the available animal classes.

The detect endpoint detects animals in one image.

The batch detect endpoint detects animals in multiple images.

These endpoints make the backend organized and easy to test.

---

## /health Endpoint

The /health endpoint checks the API status.

It tells the user if the backend is running.

It also shows whether the model is loaded.

This is useful for testing.

It helps confirm that the backend is ready before running detection.

---

## /classes Endpoint

The /classes endpoint returns the animal classes.

It also returns the legal status of each class.

This helps the frontend know what animals the model can detect.

It also helps explain the classification system.

---

## /detect Endpoint

The /detect endpoint is used for single image detection.

The user uploads one image.

The backend preprocesses the image.

The YOLO model detects animals in the image.

The backend returns the detection results.

This is the main detection endpoint.

---

## /detect/batch Endpoint

The /detect/batch endpoint is used for multiple images.

The user can upload several images at once.

The backend processes each image.

The model runs detection on each image.

The backend returns a list of results.

This feature is useful for testing many images quickly.

---

## Image Preprocessing

The backend preprocesses the image before detection.

The image is decoded.

The image is resized to 640 by 640.

CLAHE normalization is applied.

This preprocessing helps match the training pipeline.

It can improve consistency between training and inference.

---

## Detection Output

The system returns useful detection information.

The output includes the image name.

The output includes whether an animal is present.

The output includes the detected species.

The output includes the confidence score.

The output includes the bounding box.

The output includes the legal status.

The output includes the timestamp.

The output includes the inference latency.

---

## frontend Folder

The frontend folder contains the user interface.

The main file inside this folder is index.html.

This file is the visual part of the project.

It is what users interact with.

It allows users to upload images.

It allows users to start detection.

It displays the detection results.

It makes the project easier to use.

---

## frontend/index.html

The index.html file is the main interface of WildTrack AI.

It includes the page structure.

It includes the styling.

It includes the upload section.

It includes the detection button.

It includes the result display area.

It shows the detected species.

It shows the confidence score.

It shows the legal or illegal label.

It is designed with a forest-themed visual style.

---

## Interface Purpose

The interface makes the system user-friendly.

Instead of using only code or API tools, users can interact visually.

They can upload images through the webpage.

They can view results clearly.

They can understand the detection output without needing technical knowledge.

This improves the overall usability of the project.

---

## Interface Features

The interface includes a project title.

It includes an upload area.

It includes image preview functionality.

It includes detection controls.

It includes result cards.

It includes confidence indicators.

It includes legal status labels.

It includes styling for a professional appearance.

It gives the project a complete application feel.

---

## model Folder

The model folder contains the model-related detection logic.

The main file inside this folder is detect.py.

This file is used for live camera detection.

It is different from the API detection file.

The API handles uploaded images.

The detect.py file handles live camera frames.

---

## model/detect.py

The detect.py file handles motion-triggered live detection.

It uses a camera input.

It stays idle until motion is detected.

When motion is detected, it opens a live detection window.

During that window, YOLO runs continuously.

The system checks for animals in the live frames.

It saves frames if detections occur.

It logs detection events.

This file supports real-time wildlife monitoring.

---

## Live Detection Concept

The live detection system does not run detection all the time.

Instead, it waits for motion.

This saves processing power.

When motion is detected, the system becomes active.

It opens a short detection period.

During this period, the model checks for animals.

This makes the live system more efficient.

---

## Motion-Triggered Detection

Motion-triggered detection is one of the key parts of the project.

The system compares frames to detect movement.

If the movement passes a threshold, the live detection starts.

The system then runs YOLO during the detection window.

This allows the system to focus only on important moments.

---

## Detection Logging

The live detection file includes logging.

When a new animal detection event occurs, the system writes it to a log file.

The log includes the timestamp.

The log includes the detected species.

The log includes the confidence score.

The log includes the legal status.

This creates a record of animal activity.

---

## Event Counting

The system avoids counting the same animal repeatedly.

If the same animal stays in the frame, it is counted once.

A new detection event is counted when an animal appears after an empty frame.

This makes the detection count more meaningful.

It prevents repeated counting of the same continuous animal appearance.

---

## Frame Saving

The live detection system can save detected frames.

When an animal is detected, the annotated frame can be saved.

This allows users to review detections later.

Saved frames can also be used for reports or demonstrations.

---

## training Folder

The training folder contains the training and tuning files.

These files explain how the model was prepared.

They include dataset processing.

They include class balancing.

They include augmentation.

They include YOLO training.

They include evaluation.

This folder is important because it shows how the final model was developed.

---

## training/data_splits_training.py

This file comes from the main training notebook.

It includes the training workflow.

It checks GPU availability.

It mounts Google Drive.

It installs Ultralytics.

It copies the dataset.

It updates the dataset configuration.

It trains the YOLO model.

It evaluates the model.

It compares baseline and YOLO results.

It saves evaluation results.

---

## training/model_tuning_training.py

This file focuses on dataset tuning.

It analyzes class distribution.

It balances the dataset.

It downsamples overrepresented classes.

It augments underrepresented classes.

It adds empty frames.

It normalizes images.

It creates a balanced dataset.

It prepares the dataset for better training results.

---

## Dataset Preparation

Dataset preparation is a major part of the project.

The dataset must be organized into training, validation, and testing sets.

Each image must have a matching label file.

The labels follow the YOLO format.

The dataset includes several wildlife classes.

The dataset also includes empty frames.

Empty frames help the model learn when no animal is present.

---

## Class Balancing

The dataset was balanced to improve model performance.

Some animal classes had more images than others.

Overrepresented classes were reduced.

Underrepresented classes were increased through augmentation.

This helps prevent the model from becoming biased toward common classes.

A balanced dataset helps improve fairness across classes.

---

## Data Augmentation

Data augmentation was used to create more training examples.

Images were modified using different techniques.

Brightness changes were applied.

Contrast changes were applied.

Noise was added.

Rotations were applied.

Flipping was used.

These changes help the model generalize better.

---

## Empty Frames

Empty frames are images with no animals.

They are important for reducing false positives.

Without empty frames, the model may detect animals where there are none.

Adding empty frames helps the system learn the difference between animal and non-animal images.

This improves real-world reliability.

---

## Image Normalization

Image normalization was applied during preparation.

CLAHE was used to improve image consistency.

This helps handle lighting differences.

Wildlife images can have different brightness levels.

Some images may be dark.

Some images may be bright.

Normalization helps reduce these variations.

---

## YOLO Model

The project uses a YOLO object detection model.

YOLO is useful for real-time object detection.

It can detect objects quickly.

It returns bounding boxes.

It returns class labels.

It returns confidence scores.

This makes it suitable for wildlife detection.

---

## Why YOLO Was Used

YOLO was selected because it is fast.

It is accurate for object detection tasks.

It works well with images and video frames.

It can detect multiple objects in one image.

It is widely used in computer vision projects.

It is suitable for real-time applications.

---

## Confidence Score

Each detection includes a confidence score.

The confidence score shows how sure the model is.

A higher confidence score means the model is more certain.

The frontend displays this score to the user.

This helps the user understand the reliability of each detection.

---

## Bounding Boxes

The model returns bounding boxes around detected animals.

A bounding box shows where the animal is located in the image.

This helps the user visually confirm the detection.

Bounding boxes are important for object detection systems.

---

## Legal Status Display

The system does more than detect animals.

It also displays legal status.

This feature connects AI detection with practical decision support.

The detected animal is mapped to a legal or illegal label.

This makes the result easier to interpret.

---

## System Workflow

The user opens the interface.

The user uploads an image.

The frontend sends the image to the backend.

The backend preprocesses the image.

The backend sends the image to the YOLO model.

The YOLO model detects animals.

The backend formats the results.

The frontend displays the results.

The user views the species, confidence, and legal status.

---

## Live Detection Workflow

The camera starts.

The system waits for motion.

Motion is detected.

A live detection window opens.

YOLO runs on the live frames.

Animals are detected.

Frames can be saved.

Detection events are logged.

The system returns to idle when the window ends.

---

## Technologies Used

Python

FastAPI

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

---

## Backend Technology

FastAPI is used for the backend.

It provides a simple way to build API routes.

It supports file uploads.

It returns JSON responses.

It works well with machine learning models.

It helps connect the frontend to the YOLO model.

---

## Frontend Technology

The frontend is built with HTML, CSS, and JavaScript.

HTML provides the page structure.

CSS provides the design.

JavaScript connects the interface to the backend.

The interface is styled to match the wildlife theme.

---

## Computer Vision Technology

OpenCV is used for image processing.

It helps decode images.

It helps resize images.

It helps process frames.

It helps with motion detection.

It helps draw bounding boxes.

It is useful for both uploaded images and live camera frames.

---

## Training Environment

Google Colab was used for training.

Colab provides access to GPU resources.

GPU support makes YOLO training faster.

The training scripts mount Google Drive.

The dataset is copied to local Colab storage.

This improves training speed.

---

## How to Run the Backend

Install the required Python packages.

Run the FastAPI server.

Use the backend URL for detection requests.

The backend can be run locally during testing.

The API can be tested using a browser, Postman, or the frontend.

---

## Example Backend Command

pip install -r requirements.txt

uvicorn api.main:app --reload

---

## How to Open the Frontend

Open the frontend folder.

Open index.html in a browser.

Upload an image.

Start detection.

View the result.

---

## Expected Output

The system should show whether an animal is present.

It should show the detected species.

It should show the confidence score.

It should show the legal status.

It should show detection details clearly.

For multiple images, it should show results for each image.

---

## Example Output Fields

Image name

Animal present

Detected species

Confidence score

Bounding box

Legal status

Timestamp

Latency

Empty frame status

---

## Project Strengths

The project has a complete workflow.

It includes training.

It includes tuning.

It includes backend deployment logic.

It includes a frontend interface.

It includes live camera detection.

It includes motion triggering.

It includes legal classification.

It is organized into clear folders.

---

## Practical Applications

Wildlife monitoring

Camera trap analysis

Environmental observation

Hunting regulation support

Animal activity tracking

Research assistance

Automated image review

Outdoor surveillance support

---

## Limitations

The system depends on the quality of the trained model.

Poor image quality can reduce accuracy.

Very dark images can affect detection.

Small or hidden animals may be missed.

The model only detects the classes it was trained on.

The legal classification is based on the predefined mapping.

The live camera version depends on hardware availability.

---

## Future Improvements

Add more animal classes.

Improve the dataset size.

Improve performance in low-light conditions.

Add a database for detection history.

Add user authentication.

Add cloud deployment.

Add a dashboard for analytics.

Add real-time alerts.

Add GPS location support.

Add automatic report generation.

Improve the frontend design further.

---

## Possible Dashboard Improvements

Total detections count.

Most detected species.

Legal versus illegal detection chart.

Detection history table.

Saved frame gallery.

Time-based animal activity graph.

Export detection logs.

Filter by species.

Filter by date.

Filter by legal status.

---

## Testing

The system can be tested using sample wildlife images.

The backend can be tested using the /health endpoint.

The detection endpoint can be tested using image uploads.

The frontend can be tested by uploading images directly.

The live detection file can be tested with a connected camera.

---

## Model Evaluation

The training scripts include model evaluation.

Evaluation helps measure the performance of the model.

Metrics such as precision, recall, F1 score, and mAP can be used.

These metrics help compare the YOLO model with a baseline method.

They also help show how well the model performs on test data.

---

## Baseline Comparison

The project includes a baseline detection approach.

The baseline uses image processing techniques.

The YOLO model is compared with this baseline.

This comparison helps show the benefit of using machine learning.

It also makes the evaluation more meaningful.

---

## Why This Project Matters

Wildlife monitoring can require many images and videos.

Manual review takes time.

AI can reduce this workload.

WildTrack AI shows how computer vision can support real-world monitoring.

The project also connects technical AI work with practical environmental use.

---

## Summary

WildTrack AI is a complete wildlife detection system.

It uses YOLO for animal detection.

It provides a FastAPI backend.

It includes a clean user interface.

It supports uploaded image detection.

It supports batch image detection.

It supports live camera detection.

It includes motion-triggered detection.

It logs animal detection events.

It classifies animals as legal or illegal.

The project demonstrates the use of AI for practical wildlife monitoring.

---

## Authors

Mamdouh El Zein

Lucien Daher

---

## Course

EECE 490

---

## Final Note

This repository represents the full project workflow.

It includes training, tuning, detection, backend logic, frontend interface, and live monitoring support.

The organized folder structure makes the project easier to read, test, and present.

WildTrack AI demonstrates how artificial intelligence can be used to build useful real-world detection systems.
