# Face Mask Detection Using CNN

## Project Overview

This project uses a Convolutional Neural Network (CNN) to classify
images into two categories:

-   **With Mask**
-   **Without Mask**

The notebook loads training and testing images, resizes them to
`150 × 150` pixels, trains a CNN model, evaluates its performance, and
predicts the class of individual images.

## Technologies and Libraries

-   Python
-   NumPy
-   Pandas
-   Matplotlib
-   TensorFlow
-   Keras
-   scikit-image

## Dataset Structure

The notebook expects the dataset to be stored in Google Drive with the
following folder structure:

``` text
Maskdata/
├── with_mask/
└── without_mask/

Maskdatatest/
├── with_mask/
└── without_mask/
```

-   `Maskdata` contains the training images.
-   `Maskdatatest` contains the testing images.
-   The class names are used as labels when loading the images.

**Note:** The dataset itself is not included in this repository. Update
the folder paths in the notebook if your dataset is stored elsewhere.

## Project Workflow

1.  Mount Google Drive in Google Colab.
2.  Load the training and testing image folders.
3.  Read each image and resize it to `150 × 150 × 3`.
4.  Convert the image data and labels into NumPy arrays.
5.  Build a CNN using Keras.
6.  Compile the model with the Adam optimizer and sparse categorical
    cross-entropy loss.
7.  Train the model for 100 epochs with a batch size of 100.
8.  Evaluate the model on the test dataset.
9.  Display predictions for test images and predict the class of
    individual images.

## CNN Architecture

The Sequential CNN model contains:

  Layer          Configuration
  -------------- -----------------------------------------------------
  Conv2D         32 filters, 3 × 3 kernel, ReLU activation
  MaxPooling2D   2 × 2 pool size
  Flatten        Converts feature maps into a one-dimensional vector
  Dense          100 units, ReLU activation
  Dense          50 units, ReLU activation
  Output Dense   2 units, Softmax activation

## Model Training

-   **Optimizer:** Adam
-   **Loss function:** Sparse categorical cross-entropy
-   **Metric:** Accuracy
-   **Epochs:** 100
-   **Batch size:** 100
-   **Input image size:** 150 × 150 × 3

## Evaluation

The notebook's recorded test evaluation shows:

-   **Test accuracy:** approximately 96.08%
-   **Test loss:** approximately 0.3164

Results may vary when the model is trained again, depending on the
dataset and training environment.

## Class Labels

The notebook sorts the class folders alphabetically. The resulting label
mapping is:

  Label   Class
  ------- --------------
  0       With Mask
  1       Without Mask

## Running the Project

1.  Open `MaskvsNoMask.ipynb` in Google Colab.
2.  Upload the dataset to Google Drive using the folder structure shown
    above.
3.  Check that the dataset paths in the notebook match your Google Drive
    folders.
4.  Run the notebook cells in order.

## Limitations

-   The notebook uses fixed Google Drive paths that may need to be
    changed.
-   The model is trained and evaluated using the provided dataset;
    performance on new real-world images may differ.
-   This is an image-classification project and should not be treated as
    a reliable safety or compliance system.
