# House Price Prediction

Welcome to the **House Price Prediction** project! This project uses **Linear Regression** to predict house prices based on various factors such as **house age**, **distance to the nearest MRT station**, **number of convenience stores**, and **latitude**. The model has been trained on a dataset containing these features and aims to predict house prices with high accuracy.

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

The **House Price Prediction** project aims to predict house prices based on several factors that could impact the price. The model uses **Linear Regression**, which attempts to establish a relationship between the features and the target variable (house price).

### Features Used:
- **House Age**: The age of the house in years.
- **Distance to the Nearest MRT Station**: The distance in meters to the nearest Mass Rapid Transit station.
- **Number of Convenience Stores**: The number of convenience stores nearby.
- **Latitude**: The geographical latitude of the house.

The goal is to predict the **house price** based on these features.

---

## 🛠 Technologies Used

- **Python**: The core language for this project.
- **Libraries**:
  - **Pandas**: For data manipulation and preprocessing.
  - **NumPy**: For numerical operations.
  - **Matplotlib & Seaborn**: For data visualization and plotting.
  - **Scikit-learn**: For implementing **Linear Regression** and model evaluation.

---

## 📊 Data Exploration & Insights

During the **Exploratory Data Analysis (EDA)** phase, several key insights were uncovered:

### 1. **House Age vs. House Price**:
   - There doesn’t seem to be a strong linear relationship between house age and price.
   - However, very new and very old houses seem to have higher prices. This suggests that market demand might favor these types of houses due to modern amenities or historical value.

### 2. **Distance to the Nearest MRT Station vs. House Price**:
   - A clear negative relationship was observed between house price and the distance to the nearest MRT station.
   - As the distance to the MRT station increases, house prices tend to decrease, suggesting that houses closer to public transport are more valuable.

### 3. **Number of Convenience Stores vs. House Price**:
   - There is a positive relationship between the number of convenience stores and house prices.
   - Houses located near more convenience stores tend to have higher prices, likely due to convenience and better amenities in the area.

### 4. **Latitude vs. House Price**:
   - While not a strong linear relationship, there is a pattern where certain latitudes correspond to higher or lower house prices.
   - This could be indicative of specific neighborhoods being more desirable, as certain latitudes could correspond to areas with higher demand or prestige.

---

## 🧑‍💻 Modeling

For the prediction, **Linear Regression** was used, which is a method that models the relationship between the independent variables (features) and the dependent variable (house price) by fitting a linear equation to the observed data.

### Steps:
1. **Data Preprocessing**:
   - **Handling Missing Values**: Missing data was handled by either dropping or imputing values based on the data's nature.
   - **Feature Encoding**: Any categorical features were encoded appropriately.
   - **Scaling**: The features were scaled (if necessary) to improve model performance.

2. **Model Training**:
   - The **Linear Regression** model was trained using **Scikit-learn**'s `LinearRegression()` class.

3. **Hyperparameter Tuning**:
   - Linear Regression doesn’t require complex hyperparameter tuning, but cross-validation was used to ensure the model generalized well.

---


