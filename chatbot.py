"""
Penang Bulletins Chat Bot

A knowledgeable chat bot that can answer questions about Penang bulletins,
tourist information, food, culture, and more.
"""

from typing import List, Dict, Optional
from penang_knowledge import PENANG_KNOWLEDGE, get_penang_info, search_penang_info


class PenangChatBot:
    """
    Chat bot specialized in Penang bulletins and information
    """
    
    def __init__(self):
        self.conversation_history = []
        self.knowledge_base = PENANG_KNOWLEDGE
        
    def generate_response(self, user_message: str) -> str:
        """
        Generate a response to the user's message based on Penang knowledge
        
        Args:
            user_message: User's input message
        
        Returns:
            Bot's response
        """
        user_message_lower = user_message.lower()
        
        # Add to conversation history
        self.conversation_history.append({"role": "user", "content": user_message})
        
        # Handle greetings
        if any(greeting in user_message_lower for greeting in ["hello", "hi", "hey", "greetings"]):
            response = self._handle_greeting()
        
        # Handle farewells
        elif any(farewell in user_message_lower for farewell in ["bye", "goodbye", "see you", "exit", "quit"]):
            response = self._handle_farewell()
        
        # Handle help requests
        elif any(word in user_message_lower for word in ["help", "what can you", "how do you"]):
            response = self._handle_help()
        
        # Handle general info questions
        elif any(word in user_message_lower for word in ["what is penang", "about penang", "tell me about penang"]):
            response = self._handle_general_info()
        
        # Handle tourist attractions
        elif any(word in user_message_lower for word in ["tourist", "visit", "attraction", "place", "see in penang", "to do"]):
            response = self._handle_tourist_attractions(user_message_lower)
        
        # Handle food questions
        elif any(word in user_message_lower for word in ["food", "eat", "dish", "cuisine", "restaurant", "hawker"]):
            response = self._handle_food_info(user_message_lower)
        
        # Handle culture and heritage
        elif any(word in user_message_lower for word in ["culture", "festival", "heritage", "tradition"]):
            response = self._handle_culture_info()
        
        # Handle bulletins
        elif any(word in user_message_lower for word in ["bulletin", "update", "news", "current", "latest"]):
            response = self._handle_bulletins(user_message_lower)
        
        # Handle practical information
        elif any(word in user_message_lower for word in ["transport", "weather", "how to get", "climate", "best time"]):
            response = self._handle_practical_info(user_message_lower)
        
        # Default response
        else:
            response = self._handle_general_query(user_message)
        
        # Add response to conversation history
        self.conversation_history.append({"role": "assistant", "content": response})
        
        return response
    
    def _handle_greeting(self) -> str:
        """Handle greeting messages"""
        return ("Hello! 👋 Welcome to the Penang Bulletins Chat Bot! "
                "I'm here to help you learn about Penang, the Pearl of the Orient. "
                "I can provide information about tourist attractions, food, culture, "
                "current bulletins, and much more. How can I assist you today?")
    
    def _handle_farewell(self) -> str:
        """Handle farewell messages"""
        return ("Thank you for chatting with me! I hope you found the information helpful. "
                "Have a wonderful time in Penang! 🌴 Feel free to come back anytime you need "
                "more information about the Pearl of the Orient. Goodbye!")
    
    def _handle_help(self) -> str:
        """Handle help requests"""
        return ("I can help you with:\n\n"
                "🏛️  General information about Penang\n"
                "🗺️  Tourist attractions and places to visit\n"
                "🍜  Food, cuisine, and where to eat\n"
                "🎭  Culture, heritage, and festivals\n"
                "📰  Current bulletins and updates\n"
                "🚌  Transportation and practical information\n"
                "☀️  Weather and best time to visit\n\n"
                "Just ask me anything about Penang, and I'll do my best to help!")
    
    def _handle_general_info(self) -> str:
        """Handle general information about Penang"""
        info = self.knowledge_base["general"]
        return (f"**About Penang ({info['name']})**\n\n"
                f"📍 Location: {info['location']}\n"
                f"👥 Population: {info['population']}\n"
                f"💬 Languages: {info['languages']}\n"
                f"🏛️  Capital: {info['capital']}\n"
                f"✨ Known as: {info['nickname']}\n"
                f"🏆 UNESCO Status: {info['unesco_status']}\n\n"
                f"Penang is a vibrant Malaysian state known for its rich cultural heritage, "
                f"world-renowned cuisine, and beautiful colonial architecture. "
                f"George Town, its capital, is a melting pot of cultures with influences "
                f"from Malay, Chinese, Indian, and European communities.")
    
    def _handle_tourist_attractions(self, query: str) -> str:
        """Handle tourist attractions queries"""
        attractions = self.knowledge_base["tourist_attractions"]
        
        # Check if asking about a specific attraction
        specific_attraction = None
        for attraction in attractions:
            if attraction["name"].lower() in query:
                specific_attraction = attraction
                break
        
        if specific_attraction:
            highlights = ", ".join(specific_attraction["highlights"])
            return (f"**{specific_attraction['name']}**\n\n"
                    f"{specific_attraction['description']}\n\n"
                    f"🌟 Highlights: {highlights}")
        else:
            # Return all attractions
            response = "**Top Tourist Attractions in Penang:**\n\n"
            for i, attraction in enumerate(attractions, 1):
                response += f"{i}. **{attraction['name']}**\n"
                response += f"   {attraction['description']}\n\n"
            response += "\nWould you like to know more about any specific attraction?"
            return response
    
    def _handle_food_info(self, query: str) -> str:
        """Handle food and cuisine queries"""
        food_info = self.knowledge_base["food_culture"]
        
        # Check if asking about specific dish
        specific_dish = None
        for dish in food_info["famous_dishes"]:
            if dish["name"].lower() in query:
                specific_dish = dish
                break
        
        if specific_dish:
            return (f"**{specific_dish['name']}**\n\n"
                    f"{specific_dish['description']}\n\n"
                    f"This is one of Penang's most famous dishes! "
                    f"You can find it at many hawker centres throughout the island.")
        
        # Check if asking about where to eat
        elif any(word in query for word in ["where", "location", "hawker"]):
            locations = "\n".join([f"• {loc}" for loc in food_info["food_locations"]])
            return (f"**Best Places to Eat in Penang:**\n\n{locations}\n\n"
                    f"These hawker centres and food streets are must-visits for authentic Penang cuisine!")
        
        else:
            # Return general food information
            response = f"**Penang Food Culture**\n\n{food_info['description']}\n\n**Famous Dishes:**\n"
            for dish in food_info["famous_dishes"]:
                response += f"• **{dish['name']}**: {dish['description']}\n"
            response += "\nPenang is truly a food paradise! Would you like to know where to find these dishes?"
            return response
    
    def _handle_culture_info(self) -> str:
        """Handle culture and heritage queries"""
        culture = self.knowledge_base["culture_heritage"]
        festivals = "\n".join([f"• {festival}" for festival in culture["festivals"]])
        
        return (f"**Penang Culture & Heritage**\n\n"
                f"🌏 Ethnic Diversity: {culture['ethnic_diversity']}\n\n"
                f"🎉 Major Festivals & Events:\n{festivals}\n\n"
                f"🏛️  Peranakan Heritage: {culture['peranakan_culture']}\n\n"
                f"Penang's multicultural society creates a unique blend of traditions, "
                f"festivals, and customs that make it one of Asia's most culturally rich destinations.")
    
    def _handle_bulletins(self, query: str) -> str:
        """Handle bulletin and updates queries"""
        bulletins = self.knowledge_base["current_bulletins"]
        
        # Check if asking about specific topic
        specific_bulletin = None
        for bulletin in bulletins:
            if bulletin["topic"].lower() in query:
                specific_bulletin = bulletin
                break
        
        if specific_bulletin:
            return (f"**{specific_bulletin['topic']}**\n\n"
                    f"{specific_bulletin['info']}")
        else:
            # Return all bulletins
            response = "**Current Penang Bulletins & Updates:**\n\n"
            for i, bulletin in enumerate(bulletins, 1):
                response += f"{i}. **{bulletin['topic']}**\n"
                response += f"   {bulletin['info']}\n\n"
            return response
    
    def _handle_practical_info(self, query: str) -> str:
        """Handle practical information queries"""
        practical = self.knowledge_base["practical_info"]
        
        if "transport" in query or "how to get" in query:
            return f"**Getting to Penang:**\n\n{practical['getting_there']}"
        
        elif "weather" in query or "climate" in query or "best time" in query:
            bulletins = self.knowledge_base["current_bulletins"]
            weather_info = next((b["info"] for b in bulletins if "Weather" in b["topic"]), "")
            return (f"**Weather & Best Time to Visit:**\n\n"
                    f"Best time: {practical['best_time_to_visit']}\n\n"
                    f"{weather_info}")
        
        else:
            return (f"**Practical Information for Penang:**\n\n"
                    f"✈️  Getting There: {practical['getting_there']}\n\n"
                    f"📅 Best Time to Visit: {practical['best_time_to_visit']}\n\n"
                    f"💰 Currency: {practical['currency']}\n\n"
                    f"🚨 Emergency Numbers: {practical['emergency_numbers']}")
    
    def _handle_general_query(self, query: str) -> str:
        """Handle general queries that don't fit specific categories"""
        # Search for relevant categories
        relevant_categories = search_penang_info(query)
        
        if relevant_categories:
            response = "Based on your question, here's some relevant information:\n\n"
            
            for category in relevant_categories[:2]:  # Limit to 2 categories
                if category == "general":
                    info = self.knowledge_base["general"]
                    response += f"📍 Penang is located on the {info['location']} and is known as the {info['nickname']}.\n\n"
                
                elif category == "current_bulletins":
                    response += "For current bulletins and updates, you can ask me about transportation, tourism guidelines, weather, or cultural events.\n\n"
            
            response += "Feel free to ask more specific questions about tourist attractions, food, culture, or bulletins!"
            return response
        
        else:
            return ("I'm not sure I understood your question completely. "
                    "I specialize in information about Penang, including tourist attractions, "
                    "food, culture, bulletins, and practical information. "
                    "Could you please rephrase your question or ask about a specific topic?")
    
    def get_conversation_history(self) -> List[Dict]:
        """Get the conversation history"""
        return self.conversation_history
    
    def clear_history(self):
        """Clear conversation history"""
        self.conversation_history = []


def main():
    """Main function to run the chat bot in CLI mode"""
    print("=" * 60)
    print("🌴 Penang Bulletins Chat Bot 🌴")
    print("=" * 60)
    print()
    
    bot = PenangChatBot()
    
    # Initial greeting
    print("Bot:", bot.generate_response("Hello"))
    print()
    
    # Main conversation loop
    while True:
        try:
            user_input = input("You: ").strip()
            
            if not user_input:
                continue
            
            # Check for exit commands
            if user_input.lower() in ["exit", "quit", "bye", "goodbye"]:
                print("Bot:", bot.generate_response(user_input))
                break
            
            # Generate and print response
            response = bot.generate_response(user_input)
            print()
            print("Bot:", response)
            print()
            
        except KeyboardInterrupt:
            print("\n\nBot: Goodbye! Thanks for chatting!")
            break
        except Exception as e:
            print(f"\nError: {e}")
            print("Bot: I encountered an error. Please try again.\n")


if __name__ == "__main__":
    main()
