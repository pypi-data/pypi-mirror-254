# StickerViaBot

一个用于生成 Sticker 的简易 Telegram Bot 框架

## Requirements

- `python>=3.7`
- `pyrogram~=2.0.97`
- `pluginlib~=0.9.0`

## Installation

```commandline
pip install StickerViaBot
```

## Usage

只需简单一个 main.py 即可运行，~~把项目 git 下来改下 main.py 不也能跑~~

```python
"""
main.py
"""
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
```

如果你要运行在 Docker 之中，只需要通过`环境变量`进行传递

## For Plugins

虽然说了怎么使用，但最重要一点还是如何编写插件。
插件的简单范例在`plugins`文件夹内，插件的规范需要参考`pluginlib`的 [文档](https://pluginlib.readthedocs.io/en/latest/api.html) 。

编写插件常用的函数放在`StickerViaBot.utils`里面。文件中`Utils`类的函数一般与`Telegram Bot`有关，依赖于`pyrogram.Client`才能使用，
设计上直接继承到`StickerViaBot.Bot`之中。

## Note

1. 设计 inline mode 用到的绘图，需要注意结果返回时间，如果超时将不返回结果。对于动图类的，建议改用 command mode ，以确保稳定工作

## License

MIT License
