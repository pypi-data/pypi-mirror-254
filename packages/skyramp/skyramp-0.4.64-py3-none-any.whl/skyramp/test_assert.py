"""
Contains helpers for interacting with Skyramp test assert.
"""
class _Assert:
    def __init__(self, assert_value: str, assert_expected_value: str) -> None:
        self.assert_value = assert_value
        self.assert_expected_value = assert_expected_value

    def to_json(self):
        """
        Convert the object to dictionary
        """
        value = self.assert_value
        if not self.assert_value.startswith("requests."):
            value = f"requests.{self.assert_value}"
        assert_string = f'{value} == "{self.assert_expected_value}"'
        return {
            "asserts": assert_string
        }
    