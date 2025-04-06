# Getting Started with Claude SDK

A collection of simple examples showing how to use Claude's API in Python. Perfect for beginners who want to build AI applications with Claude!

## What is Claude?

Claude is Anthropic's AI assistant that can help with:

- Writing and analysis
- Answering questions
- Code assistance
- Language translation
- And much more!

## Requirements

- Python 3.7.1+
- Anthropic API key ([Sign up here](https://www.anthropic.com/))

## Quick Start

1. **Install Claude's SDK**

   ```bash
   pip install anthropic python-dotenv
   ```

2. **Set Up Your API Key**
   ```bash
   # Create a .env file and add your key
   ANTHROPIC_API_KEY=your_api_key_here
   ```

## Example Apps

### 1. Basic Translation (`hello.py`)

```python
from anthropic import Anthropic
client = Anthropic(api_key=api_key)

# Simple example of calling Claude
response = client.messages.create(
    model="claude-3-sonnet",
    messages=[{"role": "user", "content": "Translate hello to French"}]
)
```

### 2. Interactive Chat (`chatbot.py`)

```python
# Basic chat that remembers conversation history
conversation_history = []
response = client.messages.create(
    model="claude-3-sonnet",
    messages=conversation_history
)
```

### 3. Specialized Assistant (`ChefBot.py`)

```python
# Custom AI assistant with specific personality
client.messages.create(
    model="claude-3-sonnet",
    system="You are ChefBot, an expert culinary assistant...",
    messages=[...]
)
```

## Try It Out!

1. **Run the Basic Translator**

   ```bash
   python hello.py
   ```

2. **Chat with Claude**

   ```bash
   python chatbot.py
   ```

3. **Get Cooking Help**
   ```bash
   python ChefBot.py
   ```

## Key Concepts

- **Messages**: The basic unit of conversation with Claude
- **System Prompts**: Instructions that shape Claude's behavior
- **Conversation History**: Maintaining context across interactions
- **Models**: Different versions of Claude (we're using claude-3-sonnet)

## Learn More

- [Claude API Documentation](https://docs.anthropic.com/)
- [Python SDK Reference](https://github.com/anthropics/anthropic-sdk-python)
- [Best Practices](https://docs.anthropic.com/claude/docs/best-practices)
