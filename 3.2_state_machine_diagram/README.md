<div id="header" align="center">
  <h1>UML State Machine Diagram</h1>
</div>

Here is a detailed description of the UML State Machine Diagram for the **Emotion Recognition System**. This diagram models the various states the system transitions through during its operation, including initialization, processing, and navigation.

## :pushpin: Overview

The **State Machine Diagram** illustrates the internal states of the system and how it transitions between them in response to user actions or API requests.

It includes:
- **Home** state with idle and description views
- **Video and Audio initialization flows**
- **Recording and dashboard states**
- Transitions based on HTTP requests and navigation events

## :twisted_rightwards_arrows: State Transitions

### :house: Home state
- `Idle` is the default state.
- From `Idle`, the user can:
  - Navigate to `Description` using `Go to /description`.
  - Start video analysis via `POST /video`.
  - Start audio analysis via `POST /audio`.

### :movie_camera: Video analysis flow
- From `VideoInit`, a request `POST /video_recording` leads to `VideoRecording`.
- Then, `GET /video_dash` leads to the `VideoDashboard`.
- The user can return to `Idle` (Home) from `VideoDashboard`.

### :microphone: Audio analysis flow
- From `AudioInit`, a request `POST /audio_recording` leads to `AudioRecording`.
- Then, `GET /audio_dash` leads to the `AudioDashboard`.
- The user can return to `Idle` (Home) from `AudioDashboard`.

## :mag: State Diagram Representation

<p align="center">
  <img src="https://github.com/space13pirate/UML-Diagrams-Labs/blob/main/3.2_state_machine_diagram/state_machine_diagram.png" alt="State Machine Diagram of the System" width="1000"/>
  <br>
  <em>State Machine Diagram of the System</em>
</p>

## :sparkles: Key Features
- Explicit modeling of system states
- Support for multiple flows (video/audio)
- Clear visualization of user interactions and system transitions
- Useful for debugging, documentation, and system behavior understanding
