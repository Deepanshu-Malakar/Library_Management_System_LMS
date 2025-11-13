from openai import OpenAI
import os
import dotenv

dotenv.load_dotenv()

api = os.getenv("OPENAI_API_KEY")

def query(prompt):
    try:
        client = OpenAI(api_key=api)

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        
        return response.choices[0].message.content

    except Exception as e:
        return e
        print(f"An error occurred: {e}")
        print("\nPlease ensure your .env file is correctly set up and contains a valid GEMINI_API_KEY.")

