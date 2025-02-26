import os
from sqlalchemy.ext.asyncio import create_async_engine
from models.task import Base
import asyncio

#データベースの接続先
DATABASE_URL = os.environ.get("DATABASE_URL")
#非同期エンジンの作成
engine = create_async_engine(DATABASE_URL,echo=True)

#データベースを初期化する関数
async def init_db():
    async with engine.begin() as conn:
        #既存のテーブルを削除
        await conn.run_sync(Base.metadata.drop_all)
        #テーブルの作成
        await conn.run_sync(Base.metadata.create_all)
    await engine.dispose() 
if __name__ == "__main__":
    asyncio.run(init_db())