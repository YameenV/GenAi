# Task Create an infinite loop when enables its user to chat with Llama-3

This is a chat application built using Streamlit, LangChain, and ChatGroq. The application allows users to create multiple chat conversations and interact with an AI assistant.

## Demo Video

Check out a quick demo of the chat application:

[![Demo Video]](https://github.com/YameenV/GenAi/assets/90130177/b1cbb31c-c29e-4795-b215-d81cc80c5f13)

## Features

- Create and manage multiple chat conversations.
- AI responses generated using LangChain's `LLMChain`.
- Persistent chat history for each conversation.


## Setup and Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- A `.env` file with your Groq API key.

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/YameenV/GenAi.git
    cd GenAi
    ```

2. Create a virtual environment and activate it:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory of the project and add your Groq API key:

    ```
    GROQ_KEY=your-groq-api-key
    ```

## Running the Application

To start the Streamlit application, run the following command:

```sh
streamlit run app.py
```
