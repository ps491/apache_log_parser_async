from pathlib import Path

from decouple import AutoConfig

BASE_DIR = Path(__file__).parent.parent
print(BASE_DIR)
config = AutoConfig(search_path=BASE_DIR.joinpath('config'))
