from __future__ import annotations
from enum import Enum

__all__ = [
    "Preprocessables",
    "Informables",
]


class Preprocessables(Enum):
    """ PreProcessType """
    # Swap
    SWAP = "Swap"                      # To determine if swap needs to cost more or less,
    #                                  # if swap is fast action or combat action
    # Skill
    SKILL = "Skill"                    # same as SWAP but for skill
    # Card
    CARD1 = "Card1"                    # same as SWAP but for card, for the first time
    CARD2 = "Card2"                    # same as SWAP but for card, for the second time
    # Damages
    DMG_ELEMENT = "DmgElement"         # To determine the element
    DMG_REACTION = "DmgReaction"       # To determine the reaction
    DMG_AMOUNT_PLUS = "DmgNumberPlus"  # To determine final amount of damage (addition/subtraction)
    DMG_AMOUNT_MINUS = "DmgNumberMinus"# To determine final amount of damage (addition/subtraction)
    DMG_AMOUNT_MUL = "DmgNumberMul"    # To determine final amount of damage (multiplication/division)
    # Roll Phase
    ROLL_CHANCES = "RollChances"       # To modify the roll chances
    ROLL_DICE_INIT = "RollDiceInit"    # To modify the initial dice

class Informables(Enum):
    DMG_DEALT = "DmgDealt"
    HEALING = "Healing"
    REACTION_TRIGGERED = "ReactionTriggered"
    PRE_SKILL_USAGE = "PreSkillUsage"
    POST_SKILL_USAGE = "PostSkillUsage"
    CHARACTER_DEATH = "CharacterDeath"
    EQUIPMENT_DISCARDING = "EquipmentDiscarding"
