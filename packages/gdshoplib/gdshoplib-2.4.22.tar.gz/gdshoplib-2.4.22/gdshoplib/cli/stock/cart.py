import webbrowser
from typing import Optional

import qrcode
import qrcode.image.svg
import typer
from jinja2 import Environment, FileSystemLoader, select_autoescape

from gdshoplib.apps.products.product import Product
from gdshoplib.core.settings import GeneralSettings

app = typer.Typer()


class Content:
    DESCRIPTION_TEMPLATE = "cart.html"

    def __init__(self):
        self.settings = GeneralSettings()
        self.jinja2_env = self.jinja2_env()

    def generate(self, platform):
        return self.render(platform)

    def get_template(self):
        return self.jinja2_env.get_template(self.DESCRIPTION_TEMPLATE)

    def render(self, data):
        return self.get_template().render(**data)

    def jinja2_env(self):
        return Environment(
            loader=FileSystemLoader(self.settings.TEMPLATES_PATH),
            autoescape=select_autoescape(),
        )

    def save(self, data):
        filename = str((self.settings.TEMPLATES_PATH / "stock_cart.html").resolve())
        with open(filename, "w") as file:
            file.write(self.render(data))
        return filename

    def qr_code(self, content):
        file = str((self.settings.TEMPLATES_PATH / "qr.png").resolve())
        qr = qrcode.QRCode(border=0)
        qr.add_data(content)
        img = qr.make_image(fit=True)
        img.save(file)

        return file


def generate_cart(product_sku, count=1, size=None):
    product = Product.get(product_sku)
    # Сгенерировать текст для карточки
    for size in [size] if size else product.size.split("/"):
        for _ in range(count):
            content = Content()
            webbrowser.get("open -a /Applications/Google\ Chrome.app %s").open(
                content.save(
                    dict(
                        product=product,
                        size=size,
                        name=content.settings.TEMPLATES_PATH / "name.png",
                        qr=content.qr_code(product.url),
                    )
                )
            )
            input("Следующий")


@app.command()
def generate(
    sku: Optional[str] = typer.Option(None),
    count: int = 1,
    size: Optional[str] = typer.Option(None),
):
    """Генерация карточек"""
    # Получить продукт, пройтись по всем продуктам
    if sku:
        generate_cart(sku, count=count, size=size)
        return

    for product in Product.query(filter=dict(status_publication="Публикация")):
        generate_cart(product.sku)


if __name__ == "__main__":
    app()
