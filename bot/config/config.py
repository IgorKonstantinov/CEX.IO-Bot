from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: int
    API_HASH: str

    AUTO_TAP: bool = True
    RANDOM_TAPS_COUNT: list = [25, 75]
    SLEEP_RANDOM: list = [10, 15]
    SLEEP_BETWEEN_TAPS: list = [25, 35]
    SLEEP_BETWEEN_MINING: list[int] = [600, 900]
    AUTO_CONVERT: bool = True
    MINIMUM_TO_CONVERT: float = 0.1
    AUTO_BUY_UPGRADE: bool = True
    AUTO_TASK: bool = False
    AUTO_CLAIM_SQUAD_BONUS: bool = False

    USE_PROXY_FROM_FILE: bool = False


settings = Settings()


