import os
from google.generativeai import configure, GenerativeModel
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
configure(api_key=GEMINI_API_KEY)


class PitchingAgent:
    def __init__(self, knowledge_base_path, communication_hub):
        self.model = GenerativeModel(model_name="gemini-1.5-pro")
        self.knowledge_base = knowledge_base_path
        self.communication_hub = communication_hub

    def generate_pitch(self, brand_name, target_market, product_features):
        # Generate market insights
        prompt_market = f"Generate market insights for {target_market}"
        market_insights = self.model.generate_content(prompt_market).text.strip()

        # Generate competitive analysis
        prompt_competition = f"Generate competitive analysis for {brand_name}"
        competitive_analysis = self.model.generate_content(prompt_competition).text.strip()

        # Create the pitch dictionary
        pitch = {
            "headline": f"{brand_name}: Redefining {target_market} Excellence",
            "tagline": f"Experience the Future of {target_market} with {brand_name}",
            "market_opportunity": market_insights if market_insights else "No data found",
            "competitive_edge": competitive_analysis if competitive_analysis else "No data found",
            "product_highlights": product_features,
            "brand_name": brand_name,  # Adding brand_name here
            "target_market": target_market  # Adding target_market here
        }

        # Log the pitch creation (for debugging)
        self.log_pitch_creation(brand_name, pitch)
        
        # Return the pitch
        return pitch

    def log_pitch_creation(self, brand_name, pitch):
        print(f"[PitchingAgent] Generated pitch for {brand_name}:\n", pitch)

    def receive_message(self, sender, message):
        if message['request'] == "generate_pitch":
            brand_name = message['brand_name']
            target_market = message['target_market']
            product_features = message['product_features']
            pitch = self.generate_pitch(brand_name, target_market, product_features)
            self.communication_hub.send_message("PitchingAgent", sender, {
                "request": "pitch_generated",
                "pitch": pitch
            })
