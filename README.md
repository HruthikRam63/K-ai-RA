# k*AI*ra: Your *AI*-Driven Personal Assistant

*Unleashing the Power of *AI* in Everyday Tasks*
<h4> kAIra, a cutting-edge voice assistant, orchestrates an array of tasks with unparalleled efficiency. From navigating web portals and delivering real-time updates to personalizing recommendations and providing insightful information, kAIra seamlessly integrates advanced AI capabilities into your daily routine.</h4>

## Project Description
<br clear="both">
<div style="width: 250px; height: 250px; overflow: hidden; border-radius: 50%; display: inline-block;">
  <img src="https://i.postimg.cc/DZs5vZqs/logo.jpg" style="width: 100%; height: 100%; object-fit: cover;" />
</div>


**kAIra** is a state-of-the-art personal assistant application engineered to transform and streamline everyday tasks through the power of *AI*. This sophisticated tool harnesses advanced speech recognition and natural language processing to facilitate seamless interaction and task management. By offering a diverse array of functionalities—ranging from real-time information retrieval and personalized responses to dynamic web searches and entertainment options—`kAIra` epitomizes the integration of technology into daily life. Its design not only enhances productivity but also enriches user engagement, making it an indispensable asset for modern, tech-savvy individuals.

## Project Navigation

