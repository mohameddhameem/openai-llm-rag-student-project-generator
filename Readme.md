# Student Project Document Generator

This is a Streamlit application for incremental document generation with retrieval-augmentation using OpenAI's GPT-3 model. Users can input prompts, upload reference documents (CSV or PDF), specify retrieval queries, and generate documents interactively.

## Installation

Follow these steps to set up and run the application:

        # Clone the repository
        git clone git@github.com:mohameddhameem/openai-llm-rag-student-project-generator.git
        cd your-repo

        # Install required libraries
        pip install streamlit pandas openai PyPDF2

## Usage

To run the Streamlit app:

        # Replace 'YOUR_API_KEY' with your OpenAI API key in 'streamlit_document_generator.py'
        # Save the code to 'streamlit_document_generator.py'

        # Run the Streamlit app
        streamlit run streamlit_document_generator.py

## Features

*   Generate documents incrementally based on user prompts
*   Upload and preview reference documents (CSV or PDF)
*   Specify retrieval queries for information augmentation
*   Accept or reject model-generated responses
*   Continue or end the conversation

## Deployment

You can deploy this Streamlit app to various platforms like Heroku, Streamlit Sharing, or your preferred hosting service. Be sure to configure environment variables for your API key in the deployment environment.

## Run Locally: 

        docker build -t streamlit-document-generator . 

        docker run -p 8501:8501 -e OPENAI_API_KEY="YOUR_API_KEY" streamlit-document-generator

# Deploying Your Streamlit Document Generator on Heroku

Follow these steps to deploy your Streamlit Document Generator app on Heroku:

## Step 1: Heroku Account Setup

If you don't have a Heroku account, sign up for a free Heroku account at [https://signup.heroku.com/](https://signup.heroku.com/).

## Step 2: Install Heroku CLI

Download and install the Heroku Command Line Interface (CLI) from [https://devcenter.heroku.com/articles/heroku-cli](https://devcenter.heroku.com/articles/heroku-cli).

## Step 3: Login to Heroku

Open a terminal and run the following command to log in to your Heroku account:

    heroku login

## Step 4: Prepare Your Streamlit App

Ensure that your Streamlit app is working locally and has a `requirements.txt` file with all dependencies listed.

## Step 5: Initialize Git Repository

If your app isn't already in a Git repository, initialize one in your project directory:

    git init

## Step 6: Create a Procfile

Create a `Procfile` (without any file extension) in your project directory with the following content:

    web: streamlit run streamlit_document_generator.py

Replace `streamlit_document_generator.py` with the name of your Streamlit app script.

## Step 7: Commit Your Changes

Add your files to the Git repository and commit your changes:

    git add .

    git commit -m "Initial commit"

## Step 8: Create a Heroku App

Create a new Heroku app with a unique name:

    heroku create your-app-name

Replace `your-app-name` with your desired app name.

## Step 9: Deploy to Heroku

Deploy your app to Heroku:

    git push heroku master

## Step 10: Open Your App

Once the deployment is complete, open your app in your web browser:

    heroku open

Your Streamlit Document Generator app is now live on Heroku!

## Additional Configuration

You may need to configure environment variables or set up a Heroku database depending on your app's requirements. Refer to the Heroku documentation for more details.

## Resources

*   Heroku Documentation: [https://devcenter.heroku.com/](https://devcenter.heroku.com/)
*   Streamlit Documentation: [https://docs.streamlit.io/](https://docs.streamlit.io/)



## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Contributing

Contributions are welcome! Please open an issue or create a pull request on the GitHub repository.


## Author

Mohamed Dhameem

## Version

1.0.0