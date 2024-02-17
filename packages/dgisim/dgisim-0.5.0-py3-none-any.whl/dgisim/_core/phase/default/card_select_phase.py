from __future__ import annotations
from dataclasses import replace
from typing import Optional, TYPE_CHECKING

from .. import phase as ph

from ...action.action import CardsSelectAction, PlayerAction, EndRoundAction
from ...action.action_generator import ActionGenerator
from ...action.enums import ActionType
from ...helper.quality_of_life import BIG_INT, just
from ...state.enums import Pid, Act

if TYPE_CHECKING:
    from ...action.types import DecidedChoiceType, GivenChoiceType
    from ...card.cards import Cards
    from ...state.game_state import GameState
    from ...state.player_state import PlayerState

__all__ = [
    "CardSelectPhase",
]


class CardSelectPhase(ph.Phase):
    _NUM_CARDS: int = 5

    def _draw_cards_and_activate(self, game_state: GameState) -> GameState:
        p1: PlayerState = game_state.player1
        p2: PlayerState = game_state.player2
        mode = game_state.mode

        from ...card.card import ArcaneLegendCard
        def draw_random_cards(deck_cards: Cards) -> tuple[Cards, Cards]:
            """
            Draw some number of random cards, and prioritize Arcane Legend Cards.
            """
            deck_cards, arcane_cards = deck_cards.pick_random_of_type(
                mode.initial_cards_num(),
                ArcaneLegendCard,
            )
            left_to_draw = mode.initial_cards_num() - arcane_cards.num_cards()
            deck_cards, normal_cards = deck_cards.pick_random(left_to_draw)
            return deck_cards, arcane_cards + normal_cards

        p1_deck, p1_hand = draw_random_cards(p1.deck_cards)
        p2_deck, p2_hand = draw_random_cards(p2.deck_cards)
        mode = game_state.mode
        return game_state.factory().f_player1(
            lambda p1: p1.factory()
            .phase(Act.ACTION_PHASE)
            .card_redraw_chances(game_state.mode.card_redraw_chances())
            .deck_cards(p1_deck)
            .hand_cards(p1_hand)
            .build()
        ).f_player2(
            lambda p2: p2.factory()
            .phase(Act.ACTION_PHASE)
            .card_redraw_chances(game_state.mode.card_redraw_chances())
            .deck_cards(p2_deck)
            .hand_cards(p2_hand)
            .build()
        ).build()

    def _to_starting_hand_select_phase(self, game_state: GameState) -> GameState:
        return game_state.factory().f_phase(
            lambda mode: mode.starting_hand_select_phase()
        ).f_player1(
            lambda p1: p1.factory().phase(Act.PASSIVE_WAIT_PHASE).build()
        ).f_player2(
            lambda p2: p2.factory().phase(Act.PASSIVE_WAIT_PHASE).build()
        ).build()

    def step(self, game_state: GameState) -> GameState:
        p1: PlayerState = game_state.player1
        p2: PlayerState = game_state.player2
        # If both players just entered waiting, assign them cards and make them take actions
        if p1.phase is Act.PASSIVE_WAIT_PHASE and p2.phase is Act.PASSIVE_WAIT_PHASE:
            return self._draw_cards_and_activate(game_state)
        elif p1.phase is Act.END_PHASE and p2.phase is Act.END_PHASE:
            return self._to_starting_hand_select_phase(game_state)
        else:
            raise Exception(f"Unknown Game State to process: {game_state}")

    def _handle_card_drawing(self, game_state: GameState, pid: Pid, action: CardsSelectAction) -> GameState:
        player: PlayerState = game_state.get_player(pid)
        new_deck, new_picked = player.deck_cards.switch_random_different(action.selected_cards)
        new_hand = player.hand_cards - action.selected_cards + new_picked
        new_redraw_chances: int = player.card_redraw_chances - 1
        new_player_phase: Act
        if new_redraw_chances > 0:
            new_player_phase = player.phase
        else:
            new_player_phase = Act.END_PHASE
        return game_state.factory().player(
            pid,
            player.factory()
            .phase(new_player_phase)
            .card_redraw_chances(new_redraw_chances)
            .deck_cards(new_deck)
            .hand_cards(new_hand)
            .build()
        ).build()

    def _handle_end_round(
            self,
            game_state: GameState,
            pid: Pid,
            action: EndRoundAction
    ) -> GameState:
        return game_state.factory().f_player(
            pid,
            lambda p: p.factory()
            .phase(Act.END_PHASE)
            .card_redraw_chances(0)
            .build()
        ).build()

    def step_action(
            self,
            game_state: GameState,
            pid: Pid,
            action: PlayerAction
    ) -> Optional[GameState]:
        if isinstance(action, CardsSelectAction):
            return self._handle_card_drawing(game_state, pid, action)
        elif isinstance(action, EndRoundAction):
            return self._handle_end_round(game_state, pid, action)
        else:
            raise ValueError(f"Unknown action {action} provided for game state:\n{game_state}")

    @classmethod
    def _choices_helper(cls, action_generator: ActionGenerator) -> GivenChoiceType:
        return (ActionType.SELECT_CARDS, ActionType.END_ROUND)

    @classmethod
    def _fill_helper(
        cls,
        action_generator: ActionGenerator,
        player_choice: DecidedChoiceType,
    ) -> ActionGenerator:
        game_state = action_generator.game_state
        pid = action_generator.pid

        if player_choice is ActionType.SELECT_CARDS:
            from ...action.action_generator_generator import CardsSelectionActGenGenerator
            return just(CardsSelectionActGenGenerator.action_generator(game_state, pid))
        elif player_choice is ActionType.END_ROUND:
            return ActionGenerator(game_state=game_state, pid=pid, action=EndRoundAction())
        else:  # pragma: no cover
            action_type_name = ActionType.__name__
            if isinstance(player_choice, ActionType):
                raise Exception(f"Unhandled player {action_type_name} {player_choice}")
            else:
                raise TypeError(f"Unexpected player choice {player_choice} where"
                                + f"where {action_type_name} is expected")

    def action_generator(self, game_state: GameState, pid: Pid) -> ActionGenerator | None:
        if pid is not self.waiting_for(game_state):
            return None
        return ActionGenerator(
            game_state=game_state,
            pid=pid,
            _choices_helper=self._choices_helper,
            _fill_helper=self._fill_helper,
        )
