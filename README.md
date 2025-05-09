# 🚗 AI-Powered Vehicle Maintenance Assistant

A smart Streamlit-based chatbot powered by OpenAI and LangChain, designed to assist users with car maintenance queries, fuel cost estimations, and real-time weather checks for travel planning.

---

## 📌 Features

- **Conversational Chat UI**: Built with Streamlit, supports natural chat with history.
- **Memory**: Retains chat context using LangChain memory.
- **Tool Integration**:
  - **Fuel Cost Calculator**: Estimates trip fuel cost based on distance, fuel efficiency, and price.
  - **Live Weather Tool**: Fetches real-time weather for any city using OpenWeatherMap API.

---

## 🛠️ Technologies Used

- [LangChain](https://github.com/langchain-ai/langchain)
- [Streamlit](https://streamlit.io/)
- [OpenAI GPT-4](https://platform.openai.com/)
- [OpenWeatherMap API](https://openweathermap.org/api)
- Python 3.10+

---

## 📁 Project Structure

```
vehicle_maintenance_assistant/
│
├── app.py                    # Streamlit frontend
├── chatbot.py                # LangChain agent & tool setup
├── memory.py                 # Chat history (LangChain memory)
├── fuel_cost_tool.py         # Fuel cost calculator tool
├── weather_tool.py           # Weather API integration
├── vehicle_prompt.py         # (Optional) Prompt template (not used in final agent)
├── .env                      # API keys
└── requirements.txt          # Dependencies
```

---

## ⚙️ Installation

### 1. Clone the Repo

```bash
git clone https://github.com/Simeon-wansi/Vehicle_maintenance_assistant.git
cd vehicle-maintenance-assistant
```

### 2. Set Up Environment

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file:

```
OPENAI_API_KEY=your_openai_key
OPENWEATHER_API_KEY=your_openweather_key
```

---

## ▶️ Running the App

```bash
streamlit run app.py
```

The app will launch in your browser at `http://localhost:8501`.

---

## 💬 How to Use

### General Questions
> “What does it mean if the ABS light is on?”  
> “When should I change my engine oil?”

### Fuel Cost Estimation
> “How much does it cost to drive 200 km if fuel is 3.5 AED/L and my car does 12 km/l?”

### Weather Forecast
> “What’s the current weather in Abu Dhabi?”  
> “How hot is it in Douala today?”

---

## 🔧 Tools Description

### `fuel_cost_calculator`
```python
@tool
def fuel_cost_calculator(distance_km: float, fuel_efficiency_km_per_l: float, fuel_price_per_l: float)
```
Estimates the fuel cost of a trip.

### `get_current_weather`
```python
@tool
def get_current_weather(city: str)
```
Returns current temperature, weather conditions, and humidity for a given city.

---

## 🧠 LangChain Architecture

- **Agent Type**: Tool-calling Agent
- **Memory**: `ConversationBufferMemory`
- **LLM**: `ChatOpenAI` (GPT-4) via `langchain_openai`
- **Tools**: Integrated with `@tool` decorators

---

## 🚀 Future Improvements

- Add **booking integrations** (e.g. service appointment API)
- Include **Google Maps API** for locating nearby garages
- Add **vehicle maintenance checklist** by car model
- Deploy to Streamlit Cloud or Hugging Face Spaces
