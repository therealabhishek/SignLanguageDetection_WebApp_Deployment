# SignLanguageDetect: Sign Language using AI

- In this application, we have trained our model to detect Sign Languages using the YoloV5 object detection algorithm.

- The working of the application has been illustrated below.

Detecting Thanks

![Thanks](https://github.com/therealabhishek/SignLanguageDetection_WebApp_Deployment/blob/main/assets/local_deploy.PNG)

In the above image, we can see that 'Thanks' sign has been detected with a confidence of 97%.

Detecting Yes

![Yes](https://github.com/therealabhishek/SignLanguageDetection_WebApp_Deployment/blob/main/assets/local_deploy1.PNG)

In the above image, we can see that 'Yes' has been detected with a confidence of 96%.

### What is the need for Sign Language Detection using AI?

- We live in a diverse world, there are many diverse human beings living in this world, having different abilities.

- One such differently diverse set of humans are the ones who hear a bit less. So, how do we communicate with them?

- Sign Language is a way of communicating with them, for that we also need to learn atleast a few signs of the many signs that are available so that we can communicate with them, hence the need to develop an AI enabled app so that we can effectively communicate with each other.

### Steps involved in the Project

- Data Collection and Annotation
  
  In data collection, we have collected our own data for 6 different signs, namely, 'Thanks', 'Yes', 'No', 'I Love You', 'Hello' and 'Please'.

  We have collected 40 images per sign, thus a total of 240 images.

  For annotating/labelling the collected images, we have used a tool called 'LabelImg'.

  The annotated images have been segregated as train and test data, zipped and then uploaded to github.

- Data Ingestion
  ![Ingestion](https://github.com/therealabhishek/SignLanguageDetection_WebApp_Deployment/blob/main/assets/Data%20Ingetions.png)

In the data ingestion stage, we have downloaded our data from github as a zipfile.

The downloaded will be stored under the 'data_ingestion' folder which is under the 'artifacts' folder.

The zipfile will be unzipped and the train and test data will be stored in 'feature_store' folder under 'data_ingestion' folder.

- Data Validation
  ![Validation](https://github.com/therealabhishek/SignLanguageDetection_WebApp_Deployment/blob/main/assets/Data%20validation.png)

We have unzipped the data file and stored it under 'feature_store' folder.

But, before proceeding further we shall check if 'train', 'test' and 'data.yaml' files are actually present under 'feature_store' folder or not.

If they are present, we shall return a validation status as 'True' if not 'False'.

- Model Training
  ![Training](https://github.com/therealabhishek/SignLanguageDetection_WebApp_Deployment/blob/main/assets/Model%20trainer.png)

In model training, the model will take various inputs, such as model version, number of epochs, batch size.

The model will be trained and the best model will be saved as 'best.pt' under the 'model_trainer' folder which is under the 'artifacts' folder.

- Model Pusher
  ![Pushing](https://github.com/therealabhishek/SignLanguageDetection_WebApp_Deployment/blob/main/assets/Model%20Pusher.png)

In model pusher, the model that we have stored 'best.pt' under the 'model_trainer' folder, will be pushed to the AWS S3 bucket.

- Model Deployment
  ![Deploy](https://github.com/therealabhishek/SignLanguageDetection_WebApp_Deployment/blob/main/assets/deployment.jpeg)

  ![DeployedApp]()


### TO RUN THE APP LOCALLY

- Clone the repository.

- Install the requirements using "pip install -r requirements.txt".

- Run "python app.py".

- Upload the image using the "Upload" button and click "Predict" to get the prediction.




