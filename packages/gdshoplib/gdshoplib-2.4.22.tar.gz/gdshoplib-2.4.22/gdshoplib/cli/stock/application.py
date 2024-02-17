import typer

from gdshoplib.cli.stock.cart import app as cart

app = typer.Typer()

app.add_typer(cart, name="cart")

if __name__ == "__main__":
    app()
