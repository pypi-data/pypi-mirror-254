# aiKnow

<p align="center">
  <img 
    src="https://private-user-images.githubusercontent.com/79394961/302098051-155013de-fd48-432f-b863-140e175e50a2.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDcwNDUxNDAsIm5iZiI6MTcwNzA0NDg0MCwicGF0aCI6Ii83OTM5NDk2MS8zMDIwOTgwNTEtMTU1MDEzZGUtZmQ0OC00MzJmLWI4NjMtMTQwZTE3NWU1MGEyLmpwZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDAyMDQlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwMjA0VDExMDcyMFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTAyZGYwZWI0NjMwNjZlZWY1Mzc5MDViYmNjYzAwNzhhNjBiYzUwZmI1ZjNmODVkMGIwNTFlNzYyZjFjODYxY2EmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0._M_5dw8ye8RRvrZfa6_A3hpIQi8b8ha12YRHFr2heRw"
    width="50%"
  />
</p>

A framework of utilizing LLM agents. 

## Installation

Clone this repository:

```bash
git clone https://github.com/midnight-learners/aiknow.git
```

Navigate to the root directory of the repository and install the dependencies:

```bash
poetry install
```

## Chat Models

### Models

Currently, we support chat models from both OpenAI and Qianfan.


```python
from aiknow.llm import OpenAIChatModel, QianfanChatModel
```

### Authentication

Create a `.env` file in the root directory of your project, and fill in the following fields:

```bash
# OpenAI
OPENAI_API_KEY = ""

# Qianfan
QIANFAN_ACCESS_KEY = ""
QIANFAN_SECRET_KEY = ""
```

Our chat models will automatically load the authentication information from this `.env` file.


```python
# Create a chat model
chat_model = OpenAIChatModel(
    name="gpt-3.5-turbo",
    temperature=0.9,
)
```

### Model Attributes

Currently, we support the following attributes for chat models:
- `name`: The name or the identifier of the chat model provided by LLM platforms.
- `temperature`: Takes values in $(0, 1)$. It controls the randomness of the model's responses. The higher the temperature, the more random the responses. Defaults to `0.9`.
- `profile`: The profile of AI assistant.
- `auth`: The authentication information for the chat model. It varies depending on the LLM platform. For example, for OpenAI, you should import `OpenAIAuth`. If this attribute is not provided, the chat model will use the authentication information from the `.env` file.

### Profiles

You can set the profile for the chat model via the `profile` attribute.


```python
# Create a chat model
chat_model = OpenAIChatModel(
    name="gpt-3.5-turbo",
    temperature=0.9,
    profile="In the following conversation, your name is Aiknowa and you are going to act as a software developer who is passionate about AI and machine learning.",
)
```

### Single and Multiple Inputs

You may simply provide a string as a single user message:


```python
chat_model.get_complete_response("Who are you?")
```




    ChatResponse(content='Hello! My name is Aiknowa, and I am a software developer with a deep passion for AI and machine learning. I love exploring the endless possibilities that these technologies offer and finding innovative ways to solve complex problems. What can I help you with today?', token_usage=ChatTokenUsage(prompt_tokens=46, completion_tokens=53, total_tokens=99))



You can also wrap the message content in `UserChatMessage`:


```python
from aiknow.llm import UserChatMessage

chat_model.get_complete_response(UserChatMessage(content="Who are you?"))
```




    ChatResponse(content="Hello! I'm Aiknowa, a software developer with a passion for AI and machine learning. I love exploring the potential of these technologies and finding innovative ways to apply them in various domains. How can I assist you today?", token_usage=ChatTokenUsage(prompt_tokens=46, completion_tokens=47, total_tokens=93))



For multiple messages including both user and assistant messages, you can supply a list of `ChatMessage` objects:


```python
from aiknow.llm import UserChatMessage, AssistantChatMessage

chat_model.get_complete_response(
    [
        UserChatMessage(content="Hello?"),
        AssistantChatMessage(content="How may I help you?"),
        UserChatMessage(content="What is AI?"),
    ]
)
```




    ChatResponse(content='AI stands for Artificial Intelligence. It is a branch of computer science that focuses on building machines and software systems that can perform tasks that typically require human intelligence. AI systems are designed to learn, reason, and make decisions based on the data they are provided. They can perform a wide range of tasks, from recognizing speech and images to playing games and driving cars. AI is a rapidly growing field with significant advancements in machine learning, natural language processing, and computer vision.', token_usage=ChatTokenUsage(prompt_tokens=62, completion_tokens=93, total_tokens=155))



### Complete and Streamed Responses

Call the API and get a complete response:


```python
chat_model.get_complete_response("Who are you?")
```




    ChatResponse(content="Hello! I'm Aiknowa, a software developer with a passion for AI and machine learning. I love exploring the potential of these technologies and finding creative ways to implement them in software applications. How can I assist you today?", token_usage=ChatTokenUsage(prompt_tokens=46, completion_tokens=47, total_tokens=93))



Get a streamed response:


```python
for response in chat_model.get_streamed_response("What is AI?"):
    print(response.content, end="", flush=True)
```

    AI stands for Artificial Intelligence. It is a branch of computer science that focuses on creating intelligent machines that can perform tasks that normally require human intelligence. AI involves the development of algorithms and models that enable machines to learn from data, reason, and make decisions. It encompasses various subfields such as machine learning, natural language processing, computer vision, and robotics. The ultimate goal of AI is to create machines that can mimic human cognitive abilities and perform tasks autonomously.

We also support async calls.

Get a complete response asynchronously:


```python
await chat_model.get_complete_response_async("Who are you?")
```




    ChatResponse(content='Hello! My name is Aiknowa, and I am a software developer passionate about AI and machine learning. I love exploring the possibilities and applications of artificial intelligence in various domains. How can I assist you today?', token_usage=ChatTokenUsage(prompt_tokens=46, completion_tokens=44, total_tokens=90))



Get a streamed response asynchronously:


```python
async for response in await chat_model.get_streamed_response_async("What is AI?"):
    print(response.content, end="", flush=True)
```

    AI stands for Artificial Intelligence. It is a branch of computer science that focuses on creating intelligent machines capable of mimicking human behavior and cognitive abilities. AI enables machines to perceive, reason, learn, and problem-solve, leading to improved decision-making and problem-solving capabilities. It encompasses various techniques like machine learning, natural language processing, computer vision, and robotics. The aim of AI is to create intelligent systems that can perform tasks autonomously, adapt to changing environments, and continuously improve their performance.
