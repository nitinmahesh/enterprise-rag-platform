import logging

from app.config.settings import get_settings

settings = get_settings()

logging.basicConfig(
    level=settings.LOG_LEVEL,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(settings.APP_NAME)
