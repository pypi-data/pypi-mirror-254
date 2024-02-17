from StickerViaBot.plugin import InlineQueryPlugin
from StickerViaBot.default_pattern import P_STICKER_ID


class Relay(InlineQueryPlugin):

    @property
    def cmd(self) -> str:
        return 'r'

    @property
    def pattern(self) -> str:
        return P_STICKER_ID

    async def iter_inline_query_results(self, bot, query):
        file_id = await bot.get_file_id_from_query(query)
        if file_id:
            yield self.build_result_cached_sticker(file_id)