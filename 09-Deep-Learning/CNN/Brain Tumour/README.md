# Brain Tumor Classification Using CNN

## Project Overview

This project uses a Convolutional Neural Network (CNN) to classify brain MRI images into four categories:

- **Glioma**
- **Meningioma**
- **No Tumor**
- **Pituitary**

The model is implemented in Python using TensorFlow/Keras. The notebook loads MRI images, resizes them to a fixed size, trains a CNN, evaluates it on a separate test set, and displays sample predictions.

> **Disclaimer:** This is an educational machine-learning project, not a medical diagnostic tool. Its predictions must not be used to make healthcare decisions.

## Dataset

The notebook expects the dataset to be arranged in the following directory structure:

```text
Brain_Tumor/
├── Training/
│   ├── glioma/
│   ├── meningioma/
│   ├── notumor/
│   └── pituitary/
└── Testing/
    ├── glioma/
    ├── meningioma/
    ├── notumor/
    └── pituitary/
```

### Image counts used

| Class | Training images | Testing images |
|---|---:|---:|
| Glioma | 1,287 | 300 |
| Meningioma | 1,319 | 306 |
| No Tumor | 1,574 | 405 |
| Pituitary | 1,349 | 300 |
| **Total** | **5,529** | **1,311** |

## Workflow

1. Mount Google Drive in Google Colab.
2. Read the training and testing folders.
3. Sort the class folder names to keep the label order consistent.
4. Load the MRI images and resize each image to **150 × 150 pixels** with one channel.
5. Convert the image collections and labels into NumPy arrays.
6. Build and compile the CNN model.
7. Train the model for **100 epochs** with a batch size of **100**.
8. Evaluate the trained model on the test dataset.
9. Generate predictions and compare predicted labels with actual labels.

## Model Architecture

The notebook defines the following Sequential CNN architecture:

| Layer | Configuration |
|---|---|
| Convolutional layer | 32 filters, 3 × 3 kernel, ReLU activation |
| Max pooling | 2 × 2 |
| Flatten | Converts feature maps into a 1D vector |
| Dense | 100 units, ReLU activation |
| Dense | 50 units, ReLU activation |
| Output | 4 units, Softmax activation |

**Compilation settings:**
- Optimizer: Adam
- Loss: Sparse categorical cross-entropy
- Metric: Accuracy

## Results

The saved notebook output shows the following test evaluation:

- **Test accuracy:** approximately **95.35%**
- **Test loss:** approximately **0.4138**

These are the results recorded in the notebook output. Results may vary if the model is trained again.

## Requirements

The notebook uses:

- Python
- TensorFlow / Keras
- NumPy
- Pandas
- Matplotlib
- scikit-image

In a notebook environment, install any missing packages with:

```bash
pip install tensorflow numpy pandas matplotlib scikit-image
```

## How to Run

1. Open `Brain_tumour.ipynb` in [Google Colab](https://colab.research.google.com/) or a compatible Jupyter environment.
2. Place the dataset in Google Drive using the folder structure shown above.
3. If your dataset is stored elsewhere, update the dataset paths in the notebook.
4. Run the notebook cells in order, including the Google Drive mounting cell.
5. Review the training output, test evaluation, and sample predictions.

## Repository Contents

```text
.
├── Brain_tumour.ipynb
└── README.md
```

The notebook contains the data-loading, preprocessing, model-building, training, evaluation, and prediction code.

## Limitations

- The notebook uses a specific Google Drive folder path; it must be changed if the dataset is stored in another location.
- The notebook's displayed accuracy is an evaluation result for this dataset split and does not establish clinical reliability.
- This project does not provide a medical diagnosis.
