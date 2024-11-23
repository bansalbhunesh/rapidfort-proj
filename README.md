# DOCX to PDF Converter

A simple web application for converting DOCX files to PDF format. The application consists of a frontend, a backend, and a file handling service, all containerized using Docker.

---

## Features

- Upload DOCX files and convert them to PDF.
- User-friendly web interface built with React and Material-UI.
- Backend API built with Flask to handle file conversions.
- File service to manage file uploads and temporary storage.
- Fully containerized using Docker for easy deployment.

---

## Prerequisites

Before running the application, ensure you have the following installed:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

---

## Quick Start

### Step 1: Clone the Repository
Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/docx-to-pdf-converter.git
cd docx-to-pdf-converter```

### Step 2: Build Docker Images

Build the Docker images for the frontend and backend services:

```bash
docker-compose build

### Step 3: Run the Application

Start the containers using Docker Compose:

```bash
docker-compose up

### Step 4: Access the Application

Open your web browser and navigate to:

### Step 5: Stop the Application

To stop the running containers, execute the following command:

```bash
docker-compose down

### Step 6: Accessing the Application

Once the application is running, open your web browser and navigate to:

[localhost:3000](http://localhost:3000)


