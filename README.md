# Thousand Docker

This repository contains a Docker project for Thousandeye, an application for monitoring network performance using ThousandEyes API.

## Features

- Integration with ThousandEyes API for retrieving test information and metrics
- Support for both regular and trial user credentials

## Requirements

- Docker: [Install Docker](https://docs.docker.com/get-docker/)
- ThousandEyes API credentials: Obtain valid API credentials from ThousandEyes(https://www.thousandeyes.com/signup/)

## Getting Started

1.  Clone the repository:

- git clone https://github.com/ShuraDarz/Thousend-docker.git

2.  Navigate to the project directory:

- cd Thousend-docker
- Configure ThousandEyes API credentials:

3.  Open the main.py file in the project directory.

- Replace API_USERNAME and API_TOKEN with your ThousandEyes API credentials.
- If applicable, replace TRIAL_USERNAME and TRIAL_TOKEN with trial user credentials.

3.  Build the Docker image:

- docker build -t thousand-docker .

4.  Run the Docker container:

- docker run -d --name thousand-container thousand-docker

## Usage

The Thousand application will now be running inside the Docker container.
