import speech_recognition as sr
import os
import webbrowser
import openai
import datetime


chatStr = ""
def chat(query):
    global chatStr
    #print(chatStr)
    openai.api_key = ""#apikey
    chatStr += f"Human: {query}\n My Automation: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]


def ai(prompt):
    openai.api_key = ""#apikey
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=3000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)


def say(text):
    os.system(f'say "{text}"')


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query.lower()
        except Exception as e:
            return "Some Error Occurred. Sorry from My Automation"


if __name__ == '__main__':
    print('Welcome to My Automation')
    say("My Automation")
    while True:
        print("Listening...")
        query = takeCommand()
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"],]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
        
        if "open music" in query:
            musicPath = ""#mp3 music path
            os.system(f"open {musicPath}")
        elif "the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            mint = datetime.datetime.now().strftime("%M")
            say(f"Sir time is {hour} hour and {mint} minutes")
        elif "open facetime" in query:
            os.system(f"")#path
        elif "open passky" in query:
            os.system(f"")#path
        elif "using artificial intelligence" in query:
            ai(prompt=query)
        elif "quit my automation" in query:
            exit()
        elif "reset chat" in query:
            chatStr = ""
        else:
            print("Chatting...")
            chat(query)
