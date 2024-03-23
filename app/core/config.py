import os
class settings:
    
    open_ai_api_key: str = os.getenv("OPEN_AI_API_KEY")
    assistant_id: str = os.getenv("ASSISTANT_ID")

    def get_database_url():
        if os.getenv("ENVIRONMENT","local") == "test":
            return "sqlite:///./test.db"
        else:
            return "postgresql://default:jkmvG3LS4KQq@ep-muddy-sunset-a1erht6n.ap-southeast-1.aws.neon.tech:5432/verceldb?sslmode=require"
        