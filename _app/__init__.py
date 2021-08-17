import datetime
import os
import random
import threading
import time

import telebot
from telebot import types
from telebot.types import InputMediaPhoto

from _service import data_base, theards
from _settings import env

bot = telebot.TeleBot(env.tg_token)

from _app import buttons, tg