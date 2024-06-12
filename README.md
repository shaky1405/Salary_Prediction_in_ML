# Salary_Prediction_in_ML

 Introduction:

“Our primary objective was to create a machine learning model capable of predicting salaries for data professionals based on various factors, and then deploy this model as a web application using Flask.”

Data Collection:

“To start, we collected data from CSV File. The dataset included features such as job title, location, experience level, education level, industry, company size, and relevant skills.”

 Data Preprocessing:

“We then proceeded with data preprocessing, which included several key steps:

Cleaning the data by handling missing values and removing duplicates.
Encoding categorical variables into numerical format using techniques like One-Hot Encoding.
Normalizing numerical features to ensure they are on a similar scale.
Performing feature engineering to create new features that could enhance our model’s performance.”
Model Development:

“For model development, we evaluated several algorithms, including Linear Regression, Random Forest, Gradient Boosting, and Support Vector Machines. After thorough evaluation, we selected the Random Forest algorithm due to its superior accuracy and interpretability.”

Model Evaluation:

“We assessed the model using metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-Squared (R²). Our Random Forest model achieved the following results:

MAE: [Value]
MSE: [Value]
R²: [Value]
These results confirmed that our model performs well in predicting salaries.”
Flask Application:

“Next, we used the Flask framework to deploy our model. Flask is an ideal choice due to its simplicity and flexibility. The application includes:

A user input form to enter job-related features like job title, location, and experience.
An output section that displays the predicted salary based on the inputs.”
Deployment Workflow:

“Our deployment workflow involved four key steps:

Model Serialization: We saved the trained model using pickle.
Flask Setup: We created a Flask app with routes to handle user input and output.
Integration: We loaded the model and used it to predict salaries based on the inputs.
Deployment: Finally, we deployed the app on a cloud platform, such as Heroku or AWS.”
