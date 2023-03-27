# ChatGPT sample for Python

This is a Python sample code to try the GPT-3.5 series model with the OpenAI API.

## Use a virtual environment if needed

```:bash
python -m venv venv
source venv/bin/activate
```

## Install packages

### When you are using a virtual environment

```:bash
venv/bin/python -m pip install --upgrade pip openai
```

### When you are not using a virtual environment

```:bash
python -m pip install --upgrade pip openai
```

## Set OPENAI_API_KEY

export OPENAI_API_KEY="sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

## Start conversation

Either way, typing bye will exit.

### When trying `openai.ChatCompletion` (recommendation)

```:bash
python chat-completion.py
```

### When trying `openai.Completion` (not recommendation)

```:bash
python completion.py
```

### When deactivating a virtual environment

```:bash
deactivate
```
