import unittest
from verify_json_policy import verify_iam_policy


class TestIAMPolicyVerification(unittest.TestCase):
    def test_valid_iam_policy_with_asterisk_at_the_end(self):
        # Valid policy with non-asterisk Resource
        valid_policy = '''
        {
            "PolicyName": "test-policy",
            "PolicyDocument": {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Effect": "Allow",
                        "Action": "s3:GetObject",
                        "Resource": "arn:aws:s3:::example-bucket/*"
                    }
                ]
            }
        }
        '''
        self.assertTrue(verify_iam_policy(valid_policy))

    def test_valid_iam_policy_with_asterisk_at_the_beginning(self):
        # Valid policy with non-asterisk Resource
        valid_policy = '''
        {
            "PolicyName": "test-policy",
            "PolicyDocument": {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Effect": "Allow",
                        "Action": "s3:GetObject",
                        "Resource": "*/arn:aws:s3:::example-bucket/"
                    }
                ]
            }
        }
        '''
        self.assertTrue(verify_iam_policy(valid_policy))

    def test_valid_iam_policy_with_asterisk_in_the_middle(self):
        # Valid policy with non-asterisk Resource
        valid_policy = '''
        {
            "PolicyName": "test-policy",
            "PolicyDocument": {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Effect": "Allow",
                        "Action": "s3:GetObject",
                        "Resource": "arn:aws:s3:*::example-bucket"
                    }
                ]
            }
        }
        '''
        self.assertTrue(verify_iam_policy(valid_policy))

    def test_valid_iam_policy_with_few_asterisks(self):
        # Valid policy with non-asterisk Resource
        valid_policy = '''
        {
            "PolicyName": "test-policy",
            "PolicyDocument": {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Effect": "Allow",
                        "Action": "s3:GetObject",
                        "Resource": "**"
                    }
                ]
            }
        }
        '''
        self.assertTrue(verify_iam_policy(valid_policy))

    def test_invalid_iam_policy_with_asterisk_resource(self):
        # Invalid policy with Resource containing single asterisk
        invalid_policy = '''
        {
            "PolicyName": "test-policy",
            "PolicyDocument": {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Effect": "Allow",
                        "Action": "s3:GetObject",
                        "Resource": "*"
                    }
                ]
            }
        }
        '''
        self.assertFalse(verify_iam_policy(invalid_policy))

    def test_json_decode_error(self):
        # Test JSON decoding error
        invalid_json = {}
        self.assertTrue(verify_iam_policy(invalid_json))

    def test_key_error(self):
        # Test KeyError for missing required key
        invalid_policy = '''
        {
            "PolicyName": "test-policy",
            "PolicyDocument": {
                "Version": "2012-10-17"
            }
        }
        '''
        self.assertTrue(verify_iam_policy(invalid_policy))

    def test_value_error(self):
        # Test ValueError for invalid data type
        invalid_policy = '''
        {
            "PolicyName": "test-policy",
            "PolicyDocument": {
                "Version": "2012-10-17",
                "Statement": "invalid_statement"
            }
        }
        '''
        self.assertTrue(verify_iam_policy(invalid_policy))


if __name__ == '__main__':
    unittest.main()
