"""
Tests for Penang Chat Bot

This module contains tests to verify the chat bot functionality.
"""

from chatbot import PenangChatBot
from penang_knowledge import get_penang_info, search_penang_info


def test_bot_initialization():
    """Test that bot initializes correctly"""
    bot = PenangChatBot(use_llm=False)  # Disable LLM for testing
    assert bot is not None
    assert bot.conversation_history == []
    print("✓ Bot initialization test passed")


def test_greeting():
    """Test greeting responses"""
    bot = PenangChatBot(use_llm=False)  # Disable LLM for testing
    response = bot.generate_response("Hello")
    assert "Welcome" in response
    assert "Penang" in response
    print("✓ Greeting test passed")


def test_tourist_attractions():
    """Test tourist attractions queries"""
    bot = PenangChatBot(use_llm=False)  # Disable LLM for testing
    response = bot.generate_response("What are the tourist attractions?")
    assert "George Town" in response or "tourist" in response.lower()
    print("✓ Tourist attractions test passed")


def test_food_info():
    """Test food information queries"""
    bot = PenangChatBot(use_llm=False)  # Disable LLM for testing
    response = bot.generate_response("Tell me about food")
    assert "food" in response.lower() or "dish" in response.lower()
    print("✓ Food information test passed")


def test_bulletins():
    """Test bulletins queries"""
    bot = PenangChatBot(use_llm=False)  # Disable LLM for testing
    response = bot.generate_response("What are the current bulletins?")
    assert "bulletin" in response.lower() or "update" in response.lower()
    print("✓ Bulletins test passed")


def test_general_info():
    """Test general information queries"""
    bot = PenangChatBot(use_llm=False)  # Disable LLM for testing
    response = bot.generate_response("What is Penang?")
    assert "Penang" in response
    assert "Malaysia" in response or "Pearl of the Orient" in response
    print("✓ General information test passed")


def test_conversation_history():
    """Test conversation history tracking"""
    bot = PenangChatBot(use_llm=False)  # Disable LLM for testing
    bot.generate_response("Hello")
    bot.generate_response("What is Penang?")
    
    assert len(bot.conversation_history) == 4  # 2 user messages + 2 bot responses
    print("✓ Conversation history test passed")


def test_knowledge_base():
    """Test knowledge base access"""
    info = get_penang_info("general")
    assert info is not None
    assert "name" in info
    print("✓ Knowledge base test passed")


def test_search_functionality():
    """Test search functionality"""
    categories = search_penang_info("food")
    assert "food_culture" in categories
    print("✓ Search functionality test passed")


def run_all_tests():
    """Run all tests"""
    print("Running Penang Chat Bot Tests...")
    print("=" * 60)
    
    test_bot_initialization()
    test_greeting()
    test_tourist_attractions()
    test_food_info()
    test_bulletins()
    test_general_info()
    test_conversation_history()
    test_knowledge_base()
    test_search_functionality()
    
    print("=" * 60)
    print("✅ All tests passed successfully!")


if __name__ == "__main__":
    run_all_tests()
