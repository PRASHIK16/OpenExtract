# OpenExtract
This is a Streamlit-based web application that extracts key financial metrics and insights from financial documents or structured data using the OpenAI API. It summarizes the financial data, aggregates key metrics, and visually represents the insights using interactive graphs.

🚀 Features
🔐 Secure user authentication (see test_auth_flow.py)

📄 Parses and processes financial data

🤖 Leverages OpenAI's LLM for summarization & metric extraction

📊 Interactive visualizations using Plotly

📁 Organized modular codebase (backend, parser, database, etc.)

🛠️ Tech Stack
Frontend: Streamlit

Backend: Python

AI/ML: OpenAI API

Data Viz: Plotly

Authentication: JSON-based user auth

Environment: Virtualenv (venv)

📂 Project Structure
graphql
Copy
Edit
Financial_data_extraction_using_openai_api/
│
├── analysis/                # For analysis scripts
├── database/                # Database or data handling
├── parser/                  # Parsing logic
├── venv/                    # Virtual environment
├── api_key.py               # OpenAI API key storage
├── backend.py               # Core backend logic
├── main.py                  # Entry point for Streamlit
├── openapi_helper.py        # Functions interacting with OpenAI
├── requirements.txt         # Dependencies
├── streamlit_app.py         # Additional streamlit UI logic
├── test_auth_flow.py        # Auth flow tests
├── users.json               # User data for login
└── utils.py                 # Utility functions
