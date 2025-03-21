<div id="header" align="center">
  <h1>UML Component Diagram</h1>
</div>

Here is a detailed description of the UML Component Diagram for the **Emotion Recognition System**. The system is designed as a web application that processes both audio and video data to recognize emotions using specialized libraries and databases.

## :pushpin: Overview

The **Component Diagram** visualizes the main modules, their interactions, and data flow in the system.

It highlights the core elements of the system architecture:

- **Flask Application** (manages the web interface, user actions, and data integration)
- **Emotion Recognition Library** (handles emotion recognition logic)
- **Audio Processing Library** (processes audio data)
- **Video Processing Library** (processes video data)
- **Audio Emotions Database**, **Video Emotions Database**, and **Probability Data** (store relevant data)

## :classical_building: Component Descriptions

### :one: Flask Application
The core of the system that integrates libraries, databases, and user actions.

- Manages user interactions through the web interface.
- Coordinates audio and video data processing.
- Implements the **IWebInterface** interface.

### :two: Emotion Recognition Library
Processes both audio and video data to predict emotions.

- Writes recognized emotions to the **Audio Emotions Database** and **Video Emotions Database**.
- Generates probability data for predictions.

### :three: Audio Processing Library
Handles audio data analysis and feature extraction.

- Reads emotion data from the **Audio Emotions Database**.

### :four: Video Processing Library
Handles video data analysis and feature extraction.

- Reads emotion data from the **Video Emotions Database**.

## :link: Component Interactions

- The **Flask Application** communicates with:
  - The **Emotion Recognition Library** to analyze data.
  - The **Audio Processing Library** and **Video Processing Library** for feature extraction.
- The **Emotion Recognition Library** writes data to:
  - The **Audio Emotions Database**
  - The **Video Emotions Database**
  - The **Probability Data** storage
- The **User Interface** interacts with the **Flask Application** to trigger analysis and view results.

## :mag: Component Diagram Representation

<p align="center">
  <img src="https://github.com/space13pirate/UML-Diagrams-Labs/blob/main/2.1_component_diagram/component_diagram.png" alt="Component Diagram of the System" width="1000"/>
  <br>
  <em>Component Diagram of the System</em>
</p>

## :sparkles: Key Features
- Modular design for enhanced scalability and flexibility.
- Clear separation of logic for improved maintainability.
- Integrated user interface for simplified user interaction.
