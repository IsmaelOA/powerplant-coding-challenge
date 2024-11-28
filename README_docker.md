
## Deploy Flask Application on GCP using Docker

This guide explains how to build a Docker image for your Flask application and deploy it on Google Cloud Platform (GCP) using the provided `Dockerfile`.

---

### Prerequisites

1. **Google Cloud SDK** installed on your system.
   - [Install Google Cloud SDK](https://cloud.google.com/sdk/docs/install).
2. **Docker** installed and running.
   - [Install Docker](https://docs.docker.com/get-docker/).
3. A **Google Cloud Project**.
   - You can create a new project in the [Google Cloud Console](https://console.cloud.google.com/).

---

### Setup Instructions

#### 1. Authenticate with Google Cloud
Log in to your Google Cloud account:
```bash
gcloud auth login
```

Set the active project:
```bash
gcloud config set project YOUR_PROJECT_ID
```

Replace `YOUR_PROJECT_ID` with your Google Cloud project ID.

---

#### 2. Build the Docker Image
Run the following command in the root of your project directory (where the `Dockerfile` is located):

```bash
docker build -t gcr.io/YOUR_PROJECT_ID/powerplant-api:latest .
```

- Replace `YOUR_PROJECT_ID` with your Google Cloud project ID.
- The `-t` flag assigns a name and tag to the Docker image.

---

#### 3. Push the Docker Image to Google Container Registry (GCR)
Tag your Docker image:
```bash
docker tag gcr.io/YOUR_PROJECT_ID/powerplant-api:latest gcr.io/YOUR_PROJECT_ID/powerplant-api:latest
```

Push the Docker image to GCR:
```bash
docker push gcr.io/YOUR_PROJECT_ID/powerplant-api:latest
```

---

#### 4. Deploy the Image to Google Cloud Run
Deploy the image to Cloud Run with the following command:
```bash
gcloud run deploy powerplant-api     --image gcr.io/YOUR_PROJECT_ID/powerplant-api:latest     --platform managed     --region YOUR_REGION     --allow-unauthenticated
```

Replace the following placeholders:
- `YOUR_PROJECT_ID`: Your Google Cloud project ID.
- `YOUR_REGION`: The region where you want to deploy the application (e.g., `us-central1`).

---

### Testing the Deployment

Once the deployment is complete, Google Cloud Run will provide a service URL. You can test the API using the following:

1. Open the URL in your browser:
   ```
   https://YOUR_CLOUD_RUN_URL/productionplan
   ```
   
2. Use a tool like `curl` to send a POST request:
   ```bash
   curl -X POST https://YOUR_CLOUD_RUN_URL/productionplan    -H "Content-Type: application/json"    -d @payload.json
   ```

3. Use Postman or any other API testing tool with the URL.

---

### Notes

- Make sure your application runs on port `8888`, as specified in the `Dockerfile`.
- If you need authentication for Cloud Run, refer to [Cloud Run Authentication](https://cloud.google.com/run/docs/authenticating/service-to-service).
- To monitor logs, use:
  ```bash
  gcloud logging read --project=YOUR_PROJECT_ID
  ```

---
