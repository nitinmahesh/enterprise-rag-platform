from app.config.settings import get_settings

settings = get_settings()

print(settings.APP_NAME)
print(settings.EMBEDDING_MODEL)
print(settings.LLM_PROVIDER)
