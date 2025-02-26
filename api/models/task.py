from sqlalchemy import Column,String,Integer,DateTime
from db import Base
from datetime import datetime

#タスクモデル
class Task(Base):
    #テーブル名
    __tablename__ = "tasks"
    #id
    id = Column("id",Integer,primary_key=True,autoincrement=True)
    #タイトル
    title = Column("title",String(20),nullable=False)
    #内容
    content = Column("content",String(255),nullable=False)
    #作成日
    create_at = Column("create_at",DateTime,default=datetime.now())
    #更新日
    update_at = Column("update_at",DateTime)