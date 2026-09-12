import typer

app = typer.Typer()

# general exception
try:
    age = int(input("enter your age ?"))
except ValueError:
    print("Please enter a number")


# creat custom exception
class InvalidInputError(Exception):
    pass


# use except
# here without cli :
# name=str(input("enter your name"))


# withcli
@app.command()
def getName(name: str) -> None:
    if not name.isalpha():
        raise InvalidInputError("enter alpha please")
    print(f"hello{name}")


if __name__ == "__main__":
    app()
