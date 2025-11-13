from openai import OpenAI
import os
import dotenv
import mysql.connector
import random

conn = mysql.connector.connect(host = "localhost",
                               user = "root",
                               password = "1234")
cur = conn.cursor()
cur.execute("use library")

dotenv.load_dotenv()

api = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api)


def count_books():
    cur.execute("select * from books")
    return len(cur.fetchall())

def latest_books():
    cur.execute("select distinct title,author,edition from books")
    b = cur.fetchall()
    b.reverse()
    books = []
    for i in range(min(4,len(b))):
        books.append(b[i])
    return books
    


def detect_intent(user_message):
    try:
        system_prompt = """
    You are an intent classifier for library management system. 
    Your job is to categorize the user's question into one of the following:

    - count_books          → user wants to know how many books exist in this library
    - latest_books         → user wants to know new or recently added books
    - books_by_author      → user asks for books of an author
    - chatbot_name         → user asks your name
    - creator_name         → user asks your creator or this software's creator name
    - general_answer       → anything else (general chat)


    Respond ONLY with the intent name. No other text.
    """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return ""
        print(f"An error occurred: {e}")
        print("\nPlease ensure your .env file is correctly set up and contains a valid GEMINI_API_KEY.")

        
def query(prompt):
    intent = detect_intent(prompt)
    if intent == "count_books":
        return f"There are {count_books()} books in the library"
    elif intent == "latest_books":
        books = latest_books()
        ret = f"newly added books are:\n"
        for i in books:
            ret += f"{i[0]} by {i[1]} edition {i[2]}\n"
        return ret
    elif intent == "chatbot_name":
        name = ["my name is Jarvis","I am Jarvis","You can call me Jarvis","Jarvis is my name"]
        random.shuffle(name)
        return name[0]
    elif intent == "creator_name":
        name = ["Deepanshu Malakar","Deepanshu Malakar created me","Its Deepanshu","I was programmed by Deepanshu"]
        random.shuffle(name)
        return name[0]
    else:
        try:
            

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

# while True:
#     message = input("YOUR MESSAGE : ")
#     if message == "quit":
#         break
#     print("AI MESSAGE : ",query(message))
