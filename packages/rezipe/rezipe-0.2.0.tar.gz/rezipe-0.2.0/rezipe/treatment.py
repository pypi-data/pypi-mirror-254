
from typing import Any, ParamSpec, TypeVar
from pint import Unit

from rezipe.ingredient import Ingredient, IngredientGroup

T_Retval = TypeVar("T_Retval")
T_ParamSpec = ParamSpec("T_ParamSpec")
T = TypeVar("T")

class GenericTreatment:
    name: str
    duration: Unit | None = None
    temperature: Unit | None = None
    notes: str | None = None

    def __init__(self, name, *, duration= None, temperature= None, notes = None,**kwargs) -> None:
        self.name = name
        self.duration = duration
        self.temperature = temperature
        self.notes = notes
        self.__dict__.update(kwargs)

    
        
    def __call__(self, *args: Ingredient | IngredientGroup, **kwds: Any) -> Any:
        pass