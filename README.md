The project is all about the design of a machine learning model that uses the age,height,weight and BMI data of an individual to predict if they have obesity.
Obesity in this model has categories like: Normal weight(no obesity),Overweight,Underweight,Other in which other is where by all the features do not point to the label

**dependicies for fastAPI**
>Install the python fastAPI module first using the command
  bash>> pip3 install fastapi
      >> pip3 install uvicorn 

**to the the API for the obesity prediction model**
The fastAPI provides various ways to test the requests made to the API,these includes swaggerUI for web based interfaces and using curl or even postman apis to test our apis.In this project i used the swaggerUI to test my obesity prediction api using POST requests.
    *to start tha api server*
            bash>> uvicorn {app_name}:app --reload e.g uvicorn obesityAPI:app --reload
