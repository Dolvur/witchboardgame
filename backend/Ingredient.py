from abc import ABC, abstractmethod
from pydantic import BaseModel
from typing import Optional


class Ingredient(BaseModel, ABC):
    type: str
    value: int
    cost: int

    @abstractmethod
    def apply_effect(self, game_state: dict, player_id: str) -> dict:
        """Apply the Ingredient's effect to the game state (e.g., update score, draw extra chips)"""
        pass

    @classmethod
    @abstractmethod
    def create(cls, value: int) -> "Ingredient":
        pass
