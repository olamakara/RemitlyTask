import json


def verify_iam_policy(json_data):
    try:
        # Parse the JSON data
        data = json.loads(json_data)

        # Validate Resource field
        policy_doc = data.get("PolicyDocument", {})
        statements = policy_doc.get("Statement", [])
        for statement in statements:
            resource = statement.get("Resource", "")
            if resource == "*":
                return False  # Reject if Resource contains a single asterisk

        return True

    except (KeyError, TypeError, ValueError, AttributeError) as e:
        print(f"Error occurred during JSON parsing and validation: {e}")
        return True

    except json.JSONDecodeError as e:
        print(f"Error decoding JSON data: {e}")
        return True

    except Exception as e:
        print(f"Error occurred: {e}")
        return True


def main(json_file_path):
    try:
        # Read JSON from file
        with open(json_file_path, 'r') as file:
            json_data = file.read()

        return verify_iam_policy(json_data)

    except (IOError, FileNotFoundError) as e:
        print(f"Error reading JSON from file: {e}")
        return True

    except Exception as e:
        print(f"Error occurred: {e}")
        return True


if __name__ == '__main__':
    json_file = input("File name: ")
    result = main(json_file)
    print("Output: " + str(result))
