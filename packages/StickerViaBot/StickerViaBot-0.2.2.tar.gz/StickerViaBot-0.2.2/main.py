from StickerViaBot import create_bot


bot = create_bot(
    session_name = 'StickerViaBot',
    api_id = 0,         # TELEGRAM_API_ID
    api_hash = "",      # TELEGRAM_API_HASH
    bot_token = "",     # TELEGRAM_BOT_TOKEN
    plugins=dict(root="plugins"),  # PLUGINS_DIR_PATH
)

if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.INFO)
    bot.run()
