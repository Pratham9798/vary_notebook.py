# Vary Notebook Script

This repository contains a Python script to generate variations of Jupyter notebook content using OpenAI's GPT-4 model. Follow the instructions below to set up your environment and run the script.

## Prerequisites

- Python 3.x
- An OpenAI API key

## Setup

### Step 1: Install Python

1. Download the latest version of Python from the [official website](https://www.python.org/downloads/).
2. Run the installer and make sure to check the box that says "Add Python to PATH" before clicking "Install Now".

### Step 2: Install Required Packages

Open Command Prompt (Windows) or Terminal (macOS/Linux) and run the following command to install the required packages:

```sh
pip install openai nbformat

notebook_path = 'C:\\Users\\YourName\\Documents\\SampleNotebook.ipynb'
new_notebook_path = 'C:\\Users\\YourName\\Documents\\SampleNotebook_Variation.ipynb'
python vary_notebook.py

