from flask import Flask,render_template, request, redirect, url_for, session
from flask_caching import Cache

import urllib.parse
from lyrics_rub import *
import pandas as pd
import logging

import unittest

class Test_app(unittest.TestCase):
    def test_create_app(self):
        self.assertIsNotNone(1)


if __name__ == '__main__':
    unittest.main()