"""
Penang Bulletins Knowledge Base

This module contains information about Penang, Malaysia including:
- General information
- Tourist attractions
- Food and cuisine
- Culture and heritage
- Current events and bulletins
"""

PENANG_KNOWLEDGE = {
    "general": {
        "name": "Penang (Pulau Pinang)",
        "location": "Northwestern coast of Peninsular Malaysia",
        "population": "Approximately 1.7 million (2023)",
        "languages": "Malay, English, Mandarin, Hokkien, Tamil",
        "capital": "George Town",
        "nickname": "Pearl of the Orient",
        "unesco_status": "George Town is a UNESCO World Heritage Site (since 2008)",
    },
    
    "tourist_attractions": [
        {
            "name": "George Town Heritage Zone",
            "description": "UNESCO World Heritage Site with colonial architecture, street art, and historical buildings",
            "highlights": ["Street art murals", "Clan Jetties", "Colonial buildings", "Heritage shophouses"]
        },
        {
            "name": "Penang Hill (Bukit Bendera)",
            "description": "Hill resort at 821m above sea level offering panoramic views",
            "highlights": ["Funicular railway", "The Habitat", "David Brown's Restaurant"]
        },
        {
            "name": "Kek Lok Si Temple",
            "description": "Largest Buddhist temple in Malaysia",
            "highlights": ["7-storey pagoda", "Bronze statue of Kuan Yin", "Floral gardens"]
        },
        {
            "name": "Penang National Park",
            "description": "Smallest national park in Malaysia with beaches and rainforest",
            "highlights": ["Monkey Beach", "Turtle Beach", "Canopy walkway", "Muka Head Lighthouse"]
        },
        {
            "name": "Batu Ferringhi Beach",
            "description": "Popular beach resort area with hotels and water sports",
            "highlights": ["Night market", "Water sports", "Beach resorts"]
        }
    ],
    
    "food_culture": {
        "description": "Penang is renowned as Malaysia's food capital",
        "famous_dishes": [
            {"name": "Char Kway Teow", "description": "Stir-fried flat rice noodles"},
            {"name": "Assam Laksa", "description": "Spicy tamarind fish noodle soup"},
            {"name": "Nasi Kandar", "description": "Rice served with various curry dishes"},
            {"name": "Rojak", "description": "Mixed fruit and vegetable salad with sweet sauce"},
            {"name": "Hokkien Mee", "description": "Prawn noodle soup"},
            {"name": "Cendol", "description": "Iced sweet dessert with coconut milk"},
            {"name": "Apom Manis", "description": "Sweet pancakes"},
            {"name": "Curry Mee", "description": "Spicy curry noodle soup"}
        ],
        "food_locations": [
            "Gurney Drive Hawker Centre",
            "New Lane Hawker Centre",
            "Kimberly Street",
            "Lorong Baru (New Lane)",
            "Red Garden Food Paradise"
        ]
    },
    
    "culture_heritage": {
        "ethnic_diversity": "Mix of Malay, Chinese, Indian, Peranakan, and Eurasian communities",
        "festivals": [
            "Thaipusam",
            "Chinese New Year",
            "Hari Raya",
            "Deepavali",
            "Penang Bridge International Marathon",
            "George Town Festival",
            "Penang Island Jazz Festival"
        ],
        "peranakan_culture": "Rich Straits Chinese (Baba-Nyonya) heritage with unique cuisine and architecture"
    },
    
    "current_bulletins": [
        {
            "topic": "Transportation Updates",
            "info": "Penang has an efficient public transport system including Rapid Penang buses and free CAT (Central Area Transit) buses in George Town. The Penang Bridge and Sultan Abdul Halim Muadzam Shah Bridge connect the island to the mainland."
        },
        {
            "topic": "Tourism Guidelines",
            "info": "Visitors are encouraged to respect local customs, dress modestly when visiting religious sites, and use designated hawker centres for authentic street food experiences."
        },
        {
            "topic": "Weather Advisory",
            "info": "Penang has a tropical climate with temperatures ranging from 23°C to 32°C year-round. Monsoon season typically occurs from April to May and September to November."
        },
        {
            "topic": "Cultural Events",
            "info": "George Town hosts various cultural events throughout the year, including the George Town Festival (July-August) and various food festivals celebrating Penang's multicultural heritage."
        },
        {
            "topic": "Conservation Efforts",
            "info": "Penang is actively preserving its UNESCO Heritage status through building conservation, cultural programs, and sustainable tourism initiatives."
        }
    ],
    
    "practical_info": {
        "getting_there": "Penang International Airport serves domestic and international flights. Ferry services and two bridges connect the island to mainland Malaysia.",
        "best_time_to_visit": "December to February for drier weather, though Penang is a year-round destination",
        "currency": "Malaysian Ringgit (MYR)",
        "emergency_numbers": "Police: 999, Ambulance: 999, Fire: 994"
    }
}


def get_penang_info(category=None):
    """
    Retrieve Penang information by category
    
    Args:
        category: Optional category to filter (general, tourist_attractions, food_culture, etc.)
    
    Returns:
        Dictionary containing requested information
    """
    if category and category in PENANG_KNOWLEDGE:
        return PENANG_KNOWLEDGE[category]
    return PENANG_KNOWLEDGE


def search_penang_info(query):
    """
    Search for information related to a query across all Penang knowledge
    
    Args:
        query: Search term or question
    
    Returns:
        List of relevant information items
    """
    query_lower = query.lower()
    results = []
    
    # Search in different categories
    keywords_map = {
        "food": "food_culture",
        "eat": "food_culture",
        "dish": "food_culture",
        "restaurant": "food_culture",
        "tourist": "tourist_attractions",
        "visit": "tourist_attractions",
        "attraction": "tourist_attractions",
        "place": "tourist_attractions",
        "culture": "culture_heritage",
        "festival": "culture_heritage",
        "heritage": "culture_heritage",
        "bulletin": "current_bulletins",
        "update": "current_bulletins",
        "news": "current_bulletins",
        "general": "general",
        "about": "general",
        "practical": "practical_info",
        "transport": "practical_info",
        "weather": "current_bulletins"
    }
    
    for keyword, category in keywords_map.items():
        if keyword in query_lower:
            results.append(category)
    
    # If no specific category found, return general info
    if not results:
        results = ["general", "current_bulletins"]
    
    # Remove duplicates while preserving order
    seen = set()
    unique_results = []
    for item in results:
        if item not in seen:
            seen.add(item)
            unique_results.append(item)
    
    return unique_results
