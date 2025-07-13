import sys


def test_case_ccoption():
    from Option import CCOption, CCOptionType, CCOptionDepends, CCOptionDependsRelation

    dep_from_string = "another_option == another_value"
    depends = CCOptionDepends.from_string(dep_from_string)
    print(f"Parsed depends: {depends.__str__()}")

    dep_from_string = "another_option != 123"
    depends_not = CCOptionDepends.from_string(dep_from_string)
    print(f"Parsed depends (not): {depends_not.__str__()}")

    dep_from_string = "!another_option"
    depends_not = CCOptionDepends.from_string(dep_from_string)
    print(f"Parsed depends (not with no value): {depends_not.__str__()}")

    # Create a CCOption instance
    option = CCOption(
        name="test_option",
        opt_type=CCOptionType.STRING,
        default="default_value",
        description="This is a test option",
        value="test_value",
        depends=CCOptionDepends(option="another_option", value="another_value", relation=CCOptionDependsRelation.EQUAL)
    )

    # Print the option
    print(option)

    # Convert to JSON and print
    json_str = option.to_json()
    print(f"JSON representation: {json_str}")


    option = CCOption.from_json(json_str)
    print(f"Option from JSON: {option.to_json()}")

    option = CCOption.from_json('{"name": "test_option", "type": "string", "default": "default_value", "description": "This is a test option", "value": "test_value", "depends": "another_option==another_value"}')
    print(f"Option from JSON string: {option.to_json()}")

    option = CCOption.from_json('{"name": "version_option", "type": "string", "default": "1.0.0", "description": "This is a test option", "depends": "use_test_lib"}')
    print(f"Option from JSON string with depends: {option.to_json()}")


if __name__ == '__main__':

    # get case from command line arguments
    test_case = None
    if len(sys.argv) > 1:
        test_case = sys.argv[1]
    else:
        print("Usage: python u_test.py <test_case>")
        sys.exit(1)

    if test_case == "option":
        test_case_ccoption()
