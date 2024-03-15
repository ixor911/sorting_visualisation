from models import Sorting
from dotenv import dotenv_values

setting = dotenv_values(".env")


sorting_game = Sorting(
    width=int(setting.get("WINDOW_WIDTH")),
    height=int(setting.get("WINDOW_HEIGHT")),
    border=int(setting.get("WINDOW_BORDER")),
    header=int(setting.get("WINDOW_HEADER")),
    fps=int(setting.get("MAX_FPS")),
    list_len=100,
    background=setting.get("BACKGROUND_COLOR"),
    candles=setting.get("CANDLES_COLOR"),
    max_speed=int(setting.get("MAX_SPEED")),
    speed=1000,
    phase_wait=int(setting.get("PHASE_WAIT"))
)
sorting_game.start()
