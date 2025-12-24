import os
from dotenv import load_dotenv
from typing import List

load_dotenv()

class Settings:
    def __init__(self):
        self.DB_URI: str = os.getenv("DB_URI")
        self.DB_NAME: str = os.getenv("DB_NAME")
        
        frontend_origins_str: str = os.getenv("FRONTEND_ORIGINS", "http://localhost:3000")
        
        self.FRONTEND_ORIGINS: List[str] = [
            url.strip() for url in frontend_origins_str.split(',')
        ]

        self.BASE_IMPORT_PATH: str = os.getenv("BASE_IMPORT_PATH", "./imports")
        
        self.WATCH_FOLDER: str = os.getenv(
            "WATCH_FOLDER", 
            os.path.join(self.BASE_IMPORT_PATH, "pendentes")
        )
        self.PROCESSED_FOLDER: str = os.getenv(
            "PROCESSED_FOLDER", 
            os.path.join(self.BASE_IMPORT_PATH, "processados")
        )
        self.ERROR_FOLDER: str = os.getenv(
            "ERROR_FOLDER", 
            os.path.join(self.BASE_IMPORT_PATH, "erros")
        )
        self.PROCESSING_FOLDER: str = os.getenv(
            "PROCESSING_FOLDER", 
            os.path.join(self.BASE_IMPORT_PATH, "processando")
        )

settings = Settings()