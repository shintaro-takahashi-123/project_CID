from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

# CallMessagesテーブル
class CallMessage(Base):
    __tablename__ = 'call_messages'
    id = Column(Integer, primary_key=True, index=True)
    message_body = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # MessageHistoryとの関係
    histories = relationship("MessageHistory", back_populates="call_message")

# ResponseMessagesテーブル
class ResponseMessage(Base):
    __tablename__ = 'response_messages'
    id = Column(Integer, primary_key=True, index=True)
    message_body = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # MessageHistoryとの関係
    histories = relationship("MessageHistory", back_populates="response_message")

# MessageHistoryテーブル
class MessageHistory(Base):
    __tablename__ = 'message_history'
    id = Column(Integer, primary_key=True, index=True)
    call_message_id = Column(Integer, ForeignKey('call_messages.id'))
    response_message_id = Column(Integer, ForeignKey('response_messages.id'))
    created_at = Column(DateTime, default=datetime.utcnow)

    # リレーション設定
    call_message = relationship("CallMessage", back_populates="histories")
    response_message = relationship("ResponseMessage", back_populates="histories")
