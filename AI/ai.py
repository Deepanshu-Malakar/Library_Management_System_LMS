# main_app.py

import os
from dotenv import load_dotenv # Used to load the .env file
from google import genai

# 1. Load the environment variables from the .env file
# This makes GEMINI_API_KEY available to your script
load_dotenv() 

# 2. The client will automatically look for the GEMINI_API_KEY
# environment variable that we just loaded.

def query(prompt):
    try:
        client = genai.Client()

        # 3. Use the client to make an API call
        response = client.models.generate_content(
            model="gemini-2.5-flash", 
            contents=prompt
        )

        
        return response.text

    except Exception as e:
        return e
        print(f"An error occurred: {e}")
        print("\nPlease ensure your .env file is correctly set up and contains a valid GEMINI_API_KEY.")

