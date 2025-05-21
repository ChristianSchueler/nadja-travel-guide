# Nadja - your ADS-friendly AI Travel Guide

An AI-powered travel guide application built with LangChain/LangGraph and Streamlit.

## Features

- Interactive chat interface for travel inquiries
- AI-powered travel recommendations
- Modern and user-friendly interface

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Copy `.env.example` to `.env` and add your API keys:
```bash
cp .env.example .env
```

3. Run the application:
```bash
streamlit run app.py
```

## Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key
- `STREAMLIT_SERVER_PORT`: Port for Streamlit server (default: 8501)
- `STREAMLIT_SERVER_ADDRESS`: Address for Streamlit server (default: 0.0.0.0)
