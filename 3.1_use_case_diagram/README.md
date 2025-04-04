<div id="header" align="center">
  <h1>UML Use Case Diagram</h1>
</div>

Here is a detailed description of the UML Use Case Diagram for the **Web Application for Emotion Recognition**. This diagram models the user interactions and system functionalities involved in emotion recognition.

## :pushpin: Overview

The **Use Case Diagram** outlines the primary functionalities available to the user and the relationship between those actions and the system.

It includes:
- **User** (actor who interacts with the system)
- **Web Application for Emotion Recognition** (the system boundary)
- **Use Cases** (specific tasks performed by the system)
- **Relationships** (denoted with `<<include>>` and `<<extend>>` for dependency and optional functionality)

## :bust_in_silhouette: Actor
- **User** – the primary actor who interacts with the system to initiate and view results of the emotion recognition process.

## :clipboard: Use Cases

### :one: Select Analysis Mode (Video/Audio)
- Allows the user to choose between video or audio emotion recognition.
- **Includes:**
  - `Start video recording` (for video-based analysis)
  - `Start audio recording` (for audio-based analysis)

### :two: View Emotion Analysis Results
- Displays the emotion recognition results to the user.
- **Extends:**
  - `Save emotion analysis results` (provides an option to save results for future reference)

### :three: View Web Service Description
- Provides information about the web service functionality.

### :four: Start Video Recording
- Initiates the recording process for video data.

### :five: Start Audio Recording
- Initiates the recording process for audio data.

### :six: Save Emotion Analysis Results
- Offers the option to save the analyzed emotion data.

## :link: Relationships
- **`<<include>>`** – used to represent mandatory functionality (e.g., `Select analysis mode` requires `Start video recording` or `Start audio recording`).
- **`<<extend>>`** – used to represent optional functionality (e.g., saving results is optional when viewing analysis results).

## :mag: Use Case Diagram Representation

<p align="center">
  <img src="https://github.com/space13pirate/UML-Diagrams-Labs/blob/main/3.1_use_case_diagram/use_case_diagram.png" alt="Use Case Diagram of the System" width="1000"/>
  <br>
  <em>Use Case Diagram of the System</em>
</p>
