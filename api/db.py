import os
from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession
from sqlalchemy.orm import sessionmaker,declarative_base


#ベースを定義
Base = declarative_base()
#データベースの接続先
DATABASE_URL = os.environ.get("DATABASE_URL")
#非同期エンジンの作成
engine = create_async_engine(DATABASE_URL,echo=True)

#非同期セッションの作成
create_session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession
)

#セッションを呼び出し元に渡す関数
async def get_session():
    async with create_session() as session:
        yield session