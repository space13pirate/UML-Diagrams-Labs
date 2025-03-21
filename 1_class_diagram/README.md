<div id="header" align="center">
  <h1>UML Class Diagram</h1>
</div>

Here is a detailed description of the UML Class Diagram for the **Emotion Recognition System**. The system consists of several components responsible for emotion detection from both speech and video, a web interface built with Flask, and supporting utilities for data handling and visualization.

## :pushpin: Overview

The **Сlass Diagram** models the main components and their interactions in the system.

It includes:
- **EmotionRecognition** (abstract class)
- **VideoEmotionRecognition** (handles video-based emotion recognition)
- **SpeechEmotionRecognition** (handles audio-based emotion recognition)
- **FlaskApp** (manages the web application and routes)
- **DataHandler** (manages input/output operations and data processing)
- **Visualization** (generates charts and visualizations)
- **StreamingResponse** (handles video streaming)

## :classical_building: Class Descriptions

### :one: EmotionRecognition (abstract class)

The base class for emotion recognition modules. It defines common attributes and methods for emotion recognition tasks.

**Attributes:**
- `_model` – the machine learning model used for emotion prediction.
- `_emotion_labels` – a list of emotion labels.

**Methods:**
- `predict()` – predicts the emotion from given input data.

### :two: VideoEmotionRecognition
Handles emotion recognition from video input using facial analysis.

**Attributes:**
- `_video_model` – the trained video emotion recognition model.
- `_face_detector` – a face detection model.
- `_landmark_predictor` – a model for extracting facial landmarks.

**Methods:**
- `gen()` – generates frames for video processing.
- `detect_face(frame)` – detects faces in a video frame.
- `extract_face_features(faces)` – extracts features from detected faces.
- `predict_emotion_from_frame(frame)` – predicts emotions from a video frame.

### :three: SpeechEmotionRecognition
Handles emotion recognition from audio recordings.

**Attributes:**
- `_audio_model` – the trained audio emotion recognition model.

**Methods:**
- `voice_recording(filename, duration)` – records a voice sample.
- `mel_spectrogram(y, sr)` – computes the mel spectrogram of an audio sample.
- `predict_emotion_from_file(filename)` – predicts emotions from an audio file.
- `prediction_to_csv(predictions, filename)` – saves predictions to a CSV file.

### :four: FlaskApp
Manages the web application, handling routes and user interactions.

**Attributes:**
- `secret_key` – a secret key for session management.
- `config` – flask application configuration.
- `routes` – routes for different functionalities.

**Methods:**
- `route()` – defines a Flask route.
- `run()` – runs the Flask application.
- `render_template()` – renders an HTML template.
- `flash()` – sends flash messages.
- `redirect()` – redirects users to another route.
- `session()` – manages user sessions.

### :five: DataHandler
Manages reading, writing, and processing data.

**Attributes:**
- `data` – holds processed data.

**Methods:**
- `read_csv(filepath)` – reads data from a CSV file.
- `to_csv(filepath)` – saves data to a CSV file.
- `get_value_counts()` – returns value counts of a dataset.
- `get_mode()` – returns the most frequent value in the dataset.

### :six: Visualization
Handles the creation and saving of visualizations.

**Attributes:**
- `chart` – stores the generated chart object.

**Methods:**
- `create_chart()` – creates a chart based on the data.
- `mark_line()` – adds a marker line to the chart.
- `encode()` – encodes data for visualization.
- `save_chart(filepath)` – saves the generated chart to a file.

### :seven: StreamingResponse
Handles the streaming of video frames.

**Attributes:**
- `stream` – the video stream object.

**Methods:**
- `stream_video()` – streams video content to the user.

## :link: Class Relationships

- **FlaskApp** interacts with:
  - `VideoEmotionRecognition` (uses for video emotion recognition)
  - `SpeechEmotionRecognition` (uses for audio emotion recognition)
  - `DataHandler` (manages data storage and retrieval)
  - `StreamingResponse` (handles video streaming)
  - `Visualization` (generates data visualizations)

- **VideoEmotionRecognition** and **SpeechEmotionRecognition** both inherit from `EmotionRecognition`.
- **VideoEmotionRecognition** and **SpeechEmotionRecognition** interact with `DataHandler` to store detected emotion data.

## :mag: Class Diagram Representation


<p align="center">
  <img src="https://github.com/space13pirate/UML-Diagrams-Labs/blob/main/1_class_diagram/class_diagram.png" alt="Class Diagram of the System" width="1000"/>
  <br>
  <em>Class Diagram of the System</em>
</p>
