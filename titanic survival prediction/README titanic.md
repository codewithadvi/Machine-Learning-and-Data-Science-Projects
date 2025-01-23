# Titanic Survivor Prediction

Welcome to the **Titanic Survivor Prediction** project! This project predicts whether a passenger survived the Titanic disaster based on various features, such as age, sex, and class. The project leverages a **Random Forest Classifier** for prediction, and **LabelEncoder** was used to preprocess categorical data. Extensive data exploration through plots and graphs helped uncover interesting insights, such as how more women survived and the age group of 31-40 years had a higher survival rate.

---

## 📖 Table of Contents

1. [Overview](#overview)  
2. [Technologies Used](#technologies-used)  
3. [Data Exploration & Insights](#data-exploration--insights)  
4. [Modeling](#modeling)  
5. [Evaluation](#evaluation)  
6. [Usage](#usage)  

---

## 🌟 Overview

The **Titanic Survivor Prediction** project aims to predict the survival of passengers on the Titanic based on historical data. The dataset includes several features such as **Age**, **Sex**, **Pclass** (Passenger Class), **SibSp** (Siblings or Spouses aboard), **Parch** (Parents or Children aboard), and **Fare**.

The following steps were involved in this project:
1. **Data Preprocessing**: Handling missing values and encoding categorical data.
2. **Exploratory Data Analysis (EDA)**: Visualizing the dataset to uncover patterns and insights.
3. **Modeling**: Building and training a **Random Forest Classifier**.
4. **Evaluation**: Measuring the model's performance using accuracy, precision, recall, and F1-score.

---

## 🛠 Technologies Used

- **Python**: The primary programming language used.
- **Libraries**:
  - **Pandas**: For data manipulation and preprocessing.
  - **NumPy**: For numerical operations.
  - **Matplotlib & Seaborn**: For data visualization and plotting.
  - **Scikit-learn**: For machine learning model implementation.

---

## 📊 Data Exploration & Insights

During the **Exploratory Data Analysis (EDA)** phase, several key insights were uncovered:

- **Gender**: More women survived the Titanic disaster than men. This pattern is evident when visualized with a **bar plot** showing the survival rates by gender.
  - Women had a higher survival rate due to "women and children first" being a common protocol during the evacuation.

- **Age Group 31-40**: Passengers in the age group of **31-40 years** had a higher survival rate compared to other age groups. This insight is supported by a **scatter plot** showing the correlation between age and survival.

- **Passenger Class**: Passengers in **first class (Pclass=1)** had a much higher survival rate than those in second or third class.

### Visualizations
- **Bar plots** for survival rates based on **Gender** and **Pclass**.
- **Histogram** showing the distribution of **Age** and **Fare**.
- **Pie charts** showing the percentage of survivors vs non-survivors.

---

## 🧑‍💻 Modeling

For the prediction, a **Random Forest Classifier** was used, which is an ensemble method combining multiple decision trees. The model was trained on the Titanic dataset to classify whether a passenger survived or not based on the features provided.

### Steps:
1. **Data Preprocessing**:
   - **Label Encoding**: Categorical features like **Sex** and **Embarked** were encoded using **LabelEncoder** to convert text labels into numerical values.
   - **Handling Missing Data**: Missing values in columns like **Age** and **Embarked** were imputed using mean or mode values.

2. **Model Training**:
   - The **Random Forest Classifier** was trained on the dataset, using **train-test split** for cross-validation.

3. **Hyperparameter Tuning**:
   - Hyperparameters like **n_estimators** (number of trees) and **max_depth** (depth of trees) were optimized using **GridSearchCV** to improve model performance.

---

## 📊 Evaluation

The performance of the **Random Forest Classifier** was evaluated using the following metrics:
- **Accuracy**: Measures the overall correctness of the model.
- **Precision**: The proportion of positive predictions that are correct.
- **Recall**: The proportion of actual positives that are identified correctly.
- **F1-Score**: A harmonic mean of precision and recall, used as a balanced metric.

---
