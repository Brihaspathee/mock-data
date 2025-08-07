import os
import urllib3
from dotenv import load_dotenv

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def define_env():
    load_dotenv(".env.secrets.aws")

def fetch_secrets():
    db_secrets = SecretsAPI(["ss.neo4j.url",
                             "ss.neo4j.username",
                             "ss.neo4j.password",
                             "ss.neo4j.database",
                             "ss.portico.url"])
    secrets = db_secrets.get_secrets()
    return secrets

class SecretsAPI:
    def __init__(self, keys, defaultValue=None) -> None:
        data = {}
        for key in keys:
            env_var = key.replace(".", "_").replace("-", "_").upper()
            data[key] = os.environ.get(env_var, defaultValue)
        self.data = data

    def get_secrets(self):
        return self.data