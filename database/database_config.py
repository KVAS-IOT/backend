from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from config.environment_variables import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_NAME

async_engine = create_async_engine(url = f"postgresql+asyncpg://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}", echo = True)
async_session_factory = async_sessionmaker(async_engine, expire_on_commit=False)

class BaseModel(DeclarativeBase):
    def __repr__(self):
        cols = [f"{col}={getattr(self, col)}" for col in self.__table__.columns.keys()]
        return f"<{self.__class__.__name__} {', '.join(cols)})>"

async def check_database_connection():
    from sqlalchemy import text
    from sqlalchemy.future import select

    async with async_session_factory() as session:
        async with session.begin():
            result = await session.execute(select(text("1")))
            if result.scalar() != 1:
                raise ValueError("Database connection wasn't established")
            print("Connection was established")