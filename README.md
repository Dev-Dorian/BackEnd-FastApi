
# Python + FastAPI + MongoDB + Render

![fastapi](https://github.com/user-attachments/assets/3cbfe5c6-a0e2-4d4c-88e7-47b49f059d26)

# MongoDB Atlas Configuration

**1.** You must select an account, in my case I use the GitHub option since it connects directly to my repositories.

![Screenshot 2024-10-28 154446](https://github.com/user-attachments/assets/3b9f0045-ca53-4b6d-a4ee-9d8e79e88da6)

2. To get the connection to the remote MongoDB Atlas database you must go to "Connect" and click on "Connect for your application".

![Screenshot 2024-10-28 154727](https://github.com/user-attachments/assets/e1e3c110-1be5-467c-8d50-8e705555dd39)

3. You must enter the user and password, copy the entire line and paste it into the client.py file of the project

![Screenshot 2024-10-28 155645](https://github.com/user-attachments/assets/077f12b9-69cb-46a4-9f1d-caa4b15c06b4)






# Clone the project

Set up the database, local mongodb or in the cloud using mongodb atlas.

In the client.py file you will find the database configuration, which has two connections, which you must choose one:
1. The local database must comment the remote database line.
2. If you use the remote database you must comment the local database line, and you must also add the user and password established in the MondoDB Atlas configuration.

![Screenshot 2024-10-28 151121](https://github.com/user-attachments/assets/14bcca59-8422-43ef-911f-8f3012529d90)

# Render Configuration

1. Login to render.

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://dashboard.render.com/register)

![Screenshot 2024-10-28 143548](https://github.com/user-attachments/assets/4e6c596b-939c-4727-b510-eacef28b3422)

2. Choose the option to create a web service.

![Screenshot 2024-10-28 143829](https://github.com/user-attachments/assets/dd3e9823-8241-4c8a-b054-c42b14e158ba)

3. Choose the clone repository in your github repositories.

![Screenshot 2024-10-28 144026](https://github.com/user-attachments/assets/911fc4d3-b8fa-43b6-a93a-4b1413cd64c5)

4. Fill in the fields according to the configuration.

![Screenshot 2024-10-28 144146](https://github.com/user-attachments/assets/0f4933af-37bf-42d0-a3b6-5d01cd6cc2ec)

5. Specify the following as the Start Command.

The project requirements.txt file is important because it allows us to install the dependencies that the web service needs to run the application.

    ```shell
    uvicorn main:app --host 0.0.0.0 --port $PORT
    ```
![Screenshot 2024-10-28 144409](https://github.com/user-attachments/assets/5679487d-fe47-4798-9f1c-6b1336a4f15e)

6. You can select the payment method you want to use, in my case I will use the free option.

![Screenshot 2024-10-28 144457](https://github.com/user-attachments/assets/56e8febf-9f66-40df-afdc-605518c4148e)

7. Once the fields are completed, create the web service.

![Screenshot 2024-10-28 144529](https://github.com/user-attachments/assets/26fd9eb3-9092-4c60-9ec1-6dc15e886b7d)

8. The services will be loaded to deploy your application on the web.

![Screenshot 2024-10-28 144723](https://github.com/user-attachments/assets/5c9a70da-f563-4711-8150-caa606bbc73c)

9. Enter the link to see your published site.

![Screenshot 2024-10-28 144852](https://github.com/user-attachments/assets/3a4d2bde-12b1-450d-be94-7e718d949eba)

10. It will direct us to our API. If you get a "Not found" message, don't worry, just add a /docs to your link.

![Screenshot 2024-10-28 145152](https://github.com/user-attachments/assets/fecd111f-6fe1-4918-8c21-629913c7d5da)

