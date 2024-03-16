import os
class settings:
    def get_database_url():
        if os.getenv("ENVIRONMENT","local") == "test":
            return "sqlite:///./test.db"
        else:
            return "postgresql://default:jkmvG3LS4KQq@ep-muddy-sunset-a1erht6n.ap-southeast-1.aws.neon.tech:5432/verceldb?sslmode=require"
        