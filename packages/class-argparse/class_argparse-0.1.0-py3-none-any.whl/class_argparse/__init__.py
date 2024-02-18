import asyncio
import inspect
from argparse import ArgumentParser


class ClassArgParser(ArgumentParser):
    """
    Used to automatically instantiate CLIs from a class

    Usage
    ```
    class Main(ClassArgParser):

        def __init__(self) -> None:
            super().__init__(name="Class ArgParser")

        async def foo(self, first: str):
            print(f"foo, first={first}")

        def bar(self):
            print("bar")

        async def baz(self, first: str, second: int):
            print(f"baz, first={first}, second={second}")

    if __name__ == "__main__":
        Main()()
    ```
    """

    __argparse_members = [
        v.__name__
        for (_, v) in inspect.getmembers(ArgumentParser(), predicate=inspect.ismethod)
    ]

    def __init__(self, name) -> None:
        self.__parser = ArgumentParser(name)
        self.__subparsers = self.__parser.add_subparsers(dest="action", required=True)
        self.__add_parsers__()

    def __add_parsers__(self):
        members = inspect.getmembers(self, predicate=inspect.ismethod)
        for ref_name, member in members:
            member_name = member.__name__
            if self.__allowed_member_name(member_name):
                # public functions only, __ functions are either private or dunder
                argpsec = inspect.getfullargspec(member)
                self.__add_method_parser__(member_name, argpsec)

    def __allowed_member_name(self, member_name: str):
        if member_name.startswith("__"):
            # __ functions are either private or dunder
            return False
        if member_name in self.__argparse_members:
            # don't want to map argparse functions again
            return False
        return True

    def __add_method_parser__(self, member_name: str, argpsec: inspect.FullArgSpec):
        method_parser = self.__subparsers.add_parser(member_name)
        args = argpsec.args[1:]
        annotations = argpsec.annotations
        for arg_name in args:
            arg_type = annotations[arg_name]
            method_parser.add_argument(arg_name, type=arg_type)

    def __call__(self):
        args = self.__parser.parse_args()
        variables = vars(args)
        action_name = variables["action"]
        del variables["action"]
        func = getattr(self, action_name)
        if inspect.iscoroutinefunction(func):
            asyncio.run(func(**variables))
        else:
            func(**variables)
