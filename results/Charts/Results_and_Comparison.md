# Results Charts Explanation

This folder contains the evaluation charts for the WildTrack AI YOLO-based wildlife detection model. These charts help explain how well the model detects each animal class and where it makes mistakes.

## Classes Evaluated

The model was evaluated on the following classes:

- Deer
- Boar
- Rabbit
- Jackal
- Pheasant
- Background

---

## 1. Confusion Matrix

The confusion matrix shows how many predictions were correct and incorrect for each class.

The diagonal values represent correct predictions. For example, the model correctly detected:

- 119 deer
- 137 boars
- 116 rabbits
- 99 jackals
- 114 pheasants

Most of the strongest values are on the diagonal, which means the model is generally predicting the correct animal class.

The off-diagonal values show mistakes. For example, some true animals were missed and predicted as background, or some background areas were predicted as animals.

---

## 2. Normalized Confusion Matrix

The normalized confusion matrix shows the same information as the confusion matrix, but as percentages instead of raw counts.

This makes it easier to compare performance between classes.

The model achieved strong class-level detection performance:

- Deer: 0.89
- Boar: 0.86
- Rabbit: 0.94
- Jackal: 0.89
- Pheasant: 1.00

This means the model performed especially well on pheasant and rabbit, while boar was slightly harder for the model compared to the other classes.

---

## 3. Precision-Recall Curve

The precision-recall curve shows the balance between precision and recall for each class.

Precision means: when the model predicts an animal, how often it is correct.

Recall means: out of all actual animals, how many the model successfully finds.

The overall result was:

**mAP@0.5 = 0.948**

This is a strong result and means the model performs well at detecting wildlife at an IoU threshold of 0.5.

Per-class AP scores:

- Deer: 0.918
- Boar: 0.914
- Rabbit: 0.953
- Jackal: 0.966
- Pheasant: 0.988

Pheasant had the highest performance, while boar and deer were slightly lower but still strong.

---

## 4. Recall-Confidence Curve

The recall-confidence curve shows how recall changes when the confidence threshold increases.

At low confidence thresholds, the model catches more animals, so recall is high. However, as the threshold increases, the model becomes more strict and may miss more animals, causing recall to decrease.

This chart helps decide how strict the detection system should be.

---

## 5. Precision-Confidence Curve

The precision-confidence curve shows how precision changes as the confidence threshold increases.

As confidence increases, precision usually improves because the model only keeps predictions it is very sure about.

In this model, precision reaches very high levels at high confidence thresholds. However, using a very high threshold can also reduce recall because some correct detections may be ignored.

---

## 6. F1-Confidence Curve

The F1-confidence curve shows the best balance between precision and recall.

The model reached its best overall F1 score at approximately:

**F1 = 0.92 at confidence = 0.241**

This means a confidence threshold around **0.24** gives the best balance between catching animals and avoiding wrong predictions.

For the final interface, a higher threshold can be used if the goal is to show only highly confident detections. However, if the goal is to avoid missing animals, a lower threshold is better.

---

## Overall Result

The evaluation results show that WildTrack AI performs well across all wildlife classes. The model achieved strong detection accuracy, with high mAP@0.5 and strong precision-recall performance.

The main limitation is that some animals can still be confused with background or missed when the confidence threshold is too high. This can be improved in the future by adding more training images, especially for difficult lighting conditions, partial animal visibility, and background-heavy scenes.
