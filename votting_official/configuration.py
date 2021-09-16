import os;
redisHost = os.environ["REDIS_HOST"]

class Configuration():
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://root:root@electionDB/election";
    JWT_SECRET_KEY = "JWT_SECRET_KEY";
    JSON_SORT_KEYS = False;
    REDIS_HOST = redisHost;
    REDIS_VOTES_LIST = "votes";

