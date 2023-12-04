# Chest X-Ray Diagnosis "Double Check" [Web App](http://127.0.0.1:5000/)

## Description
The idea was to build a transfer learning, convolutional neural network model that can take in chest x-ray images and make a prediction regarding the patient's disease state/lack thereof. 

## Use Cases
Doctors could use it as a double check when assessing x-rays. Radiology students could use the app as a learning tool, uploading images they weren't sure about. Potentially, even every day citizens could be empowered by such an app to get a second opinion of their own health status, a major precept of the [patient-data-ownership movement](https://www.aafp.org/news/blogs/freshperspectives/entry/doctor_or_patient_who_owns.html). 
 
## Technologies Used
![PYTHON BADGE](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![TENSOR FLOW BADGE](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![COLAB BADGE](https://img.shields.io/badge/Colab-F9AB00?style=for-the-badge&logo=googlecolab&color=525252)
![HTML BADGE](https://img.shields.io/badge/HTML-239120?style=for-the-badge&logo=html5&logoColor=white)
![CSS BADGE](https://img.shields.io/badge/CSS-239120?&style=for-the-badge&logo=css3&logoColor=white)
![FLASK BADGE](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![HEROKU BADGE](https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)
![GIT BADGE](https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white)
![GITHUB BADGE](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)


- HTML, CSS and Javascript for structure, styling, and interactivity
- Python and TensorFlow framework to train machine learning model on the [National Institue of Health's Chest X-Ray dataset](https://www.nih.gov/news-events/news-releases/nih-clinical-center-provides-one-largest-publicly-available-chest-x-ray-datasets-scientific-community)
- Transfer learning leveraged from MobileNet CNN architecture model for image classification. 
- Flask to deploy the model, hosted on Heroku

## Optimizations
Next steps include further filtering of orginal dataset to purify training pools. Seperate models will be developped gender and 
