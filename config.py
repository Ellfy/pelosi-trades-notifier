import os
import json
import logging
import datetime

logger = logging.getLogger("PelosiTracker.Config")

def load_config():
    """Load configuration from external file or use defaults"""
    default_config = {
        "base_url": "https://disclosures-clerk.house.gov/FinancialDisclosure",
        "search_url": "https://disclosures-clerk.house.gov/public_disc/ptr-pdfs/2024/{trade_id}.pdf",
        "last_name": "pelosi",
        "filing_year": datetime.datetime.now().year,
        "check_interval_seconds": 200,
        "data_file": "pelosi_disclosures.json",
        "email": {
            "smtp_server": "smtp.gmail.com",
            "smtp_port": 587,
            "sender_email": "ZKK@gmail.com",
            "sender_password": "PLACEHOLD",
            "recipient_email": "ZKK@gmail.com"
        }
    }
    
    try:
        # Try to load from config.json
        if os.path.exists("config.json"):
            with open("config.json", "r") as f:
                return json.load(f)
        else:
            logger.warning("config.json not found. Using default configuration.")
            # Create a sample config file if it doesn't exist
            with open("config.json.sample", "w") as f:
                json.dump(default_config, f, indent=4)
            logger.info("Created config.json.sample. Please edit this file and rename to config.json.")
            return default_config
    except Exception as e:
        logger.error(f"Error loading configuration: {e}")
        return default_config 

import json

def load_config():
    with open("config.json", "r") as f:
        return json.load(f)

