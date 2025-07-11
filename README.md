# 🌦 Weather App

A simple and elegant weather web application built with *Django* and *Bootstrap* that lets you search for any city and view the current weather conditions.

---

## 🚀 Features

- 🔍 Search for any city to get the current weather  
- 🌡 Displays temperature, weather description, humidity, and wind speed  
- 📦 Integrates with [OpenWeatherMap API](https://openweathermap.org/api)  
- 💡 Uses .env file for secure API key management  
- 🧩 Built with Django and Bootstrap for a responsive and clean UI

---


## 🛠 How to Run the Project

### 1️⃣ Clone or Download the Project

Download the project as a ZIP file or clone it using:

bash
git clone https://github.com/your-username/weather-app.git
cd weather-app


---

### 2️⃣ Install Django and Other Dependencies

Make sure Python is installed on your system. Then open a terminal and run:

bash
pip install django requests python-dotenv


---

### 3️⃣ Get Your OpenWeatherMap API Key

- Visit [OpenWeatherMap](https://openweathermap.org/api)  
- Sign up and generate a free API key

---

### 4️⃣ Create a .env File

In the same directory as manage.py, create a file named .env and add the following:

env
API_KEY=your_api_key_here
URL=https://api.openweathermap.org/data/2.5/weather


Replace your_api_key_here with your actual API key.

---

### 5️⃣ Run the Django Development Server

Run the following command to start the server:

bash
python manage.py runserver


Then open your browser and go to:

[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🧠 Tech Stack

- *Backend*: Django, Python  
- *Frontend*: HTML, CSS, Bootstrap  
- *API*: OpenWeatherMap  
- *Security*: .env for API key management

---

## 👨‍💻 Author

Made with ❤ by [Ashutosh Rath]

---

## 📄 License

This project is licensed under the [MIT License](LICENSE)
