# OpenExtract
> A lightweight AI-powered tool for extracting financial insights from documents using OpenAI and Streamlit.
OpenExtract is a Python-based tool for extracting and analyzing financial data from documents like PDFs and DOCX files. It leverages OpenAI’s API for intelligent text extraction and summarization, making financial data processing easy and efficient.

---

## Features

- Extract text and data from PDFs and DOCX files
- Use OpenAI API for advanced text summarization and analysis
- Data processing with pandas and numpy
- Optional machine learning capabilities for classification
- Interactive frontend built with Streamlit for user-friendly interface
- Environment variable management with python-dotenv

---

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/PRASHIK16/OpenExtract.git
cd OpenExtract
Create and activate a virtual environment (optional but recommended):

bash
Copy
Edit
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Set up your environment variables:

Create a .env file in the root directory.

Add your OpenAI API key like this:

env
Copy
Edit
OPENAI_API_KEY=your_api_key_here
Usage
Run the Streamlit app
bash
Copy
Edit
streamlit run streamlit_app.py
This will launch the web interface where you can upload files and analyze financial data.

Running backend scripts
Use the provided Python scripts (main.py, backend.py, etc.) to run data extraction and analysis from the command line or integrate with other systems.

Project Structure
bash
Copy
Edit
OpenExtract/
├── analysis/             # Data analysis modules
├── database/             # Database-related scripts or files
├── parser/               # Document parsing utilities
├── __pycache__/          # Python cache files
├── venv/                 # Virtual environment (optional)
├── backend.py            # Backend logic
├── main.py               # Main script
├── streamlit_app.py      # Streamlit frontend
├── requirements.txt      # Python dependencies
├── README.md             # Project overview and instructions
└── .env                  # Environment variables (not included in repo)
Contributing
Contributions are welcome! Please open issues or pull requests for bug fixes and enhancements.

License
This project is licensed under the MIT License. See the LICENSE file for details.


