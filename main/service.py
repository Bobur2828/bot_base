from main.instance.handlers import feed_update


class BotService:

    @classmethod
    async def feed_update(cls, token: str, update: dict):

        await feed_update(token, update)
