"""
The definition of an *Event* in this project is, something that can be
preprocessed by statuses according to the description of each status.
"""
from __future__ import annotations
from dataclasses import dataclass, replace
from enum import Enum
from typing import TYPE_CHECKING

from typing_extensions import Self

from .element import Element, Reaction

if TYPE_CHECKING:
    from .card.card import Card, EquipmentCard
    from .character.character import Character
    from .character.enums import CharacterSkill, CharacterSkillType
    from .dice import ActualDice
    from .effect.effect import SpecificDamageEffect
    from .effect.structs import DamageType, StaticTarget
    from .dice import AbstractDice
    from .state.game_state import GameState
    from .state.enums import Pid
    from .status.status import EquipmentStatus

__all__ = [
    # enums
    "EventSpeed",
    "EventSubType",
    "EventType",

    "InformableEvent",
    "DmgIEvent",
    "CharacterDeathIEvent",
    "EquipmentDiscardIEvent",
    "HealIEvent",
    "ReactionIEvent",
    "SkillIEvent",

    "PreprocessableEvent",
    "ActionPEvent",
    "CardPEvent",
    "DiceRollInitPEvent",
    "DmgPEvent",
    "RollChancePEvent",
]


class EventSpeed(Enum):
    FAST_ACTION = "Fast-Action"
    COMBAT_ACTION = "Combat-Action"


class EventSubType(Enum):
    pass


class EventType(Enum):
    SKILL1 = "Normal-Attack1"
    SKILL2 = "Elemental-Skill1"
    SKILL3 = "Elemental-Skill2"
    ELEMENTAL_BURST = "Elemental-Burst"
    SWAP = "Swap"

    def is_skill(self) -> bool:
        """ :returns: True if this event is a skill"""
        return (
            self is EventType.SKILL1
            or self is EventType.SKILL2
            or self is EventType.SKILL3
            or self is EventType.ELEMENTAL_BURST
        )


@dataclass(frozen=True, kw_only=True)
class InformableEvent:
    pass


@dataclass(frozen=True, kw_only=True)
class DmgIEvent(InformableEvent):
    dmg: SpecificDamageEffect


@dataclass(frozen=True, kw_only=True)
class CharacterDeathIEvent(InformableEvent):
    target: StaticTarget


@dataclass(frozen=True, kw_only=True)
class EquipmentDiscardIEvent(InformableEvent):
    target: StaticTarget
    status: type[EquipmentStatus]


@dataclass(frozen=True, kw_only=True)
class HealIEvent(InformableEvent):
    target: StaticTarget
    heal_amount: int


@dataclass(frozen=True, kw_only=True)
class ReactionIEvent(InformableEvent):
    source: StaticTarget
    target: StaticTarget
    source_type: DamageType
    reaction: Reaction



@dataclass(frozen=True, kw_only=True)
class SkillIEvent(InformableEvent):
    source: StaticTarget
    skill_type: CharacterSkill
    skill_true_type: CharacterSkillType

    def is_skill_from_character(
            self,
            game_state: GameState,
            pid_to_check: Pid,
            skill_type: None | CharacterSkill = None,
            char_type: None | type[Character] = None,
    ) -> bool:
        return (
            self.source.pid is pid_to_check
            and (
                skill_type is None
                or self.skill_type is skill_type
            )
            and (
                char_type is None
                or isinstance(game_state.get_character_target(self.source), char_type)
            )
        )


@dataclass(frozen=True, kw_only=True)
class PreprocessableEvent:
    pass


@dataclass(frozen=True, kw_only=True)
class ActionPEvent(PreprocessableEvent):
    source: StaticTarget       # this source is who caused the GameEvent
    target: None | StaticTarget = None
    event_type: EventType
    event_sub_type: None | EventSubType | CharacterSkillType = None
    event_speed: EventSpeed
    dice_cost: AbstractDice

    def with_new_cost(self, new_cost: AbstractDice) -> Self:
        return replace(self, dice_cost=new_cost)


@dataclass(frozen=True, kw_only=True)
class CardPEvent(PreprocessableEvent):
    pid: Pid
    card_type: type[Card]
    dice_cost: AbstractDice
    invalidated: bool = False

    def with_new_cost(self, new_cost: AbstractDice) -> Self:
        return replace(self, dice_cost=new_cost)

    def invalidate(self) -> Self:
        return replace(self, invalidated=True)


@dataclass(frozen=True, kw_only=True)
class DiceRollInitPEvent(PreprocessableEvent):
    pid: Pid
    dice: ActualDice

    def can_update(self) -> bool:
        """ :returns: True if there are dice that can be 'collapsed'. """
        return self.dice[Element.ANY] > 0

    def update(self, elem: Element, num: int) -> Self:
        """ :returns: event where num dice (if possible) are 'collapsed' into elem. """
        num = min(num, self.dice[Element.ANY])
        return replace(self,
            dice=self.dice + {elem: num, Element.ANY: -num},
        )


@dataclass(frozen=True, kw_only=True)
class DmgPEvent(PreprocessableEvent):
    dmg: SpecificDamageEffect

    def delta_damage(self, d_damage: int) -> Self:
        new_damage = max(0, self.dmg.damage + d_damage)
        return replace(self, dmg=replace(self.dmg, damage=new_damage))

    def convert_element(self, element: Element) -> Self:
        return replace(self, dmg=replace(self.dmg, element=element))

    def change_target(self, target: StaticTarget) -> Self:
        return replace(self, dmg=replace(self.dmg, target=target))


@dataclass(frozen=True, kw_only=True)
class RollChancePEvent(PreprocessableEvent):
    pid: Pid
    chances: int
