# Dell_Hackathon

This Page contains code for the DELL Hackathon held at the Shiv Nadar University on 29 and 30th August 2018. 

This project was done on the topic of Machine Learning on the Credit Card Fraud detection and was based on Django framework.
This webapp detects fraud in a 2 step process. The first step uses a quick filter to detect fraud. If fraud is not detected then it takes it striaght to the OTP page and if the fraud is detected it goes to step two.

Step two uses the ensemble learning (combination of 3 algorithms- knn, logistic, adaboost ) to predict the fraud. If the fraud is deteced then futher more user authentication like security questions are required for transaction. If no fraud detected then it goes straight to the OTP page  

Team Name: Four 4 One

The Team Members:

Ansh Tandon (UX and Data Preprocessing)

Keshav Chandak (Machine Learning and Backend)

Kshitij Srivastava (Backend, Database, User Authentication)

Shreyangi Prasad (Frontend)

## File Name

Pre-processed data set for Classification
sample.csv

Models Trained using the scikit-learn and parameters of the model saved using pickle in these files
Adaboost.sav
Logistic.sav
naivebayes.sav
Knn.sav

## Webapp

Contained in the First Folder
templates folder contains HTML files used for rendering
static/first folder contains the static files used in the HTML

views.py contains the logic and for rendering the HTML files
urls.py contains the url contained in the file
models.py contains how data will be stored in the database
forms.py conatins how user data will be taken from the user





