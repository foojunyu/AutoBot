# AutoBot - Penang Bulletins Chat Bot 🌴

A knowledgeable chat bot that can answer questions about Penang bulletins, tourist information, food, culture, and more!

**NEW:** Now enhanced with free LLM API integration for dynamic and latest responses! 🤖

## Features

- 🏛️ General information about Penang
- 🗺️ Tourist attractions and places to visit
- 🍜 Food, cuisine, and dining recommendations
- 🎭 Culture, heritage, and festivals
- 📰 Current bulletins and updates
- 🚌 Transportation and practical information
- ☀️ Weather and travel tips
- 🤖 **AI-powered responses** using free LLM APIs (Groq or HuggingFace)

## Quick Start

### Prerequisites

- Python 3.7 or higher

### Installation

1. Clone the repository:
```bash
git clone https://github.com/foojunyu/AutoBot.git
cd AutoBot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. **(Optional but Recommended)** Set up LLM API for enhanced responses:
   
   Copy the example environment file:
   ```bash
   cp .env.example .env
   ```
   
   Get a free API key from one of these providers:
   - **Groq** (Recommended): https://console.groq.com/keys
   - **HuggingFace**: https://huggingface.co/settings/tokens
   
   Edit `.env` and add your API key:
   ```
   GROQ_API_KEY=your_api_key_here
   ```

### Running the Chat Bot

Run the chat bot in CLI mode:
```bash
python chatbot.py
```

**Note:** The bot works in two modes:
- **LLM Mode** (with API key): Uses AI to generate dynamic, context-aware responses
- **Fallback Mode** (without API key): Uses built-in knowledge base with pre-defined responses

## Usage Examples

Once the bot is running, you can ask questions like:

- "What are the top tourist attractions in Penang?"
- "Tell me about Penang food"
- "What are the current bulletins?"
- "How do I get to Penang?"
- "What's the weather like?"
- "Tell me about Penang culture"

### Example Conversation

```
You: Hello
Bot: Hello! 👋 Welcome to the Penang Bulletins Chat Bot! I'm here to help you 
     learn about Penang, the Pearl of the Orient...

You: What are the famous dishes?
Bot: **Penang Food Culture**

Penang is renowned as Malaysia's food capital

**Famous Dishes:**
• Char Kway Teow: Stir-fried flat rice noodles
• Assam Laksa: Spicy tamarind fish noodle soup
• Nasi Kandar: Rice served with various curry dishes
...

You: Show me the current bulletins
Bot: **Current Penang Bulletins & Updates:**

1. **Transportation Updates**
   Penang has an efficient public transport system...
...
```

## Project Structure

```
AutoBot/
├── chatbot.py           # Main chat bot implementation
├── penang_knowledge.py  # Knowledge base about Penang
├── llm_integration.py   # LLM API integration (Groq, HuggingFace)
├── requirements.txt     # Python dependencies
├── .env.example         # Example environment variables
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## LLM Integration

The bot now supports free LLM APIs for generating dynamic responses:

### Supported Providers

1. **Groq** (Recommended)
   - Fast inference with Llama 3.1 model
   - Free tier available
   - Get API key: https://console.groq.com/keys

2. **HuggingFace Inference API**
   - Access to Mistral 7B model
   - Free tier available
   - Get API key: https://huggingface.co/settings/tokens

### How It Works

- When you ask a question, the bot uses LLM to generate contextual responses
- The LLM is provided with Penang knowledge as context
- Conversation history is maintained for coherent multi-turn conversations
- Falls back to rule-based responses if LLM is unavailable

## Knowledge Base

The bot has extensive knowledge about:

- **General Info**: Location, population, languages, UNESCO status
- **Tourist Attractions**: George Town, Penang Hill, Kek Lok Si Temple, Penang National Park, Batu Ferringhi Beach
- **Food**: Famous dishes like Char Kway Teow, Assam Laksa, Nasi Kandar, and hawker centre locations
- **Culture**: Festivals, ethnic diversity, Peranakan heritage
- **Bulletins**: Transportation, tourism guidelines, weather, cultural events, conservation efforts
- **Practical Info**: Transportation, weather, currency, emergency contacts

## Contributing

Feel free to contribute by:
1. Adding more Penang information to the knowledge base
2. Improving the conversation handling
3. Adding new features
4. Reporting bugs

## License

MIT License
