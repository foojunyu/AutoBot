"""
LLM Integration Module

This module provides integration with free LLM APIs to enhance the chat bot
with the ability to generate dynamic responses based on the latest information.
"""

import os
import json
from typing import Optional, Dict, List
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class LLMProvider:
    """
    Base class for LLM providers
    """
    
    def generate_response(self, messages: List[Dict[str, str]], context: str = "") -> Optional[str]:
        """
        Generate a response using the LLM
        
        Args:
            messages: List of conversation messages
            context: Additional context to provide to the LLM
        
        Returns:
            Generated response or None if failed
        """
        raise NotImplementedError


class GroqProvider(LLMProvider):
    """
    Groq API provider (free tier available)
    Get API key from: https://console.groq.com/keys
    """
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("GROQ_API_KEY")
        self.model = "llama-3.1-8b-instant"  # Fast and free model
        
    def generate_response(self, messages: List[Dict[str, str]], context: str = "") -> Optional[str]:
        """Generate response using Groq API"""
        if not self.api_key:
            return None
            
        try:
            from groq import Groq
            
            client = Groq(api_key=self.api_key)
            
            # Prepare messages with context
            system_message = {
                "role": "system",
                "content": (
                    "You are a knowledgeable chat bot specializing in Penang, Malaysia. "
                    "Provide accurate, helpful, and friendly responses about Penang's tourist attractions, "
                    "food, culture, bulletins, and practical information. "
                    "Keep responses concise and informative.\n\n"
                    f"Context: {context}"
                )
            }
            
            full_messages = [system_message] + messages
            
            # Generate response
            response = client.chat.completions.create(
                model=self.model,
                messages=full_messages,
                max_tokens=500,
                temperature=0.7,
            )
            
            # Validate response has choices
            if response.choices and len(response.choices) > 0:
                return response.choices[0].message.content
            
            return None
            
        except Exception as e:
            print(f"Groq API error: {e}")
            return None


class HuggingFaceProvider(LLMProvider):
    """
    HuggingFace Inference API provider (free tier available)
    Get API key from: https://huggingface.co/settings/tokens
    """
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("HUGGINGFACE_API_KEY")
        self.api_url = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
        
    def generate_response(self, messages: List[Dict[str, str]], context: str = "") -> Optional[str]:
        """Generate response using HuggingFace API"""
        if not self.api_key:
            return None
            
        try:
            import requests
            
            headers = {"Authorization": f"Bearer {self.api_key}"}
            
            # Format messages for the model
            prompt = self._format_messages(messages, context)
            
            payload = {
                "inputs": prompt,
                "parameters": {
                    "max_new_tokens": 500,
                    "temperature": 0.7,
                    "return_full_text": False
                }
            }
            
            response = requests.post(self.api_url, headers=headers, json=payload, timeout=30)
            
            if response.status_code == 200:
                try:
                    result = response.json()
                    if isinstance(result, list) and len(result) > 0:
                        return result[0].get("generated_text", "").strip()
                except ValueError:
                    # JSON decode error
                    print("HuggingFace API: Invalid JSON response")
            
            return None
            
        except Exception as e:
            print(f"HuggingFace API error: {e}")
            return None
    
    def _format_messages(self, messages: List[Dict[str, str]], context: str) -> str:
        """Format messages into a prompt string"""
        prompt = f"Context: You are a Penang expert chat bot. {context}\n\n"
        
        for msg in messages:
            role = msg["role"]
            content = msg["content"]
            if role == "user":
                prompt += f"User: {content}\n"
            elif role == "assistant":
                prompt += f"Assistant: {content}\n"
        
        prompt += "Assistant:"
        return prompt


class LLMManager:
    """
    Manager for LLM providers with fallback support
    """
    
    def __init__(self):
        self.providers = []
        
        # Try to initialize Groq (preferred - fast and free)
        groq_key = os.getenv("GROQ_API_KEY")
        if groq_key:
            self.providers.append(GroqProvider(groq_key))
        
        # Try to initialize HuggingFace as fallback
        hf_key = os.getenv("HUGGINGFACE_API_KEY")
        if hf_key:
            self.providers.append(HuggingFaceProvider(hf_key))
    
    def is_available(self) -> bool:
        """Check if any LLM provider is available"""
        return len(self.providers) > 0
    
    def generate_response(self, messages: List[Dict[str, str]], context: str = "") -> Optional[str]:
        """
        Generate response using available LLM providers
        
        Args:
            messages: Conversation messages
            context: Additional context about Penang
        
        Returns:
            Generated response or None if all providers fail
        """
        for provider in self.providers:
            response = provider.generate_response(messages, context)
            if response:
                return response
        
        return None


def format_penang_context(knowledge_base: Dict) -> str:
    """
    Format Penang knowledge base into context for LLM
    
    Args:
        knowledge_base: Dictionary containing Penang information
    
    Returns:
        Formatted context string
    """
    context_parts = []
    
    # Add general info
    if "general" in knowledge_base:
        info = knowledge_base["general"]
        context_parts.append(
            f"Penang is located on the {info['location']}. "
            f"It's known as the {info['nickname']} and has a population of {info['population']}."
        )
    
    # Add tourist attractions
    if "tourist_attractions" in knowledge_base:
        attractions = [attr["name"] for attr in knowledge_base["tourist_attractions"][:3]]
        context_parts.append(f"Top attractions: {', '.join(attractions)}.")
    
    # Add food info
    if "food_culture" in knowledge_base:
        dishes = [dish["name"] for dish in knowledge_base["food_culture"]["famous_dishes"][:3]]
        context_parts.append(f"Famous dishes: {', '.join(dishes)}.")
    
    # Add current bulletins
    if "current_bulletins" in knowledge_base:
        topics = [b["topic"] for b in knowledge_base["current_bulletins"][:3]]
        context_parts.append(f"Current bulletin topics: {', '.join(topics)}.")
    
    return " ".join(context_parts)
