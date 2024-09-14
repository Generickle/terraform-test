
# ChatGPT Clone in Flask with Docker and Azure Kubernetes Service (AKS)

This project creates a simple ChatGPT clone using Flask, OpenAI's API, Docker, and Azure Kubernetes Service (AKS). The web app allows users to send messages and receive responses from OpenAI's GPT model. The app is containerized using Docker and deployed on AKS.

## Project Setup

### 1. Prerequisites

Ensure you have the following installed:
- [Docker](https://www.docker.com/)
- [Python 3.x](https://www.python.org/downloads/)
- An [OpenAI API key](https://platform.openai.com/account/api-keys)

### 2. Clone the Repository

```bash
git clone https://github.com/Generickle/terraform-test
cd terraform-test
```

### 3. Install Python Dependencies

To install the required Python packages, run:

```bash
pip install -r requirements.txt
```

### 4. Obtain OpenAI API Key

Sign up at [OpenAI](https://platform.openai.com/account/api-keys) and generate an API key. Once you have the key, you can store it in a `.env` file:

```bash
echo "OPENAI_API_KEY=your-api-key" > .env
```

### 5. Update `app.py` with the New OpenAI API

Ensure that you are using the latest OpenAI API interface:

```python
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": user_message}]
)
```

### 6. Create the Dockerfile

A `Dockerfile` is included in this project, and it defines the instructions for containerizing the application:

```Dockerfile
# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Flask and OpenAI
RUN pip install Flask openai python-dotenv

# Expose the port on which the app will run
EXPOSE 5000

# Define environment variable for Flask app
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the Flask app
CMD ["flask", "run"]
```

### 7. Build and Run Docker Container

To build the Docker image:

```bash
docker build -t chatgpt-clone .
```

To run the container:

```bash
docker run -p 5000:5000 -e OPENAI_API_KEY=your-api-key chatgpt-clone
```

### 8. Deploy to Azure Kubernetes Service (AKS)

You can deploy this containerized app on Azure Kubernetes Service (AKS) using Terraform. For a detailed guide on creating an AKS cluster using Terraform, refer to this [blog post](https://www.middlewareinventory.com/blog/terraform-aks-example-creating-azure-k8s-cluster-devops-junction/#google_vignette).

This blog provides a comprehensive step-by-step guide on how to set up an AKS cluster using Terraform, allowing you to manage the infrastructure as code and scale your deployment efficiently.

### 9. Access the Application

Once deployed, access the app in your web browser by navigating to `http://localhost:5000` or the assigned external IP address if deployed on Azure.

## References

- https://www.middlewareinventory.com/blog/terraform-aks-example-creating-azure-k8s-cluster-devops-junction/#google_vignette

### Terraform-AKS
Terraform script to automate Azure Kubernetes Services creation

Use the Terraform-AKS-development for small scale development purposes.

Use the Terraform-AKS-production for production purposes.

Find the full article here:
https://www.middlewareinventory.com/blog/terraform-aks-example-creating-azure-k8s-cluster-devops-junction/
