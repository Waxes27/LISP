class Decorators:
    def muted(self, function_name: str):
        """Decorator for muting tests temporarily

        Please use this like you would use Java annotations (@muted).
        This is not made for escaping the need to test, it is a quick workaround for current (19 Aug 2021) tests that were made before passing tests were enforced by the pipeline
        """
        def _decorator():
            print(function_name.__name__ + " has been muted")

        return _decorator
