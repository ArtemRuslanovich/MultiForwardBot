import asyncpg

class Request:
    def __init__(self, database_url):
        self.database_url = database_url

    async def connect(self):
        self.connection = await asyncpg.connect(self.database_url)

    async def close(self):
        await self.connection.close()

    async def get_users_and_chats(self):
        # Запрос к базе данных для получения информации о пользователях и чатах
        query = "SELECT * FROM users_chats"
        return await self.connection.fetch(query)

    async def add_user_or_chat(self, user_id, chat_id):
        # Добавление нового пользователя или чата в базу данных
        query = "INSERT INTO users_chats (user_id, chat_id) VALUES ($1, $2)"
        await self.connection.execute(query, user_id, chat_id)
