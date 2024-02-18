# Class-Argparse

Class based argument parser to simplify writing CLIs that have lots of options

## How to use

```python
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

## How this works

1. The class `ClassArgParser` extends `ArgumentParser`
2. The initialization function finds add adds all the methods on child classes that are public i.e. their names don't start with `__`
3. The object of the class is called and after identifying whether the function being called it is async or sync it runs the function accordingly
