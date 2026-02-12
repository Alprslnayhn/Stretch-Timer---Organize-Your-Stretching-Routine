
---

# 🏋️‍♂️ Stretch Timer & Workout Manager

**A robust, client-side web application designed to orchestrate complex physical therapy routines, interval training, and stretching sessions.**

Initially developed as a simple loop timer, this project has evolved into a fully-featured **Workout Management System**. It features local data persistence, custom audio cues, and a dynamic state machine capable of handling both duration-based and repetition-based exercises.

---

## 📋 Table of Contents

* [Features](https://www.google.com/search?q=%23-features)
* [Architecture & Evolution](https://www.google.com/search?q=%23-architecture--evolution)
* [Installation & Usage](https://www.google.com/search?q=%23-installation--usage)
* [Project Structure](https://www.google.com/search?q=%23-project-structure)
* [Contributing](https://www.google.com/search?q=%23-contributing)
* [License](https://www.google.com/search?q=%23-license)

---

## ✨ Features

### Core Functionality

* **Hybrid Exercise Support:** Seamlessly mix **Time-based** (e.g., Planks), **Repetition-based** (e.g., Squats), and **Hybrid** exercises in a single routine.
* **Dynamic State Machine:** The timer logic handles complex transitions: `Prepare` -> `Work` -> `Rest (Inter-set)` -> `Rest (Inter-exercise)`.
* **Smart Audio Feedback:** Distinct auditory cues for start, stop, and completion events.
* **Auto-Flow Options:** Configurable settings to either auto-advance between sets or wait for user confirmation (ideal for rep tracking).

### Data Persistence

* **Local Storage Integration:** Routines are serialized and stored in the browser's `localStorage`. No database or backend required.
* **CRUD Operations:** Users can Create, Read, Update, and Delete custom workout programs.

---

## 🏗 Architecture & Evolution

This project demonstrates a clear evolution from a stateless script to a stateful application.

### v1.0: The Stateless Loop (Legacy)

The initial iteration was a linear script designed for uniform stretching loops. It lacked state retention and flexibility.

* **Limitation:** Could only handle a single duration variable for all sets.
* **UI:** Minimalist, single-purpose interface.

*(Fig 1: The initial prototype focusing on simple loops)*

---

### v2.0: The Workout Manager (Current)

The codebase was refactored to support Object-Oriented principles, allowing for modular exercise objects and a persistent workout state.

#### 1. Routine Construction (The Builder Pattern)

Users define complex workout structures. The application parses inputs (sets, reps, rest times) into a structured JSON-like object before execution.

#### 2. Program Management & Persistence

The UI now includes a dashboard for managing saved routines. This allows for rapid context switching between different therapy sessions (e.g., "Hyperlordosis Correction" vs. "Morning Stretch").

#### 3. Execution Environment

The runtime interface is optimized for focus. It features a reactive UI that updates the DOM based on the timer's current state tick.

* **Visual Feedback:** Progressive circular progress bar.
* **Interaction:** Manual overrides for repetition completion.

#### 4. System Configuration

Global settings manage the application's behavior, controlling audio volume, vibration feedback, and transition logic.

---

## 🚀 Installation & Usage

This project is a **Static Web Application**. It requires no backend compilation or package manager installation.

### Option 1: Direct Usage

Simply clone the repository and open the main HTML file in any modern browser.

```bash
git clone https://github.com/Alprslnayhn/Stretch-Timer---Organize-Your-Stretching-Routine.git
# Navigate to folder and double-click index.html

```

### Option 2: Local Server (Recommended)

For the best experience (especially to avoid CORS issues with audio assets), serve the files using Python's built-in HTTP server:

```bash
cd Stretch-Timer---Organize-Your-Stretching-Routine
python3 -m http.server 8000

```

Then visit `http://localhost:8000` in your browser.

---

## 📂 Project Structure

```text
/
├── index.html          # Main application entry point (formerly 2.2-main.html)
├── css/                # Stylesheets and responsive design rules
├── js/                 # Application logic (Timer class, UI handlers)
├── assets/             # Audio files (beep.mp3, finish.mp3)
├── img/                # Screenshots for documentation
└── README.md           # Project documentation

```

---

## 🤝 Contributing

Contributions to improve the logic or UI are welcome. Please follow these steps:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/NewFeature`).
3. Commit your changes.
4. Push to the branch and open a **Pull Request**.

---

## 📄 License

This project is open-source and available under the [MIT License](https://www.google.com/search?q=LICENSE).

---

*Developed by [Alprslnayhn](https://www.google.com/search?q=https://github.com/Alprslnayhn) - 2026*

---

