import unittest
from unittest.mock import patch, MagicMock

class TestEC2InstanceCreation(unittest.TestCase):

    @patch("boto3.client")
    def test_run_instances(self, mock_boto_client):
        # Mock the boto3 client
        mock_ec2 = MagicMock()
        mock_boto_client.return_value = mock_ec2

        # Sample response to mimic EC2 run_instances
        mock_ec2.run_instances.return_value = {
            "Instances": [{"InstanceId": "i-1234567890abcdef0"}]
        }

        # Import the module (assuming the code is in a file named create_instance.py)
        import create_instance

        # Run the EC2 instance creation function
        instance_id = create_instance.run_ec2_instance()

        # Validate the Instance ID
        self.assertEqual(instance_id, "i-1234567890abcdef0")
        mock_ec2.run_instances.assert_called_once()

if __name__ == "__main__":
    unittest.main()
