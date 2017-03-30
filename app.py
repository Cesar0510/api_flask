#! /usr/bin/env python
# -*- coding: utf-8 -*-
#---------------------------------------------
# Copyright:   (c) Cesar Herdenez 2017
# Licence:     BSD 3-Clause License
#-------------------------------------------


from flask import Flask
from config import Development


app = Flask(__name__)
app.config.from_object(Development)

#if __name__ == '__main__':
