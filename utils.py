import re

NITRO_REGEX = re.compile(
    r"(https?:\/\/)?(www\.)?(discord\.gift\/|discordapp\.com\/gifts\/)([A-Za-z0-9]+)"
)

GIVEAWAY_KEYWORDS = ["giveaway", "react", "ends in", "winner"]

def find_nitro(text):
    match = NITRO_REGEX.search(text)
    return match.group(4) if match else None

def is_giveaway(text):
    text = text.lower()
    return any(k in text for k in GIVEAWAY_KEYWORDS)
