from django.db import models
class BotClient(models.Model):
    """
    BotClient model for bot clients
    """
    LANGUAGE_CHOICES = [
        ('ru', '🇷🇺 Ruscha'),
        ('en', '🇺🇸 Inglizcha'),
        ('uz', '🇺🇿 O\'zbekcha'),
    ]
    
    chat_id = models.BigIntegerField(verbose_name="Chat ID")
    first_name = models.CharField(max_length=100, verbose_name="Ism")
    last_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Familiya")
    username = models.CharField(max_length=100, blank=True, null=True, verbose_name="Telegram Username")
    phone = models.CharField(max_length=15,blank=True,null=True,verbose_name="Telefon raqam")
    language_code = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, verbose_name="Til kodi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Botga a'zo bo'lgan sana sana")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yangilangan sana")

    class Meta:
        verbose_name = "Bot mijoz"
        verbose_name_plural = "Bot mijozlari"
        ordering = ['-updated_at']


    @classmethod
    async def create_or_update(
        cls,
        chat_id: int,
        first_name: str,
        last_name: str,
        username: str,
        language_code: str,
    ):
        """
        Create or update a bot client
        """
        client, created = await cls.objects.aget_or_create(
            chat_id=chat_id,
        )
        client.first_name = first_name
        client.last_name = last_name
        client.username = username
        client.language_code = language_code
        await client.asave()
        return client, created

    @classmethod
    async def change_language(cls, chat_id: int, language_code: str):
        """
        Change language for a bot client
        """
        client = await cls.objects.aget(chat_id=chat_id)
        client.language_code = language_code
        await client.asave()
    def __str__(self):
        return f"{self.first_name} | @{self.username}"
    

    @classmethod
    async def get_language(cls, chat_id: int):
        client = await cls.objects.aget(chat_id=chat_id)
        return client.language_code
    
    @classmethod
    async def change_is_active(cls,chat_id:int,status:str):
        client = await cls.objects.aget(chat_id=chat_id)
        client.is_active = status
        await client.asave()
