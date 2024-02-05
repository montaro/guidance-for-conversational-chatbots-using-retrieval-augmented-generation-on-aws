from dataclasses import dataclass


@dataclass(frozen=True)
class Config:
    DYNAMODB_TABLE_NAME = "conversation-history-store"
    KENDRA_INDEX = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    KENDRA_REGION = "eu-west-2"


config = Config()
