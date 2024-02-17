from pydantic import BaseModel

from gdshoplib.apps.platforms.base import Platform
from gdshoplib.apps.products.product import Product
from gdshoplib.packages.feed import Feed
from gdshoplib.services.gdshop.gdshop import DB


class VKProductModel(BaseModel):
    ...


class VKManager(Platform, Feed):
    DESCRIPTION_TEMPLATE = "vk.txt"
    KEY = "VK"

    @property
    def product_filter(self):
        return dict(status_description="Готово")

    # def get_products(self) -> List[VKProductModel]:
    #     ...

    # def push_feed(self):
    #     # Обновить товары в VK
    #     ...


class VKPartnersManager(Platform, Feed):
    DESCRIPTION_TEMPLATE = "vk.txt"
    KEY = "VK-PARTNERS"

    @property
    def products(self):
        for sku in DB().get_partners_products():
            if not sku:
                break
            product = Product.get(sku[0])
            if not product:
                break
            yield product
