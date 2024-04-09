import cProfile
import pstats
import unittest

# Ваши импорты и определения класса RegistrationFormTestCase

def run_tests():
    cProfile.runctx('unittest.main()', globals(), locals(), filename='test_profile.prof')
    stats = pstats.Stats('test_profile.prof')
    stats.print_stats()

if __name__ == "__main__":
    run_tests()