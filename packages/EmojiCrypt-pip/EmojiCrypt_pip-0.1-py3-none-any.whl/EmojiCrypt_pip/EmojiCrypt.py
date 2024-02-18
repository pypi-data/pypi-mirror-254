from colorama import Fore
import sys

emojis={'a': '😀', 'b': '🤓', 'c': '👀', 'd': '😁', 'e': '😆', 'f': '😅', 'g': '🤣', 'h': '😂', 'i': '🙂', 'j': '🙃', 'k': '🫠', 'l': '😉', 'm': '😊', 'n': '😇', "ñ": "🌟",'o': '🥰', 'p': '😍', 'q': '🤩', 'r': '😘', 's': '😗', 't': '😚', 'u': '😙', 'v': '🥲', 'w': '😋', 'x': '😛', 'y': '😜', 'z': '🤪', ' ': '😝', ',': '🤑', '.': '🤗', ';': '🤭', ':': '🫢', '-': '🤐', '_': '🤫', '/': '🤔', '*': '🫡', '+': '🤨', '(': '😐', ')': '😑', '%': '😶', '&': '🫥', '"': '🥵', '!': '😏', '?': '😒', '$': '🙄', "'": '😬','A': '🏰', 'B': '🗽', 'C': '🎡', 'D': '🚀', 'E': '💎','F': '📱', 'G': '💻', 'H': '🎨', 'I': '🎲', 'J': '🧩','K': '🎸', 'L': '🎺', 'M': '🏀', 'N': '⚽', 'O': '🏓','P': '🎳', 'Q': '🛹', 'R': '🎿', 'S': '🪂', 'T': '🏹','U': '🎭', 'V': '💙', 'W': '🧵', 'X': '🧶', 'Y': '📚','Z': '📌', '0': '🧲', 'Ñ': '🔔'}


def encrypt(ms):
    """
    Function to encrypt a message to emojis
    """
    finals = []
    for letra in ms:
        x = emojis.get(letra)
        if x is not None:
            finals.append(x)
        elif x is None:
            print("Null character found: "+letra)
    return "".join(finals)


def decrypt(ms):
    """
    Function to descrypt emojis to a message
    """
    finals = []
    for emoji in ms:
        for key, value in emojis.items():
            if emoji == value:
                finals.append(key)
                break
    return "".join(finals)