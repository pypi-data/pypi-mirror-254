from typing import AsyncGenerator, Union

import pluginlib
from pyrogram.types import InlineQuery, \
    InlineQueryResultCachedSticker, Message, InlineQueryResultArticle

from .bot import Bot


@pluginlib.Parent('inline_query')
class InlineQueryPlugin(object):

    usage = ''

    @property
    @pluginlib.abstractmethod
    def cmd(self) -> str:
        return ''

    @property
    @pluginlib.abstractmethod
    def pattern(self) -> str:
        return ''

    @pluginlib.abstractmethod
    async def iter_inline_query_results(
            self,
            bot: Bot,
            query: InlineQuery
    ) -> AsyncGenerator[Union[InlineQueryResultCachedSticker, InlineQueryResultArticle], None]:
        yield

    @property
    def inline_pattern(self) -> str:
        return rf'{self.cmd}(@{self.pattern}@)'

    @staticmethod
    def build_result_cached_sticker(file_id) -> InlineQueryResultCachedSticker:
        return InlineQueryResultCachedSticker(sticker_file_id=file_id)


@pluginlib.Parent('command')
class CommandPlugin(object):

    @property
    @pluginlib.abstractmethod
    def command(self) -> str:
        return ''

    @pluginlib.abstractmethod
    async def reply_msg(self, bot: Bot, message: Message):
        return
