<h1 align="center">Vuex/FastAPI Event Management System</h1>

<p align="center">
  <a href="#overview">Overview</a> •
  <a href="#features">Features</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#api-documentation">API Documentation</a> •
  <a href="#contributing">Contributing</a> •
  <a href="#license">License</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  <img src="https://img.shields.io/badge/Author-SmartMatt-blue" />
</p>

## Overview
This repository contains a full-stack event management system, developed as a practical implementation of the concepts learned from the tutorial ["Fast API and Vue JS CRUD Application | Vuex | Vuetify | Nuxt | MySQL | Docker | REST API | Swagger"](https://www.youtube.com/watch?v=Xr7O4uq52eQ). It features a Vue.js frontend with Vuex and Vuetify, and a FastAPI backend, all connected to a MySQL database.

### Description
The system enables the creation, editing, display, and deletion of events. It's designed with a user-friendly interface built with Vuetify and Nuxt, offering a seamless user experience. The backend API, crafted with FastAPI, provides robust and efficient handling of data with MySQL.

## Features
- **Frontend**
  - Built with Vue.js, Vuex, Vuetify, and Nuxt.
  - Functionalities include:
    - Creating events.
    - Editing event details.
    - Displaying a list of events.
    - Deleting events.

- **Backend**
  - Developed using FastAPI.
  - RESTful API endpoints for:
    - Retrieving events.
    - Creating new events.
    - Editing existing events.
    - Deleting events.
  - MySQL database integration.

## Installation
1. **Frontend Setup**
   - Ensure you have [Yarn](https://yarnpkg.com/) installed.
   - Navigate to the frontend directory and run `yarn install` to install dependencies.

2. **Backend Setup**
   - Ensure you have Python and FastAPI installed.
   - Navigate to the backend directory and run `pip install -r requirements.txt` to install required packages.

3. **Database Setup**
   - Set up a MySQL database.
   - Configure the database connection details in the backend settings.

## Usage
1. Start the frontend server:
   - In the frontend directory, run `yarn dev`.
   - The frontend will be available at `localhost:3000`.

2. Start the backend server:
   - In the backend directory, run `uvicorn main:app --reload`.
   - The API will be available at `localhost:8000`.

## API Documentation
Access the Swagger UI for the API documentation and testing at `localhost:8000/docs`.

## Contributing
Contributions to this project are welcome. Please ensure to follow the guidelines:

- Fork the repository.
- Create a new branch for each feature or improvement.
- Submit a pull request with a clear description of your changes.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
&copy; 2023 Mateusz Płonka (SmartMatt). All rights reserved.
<a href="https://smartmatt.pl/">
    <img src="https://smartmatt.pl/github/smartmatt-logo.png" title="SmartMatt Logo" align="right" width="60" />
</a>

<p align="left">
  <a href="https://smartmatt.pl/">Portfolio</a> •
  <a href="https://github.com/SmartMaatt">GitHub</a> •
  <a href="https://www.linkedin.com/in/mateusz-p%C5%82onka-328a48214/">LinkedIn</a> •
  <a href="https://www.youtube.com/user/SmartHDesigner">YouTube</a> •
  <a href="https://www.tiktok.com/@smartmaatt">TikTok</a>
</p>
