# Python Chatterbot Chatbot/s

This is a terminal-based program written in Python. This program uses a imported Library called "Chatterbot" along with "ChatterbotCorpusTrainer". There is currently only one functioning Chatbot named "OptimisticBot", who as it's name suggests, the bot is constantly happy and upbeat.

## Instructions for Build and Use

Steps to build and/or run the software:

1. You will need at least Python 3.10 or later installed on your machine.

2. Once you have Python installed, you will need to install the chatterbot library by typing: 'python -m pip install chatterbot' into your machine's terminal.

3. After downloading this repo, the virtual environment attached will provide the functionality and the "brain" for the chatbot.

4. Then you can run ChatBots.py, the program will compile, and then the chatbot will be active. (Mind you, EVERYTHING you say to the chatbot will be logged in db.sqlite3, which this trains the chatbots with more and more input it receives, meaning it's responses grow as you chat with it).

Instructions for using the software:

1. Once you get the repo installed or have Chatterbot and Python working, you compile the ChatBots.py file.
2. Once the program compiles (which it can take a couple seconds), you can interact with the chatbot by typing into the terminal and pressing 'enter' to send a message. The chatbot will then respond.
3. You can exit the program by typing 'exit' into the terminal.

## Development Environment

To recreate the development environment, you need the following software and/or libraries with the specified versions:

* You will need to make sure to download any version higher than or equal to 3.10 of Python.
* You will need to also create a virtual environment on your machine using: 'python -m venv venv', then: 'source venv/bin/activate', and then python -m pip install chatterbot.
* From then on, you can create a Python file in that directory and just type 'from chatterbot import ChatBot' and 'from chatterbot.trainers import ChatterBotCorpusTrainer' to establish the Chatbot along with it's input-based learning. 

## Useful Websites to Learn More

I found these websites useful in developing this software:

* Reading: [This is a GREAT tutorial for how Chatterbot works and how to implement it](https://realpython.com/build-a-chatbot-python-chatterbot/)

* Reading: [Here's another great source that talks about how Chatterbot works and how it can be implemented](https://pypi.org/project/ChatterBot/)

* GitHub Repo Origin: [Here is the GitHub Repo for Chatterbot](https://github.com/gunthercox/ChatterBot)

* YouTube Video: [Here's a great video showing how to install Chatterbot and what's it's like being used](https://www.youtube.com/watch?v=ibu1Pjb6qEM)

## Future Work

The following items I plan to fix, improve, and/or add to this project in the future:

* [ ] I would really like to add more chatbots, each featuring their own one-dimensional expression of various emotions. 
* [ ] Of course training the main chatbot more.
* [ ] Swapping db.sqlite to a JSON stored data since sqlite is a nuisance when it comes to removing or deleting data rows that can corrupt how the Chatbot reacts. 