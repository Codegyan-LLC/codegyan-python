import unittest
from codegyan import Codegyan


class TestSingletonPattern(unittest.TestCase):
    """Test cases to verify the singleton pattern implementation in Codegyan class."""
    
    def setUp(self):
        """Reset the singleton instance before each test to ensure isolation."""
        # This is a bit of a hack but necessary for testing singleton with unittest
        # We directly access the class variable to reset it
        Codegyan._instance = None
    
    def tearDown(self):
        """Clean up after each test."""
        Codegyan._instance = None
    
    def test_singleton_instance_creation(self):
        """Test that only one instance of Codegyan is created."""
        # Create first instance
        client1 = Codegyan('test_api_key_1', 'test_client_id_1')
        
        # Create second instance with same credentials
        client2 = Codegyan('test_api_key_1', 'test_client_id_1')
        
        # Both instances should be the same object
        self.assertIs(client1, client2)
        
    def test_singleton_different_credentials_first_call(self):
        """Test singleton behavior when first instance uses specific credentials."""
        # Create first instance
        client1 = Codegyan('first_key', 'first_id')
        
        # Create second instance with different credentials
        # Should still return the first instance due to singleton pattern
        client2 = Codegyan('different_key', 'different_id')
        
        # Both instances should be the same object (first one)
        self.assertIs(client1, client2)
        
        # The instance should have the credentials from the first initialization
        self.assertEqual(client1.api_key, 'first_key')
        self.assertEqual(client1.client_id, 'first_id')
        
    def test_singleton_initialization_happens_once(self):
        """Test that initialization logic in __init__ runs only once."""
        # We'll test this by checking that the api_key and client_id
        # are only set from the first initialization call
        
        # Create first instance with specific credentials
        client1 = Codegyan('first_key', 'first_id')
        
        # Store the values from first initialization
        first_api_key = client1.api_key
        first_client_id = client1.client_id
        
        # Create second instance with different credentials
        # Due to singleton pattern, this should return the same instance
        # and NOT re-initialize with the new credentials
        client2 = Codegyan('second_key', 'second_id')
        
        # Both should be the same instance
        self.assertIs(client1, client2)
        
        # The instance should still have the credentials from the FIRST initialization
        # because __init__ returns early after the first time due to _initialized flag
        self.assertEqual(client2.api_key, first_api_key)
        self.assertEqual(client2.client_id, first_client_id)
        
        # And they should NOT have the second set of credentials
        self.assertNotEqual(client2.api_key, 'second_key')
        self.assertNotEqual(client2.client_id, 'second_id')
    
    def test_singleton_shared_state(self):
        """Test that instances share state due to being the same object."""
        # Create first instance and set attributes
        client1 = Codegyan('api_key', 'client_id')
        client1.test_attribute = "shared_value"
        
        # Create second instance
        client2 = Codegyan('api_key', 'client_id')
        
        # Second instance should have the attribute set by first
        self.assertEqual(client2.test_attribute, "shared_value")
        
        # Modifying attribute through second instance should affect first
        client2.test_attribute = "modified_value"
        self.assertEqual(client1.test_attribute, "modified_value")


if __name__ == '__main__':
    unittest.main()