import asyncio
import logging

import pluginlib
from pyrogram import Client, filters
from pyrogram.handlers import InlineQueryHandler, MessageHandler
from pyrogram.types import Message, InlineQuery, \
    InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton

from .utils import Utils


SESSION_NAME = 'StickerBot'
CACHE_TIME = 60


class Bot(Client, Utils):

    def __init__(self, *args, **kwargs):
        super(Bot, self).__init__(*args, **kwargs)
        self.inline_plugins = None

    async def run_in_executor(self, func, *args, **kwargs):
        return await self.loop.run_in_executor(
            executor=None,
            func=func, *args, **kwargs
        )


def create_bot(
        api_id: int,
        api_hash: str,
        bot_token: str,
        plugins: dict = None,
        cache_time: int = CACHE_TIME,
        session_name: str = SESSION_NAME,
) -> Bot:

    bot = Bot(
        name=session_name,
        api_id=api_id,
        api_hash=api_hash,
        bot_token=bot_token
    )

    @bot.on_message(filters=filters.command('start') & filters.private)
    async def hello(client: Client, message: Message) -> None:
        await message.reply(
            f'欢迎使用 {session_name}\n'
            '向 Bot 发送静态 Sticker 来获取 [FILE_ID] 或 [MSG_ID] \n'
            '\n'
            '[FILE_ID] 是能在用户间共享使用的 Sticker ID\n'
            '[MSG_ID] 是当前用户与 Bot 对话中 Sticker 的聊天记录 ID , 仅当前用户使用的便捷参数',
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton('试试 Inline 模式!', switch_inline_query='')]]
            )
        )

    @bot.on_message(filters=filters.private & filters.sticker)
    async def sticker(client: Client, message: Message) -> None:
        await message.reply(
            '**[FILE_ID]**\n'
            f'`{message.sticker.file_id}`\n'
            '**[MSG_ID]**\n'
            f'`MSG{message.id}`\n',
            reply_to_message_id=message.id,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton('Try! [FILE_ID]', switch_inline_query=f'r@{message.sticker.file_id}@'),
                    InlineKeyboardButton('Try! [MSG_ID]', switch_inline_query=f'r@MSG{message.id}@')],
                ]
            )
        )

    async def handle_inline_query(bot: Bot, query: InlineQuery, iter_results):
        result = [i async for i in iter_results(bot, query)]
        await query.answer(
            result if any(result) else [
                InlineQueryResultArticle(
                    'No Sticker',
                    input_message_content=InputTextMessageContent(f'**Invalid Input:**\n`{query.query}`')
                )
            ],
            is_gallery=any(result),
            cache_time=cache_time,
        )

    def _async_partial(func, *args, **kwargs):
        async def async_func(*args2, **kwargs2):
            result = func(*args, *args2, **kwargs, **kwargs2)
            if asyncio.iscoroutinefunction(func):
                result = await result
            return result
        return async_func

    loader = pluginlib.PluginLoader(library=plugins['root'])
    inline_query: dict = loader.plugins.inline_query
    bot.inline_plugins = inline_query
    for name, cls in inline_query.items():
        logging.info(f'Loading Inline Query Plugin: {name}')
        plugin = cls()
        bot.add_handler(
            InlineQueryHandler(
                _async_partial(handle_inline_query, iter_results=plugin.iter_inline_query_results),
                filters.regex(plugin.inline_pattern)
            )
        )

    async def handle_command(bot: Bot, message: Message, reply_msg):
        await reply_msg(bot, message)

    command: dict = loader.plugins.command
    for name, cls in command.items():
        logging.info(f'Loading Command Plugin: {name}')
        plugin = cls()
        bot.add_handler(
            MessageHandler(
                _async_partial(handle_command, reply_msg=plugin.reply_msg),
                filters.private & filters.command(plugin.command)
            )
        )

    return bot
