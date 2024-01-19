from aiogram.types import Message
from utils.dbconnect import Request

async def forward_from_channel(message: Message, request: Request):
    users_chats = await request.get_users_and_chats()
    for user_chat in users_chats:
        user_id, chat_id = user_chat['user_id'], user_chat['chat_id']
        await message.copy_to(chat_id)