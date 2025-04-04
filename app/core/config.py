from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    GOOGLE_CLIENT_ID: str = "1045727623358-v2o1k3kskfaeh8g3pajg2de5v0suvspv.apps.googleusercontent.com"
    GOOGLE_CLIENT_SECRET: str = "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"
    
    class Config:
        env_file = ".env"

settings = Settings() 