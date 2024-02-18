class NotInCI(Exception):
    """Exception raised when CI env variables are not found
    in the environment.
    """
    def __init__(self, env_variable):
        self.message = (f"We did not find {env_variable} among the environment"
                        " variables. Make sure you exported correctly.")
        super().__init__(self.message)
