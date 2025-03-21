<div id="header" align="center">
  <h1>UML Activity Diagram</h1>
</div>

Here is a detailed description of the UML Activity Diagram for the **Emotion Recognition System**. This diagram represents the process flow of analyzing emotions using both video and audio data.

## :pushpin: Overview

The **Activity Diagram** illustrates the decision-making process and the sequential steps followed during the emotion recognition task.

It includes:
- **User** (initiates and views the results)
- **System** (handles the core process of activating devices, recording data, and detecting emotions)

## :arrow_forward: Process Description

### :one: Start Process
The process starts when the **User** selects the desired analysis mode.

### :two: Decision Point
A decision node directs the process based on the selected mode:
- **Video Mode** – activates the camera for real-time facial landmark detection and emotion recognition.
- **Audio Mode** – activates the microphone to record audio data and analyze emotions from the recording.

### :three: Video Analysis Flow
1. The **System** activates the camera.
2. The camera records video while simultaneously:
   - displaying the video on the monitor;
   - detecting key facial landmarks in real time;
   - recognizing emotions from the detected landmarks.
3. The process concludes with the **System** ending the recording.

### :four: Audio Analysis Flow
1. The **System** activates the microphone.
2. The microphone records audio data.
3. The **System** processes the audio recording to detect emotions.
4. The process concludes with the **System** ending the recording.

### :five: Display Results
Once the recording is completed, the **System** provides the analysis results to the **User**.

## :mag: Activity Diagram Representation

<p align="center">
  <img src="https://github.com/space13pirate/UML-Diagrams-Labs/blob/main/3.2_activity_diagram/activity_diagram.png" alt="Activity Diagram of the System" width="1000"/>
  <br>
  <em>Activity Diagram of the System</em>
</p>


## :sparkles: Key Features
- Clear branching logic for video and audio modes
- Real-time video analysis flow with facial detection and emotion recognition
- Efficient handling of audio data for emotion detection
- Organized flow ensuring results are displayed upon completion
