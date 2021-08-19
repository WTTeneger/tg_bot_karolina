import datetime
import os
import random
import threading
import time
import schedule
from collections import namedtuple



import telebot
from telebot import types
from telebot.types import InputMediaPhoto

from _service import data_base, theards
from decouple import config
bot = telebot.TeleBot(config('tg_token'))

from _app import buttons, tg
person = namedtuple('per', ['name', 'age', 'sex'])
