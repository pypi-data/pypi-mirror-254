import asyncio
import inspect
from argparse import ArgumentParser
import typing


class ClassArgParser(ArgumentParser):
    """
    Used to automatically instantiate CLIs from a class

    Usage
    ```
    from typing import Literal

    class Main(ClassArgParser):

        def __init__(self) -> None:
            super().__init__(name="Class ArgParser")

        def no_args(self):
            print("no_args")

        def some_args(self, arg: str):
            print("some_args", arg)

        def default_values(self, arg: str, default: int = 0):
            print("default_values", arg, default)

        def list_values(self, values: List[str]):
            print("list_values", values)

        def untyped_arg(self, untyped):
            print("untyped_arg", untyped)

        async def async_func(self, arg: str):
            print("async_func", arg)

        def literal_options(self, arg: Literal["a", "b"]):
            print("literal_options", arg)

    if __name__ == "__main__":
        Main()()
    ```
    """

    __argparse_members = [
        v.__name__
        for (_, v) in inspect.getmembers(ArgumentParser(), predicate=inspect.ismethod)
    ]

    def __init__(self, name, **kwargs) -> None:
        super().__init__(name, **kwargs)
        self.__subparsers = self.add_subparsers(
            dest="action",
            required=True,
            parser_class=ArgumentParser,
        )
        self.__add_parsers__()

    def __add_parsers__(self):
        members = inspect.getmembers(self, predicate=inspect.ismethod)
        for ref_name, member in members:
            member_name = member.__name__
            if self.__allowed_member_name(member_name):
                # public functions only, __ functions are either private or dunder
                argpsec = inspect.signature(member)
                self.__add_method_parser__(member_name, argpsec)

    def __allowed_member_name(self, member_name: str):
        if member_name.startswith("__"):
            # __ functions are either private or dunder
            return False
        if member_name in self.__argparse_members:
            # don't want to map argparse functions again
            return False
        return True

    def __add_method_parser__(self, member_name: str, argpsec: inspect.Signature):
        method_parser = self.__subparsers.add_parser(member_name)
        for arg_name, signature in argpsec.parameters.items():
            self.__add_argument__(
                parser=method_parser, arg_name=arg_name, signature=signature
            )

    def __add_argument__(
        self,
        parser: ArgumentParser,
        arg_name: str,
        signature: inspect.Parameter,
    ):
        has_default = signature.default is not inspect._empty
        default_value = signature.default if has_default else None
        arg_name = f"--{arg_name}" if has_default else arg_name
        arg_type = signature.annotation
        if typing.get_origin(arg_type) == typing.Literal:
            choices = typing.get_args(arg_type)
            parser.add_argument(arg_name, choices=choices, default=default_value)
        elif typing.get_origin(arg_type) == list:
            list_type = typing.get_args(arg_type)[0]
            parser.add_argument(
                arg_name, type=list_type, nargs="*", default=default_value
            )
        elif arg_type is not inspect._empty:
            parser.add_argument(arg_name, type=arg_type, default=default_value)
        else:
            parser.add_argument(arg_name, default=default_value)

    def __call__(self):
        args = self.parse_args()
        variables = vars(args)
        action_name = variables["action"]
        del variables["action"]
        func = getattr(self, action_name)
        if inspect.iscoroutinefunction(func):
            asyncio.run(func(**variables))
        else:
            func(**variables)
