
from dataclasses import asdict, dataclass
import decimal
from functools import lru_cache
from typing import Any, Literal, Self, overload
import marvin
from pint import Unit
from pydantic import BaseModel
import pandas as pd
from rezipe.goods import Goods
from rezipe.utils_jupyter import is_in_notebook, show_dataframe
from joblib import Memory

memory = Memory('~/.config/rezipe/cache', verbose=1)

@dataclass
class IngredientGroup:
    ingredients: list["Ingredient"]

    @property
    def weight(self) -> Unit:
        return sum(ingredient.weight for ingredient in self.ingredients)

    @overload
    def __add__(self, other: Self) -> Self:
        return IngredientGroup(ingredients=self.ingredients + other.ingredients)
    
    @overload
    def __add__(self, other: "Ingredient") -> Self:
        return IngredientGroup(ingredients=self.ingredients + [other])
    
    def _scale(self, factor: float) -> Self:
        return IngredientGroup(ingredients=[Ingredient(name=ingredient.name, weight=ingredient.weight*factor) for ingredient in self.ingredients])

    @overload
    def scale(self, factor: float) -> Self:
        return self._scale(factor)

    @overload
    def scale(self, ingredient: "Ingredient", want_to_be: Unit) -> Self:
        return self._scale(want_to_be / ingredient.weight)
    
    def scale_to(self, desired_weight: Unit) -> Self:
        return self._scale(desired_weight / self.weight)

    def __mul__(self, factor: float) -> Self:
        return self._scale(factor)

    def provide_nutrition(self, format: Literal['tldr', 'full']) -> dict[str, decimal.Decimal]:
        pass
    
    def pretty(self, show_pct=True) -> None:
        new_var = [asdict(ingredient) for ingredient in self.ingredients]
        df = pd.DataFrame.from_records(new_var)

        # drop all null columns
        df = df.dropna(axis=1, how='all')

        # add weight pct column
        if show_pct and 'weight' in df.columns:
            df['weight_pct'] = df['weight'] / df['weight'].sum() * 100
            # round to 2 decimal places
            df['weight_pct'] = df['weight_pct'].round(2)

        return show_dataframe(df)

    def get_nutrition(self) -> dict[str, decimal.Decimal]:
        data = [ingredient.get_nutrition() for ingredient in self.ingredients]
        return data

    def get_nutrition_table(self) -> None:
        data = self.get_nutrition()
        df = pd.DataFrame.from_records(data)

        # strip str subject column
        df['subject'] = df['subject'].str.strip()

        df = df.set_index('subject')
        return df

    def __repr__(self) -> str:
        return self.pretty()
    
    def change_weight_unit(self, new_unit: Unit) -> Self:
        self.ingredients = [ingredient.change_weight_unit(new_unit) for ingredient in self.ingredients]
        return self

# alias
IG = ส่วนผสมทั้งหมด = IngredientGroup
IngredientGroup.ปรับให้มีน้ำหนัก = IngredientGroup.scale_to
IngredientGroup.ขอน้ำหนักหน่วย = IngredientGroup.change_weight_unit

@marvin.model
class TLDRNutrition(BaseModel):
    subject: str
    calories_cal: decimal.Decimal
    crab_gram: decimal.Decimal
    protein_gram: decimal.Decimal
    fat_gram: decimal.Decimal
    fiber_gram: decimal.Decimal

@memory.cache
def get_nutrition(subject: str) -> dict[str, decimal.Decimal]:
    return TLDRNutrition(subject).model_dump()

@dataclass
class Ingredient(Goods):
    weight: Unit | None = None

    @property
    def ai_repr(self) -> str:
        return f"{self.name} {self.weight if self.weight is not None else ''}"
    
    def get_nutrition(self) -> dict:
        return get_nutrition(self.ai_repr)

    @overload
    def __add__(self, other: Self) -> IngredientGroup:
        return IngredientGroup(ingredients=[self, other])

    @overload
    def __add__(self, other: IngredientGroup) -> IngredientGroup:
        return IngredientGroup(ingredients=[self] + other.ingredients)
    
    @classmethod
    def as_follow(cls, *args: list[str | Unit]):
        maybe_ig = [cls(name=name, weight=weight) for name, weight in zip(args[::2], args[1::2])]
        return IngredientGroup(ingredients=maybe_ig)

    def change_weight_unit(self, new_unit: Unit) -> Self:
        self.weight = self.weight.to(new_unit)
        return self


# alias
I = ส่วนผสม = Ingredient 
ส่วนผสม.ดังต่อไปนี้ = Ingredient.as_follow