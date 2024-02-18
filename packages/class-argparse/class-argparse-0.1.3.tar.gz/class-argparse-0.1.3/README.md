# Class-Argparse

Class based argument parser to simplify writing CLIs that have lots of options

## How to use

```python
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

## How this works

1. The class `ClassArgParser` extends `ArgumentParser`
2. The initialization function finds add adds all the methods on child classes that are public i.e. their names don't start with `__`
3. The object of the class is called and after identifying whether the function being called it is async or sync it runs the function accordingly
