# memory.py
import json
import os
from typing import Any, Dict, Optional, Tuple
from uuid import uuid4

import boto3
from langchain import ConversationChain
from langchain.memory import (
    ConversationBufferMemory,
    ConversationBufferWindowMemory,
    ConversationSummaryMemory,
    DynamoDBChatMessageHistory,
)
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
)
from langchain.prompts.prompt import PromptTemplate
from langchain.schema import messages_to_dict

import config

# import config


class chatMemory:
    def __init__(self, session_id) -> None:
        self.session_id = session_id
        self.memory = self.create_memory()

    # def create_memory(self,session_id,message)-> None:
    def create_memory(self) -> Any:
        message_history = DynamoDBChatMessageHistory(
            table_name=config.config.DYNAMODB_TABLE_NAME, session_id=self.session_id
        )

        print(message_history.messages)
        memory = ConversationBufferWindowMemory(
            memory_key="history",
            chat_memory=message_history,
            return_messages=True,
            k=10,
        )
        return memory
