CHAT_APP_IN_PYTHON

Connect, Communicate, Conquer in Real-Time

last-commit repo-top-language repo-language-count
Built with the tools and technologies:

Python

Table of Contents

Overview
Getting Started
Prerequisites
Installation
Usage
Testing
Overview

chat_app_in_python is a straightforward, multi-threaded chat system designed to facilitate real-time text communication between multiple clients and a central server. It provides a solid foundation for building interactive chat applications within local network environments.

Why chat_app_in_python?

This project simplifies the development of real-time messaging systems. The core features include:

🟢 Concurrency: Supports multiple clients simultaneously through multi-threaded server architecture.
🔵 Bidirectional Communication: Enables seamless, real-time message exchange between clients and server.
🟠 Client Management: Handles user interactions and message sending/receiving efficiently.
🟣 Message Broadcasting: Ensures messages are broadcasted to all connected clients instantly.
🟡 Session Handling: Manages user sessions and dynamic join/leave events smoothly.
Getting Started

Prerequisites

This project requires the following dependencies:

Programming Language: Python
Package Manager: Conda
Installation

Build chat_app_in_python from the source and install dependencies:

Clone the repository:

❯ git clone https://github.com/Abdullah-319/chat_app_in_python
Navigate to the project directory:

❯ cd chat_app_in_python
Install the dependencies:

Using conda:

❯ conda env create -f conda.yml
Usage

Run the project with:

Using conda:

conda activate {venv}
python {entrypoint}
Testing

Chat_app_in_python uses the {test_framework} test framework. Run the test suite with:

Using conda:

conda activate {venv}
pytest
⬆ Return
