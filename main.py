import os
from speech_to_text import options

os.system('cls' if os.name == 'nt' else 'clear')
color="\033[1;32m"
print(f"{color}Welcome to the Audio-to-Text Converter!\033[0m\n".center(100))

options()