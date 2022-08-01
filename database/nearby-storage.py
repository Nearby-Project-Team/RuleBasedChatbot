import logging
from chatterbot import languages
from chatterbot.tagging import PosLemmaTagger
from chatterbot.storage.sql_storage import SQLStorageAdapter
from chatterbot.storage.storage_adapter import StorageAdapter

if __name__ == "__main__":
    sql = SQLStorageAdapter()
    sql.create_database([
        
    ])