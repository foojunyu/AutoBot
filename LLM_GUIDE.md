# LLM Integration Guide

This guide explains how to set up and use the free LLM API integration for enhanced chat bot responses.

## Overview

The Penang Chat Bot now supports integration with free LLM APIs to provide:
- Dynamic, context-aware responses
- More natural conversations
- Up-to-date information beyond the built-in knowledge base
- Ability to handle complex or open-ended questions

## Supported LLM Providers

### 1. Groq (Recommended)

**Why Groq?**
- ⚡ Extremely fast inference
- 🆓 Generous free tier
- 🤖 Access to Llama 3.1 models
- 🔒 Secure and reliable

**Getting Started:**

1. Visit https://console.groq.com/keys
2. Sign up for a free account
3. Create a new API key
4. Copy your API key

**Free Tier Limits:**
- 30 requests per minute
- 14,400 requests per day
- More than enough for personal use!

### 2. HuggingFace Inference API

**Why HuggingFace?**
- 🤗 Large model selection
- 🆓 Free tier available
- 🔬 Access to latest open-source models
- 📚 Great for experimentation

**Getting Started:**

1. Visit https://huggingface.co/settings/tokens
2. Sign up for a free account
3. Create a new access token (read access is sufficient)
4. Copy your token

**Free Tier Limits:**
- Rate-limited based on usage
- May experience slower responses during peak times

## Setup Instructions

### Step 1: Install Dependencies

```bash
cd AutoBot
pip install -r requirements.txt
```

### Step 2: Configure API Key

**Option A: Using .env file (Recommended)**

1. Copy the example file:
```bash
cp .env.example .env
```

2. Edit `.env` and add your API key:
```
# For Groq (recommended)
GROQ_API_KEY=gsk_your_actual_api_key_here

# OR for HuggingFace
# HUGGINGFACE_API_KEY=hf_your_actual_token_here
```

**Option B: Using Environment Variables**

```bash
# For Groq
export GROQ_API_KEY="gsk_your_actual_api_key_here"

# OR for HuggingFace
export HUGGINGFACE_API_KEY="hf_your_actual_token_here"
```

### Step 3: Run the Bot

```bash
python chatbot.py
```

You should see:
```
🤖 LLM mode enabled - Using AI for enhanced responses!
```

## Usage Examples

### With LLM Enabled

```
You: What's the best time to visit Penang for food lovers?

Bot: For food lovers, Penang is great year-round, but the best time is 
     December to February when the weather is cooler and more comfortable 
     for exploring outdoor hawker centers. You'll also catch the Penang 
     Food Festival if you visit during these months. The outdoor dining 
     experience at places like Gurney Drive and New Lane Hawker Centre 
     is much more pleasant in cooler weather!
```

### Complex Questions

```
You: I'm vegetarian, what can I eat in Penang?

Bot: Penang has excellent vegetarian options! Look for Indian vegetarian 
     restaurants (serving dosa, roti canai without egg), Chinese Buddhist 
     vegetarian restaurants, and many hawker stalls offer vegetarian 
     versions of local dishes. Try vegetarian Char Kway Teow, vegetarian 
     Nasi Kandar, and fresh tropical fruits...
```

## How It Works

1. **Context Injection**: The bot provides the LLM with Penang knowledge as context
2. **Conversation History**: Recent messages are included for coherent conversations
3. **Response Generation**: The LLM generates a response based on your question and context
4. **Fallback**: If LLM fails or is unavailable, the bot uses built-in responses

## Troubleshooting

### "No LLM API key found" Message

**Problem:** The bot can't find your API key

**Solutions:**
- Check that `.env` file exists and contains your API key
- Ensure the key name is exactly `GROQ_API_KEY` or `HUGGINGFACE_API_KEY`
- Try setting the environment variable directly
- Verify your API key is valid

### Slow Responses

**Problem:** The bot takes a long time to respond

**Solutions:**
- This is normal for HuggingFace free tier during peak hours
- Switch to Groq for faster responses
- Check your internet connection

### API Errors

**Problem:** The bot shows API error messages

**Solutions:**
- Verify your API key is correct and active
- Check if you've exceeded rate limits
- Ensure you have internet connectivity
- Try the fallback provider

### Bot Falls Back to Knowledge Base

**Problem:** Bot uses built-in responses instead of LLM

**Solutions:**
- Check that LLM mode enabled message appears at startup
- Verify API key is set correctly
- Check for error messages in console
- The bot automatically falls back if LLM fails

## Testing LLM Integration

Test that LLM is working:

```python
from chatbot import PenangChatBot
from llm_integration import LLMManager

# Check if LLM is available
manager = LLMManager()
print(f"LLM available: {manager.is_available()}")

# Test the bot
bot = PenangChatBot(use_llm=True)
response = bot.generate_response("Tell me something interesting about Penang")
print(response)
```

## Privacy and Security

- Your API keys are stored locally and never shared
- Conversations are not logged by the bot
- Each provider has their own privacy policy
- .env file is gitignored to prevent accidental commits

## Cost Considerations

Both Groq and HuggingFace offer **generous free tiers** that are more than sufficient for:
- Personal projects
- Learning and experimentation
- Small-scale applications

For production use at scale, review each provider's pricing.

## Disabling LLM

To use the bot without LLM (using only built-in knowledge):

```python
bot = PenangChatBot(use_llm=False)
```

Or simply don't set any API keys - the bot will automatically use fallback mode.

## Support

For issues or questions:
1. Check the main README.md
2. Review EXAMPLES.md for usage patterns
3. Open an issue on GitHub
