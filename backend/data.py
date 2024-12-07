import datetime
from typing import List

import pandas as pd

from models import ItemCollection, Item


map_dict = {
    "item_name": "Имя Товара",
    "item_id": "Артикул",
    "brand_name": "Имя бренда",
    "rest_count": "Остаток",
    "timestamp": "Дата"
}
def map_name(field_name: str) -> str:
    return map_dict[field_name]


def read_excel(path):
    try:
        df = pd.read_excel(path)
    except Exception as e:
        df = pd.DataFrame()
        df.to_excel(path)
    return df


def append_to_df(df: pd.DataFrame, item_collection: ItemCollection):
    items: List[Item] = item_collection.items
    items_dict: dict = {}
    for key in Item.model_fields.keys():
        mapped_name = map_name(key)
        items_dict[mapped_name] = []

    for item in items:
        for key in Item.model_fields.keys():
            attr_value = getattr(item, key)
            if isinstance(attr_value, datetime.datetime):
                attr_value = attr_value.strftime("%d-%m-%Y")
            mapped_name = map_name(key)
            items_dict[mapped_name].append(attr_value)

    new_df = pd.DataFrame(items_dict)
    df = pd.concat([df, new_df], ignore_index=True)
    df.to_excel("data.xlsx", index=False)
