<div id="header" align="center">
  <h1>UML Deployment Diagram</h1>
</div>

Here is a detailed description of the UML Deployment Diagram for the **Emotion Recognition System**. This system is designed as a distributed application that leverages web, processing, and database components to analyze and recognize emotions from audio and video data.

## :pushpin: Overview

The **Deployment Diagram** visualizes the physical deployment structure of the system, detailing how different hardware and software elements interact.

It includes:
- **User Device** (runs the web browser for user interactions)
- **Web Server** (hosts the Flask application and processing libraries)
- **Database Server** (stores processed emotion data)

## :classical_building: Node Descriptions

### :one: User Device
Represents the user's environment for interacting with the system.

**Component:**
- **Web Browser** – the interface for sending HTTP requests to the web server and displaying results.

### :two: Web Server
Manages the core logic, data flow, and emotion recognition processes.

**Artifacts:**
- **Flask Application** – the web interface and control hub for interacting with processing libraries.
- **Emotion Recognition Library** – handles emotion recognition logic.
- **Audio Processing Library** – processes audio data for emotion detection.
- **Video Processing Library** – processes video data for emotion detection.

### :three: Database Server
Stores and manages all analyzed data from the system.

**Databases:**
- **Video Emotions Database** – stores processed video emotion data.
- **Audio Emotions Database** – stores processed audio emotion data.
- **Probability Data** – stores probability values for predicted emotions.

## :link: Communication Flow

- The **Web Browser** sends HTTP requests to the **Flask Application**.
- The **Flask Application** communicates with:
  - **Emotion Recognition Library** for emotion prediction logic.
  - **Audio Processing Library** and **Video Processing Library** for specialized data analysis.
- The **Emotion Recognition Library** writes data to:
  - **Video Emotions Database**
  - **Audio Emotions Database**
  - **Probability Data** storage
- The **Audio Processing Library** and **Video Processing Library** read data from their respective databases for accurate analysis.

## :mag: Deployment Diagram Representation

<p align="center">
  <img src="https://github.com/space13pirate/UML-Diagrams-Labs/blob/main/2.2_deployment_diagram/deployment_diagram.png" alt="Deployment Diagram of the System" width="1000"/>
  <br>
  <em>Deployment Diagram of the System</em>
</p>

## :sparkles: Key Features
- Clear separation of user interface, business logic, and data storage.
- Distributed design for improved scalability and performance.
- Modular structure to allow easy expansion and updates.
