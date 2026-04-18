# test_rangoexchange.py
"""
Tests for RangoExchange module.
"""

import unittest
from rangoexchange import RangoExchange

class TestRangoExchange(unittest.TestCase):
    """Test cases for RangoExchange class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = RangoExchange()
        self.assertIsInstance(instance, RangoExchange)
        
    def test_run_method(self):
        """Test the run method."""
        instance = RangoExchange()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
