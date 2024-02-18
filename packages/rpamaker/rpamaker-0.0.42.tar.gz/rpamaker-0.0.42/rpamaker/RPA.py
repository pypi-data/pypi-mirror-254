from decouple import config

def get_enviroment(secret):
    """Get enviroment variable from .env file"""        
    return config(secret, default='') 