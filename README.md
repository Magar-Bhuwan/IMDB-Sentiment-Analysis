# 🎬 IMDB Sentiment Analysis

A Natural Language Processing (NLP) project that classifies IMDB movie reviews as **Positive 😊** or **Negative 😞** using Machine Learning techniques.

The project combines:

* Data preprocessing and cleaning
* Word2Vec embeddings
* Support Vector Machine (SVM) classification
* Interactive Streamlit web application
* Real-time sentiment prediction

---

## 📌 Project Overview

This project performs sentiment analysis on movie reviews from the IMDB dataset.

The objective is to determine whether a review expresses a **positive** or **negative** opinion.

### Workflow

1. Data preprocessing
2. Text cleaning
3. Word2Vec feature extraction
4. Model training using SVM
5. Real-time prediction using Streamlit

---

## 🚀 Streamlit Web Application

The trained SVM sentiment analysis model is deployed using Streamlit, enabling users to classify movie reviews in real time through an interactive web interface.

### 🌐 Live Demo

Add your deployed Streamlit URL here:

```text
https://your-streamlit-app.streamlit.app
```

---

## 📸 Application Screenshots

### 🏠 Home Page

/media/suko-magar/LocalDisk/ML with Python/Projects/IMDB Sentimental Analysis/Output/Home Page.jpg

---

### ✍️ User Input Page

Users enter a movie review for sentiment prediction.

/media/suko-magar/LocalDisk/ML with Python/Projects/IMDB Sentimental Analysis/Output/User Input_page-0001.jpg

---

### 😊 Positive Sentiment Analysis

Example output for a positive movie review.

!/media/suko-magar/LocalDisk/ML with Python/Projects/IMDB Sentimental Analysis/Output/Positive Sentimental Analysis.jpg

---

### 😞 Negative Sentiment Analysis

Example output for a negative movie review.

/media/suko-magar/LocalDisk/ML with Python/Projects/IMDB Sentimental Analysis/Output/Negative Sentimental Analysis.jpg

---

## 📂 Project Structure

```text
IMDB SENTIMENTAL ANALYSIS/
│
├── IMDB/
│   ├── IMDB_sentiment.ipynb
│   ├── IMDB_Dataset.csv
│   ├── SVM_model.joblib
│   └── Word2Vec_imdb_250.joblib
│
├── Output/
│   ├── Home Page.jpg
│   ├── Negative Sentimental Analysis.jpg
│   ├── Positive Sentimental Analysis.jpg
│   └── User Input_page-0001.jpg
│
├── Streamlit/
│   ├── streamlit_app.py
│   └── utils.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🛠 Technologies Used

### Programming Language

* Python

### Data Analysis

* Pandas
* NumPy

### Natural Language Processing

* NLTK
* Gensim Word2Vec

### Machine Learning

* Scikit-learn
* Support Vector Machine (SVM)

### Deployment

* Streamlit

### Model Persistence

* Joblib

---

## 🔄 Machine Learning Pipeline

### 1. Data Cleaning

* Lowercasing text
* Removing HTML tags
* Removing URLs
* Removing punctuation
* Stopword removal
* Lemmatization

### 2. Feature Engineering

Word2Vec converts movie reviews into dense numerical vector representations.

#### Word2Vec Configuration

* Vector Size: 250
* Architecture: Skip-Gram (`sg=1`)
* Minimum Word Count: 2

### 3. Model Training

Support Vector Machine (SVM) is trained on the generated Word2Vec embeddings.

### 4. Model Evaluation

The model performance is evaluated using:

* Accuracy Score
* Precision
* Recall
* F1 Score
* Confusion Matrix

---

## 📊 Dataset

**IMDB Movie Reviews Dataset**

* 50,000 movie reviews
* Binary sentiment classification
* Positive and Negative labels

Dataset Source:

https://ai.stanford.edu/~amaas/data/sentiment/

---

## 📈 Results

Add your actual model performance metrics below.

| Metric    | Score |
| --------- | ----- |
| Accuracy  | XX%   |
| Precision | XX%   |
| Recall    | XX%   |
| F1 Score  | XX%   |

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Magar-Bhuwan/IMDB-Sentiment-Analysis.git
cd IMDB-Sentiment-Analysis
```

Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Streamlit Application

```bash
streamlit run Streamlit/streamlit_app.py
```

The application will start at:

```text
http://localhost:8501
```

---

## 🔮 Future Improvements

* BERT-based sentiment classification
* Deep Learning models (LSTM, GRU)
* Confidence score visualization
* Docker deployment
* Cloud deployment
* REST API integration

---

## 👨‍💻 Author

**Bhuwan Magar**

GitHub: https://github.com/Magar-Bhuwan

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
