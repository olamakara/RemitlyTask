##Verifying JSON input
The programme verifies the input JSON data. Input data format is defined as AWS::IAM::Role Policy - definition and 
example (https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-role-policy.html). Method returns logical false if an input JSON Resource field 
contains a single asterisk and true in any other case. 

JSON example:
```
{
    "PolicyName": "root",
    "PolicyDocument": {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "IamListAccess",
                "Effect": "Allow",
                "Action": [
                    "iam:ListRoles",
                    "iam:ListUsers"
                ],
                "Resource": "*"
            }
        ]
    }
}
```

##How to Run
If you don't have python installed on your computer, please install it from the internet, 
add installed folder to PATH and follow the instructions below.

1. Download the code from this repository (Code -> Download ZIP) and unpack the folder on your computer.
2. Open unpacked folder in terminal and type:
    
    ```python -m verify_json_policy```

3. Type the name of the input file
   
   ```example.json```
4. To run tests, type:
    
    ```python -m test_verify_json_policy```

   
If you want to use your own file, add it to the current folder and type its name instead.
