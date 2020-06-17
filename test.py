import server
import unittest
import xmlrunner
import helpers
import time
      
        # wow cant remember python

class TestHelpers(unittest.TestCase):
    """unit tests: helper functions."""

    def test_is_person(self):
        """Test adder function."""

        self.assertEqual(helpers.is_person('Henna'), True)
#         self.assertEqual(helpers.is_person('. '), True)
    def a(self):
        """Test adder function."""

        self.assertEqual(helpers.is_person('User'), True)
    def b(self):
        """Test adder function."""

        self.assertEqual(helpers.is_person('Henna'), True)
#         self.assertEqual(helpers.is_person('. '), True)
    def z(self):
        """Test adder function."""

        self.assertEqual(helpers.is_person('Henna'), True)     
    def test_wait(self):
        """Test wait function."""
            
        self.assertEqual(helpers.wait(10), True)  
    def test_wait1(self):
        """Test wait function."""
            
        self.assertEqual(helpers.wait(100), True)   
    def test_wait2(self):
        """Test wait function."""
            
        self.assertEqual(helpers.wait(50), True)        
    def test_wait3(self):
        """Test wait function."""
            
        self.assertEqual(helpers.wait(15), True)  
    def test_wait4(self):
        """Test wait function."""
            
        self.assertEqual(helpers.wait(32), True)   
    def test_wait5(self):
        """Test wait function."""
            
        self.assertEqual(helpers.wait(73), True)        

class TestFlaskRoutes(unittest.TestCase):
    """Test Flask routes."""

    def test_index(self):
        """Make sure index page returns correct HTML."""

        # Create a test client
        client = server.app.test_client()
        server.app.config['TESTING'] = True

            # Use the test client to make requests
        result = client.get('/')

        # Compare result.data with assert method
        self.assertIn(b'<h1>Welcome</h1>', result.data)
#         self.assertIn(b'<h1>Bob</h1>', result.data)
        self.assertEqual(result.status_code, 200)

    def test_form(self):
        """Test that / route processes form data correctly."""

        client = server.app.test_client()
        server.app.config['TESTING'] = True
        result = client.post('/', data={'person': 'Henna'})
        self.assertIn(b'Henna', result.data)  
        self.assertEqual(result.status_code, 200)

    def test_test(self):
        """Test that / route processes form data correctly."""

        client = server.app.test_client()
        server.app.config['TESTING'] = True
        result = client.post('/', data={'person': 'Henna'})
        self.assertIn(b'Henna', result.data)  
        self.assertEqual(result.status_code, 200)  

    def fake_test(self):
        """Test that / route processes form data correctly."""

        client = server.app.test_client()
        server.app.config['TESTING'] = True
        result = client.post('/', data={'person': 'Henna'})
        self.assertIn(b'Henna', result.data)  
        self.assertEqual(result.status_code, 200)
        
        
    def A(self):
        """Make sure index page returns correct HTML."""

        # Create a test client
        client = server.app.test_client()
        server.app.config['TESTING'] = True

            # Use the test client to make requests
        result = client.get('/')

        # Compare result.data with assert method
        self.assertIn(b'<h1>Welcome</h1>', result.data)
#         self.assertIn(b'<h1>Bob</h1>', result.data)
        self.assertEqual(result.status_code, 200)

    def B(self):
        """Test that / route processes form data correctly."""

        client = server.app.test_client()
        server.app.config['TESTING'] = True
        result = client.post('/', data={'person': 'Henna'})
        self.assertIn(b'Henna', result.data)  
        self.assertEqual(result.status_code, 200)
    def Z(self):
        """Make sure index page returns correct HTML."""

        # Create a test client
        client = server.app.test_client()
        server.app.config['TESTING'] = True

            # Use the test client to make requests
        result = client.get('/')

        # Compare result.data with assert method
        self.assertIn(b'<h1>Welcome</h1>', result.data)
#         self.assertIn(b'<h1>Bob</h1>', result.data)
        self.assertEqual(result.status_code, 200)

    def D(self):
        """Test that / route processes form data correctly."""

        client = server.app.test_client()
        server.app.config['TESTING'] = True
        result = client.post('/', data={'person': 'Henna'})
        self.assertIn(b'Henna', result.data)  
        self.assertEqual(result.status_code, 200)
          


   
    
if __name__ == "__main__":
    unittest.main(
        # testRunner=xmlrunner.XMLTestRunner(output=os.environ.get('CIRCLE_TEST_REPORTS','test-reports')),
        testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
        # these make sure that some options that are not applicable
        # remain hidden from the help menu.
        failfast=False, buffer=False, catchbreak=False)       
#test
