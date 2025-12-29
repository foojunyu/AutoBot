#!/usr/bin/env python3
"""
Demo script for Penang Chat Bot

This script demonstrates the capabilities of the Penang Bulletins Chat Bot
with pre-scripted conversations.
"""

from chatbot import PenangChatBot
import time


def print_slowly(text, delay=0.02):
    """Print text with a slight delay to simulate typing"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def demo_conversation():
    """Run a demo conversation with the bot"""
    print("\n" + "=" * 70)
    print(" " * 20 + "🌴 PENANG CHAT BOT DEMO 🌴")
    print("=" * 70 + "\n")
    
    bot = PenangChatBot()
    
    # Define demo conversations
    demo_queries = [
        ("Hello!", "Greeting the bot"),
        ("What can you tell me about Penang?", "Getting general information"),
        ("What are the top tourist attractions?", "Exploring attractions"),
        ("Tell me about Penang food", "Learning about cuisine"),
        ("What are the current bulletins?", "Checking bulletins"),
        ("How's the weather?", "Weather information"),
        ("Where can I eat?", "Finding food locations"),
    ]
    
    for query, description in demo_queries:
        print(f"[{description}]")
        print(f"\n👤 You: {query}")
        print("\n🤖 Bot: ", end="")
        
        response = bot.generate_response(query)
        
        # Print response (limit length for demo)
        if len(response) > 500:
            print(response[:500] + "...\n")
        else:
            print(response + "\n")
        
        print("-" * 70)
        time.sleep(1)  # Pause between exchanges
    
    print("\n" + "=" * 70)
    print("Demo completed! The bot is ready to answer your questions.")
    print("Run 'python chatbot.py' to start an interactive session.")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    demo_conversation()