- [Project Overview](#kairayour-ai-driven-personal-assistant)
- [Project Description](#project-description)
- [Project Directory Structure](#project-directory-structure)
- [Requirements](#requirements)
- [Development Setup](#development-setup)
  - [macOS and Linux](#for-macos-and-linux)
  - [Windows](#for-windows)
- [Usage Details](#usage-details)
- [Features](#features)
- [Challenges Faced](#challenges-faced)
- [Further Development](#further-development)
- [Contributions](#contributions)
- [Screenshots](#screenshots)


## Project Directory Structure

The project directory is organized as follows:

```
kAIra_Project
├── web_app/
│   ├── static/
│   │   ├── images/
│   │   │   └── logo.png
│   │   └── css/
│   │       └── kAIra_UI.css
│   ├── templates/
│   │   ├── kAIra_frontend.html
│   │   └── results.html
│
├── assistant_services.py
├── kAIra_main.py
└── README.md
```

### Directory Breakdown

- **web_app/**: Contains the web application files.
  - **static/**: Holds static assets such as images and CSS files.
    - **images/**: Directory for image files.
    - **css/**: Directory for CSS files, including `kAIra_UI.css`.
  - **templates/**: Contains HTML templates used for rendering pages.
    - `kAIra_frontend.html`: Main interface template.
    - `results.html`: Template for displaying results.

- **assistant_services.py**: Contains the Python functions that handle various services and functionalities of the assistant.

- **kAIra_main.py**: The main application file that sets up the Flask server, defines routes, and processes commands.

- **README.md**: Documentation file providing an overview of the project.

## Requirements

#### Web Technologies
- **HTML**: For structuring the web pages.
- **CSS**: For styling the web pages, including `kAIra_UI.css` for custom styles.
- **JavaScript**: For implementing client-side interactivity, including `kAIra_features.js` for speech recognition and command handling.

#### Backend
- **Python**: Programming language used for server-side logic.
- **Flask**: Web framework for handling HTTP requests, routing, and rendering templates.

#### Libraries/Frameworks
- **Pyttsx3**: Text-to-speech conversion library for speech synthesis.
- **Flask**: Framework for web server and routing.
- **Speech Recognition API**: For converting spoken commands into text.
- **Requests**: For making HTTP requests to external APIs.

#### Speech Recognition Integration
- **SpeechRecognition API**: For capturing and processing voice commands from users.

#### Data Handling
- **JSON**: For structuring and exchanging data between the frontend and backend.

#### Frontend Assets
- **Google Fonts**: For custom font styles, including 'Teko', 'Playfair Display', and others.
- **Images**: For visual elements, including logos and icons.
- **GIFs**: Background images or animations used for visual effects.

#### Additional Resources
- **External APIs**: For accessing additional functionalities like stock prices, weather, and local information.

## Development Setup

### For macOS and Linux:

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/yourusername/kAIra.git
    ```

2. **Navigate to the Project Directory:**
    ```bash
    cd kAIra
    ```

3. **Install Python Dependencies:**
    Ensure you have Python installed. Create a virtual environment and install the necessary packages.
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

4. **Set Up Environment Variables:**
    Create a `.env` file in the project root and configure any required environment variables.

5. **Start the Flask Server:**
    ```bash
    python kAIra_main.py
    ```

6. **Open the Application:**
    Navigate to `http://localhost:5000` in your web browser to access the application.

### For Windows:

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/yourusername/kAIra.git
    ```

2. **Navigate to the Project Directory:**
    ```bash
    cd kAIra
    ```

3. **Install Python Dependencies:**
    Ensure you have Python installed. Create a virtual environment and install the necessary packages.
    ```bash
    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt
    ```

4. **Set Up Environment Variables:**
    Create a `.env` file in the project root and configure any required environment variables.

5. **Start the Flask Server:**
    ```bash
    python kAIra_main.py
    ```

6. **Open the Application:**
    Navigate to `http://localhost:5000` in your web browser to access the application.

## Usage Details

Once you have set up the `kAIra` application, you can interact with it as follows:

1. **Accessing the Application:**
   Open your web browser and navigate to `http://localhost:5000`. This will load the main interface of `kAIra`.

2. **Voice Interaction:**
   Click the microphone button on the main interface to activate voice recognition. Speak your command or query, and `kAIra` will process and respond accordingly.

3. **Commands and Queries:**
   With `kAIra`, you can greet with "hello" or "hey", check the time, get a joke, perform calculations, ask for tips, play a game, and receive motivational quotes. You can also search Wikipedia, find local info, get recipes, book recommendations, stock prices, flight statuses, and daily updates like horoscopes and historical events.

4. **Error Handling:**
   If `kAIra` fails to understand a command, it will prompt you to try again or provide alternative suggestions.

5. **Voice Feedback:**
   `kAIra` will respond to your queries and commands using voice feedback, ensuring a hands-free and interactive experience.

## Features

`kAIra` is a versatile voice assistant designed to provide a broad array of services through natural language commands. Here are the primary functionalities available:

- **Greetings**
  - **Command:** "Hello" or "Hey"
  - **Action:** Greets the user and offers assistance.

- **Time Inquiry**
  - **Command:** "What time is it?"
  - **Action:** Provides the current time.

- **Web Navigation**
  - **Command:** "Open [website name]"
  - **Action:** Opens the specified website in a new tab.

- **Jokes and Fun**
  - **Command:** "Tell me a joke" or "Fun fact"
  - **Action:** Provides a joke or a fun fact.

- **Calculations and Tips**
  - **Command:** "Calculate [expression]" or "Calculate tip on [amount] [percentage]"
  - **Action:** Evaluates mathematical expressions or computes tip amounts.

- **Local Information**
  - **Command:** "Find [type] nearby"
  - **Action:** Finds and displays local information such as restaurants, gyms, or events.

- **Recipes and Book Recommendations**
  - **Command:** "Recipe for [dish]" or "Recommend a book"
  - **Action:** Provides a recipe or book recommendation.

- **Travel and Stock Information**
  - **Command:** "Travel info for [destination]" or "Stock price of [company]"
  - **Action:** Provides travel information or stock prices.

- **Inspirational Quotes and Daily Horoscope**
  - **Command:** "Inspirational quote" or "Daily horoscope for [sign]"
  - **Action:** Provides an inspirational quote or horoscope.

## Challenges Faced

- **Integration and Compatibility**
  - **Challenge:** Ensuring the seamless integration of text-to-speech (pyttsx3) within the Flask application, with consistent performance across different operating systems.
  - **Solution:** Implemented threading for non-blocking speech synthesis and conducted extensive testing for cross-platform compatibility.

- **Accuracy and Responsiveness**
  - **Challenge:** Achieving accurate speech recognition and managing the responsiveness of text-to-speech functionalities.
  - **Solution:** Fine-tuned the speech recognition model and handled errors gracefully to enhance responsiveness.

- **Dynamic URL and Command Handling**
  - **Challenge:** Creating flexible URL handling and processing diverse user commands without hardcoding.
  - **Solution:** Developed dynamic URL management and a robust command-processing system.

- **UI/UX Design**
  - **Challenge:** Designing a user-friendly interface with interactive elements and ensuring real-time feedback.
  - **Solution:** Enhanced UI/UX with dynamic tooltips, interactive elements, and synchronized voice interactions.

- **Concurrency and Performance**
  - **Challenge:** Managing concurrent audio playback and optimizing performance.
  - **Solution:** Implemented concurrency management techniques and optimized code for minimal latency.

- **Debugging and Error Management**
  - **Challenge:** Addressing issues related to speech recognition, text-to-speech functionality, and dynamic content rendering.
  - **Solution:** Employed comprehensive debugging and error handling strategies.

## Further Development

The following enhancements are planned for future versions of `kAIra` to improve functionality and user experience:

- **Enhanced Natural Language Understanding**  
  - We aim to implement advanced NLP models to better process user commands, integrating machine learning algorithms and context-aware processing for more intuitive interactions.

- **Personalization Features**  
  - Users will be able to customize responses and voice preferences through user profiles that store settings for speech, interaction style, and favorite commands.

- **Expanded Service Integration**  
  - Support for additional services, such as smart home devices and third-party APIs, will be added by developing connectors and integrations for popular services and IoT devices.

- **Multilingual Support**  
  - `kAIra` will support multiple languages by implementing language detection and translation features, broadening its accessibility.

- **Mobile App Development**  
  - Mobile applications for iOS and Android will be created to offer `kAIra` on-the-go, with synchronized functionalities and notifications.

- **Improved Security and Privacy**  
  - Data protection and user privacy will be enhanced through encryption and privacy controls for managing data access.

## Contributions

Contributions to the `kAIra` project are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your changes.
3. Commit your changes and push to your branch.
4. Open a pull request with a clear description of your changes.

## Screenshots

<p align="center">
    <img src="https://i.postimg.cc/xjb0nRrb/Screenshot-2024-08-14-220245.png" alt="Screenshot 1" width="300"/>
    <img src="https://i.postimg.cc/15Pb2cyS/Screenshot-2024-08-14-220311.png" alt="Screenshot 2" width="300"/>
    <img src="https://i.postimg.cc/cC7266MP/Screenshot-2024-08-14-220301.png" alt="Screenshot 3" width="300"/>
</p>
