# Sentiment Analysis using Machine Learning and Deep Learning

## Overview
This project explores sentiment analysis, a key aspect of natural language processing (NLP), aimed at determining the polarity of text data—whether positive, neutral, or negative. Given the surge in digital content across social media, news, and e-commerce platforms, sentiment analysis has become crucial for businesses and organizations to gauge public opinion on products, services, or events. Our approach leverages both traditional machine learning algorithms and advanced deep learning models to automate sentiment analysis, focusing on Twitter data for its diverse and vast user-generated content.

### Team Members
- Pranit Sehgal - *School of Computing & Augmented Intelligence, Arizona State University, Tempe, United States* - pvsehgal@asu.edu
- Bharath Kumar Bandaru - *School of Computing & Augmented Intelligence, Arizona State University, Tempe, United States* - bbandaru@asu.edu
- Karthik Nerella - *School of Computing & Augmented Intelligence, Arizona State University, Tempe, United States* - knerell2@asu.edu
- Hari Chandana Guddeti - *School of Computing & Augmented Intelligence, Arizona State University, Tempe, United States* - hguddeti@asu.edu


## Problem Statement
Sentiment analysis identifies and categorizes opinions expressed in text data to understand customer sentiments towards products, services, or topics. This project focuses on analyzing Twitter data due to its rich, diverse content and real-time nature, contrasting with the often manipulated and biased nature of Amazon reviews.


### Datasets
- Utilized the SemEval-2014 Task 9 dataset, focusing on binary and fine-grained sentiment classification of tweets.
- Aimed to compare the performance of machine learning and deep learning models on this dataset.

### Machine Learning Algorithms
- **Logistic Regression**
- **Support Vector Machines (SVM)**
- **Naive Bayes**
- **Decision Trees**
- **Random Forest**

### Deep Learning Algorithms
- **Convolutional Neural Networks (CNN)**
- **Recurrent Neural Networks (RNN), including LSTM and GRU**
- **RoBERTa (Robustly Optimized BERT Approach)**

### Ensemble Methods
- **Averaging**
- **Max Voting**

## System Architecture
Our system architecture integrates machine learning and deep learning algorithms with a backend built on Flask, acting as a REST API. The frontend GUI interacts with the backend, allowing users to input text for sentiment analysis.

## Evaluation Metrics
- **Accuracy**
- **Precision**
- **Recall**
- **F1-Score**

## User Interface
The application features a user-friendly graphical interface where users can input text for sentiment analysis. The backend processes this input using the selected deep learning model, and the sentiment analysis result is displayed to the user.

## Project Timeline and Division of Work
The project was structured in phases, from reviewing related research and data understanding to model selection, implementation, evaluation, and development of the user interface.

## Conclusion
Our findings highlight the efficacy of deep learning models, particularly RoBERTa, in performing sentiment analysis over traditional machine learning models. The developed sentiment analysis application provides an efficient tool for analyzing Twitter data, offering insights into public sentiment.

## Future Directions
- Explore additional datasets and compare their effectiveness in sentiment analysis.
- Investigate the integration of more sophisticated deep learning models.
- Enhance the user interface for a more interactive analysis experience.

## How to Run
Instructions for setting up and running the project:
1. Clone the repository.
2. Install required Python libraries: `pip install -r requirements.txt`.
3. Run the Flask backend server.
4. Access the GUI through the provided URL to perform sentiment analysis.

## Contributions
We welcome contributions to improve the project's accuracy, extend the dataset, or enhance the application's functionality. Please submit pull requests or issues for discussion.

## Contact
For further information or queries, please reach out to the respective team members via the provided email addresses.
