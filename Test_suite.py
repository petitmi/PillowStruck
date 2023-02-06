from Test.test_artist_struck import Test_artist_struck as tas
from Test.test_spotify_stare import Test_spotify_stare as tss
from Test.test_app import Test_app as ta
from Test.test_lyrics_rub import Test_lyrics_rub as tlr
from Test.test_lyrics_struck import Test_lyrics_struck as tls 


import unittest

def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(tas))
    suite.addTest(unittest.makeSuite(tss))
    suite.addTest(unittest.makeSuite(ta))
    suite.addTest(unittest.makeSuite(tlr))
    suite.addTest(unittest.makeSuite(tls))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))
    
my_suite()