#!/usr/bin/env python3
from Base import app
from proclaimAPI import ProclaimAPI
import os
print('new...')
os.chdir(os.path.dirname(os.path.abspath(__file__)))
ProclaimAPI(app.ProclaimAction.PreviousSlide)