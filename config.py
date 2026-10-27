# API Keys
FOUR_SIM_API_KEY = "630021335510c8680196018f40d1dd33"
OTPDOCTOR_API_KEY = "xp9lwevsj063vn85kixjc1tzl9dnugh4"
TEMPOTP_API_KEY = "ce281f8ca8910e6b7b950808d11a87c1"
TEMPORASMS_API_KEY = "57d9ffd5704c5da10a3e82439e511bb53909"

import os
OTPINDIA_API_KEY = os.environ.get("OTPINDIA_API_KEY", "073c8a6b740c9f677e0e91ddcea87dbad24c7583554ec5d5")
BACKGROUND_TIMEOUT_OTPINDIA = 900

# SpyEye
BASE_URL = "https://spyeyeloots3.online/up_yono"

SPYEYE_API_KEY = "TBRSUMANTHARE8I8"
SECRET_KEY = "7a5d8fda4b2e9c4d"

# Timers
MAIN_GAME_WAIT = 130
SUBGAME_FOREGROUND_WAIT = 40
NEXT_GAME_DELAY = 3

BACKGROUND_TIMEOUT_4SIM = 900
BACKGROUND_TIMEOUT_OTPDOCTOR = 1200
BACKGROUND_TIMEOUT_TEMPOTP = 900
BACKGROUND_TIMEOUT_TEMPORASMS = 900

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

# Games map...
GAME_MAP = {
    "567slots": {"api": "567slots", "ui": "567slots"},
    "MBMBet": {"api": "mbmbet", "ui": "MBMBet"},
    "Bingo": {"api": "bingo101", "ui": "Bingo"},
    "IndSlots": {"api": "indslots", "ui": "IndSlots"},
    "HiRummy": {"api": "hirummy", "ui": "HiRummy"},
    "Maha": {"api": "mahagames", "ui": "Maha"},
    "YonoVip": {"api": "yonovip", "ui": "YonoVip"},
    "789Jackpots": {"api": "789jackpots", "ui": "789Jackpots"},
    "INDRummy": {"api": "indrummy", "ui": "INDRummy"},
    "YonoGames": {"api": "yonogames", "ui": "YonoGames"},
    "SpinCrush": {"api": "spincrush", "ui": "SpinCrush"},
    "YonoSlots": {"api": "yonoslots", "ui": "YonoSlots"},
    "GoGoRummy": {"api": "gogorummy", "ui": "GoGoRummy"},
    "INDclub": {"api": "indclub", "ui": "INDclub"},
    "YonoArcade": {"api": "yonoarcade", "ui": "YonoArcade"},
    "Rummy91": {"api": "rummy91", "ui": "Rummy91"},
    "RummyLudo": {"api": "rummyludo", "ui": "RummyLudo"},
    "YonoRummy": {"api": "yonorummy", "ui": "YonoRummy"},
    "ShareSlots": {"api": "shareslots", "ui": "ShareSlots"},
    "YesSpin": {"api": "yesspin", "ui": "YesSpin"},
    "GoldRummy": {"api": "goldrummy", "ui": "GoldRummy"},
    "TopRummy": {"api": "toprummy", "ui": "TopRummy"},
    "JoyRummy": {"api": "joyrummy", "ui": "Joyrummy"}
}
API_TO_UI = {v["api"].lower(): v["ui"] for v in GAME_MAP.values()}