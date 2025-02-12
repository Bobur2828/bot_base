import asyncio
import aiogram

from django.core.management.base import BaseCommand
from config import settings


bot = aiogram.Bot(token=settings.BOT_TOKEN)


class Command(BaseCommand):
    help = "Clear old cache and old requests for the bot."

    def handle(self, *args, **kwargs):
        """
        Clear old cache and old requests for the bot.
        """
        print("Clearing old cache and requests...")
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.clear_cache())

    async def clear_cache(self):
        """
        Delete old webhook and clear cache.
        """
        # Get current webhook info
        webhook_info = await bot.get_webhook_info()
        print("Current Webhook Info:", webhook_info)

        # If there is an existing webhook, delete it
        if webhook_info.url:
            await bot.delete_webhook()
            print("Old webhook deleted.")

        # Keshni tozalash uchun qo'shimcha amaliyotlarni amalga oshirish
        # Botning xabarlarini o'chirish, agar kerak bo'lsa (boshqa xabarlar)
        # Ammo, buni amalga oshirish uchun bu yerda kerakli amallarni qo'shishingiz mumkin

        print("Old cache and requests cleared.")
