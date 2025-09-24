import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Snowflake Configuration
    SNOWFLAKE_ACCOUNT = os.getenv('SNOWFLAKE_ACCOUNT', 'sfsehol-natwest_learnaix_hack4acause_zrkzae')
    SNOWFLAKE_USER = os.getenv('SNOWFLAKE_USER', 'USER')
    SNOWFLAKE_PASSWORD = os.getenv('SNOWFLAKE_PASSWORD', 'sn0wf@ll')
    SNOWFLAKE_WAREHOUSE = os.getenv('SNOWFLAKE_WAREHOUSE', 'COMPUTE_WH')
    SNOWFLAKE_DATABASE = os.getenv('SNOWFLAKE_DATABASE', 'SNOWFLAKE_SAMPLE_DATA')
    SNOWFLAKE_SCHEMA = os.getenv('SNOWFLAKE_SCHEMA', 'TPCH_SF1')
    
    # Gemini AI Configuration
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', 'AIzaSyBrVOt06duPLytNq6nYIhTByqJIaW2xCMk')
    
    # Flask Configuration
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    DEBUG = True
