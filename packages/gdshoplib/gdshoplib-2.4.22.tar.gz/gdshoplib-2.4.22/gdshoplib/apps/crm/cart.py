from typing import Optional

from pydantic import BaseModel, ValidationError

from gdshoplib.services.gdshop.gdshop import DB


class Cart:
    def __init__(self) -> None:
        self.raws = []

    @classmethod
    def get(cls, order_id):
        cart = Cart()
        for row in DB().get_cart(order_id):
            cart.append(row)

    def extend(self, product):
        try:
            self.raws.append(
                CartRow(
                    sku=product.sku,
                    name=product.name,
                    url="-",
                    supply_price=0,
                    sell_price=product.price_now,
                    quantity=1,
                    supply_discount="-",
                    error=None,
                )
            )
        except ValidationError as e:
            self.raws.append(
                CartRowInvalid(
                    sku=product.sku,
                    name=product.name,
                    url="-",
                    supply_price=0,
                    sell_price=product.price_now,
                    quantity=1,
                    supply_discount="-",
                    error=str(e),
                )
            )

    def append(self, row):
        keys = CartRow.schema()["properties"].keys()
        self.raws.append(CartRow(**dict(zip(keys, row))))

    def __contains__(self, product):
        return product.sku in [i.sku for i in self.raws]

    def update_cart_row(self):
        for r in self.rows:
            self.notion.update_block(
                r.block_id,
                params={
                    "table_row": {
                        "cells": [
                            [self.row_object_formater(r.name)],
                            [self.row_object_formater(r.link)],
                            [self.row_object_formater(r.price)],
                            [self.row_object_formater(r.quantity)],
                            [self.row_object_formater(r.error)],
                        ]
                    }
                },
            )

    def row_object_formater(self, data):
        return {
            "type": "text",
            "text": {"content": f"{data}" if data else "", "link": None},
            "annotations": {
                "bold": False,
                "italic": False,
                "strikethrough": False,
                "underline": False,
                "code": False,
                "color": "default",
            },
            "plain_text": f"{data}" if data else "",
            "href": None,
        }


class CartRow(BaseModel):
    sku: Optional[str]
    name: str
    url: str
    supply_price: float
    sell_price: Optional[str]
    quantity: int
    supply_discount: str
    error: Optional[str]


class CartRowInvalid(BaseModel):
    sku: Optional[str]
    name: Optional[str]
    url: Optional[str]
    supply_price: Optional[str]
    sell_price: Optional[str]
    quantity: Optional[str]
    supply_discount: Optional[str]
    error: str
