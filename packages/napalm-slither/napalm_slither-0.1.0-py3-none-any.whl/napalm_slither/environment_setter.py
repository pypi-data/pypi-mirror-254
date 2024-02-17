import os


class EnvironmentSetter:
    """
    A context manager for setting an environment variable within a context.

    The environment variable is set when entering the context and removed when exiting the context.

    Attributes:
        key (str): The name of the environment variable to set.
        value (str): The value to set the environment variable to.
        original_value (str): The original value of the environment variable before it was set.
    """

    def __init__(self, key, value):
        """
        Initializes the set_environment context manager with the specified key and value.

        Args:
            key (str): The name of the environment variable to set.
            value (str): The value to set the environment variable to.
        """
        self.key = key
        self.value = str(value)

    def __enter__(self):
        """
        Sets the environment variable to the specified value when entering the context.

        If the environment variable already exists, its original value is stored so it can be restored when exiting the context.
        """
        self.original_value = os.environ.get(self.key)
        os.environ[self.key] = self.value

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Removes the environment variable or restores its original value when exiting the context.

        If the environment variable did not exist before entering the context, it is removed. If it did exist, its original value is restored.
        """
        if self.original_value is None:
            os.environ.pop(self.key, None)
        else:
            os.environ[self.key] = self.original_value
