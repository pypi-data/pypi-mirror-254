from __future__ import annotations
from dataclasses import dataclass, replace, fields
from typing import Callable, TYPE_CHECKING
from typing_extensions import Self

if TYPE_CHECKING:
    from ..card.cards import Cards
    from ..dice import ActualDice
    from ..state.enums import Pid
    from ..state.game_state import GameState

    from .action import PlayerAction, Instruction
    from .types import DecidedChoiceType, GivenChoiceType

__all__ = [
    "ActionGenerator",
]


def _dummy_choices_helper(_: ActionGenerator) -> GivenChoiceType:
    raise NotImplementedError("You are supposed to override this if needed")


def _dummy_fill_helper(_a: ActionGenerator, _b: DecidedChoiceType) -> ActionGenerator:
    raise NotImplementedError("You are supposed to override this if needed")


@dataclass(frozen=True, kw_only=True)
class ActionGenerator:
    """
    ActionGenerator is a class recording a state of choices made so far.

    If both action and instruction is None, then this action generator is used 
    to generate other ActionGenerators that may eventually generate some action.
    """
    #: the current game_state that the action generator is based on.
    game_state: GameState
    #: the `pid` of the player ActionGenerator is generating action for.
    pid: Pid
    action: None | PlayerAction = None
    instruction: None | Instruction = None
    # used to provide all valid choices for users to choose
    _choices_helper: Callable[[Self], GivenChoiceType] = _dummy_choices_helper  # type: ignore
    # takes user's choice and check if it is valid, if so return another
    # action generator representing the next phase of choice, otherwise raise
    # Exception
    _fill_helper: Callable[[Self, DecidedChoiceType], Self] = _dummy_fill_helper  # type: ignore

    def _action_filled(self) -> bool:
        return self.action is None \
            or self.action._filled(exceptions={"instruction"})

    def _instruction_filled(self) -> bool:
        return self.instruction is None \
            or self.instruction._filled()

    def filled(self) -> bool:
        """
        :returns: `True` if ActionGenerator is ready to produce the final action.
        """
        return not (self.action is None and self.instruction is None) \
            and self._action_filled() and self._instruction_filled()

    def generate_action(self) -> PlayerAction:
        """
        :returns: the final PlayerAction.

        Precondition: `.filled()` is `True`.
        """
        assert self.filled()
        assert self.action is not None
        action = self.action
        if self.instruction is not None:
            action = replace(action, instruction=self.instruction)
        return action

    def choices(self) -> GivenChoiceType:
        """
        :returns: the choices to make a decision from.

        - If return value is a tuple, choose one value from the tuple.
        - If return value is `ActualDice`, choose some dice based on the context.
        - If return value is `AbstractDice`, choose some dice of `ActualDice` that
          can satisfy the `AbstractDice`.
        - If return value is `Cards`, choose some cards from it based on the context.
        """
        assert not self.filled()
        return self._choices_helper(self)

    def dice_available(self) -> ActualDice:
        """
        :returns: the dice the player holds.

        A shortcut method to quickly get the player's dice.
        """
        return self.game_state.get_player(self.pid).dice

    def hand_cards_available(self) -> Cards:
        """
        :returns: the hand cards the player holds.

        A shortcut method to quickly get the player's hand cards.
        """
        return self.game_state.get_player(self.pid).hand_cards

    def choose(self, choice: DecidedChoiceType) -> ActionGenerator:
        """
        :param choice: the choice that the user makes for this stage.

        :returns: a new ActionGenerator representing the next stage of choices.
        """
        assert not self.filled()
        return self._fill_helper(self, choice)

    def __str__(self) -> str:
        field_pairs = [f"<{field.name}, {getattr(self, field.name)}>" for field in fields(self)]
        content = '\n'.join(field_pairs)
        return self.__class__.__name__ + '\n' + content
