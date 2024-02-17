"""
This file contains the base class "Effect" for all effects,
and implementation of all effects.

The classes are divided into 5 sections ordered. Within each section, they are
ordered alphabetically.

- base class, which is Effect
- type classes, used to identify what type of effect an effect is
- phase classes, effects that controls the flow of the game
- concrete classes, the implementation of effects that are actually in the game
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass, field, fields, replace
from enum import Enum
from itertools import chain
from typing import cast, FrozenSet, Iterable, Optional, Sequence, TYPE_CHECKING, Union

from typing_extensions import override

from ..helper.quality_of_life import dataclass_repr
from ..status import status as stt
from ..summon import summon as sm
from ..support import support as sp

from ..character.enums import CharacterSkill
from ..dice import ActualDice
from ..element import Element, Reaction, ReactionDetail
from ..event import *
from ..helper.quality_of_life import just, case_val, BIG_INT
from ..state.enums import Pid, Act
from ..status.enums import Preprocessables, Informables
from ..status.status_processing import StatusProcessing
from .enums import DynamicCharacterTarget, TriggeringSignal, Zone
from .structs import StaticTarget, DamageType

if TYPE_CHECKING:
    from ..card.card import Card
    from ..dice import ActualDice
    from ..encoding.encoding_plan import EncodingPlan
    from ..state.game_state import GameState
    from ..status.statuses import Statuses

__all__ = [
    # base
    "Effect",

    # type
    "CheckerEffect",
    "DirectEffect",
    "PhaseEffect",
    "PhaseStartEffect",
    "TriggerrbleEffect",

    # Triggerrable Effect
    "AllStatusTriggererEffect",
    "PlayerStatusTriggererEffect",
    "PersonalStatusTriggererEffect",
    "TriggerStatusEffect",
    "TriggerHiddenStatusEffect",
    "TriggerCombatStatusEffect",
    "TriggerSummonEffect",
    "TriggerSupportEffect",

    # Phase Effect
    "CardSelectPhaseStartEffect",
    "DeathSwapPhaseStartEffect",
    "DeathSwapPhaseEndEffect",
    "EndPhaseCheckoutEffect",
    "EndRoundEffect",
    "RollPhaseStartEffect",
    "SetBothPlayerPhaseEffect",
    "TurnEndEffect",

    # Checker Effect
    "AliveMarkCheckerEffect",  # mark dead characters defeated and revive the revivables
    "DefeatedMarkCheckerEffect",
    "SwapCharacterCheckerEffect",  # detect on swap
    "DeathCheckCheckerEffect",  # detect death swap
    "DefeatedCheckerEffect",

    # Direct Effect
    "ConsecutiveActionEffect",
    "SwapCharacterEffect",
    "BackwardSwapCharacterEffect",
    "ForwardSwapCharacterEffect",
    "ForwardSwapCharacterCheckEffect",
    "ApplyElementalAuraEffect",
    "SpecificDamageEffect",
    "ReferredDamageEffect",
    "EnergyRechargeEffect",
    "EnergyDrainEffect",
    "RecoverHPEffect",
    "ReviveRecoverHPEffect",
    "DrawRandomCardEffect",
    "DrawRandomCardOfTypeEffect",
    "PublicAddCardEffect",
    "PublicRemoveCardEffect",
    "PublicRemoveAllCardEffect",
    "PrivateAddCardEffect",
    "AddDiceEffect",
    "RemoveDiceEffect",
    "AddCharacterStatusEffect",
    "RemoveCharacterStatusEffect",
    "UpdateCharacterStatusEffect",
    "OverrideCharacterStatusEffect",
    "RelativeAddCharacterStatusEffect",
    "AddHiddenStatusEffect",
    "RemoveHiddenStatusEffect",
    "UpdateHiddenStatusEffect",
    "OverrideHiddenStatusEffect",
    "AddCombatStatusEffect",
    "RemoveCombatStatusEffect",
    "UpdateCombatStatusEffect",
    "OverrideCombatStatusEffect",
    "AddSummonEffect",
    "RemoveSummonEffect",
    "UpdateSummonEffect",
    "OverrideSummonEffect",
    "AllSummonIncreaseUsageEffect",
    "OneSummonDecreaseUsageEffect",
    "OneSummonIncreaseUsageEffect",
    "AddSupportEffect",
    "RemoveSupportEffect",
    "UpdateSupportEffect",
    "OverrideSupportEffect",
    "CastSkillEffect",
    "BroadcastPostSkillInfoEffect",
    "BroadcastPreSkillInfoEffect",
    "SetRedrawChancesEffect",
    "SetRerollChancesEffect",
]

############################## base ##############################


@dataclass(frozen=True, repr=False)
class Effect:
    def execute(self, game_state: GameState) -> GameState:  # pragma: no cover
        """
        :returns: the game state after effect execution.

        Called to execute the effect on the passed-in `game_state`.
        """
        raise Exception("Not Overriden or Implemented")

    def name(self) -> str:
        return self.__class__.__name__

    def dict_str(self) -> Union[dict, str]:
        return asdict(self)

    def encoding(self, encoding_plan: EncodingPlan) -> list[int]:
        """
        :returns: the encoding of this effect.
        """
        from ..card.card import Card
        from ..status.status import Status

        values = list(chain.from_iterable([
            [self.__getattribute__(fld.name)]
            for fld in fields(self)
        ]))
        ret_val = [encoding_plan.code_for(self)]
        for value in values:
            if isinstance(value, bool):
                ret_val.append(1 if value else 0)
            elif isinstance(value, int):
                ret_val.append(value)
            elif isinstance(value, Enum):
                assert isinstance(value.value, int)
                ret_val.append(value.value)
            elif value is None:
                ret_val.append(0)
            elif isinstance(value, StaticTarget):
                ret_val.extend(value.encoding(encoding_plan))
            elif isinstance(value, Status):
                ret_val.extend(value.encoding(encoding_plan))
            elif isinstance(value, ReactionDetail):
                ret_val.extend(value.encoding())
            elif isinstance(value, DamageType):
                ret_val.extend(value.encoding())
            elif isinstance(value, ActualDice):
                ret_val.extend(value.encoding(encoding_plan))
            elif issubclass(value, Card):
                ret_val.append(encoding_plan.code_for(value))
            elif issubclass(value, Status):
                ret_val.append(encoding_plan.code_for(value))
            else:
                raise Exception(f"Unexpected Type {type(value)} of {self.__class__.__name__}")
        fillings = encoding_plan.EFFECT_FIXED_LEN - len(ret_val)
        if fillings < 0:
            raise Exception("Too many values in effect", self)
        ret_val.extend([0] * fillings)
        return ret_val

    def __repr__(self) -> str:
        return dataclass_repr(self)


############################## type ##############################
@dataclass(frozen=True, repr=False)
class TriggerrbleEffect(ABC, Effect):
    @abstractmethod
    def new_effects(self, game_state: GameState) -> Sequence[Effect]:
        pass


@dataclass(frozen=True, repr=False)
class DirectEffect(Effect):
    pass


@dataclass(frozen=True, repr=False)
class CheckerEffect(Effect):
    pass


@dataclass(frozen=True, repr=False)
class PhaseEffect(Effect):
    pass


@dataclass(frozen=True, repr=False)
class PhaseStartEffect(Effect):
    """ The effects needs to be manually handled and removed by the Phase class """
    pass

############################## Triggerrable Effect ##############################


@dataclass(frozen=True, repr=False)
class AllStatusTriggererEffect(TriggerrbleEffect):
    """
    This effect triggers the characters' statuses with the provided signal in order.
    """
    pid: Pid
    signal: TriggeringSignal

    @override
    def new_effects(self, game_state: GameState) -> Sequence[Effect]:
        raise Exception("Not Reached")

    def execute(self, game_state: GameState) -> GameState:
        effects = StatusProcessing.trigger_all_statuses_effects(game_state, self.pid, self.signal)
        return game_state.factory().f_effect_stack(
            lambda es: es.push_many_fl(effects)
        ).build()


@dataclass(frozen=True, repr=False)
class PlayerStatusTriggererEffect(TriggerrbleEffect):
    pid: Pid
    self_signal: TriggeringSignal
    other_signal: TriggeringSignal

    @override
    def new_effects(self, game_state: GameState) -> Sequence[Effect]:
        self_effects = StatusProcessing.trigger_player_statuses_effects(
            game_state, self.pid, self.self_signal
        )
        oppo_effects = StatusProcessing.trigger_player_statuses_effects(
            game_state, self.pid.other(), self.other_signal
        )
        return self_effects + oppo_effects

    def execute(self, game_state: GameState) -> GameState:
        effects = self.new_effects(game_state)
        if not effects:
            return game_state
        return game_state.factory().f_effect_stack(
            lambda es: es.push_many_fl(effects)
        ).build()


@dataclass(frozen=True, repr=False)
class PersonalStatusTriggererEffect(TriggerrbleEffect):
    target: StaticTarget
    signal: TriggeringSignal

    @override
    def new_effects(self, game_state: GameState) -> Sequence[Effect]:
        return StatusProcessing.trigger_personal_statuses_effect(
            game_state,
            self.target,
            self.signal
        )

    def execute(self, game_state: GameState) -> GameState:
        effects = self.new_effects(game_state)
        if not effects:
            return game_state
        return game_state.factory().f_effect_stack(
            lambda es: es.push_many_fl(effects)
        ).build()


@dataclass(frozen=True, repr=False)
class TriggerStatusEffect(TriggerrbleEffect):
    target: StaticTarget
    status: type[stt.PersonalStatus]
    signal: TriggeringSignal

    @override
    def new_effects(self, game_state: GameState) -> Sequence[Effect]:
        character = game_state.get_target(self.target)
        from ..character.character import Character
        if not isinstance(character, Character):  # pragma: no cover
            return []
        effects: list[Effect] = []

        statuses: Statuses
        if issubclass(self.status, stt.CharacterHiddenStatus):
            statuses = character.hidden_statuses
        elif issubclass(self.status, stt.EquipmentStatus | stt.CharacterStatus):
            statuses = character.character_statuses
        else:  # pragma: no cover
            raise Exception("Unexpected Status Type to Trigger", self.status)
        status = statuses.find(self.status)
        if status is None:
            return []
        effects = status.react_to_signal(game_state, self.target, self.signal)
        return effects

    def execute(self, game_state: GameState) -> GameState:
        effects = self.new_effects(game_state)
        if not effects:
            return game_state
        return game_state.factory().f_effect_stack(
            lambda es: es.push_many_fl(effects)
        ).build()


@dataclass(frozen=True, repr=False)
class TriggerHiddenStatusEffect(TriggerrbleEffect):
    target_pid: Pid  # the player the status belongs to
    status: type[stt.PlayerHiddenStatus]
    signal: TriggeringSignal

    @override
    def new_effects(self, game_state: GameState) -> Sequence[Effect]:
        statuses = game_state.get_player(self.target_pid).hidden_statuses
        status = statuses.find(self.status)
        if status is None:
            return []
        return status.react_to_signal(
            game_state,
            StaticTarget(
                pid=self.target_pid,
                zone=Zone.HIDDEN_STATUSES,
                id=-1,
            ),
            self.signal,
        )

    def execute(self, game_state: GameState) -> GameState:
        effects = self.new_effects(game_state)
        if not effects:
            return game_state
        return game_state.factory().f_effect_stack(
            lambda es: es.push_many_fl(effects)
        ).build()


@dataclass(frozen=True, repr=False)
class TriggerCombatStatusEffect(TriggerrbleEffect):
    target_pid: Pid  # the player the status belongs to
    status: type[stt.CombatStatus]
    signal: TriggeringSignal

    @override
    def new_effects(self, game_state: GameState) -> Sequence[Effect]:
        statuses = game_state.get_player(self.target_pid).combat_statuses
        status = statuses.find(self.status)
        if status is None:
            return []
        return status.react_to_signal(
            game_state,
            StaticTarget(
                pid=self.target_pid,
                zone=Zone.COMBAT_STATUSES,
                id=-1,
            ),
            self.signal,
        )

    def execute(self, game_state: GameState) -> GameState:
        effects = self.new_effects(game_state)
        if not effects:
            return game_state
        return game_state.factory().f_effect_stack(
            lambda es: es.push_many_fl(effects)
        ).build()


@dataclass(frozen=True, repr=False)
class TriggerSummonEffect(TriggerrbleEffect):
    target_pid: Pid
    summon: type[sm.Summon]
    signal: TriggeringSignal

    @override
    def new_effects(self, game_state: GameState) -> Sequence[Effect]:
        summons = game_state.get_player(self.target_pid).summons
        summon = summons.find(self.summon)
        if summon is None:
            return []
        return summon.react_to_signal(
            game_state,
            StaticTarget(
                pid=self.target_pid,
                zone=Zone.SUMMONS,
                id=-1,
            ),
            self.signal,
        )

    def execute(self, game_state: GameState) -> GameState:
        effects = self.new_effects(game_state)
        if not effects:
            return game_state
        return game_state.factory().f_effect_stack(
            lambda es: es.push_many_fl(effects)
        ).build()


@dataclass(frozen=True, repr=False)
class TriggerSupportEffect(TriggerrbleEffect):
    target_pid: Pid
    support_type: type[sp.Support]
    sid: int
    signal: TriggeringSignal

    @override
    def new_effects(self, game_state: GameState) -> Sequence[Effect]:
        supports = game_state.get_player(self.target_pid).supports
        support = supports.find(self.support_type, self.sid)
        if support is None:
            return []
        return support.react_to_signal(
            game_state,
            StaticTarget(
                pid=self.target_pid,
                zone=Zone.SUPPORTS,
                id=self.sid,
            ),
            self.signal,
        )

    def execute(self, game_state: GameState) -> GameState:
        effects = self.new_effects(game_state)
        if not effects:
            return game_state
        return game_state.factory().f_effect_stack(
            lambda es: es.push_many_fl(effects)
        ).build()

############################## Phase Effect ##############################


@dataclass(frozen=True, repr=False)
class CardSelectPhaseStartEffect(PhaseStartEffect):
    pass


@dataclass(frozen=True, repr=False)
class DeathSwapPhaseStartEffect(PhaseStartEffect):
    pass


@dataclass(frozen=True, repr=False)
class DeathSwapPhaseEndEffect(PhaseEffect):
    my_pid: Pid
    my_last_phase: Act
    other_last_phase: Act

    def execute(self, game_state: GameState) -> GameState:
        player = game_state.get_player(self.my_pid)
        other_player = game_state.get_other_player(self.my_pid)
        player = player.factory().phase(self.my_last_phase).build()
        other_player = other_player.factory().phase(self.other_last_phase).build()
        return game_state.factory().player(
            self.my_pid,
            player
        ).other_player(
            self.my_pid,
            other_player
        ).build()


@dataclass(frozen=True, repr=False)
class EndPhaseCheckoutEffect(PhaseEffect):
    """
    This is responsible for triggering character statuses/summons/supports by the
    end of the round.
    """

    def execute(self, game_state: GameState) -> GameState:
        active_id = game_state.active_player_id
        # active_player = game_state.get_player(active_id)
        effects = [
            AllStatusTriggererEffect(
                active_id,
                TriggeringSignal.END_ROUND_CHECK_OUT
            ),
            # TODO: add active_player's team status, summons status... here
        ]
        return game_state.factory().f_effect_stack(
            lambda es: es.push_many_fl(effects)
        ).build()


@dataclass(frozen=True, repr=False)
class EndRoundEffect(PhaseEffect):
    """
    This is responsible for triggering other clean ups (e.g. remove satiated)
    """

    def execute(self, game_state: GameState) -> GameState:
        active_id = game_state.active_player_id
        active_player = game_state.get_player(active_id)
        effects = [
            AllStatusTriggererEffect(
                active_id,
                TriggeringSignal.ROUND_END
            ),
            # TODO: add active_player's team status, summons status... here
        ]
        return game_state.factory().f_effect_stack(
            lambda es: es.push_many_fl(effects)
        ).build()


@dataclass(frozen=True, repr=False)
class RollPhaseStartEffect(PhaseStartEffect):
    pass


@dataclass(frozen=True, repr=False)
class SetBothPlayerPhaseEffect(PhaseEffect):
    phase: Act

    def execute(self, game_state: GameState) -> GameState:
        return game_state.factory().f_player1(
            lambda p: p.factory().phase(self.phase).build()
        ).f_player2(
            lambda p: p.factory().phase(self.phase).build()
        ).build()


@dataclass(frozen=True, repr=False)
class TurnEndEffect(PhaseEffect):
    def execute(self, game_state: GameState) -> GameState:
        active_player_id = game_state.active_player_id
        player = game_state.get_player(active_player_id)
        other_player = game_state.get_other_player(active_player_id)
        assert player.phase is Act.ACTION_PHASE
        if player.get_consec_action():
            game_state = game_state.factory().f_player(
                active_player_id,
                lambda p: p.factory().consec_action(False).build()
            ).build()
        elif other_player.phase is not Act.END_PHASE:
            game_state = game_state.factory().active_player_id(
                active_player_id.other()
            ).player(
                active_player_id,
                player.factory().phase(Act.PASSIVE_WAIT_PHASE).build()
            ).other_player(
                active_player_id,
                other_player.factory().phase(Act.ACTION_PHASE).build()
            ).build()
        active_player_id = game_state.active_player_id
        return game_state.factory().f_effect_stack(
            lambda es: es.push_one(
                AllStatusTriggererEffect(
                    active_player_id,
                    TriggeringSignal.PRE_ACTION,
                )
            )
        ).build()


############################## Checker Effect ##############################


@dataclass(frozen=True, repr=False)
class AliveMarkCheckerEffect(CheckerEffect):
    """ Revive all revivable characters.  """

    def execute(self, game_state: GameState) -> GameState:
        active_pid = game_state.active_player_id
        revival_effects: list[Effect] = []
        for pid in (active_pid, active_pid.other()):
            for char in game_state.get_player(pid).characters.get_character_in_activity_order():
                if not char.is_alive() or char.hp > 0:
                    continue
                char_source = StaticTarget(pid, Zone.CHARACTERS, char.id)
                revival_status = next((
                    status
                    for status in char.get_all_statuses_ordered_flattened()
                    if (
                        isinstance(status, stt.RevivalStatus)
                        and status.revivable(game_state, char_source)
                    )
                ), None)
                if revival_status is not None:
                    assert isinstance(revival_status, stt.PersonalStatus)
                    revival_effects.append(
                        TriggerStatusEffect(
                            target=char_source,
                            status=revival_status.__class__,
                            signal=TriggeringSignal.TRIGGER_REVIVAL,
                        )
                    )
                else:
                    game_state = game_state.factory().f_player(
                        pid,
                        lambda p: p.factory().f_characters(
                            lambda cs: cs.factory().f_character(
                                char.id,
                                lambda c: c.factory().hp(-BIG_INT).alive(False).build()
                            ).build()
                        ).build()
                    ).build()
        if revival_effects:
            game_state = game_state.factory().f_effect_stack(
                lambda es: es.push_many_fl(revival_effects)
            ).build()
        return game_state

@dataclass(frozen=True, repr=False)
class DefeatedMarkCheckerEffect(CheckerEffect):
    """ Mark all defeated characters as defeated.  """

    def execute(self, game_state: GameState) -> GameState:
        active_pid = game_state.active_player_id
        for pid in (active_pid, active_pid.other()):
            for char in game_state.get_player(pid).characters.get_character_in_activity_order():
                if char.is_alive() or char.hp >= 0:
                    continue
                char_source = StaticTarget(pid, Zone.CHARACTERS, char.id)
                on_death_effects = StatusProcessing.trigger_personal_statuses_effect(
                    game_state, char_source, TriggeringSignal.DEATH_DECLARATION
                )
                for effect in on_death_effects:
                    game_state = effect.execute(game_state)
                from ..status.statuses import Statuses
                equipment_statuses = [
                    type(status)
                    for status in char.character_statuses
                    if isinstance(status, Statuses._EQUIPMENT_CATEGORIES)
                ]
                game_state = StatusProcessing.inform_all_statuses(
                    game_state,
                    pid,
                    Informables.CHARACTER_DEATH,
                    CharacterDeathIEvent(target=char_source),
                ).factory().f_player(
                    pid,
                    lambda p: p.factory().f_characters(
                        lambda cs: cs.factory().f_character(
                            char.id,
                            lambda c: type(c).from_default(c.id).factory()
                            .hp(0).alive(False).build()
                        ).build()
                    ).build()
                ).build()
                for equipment_status in equipment_statuses:
                    game_state = StatusProcessing.inform_all_statuses(
                        game_state,
                        pid,
                        Informables.EQUIPMENT_DISCARDING,
                        EquipmentDiscardIEvent(
                            target=char_source,
                            status=equipment_status,
                        ),
                    )
        return game_state


@dataclass(frozen=True, repr=False)
class SwapCharacterCheckerEffect(CheckerEffect):
    my_active: StaticTarget
    oppo_active: StaticTarget

    def execute(self, game_state: GameState) -> GameState:
        my_ac_id = game_state.get_player(self.my_active.pid).just_get_active_character().id
        oppo_ac_id = game_state.get_player(
            self.oppo_active.pid).just_get_active_character().id
        my_pid = self.my_active.pid
        effects: list[Effect] = []
        if my_ac_id != self.my_active.id:  # pragma: no cover
            effects += [
                PlayerStatusTriggererEffect(
                    pid=my_pid,
                    self_signal=TriggeringSignal.SELF_SWAP,
                    other_signal=TriggeringSignal.OPPO_SWAP,
                ),
            ]
        if oppo_ac_id != self.oppo_active.id:
            effects += [
                PlayerStatusTriggererEffect(
                    pid=my_pid,
                    self_signal=TriggeringSignal.OPPO_SWAP,
                    other_signal=TriggeringSignal.SELF_SWAP,
                ),
            ]
        if not effects:
            return game_state
        return game_state.factory().f_effect_stack(
            lambda es: es.push_many_fl(effects)
        ).build()


@dataclass(frozen=True, repr=False)
class DeathCheckCheckerEffect(CheckerEffect):
    """
    Checks if Death Swap Phase is required to be inserted or game should end.
    If death swap is required, then the Death Swap Phase is inserted to be executed.
    """
    def execute(self, game_state: GameState) -> GameState:
        p1_character = game_state.player1.characters.get_active_character()
        p2_character = game_state.player2.characters.get_active_character()
        assert p1_character is not None and p2_character is not None
        pid: Pid
        if p1_character.is_defeated():
            pid = Pid.P1
        elif p2_character.is_defeated():
            pid = Pid.P2
        else:  # if no one defeated, continue
            return game_state
        death_swap_player = game_state.get_player(pid)
        waiting_player = game_state.get_other_player(pid)
        # TODO: check if game ends
        if death_swap_player.defeated():
            raise Exception("Not Reached! Should be caught by DefeatedCheckerEffect")
        effects: list[Effect] = []
        # TODO: trigger other death based effects
        effects.append(DeathSwapPhaseStartEffect())
        effects.append(DeathSwapPhaseEndEffect(
            pid,
            death_swap_player.phase,
            waiting_player.phase,
        ))
        return game_state.factory().effect_stack(
            game_state.effect_stack.push_many_fl(tuple(effects))
        ).player(
            pid,
            game_state.get_player(pid).factory().phase(
                Act.ACTION_PHASE
            ).build()
        ).other_player(
            pid,
            game_state.get_other_player(pid).factory().phase(
                Act.PASSIVE_WAIT_PHASE
            ).build()
        ).build()


@dataclass(frozen=True, repr=False)
class DefeatedCheckerEffect(CheckerEffect):
    """
    Checks if game should end immediately due to the defeat of a player.

    This effect is supposed to be used after revive check, meaning if all characters
    have 0 hp, then the game should end.
    """
    def execute(self, game_state: GameState) -> GameState:
        if game_state.player1.defeated() \
                or game_state.player2.defeated():
            return game_state.factory().phase(game_state.mode.game_end_phase()).build()
        return game_state

############################## Direct Effect ##############################


@dataclass(frozen=True, repr=False)
class ConsecutiveActionEffect(DirectEffect):
    target_pid: Pid

    def execute(self, game_state: GameState) -> GameState:
        return game_state.factory().f_player(
            self.target_pid,
            lambda p: p.factory().consec_action(True).build()
        ).build()


@dataclass(frozen=True, repr=False)
class SwapCharacterEffect(DirectEffect):
    target: StaticTarget

    def execute(self, game_state: GameState) -> GameState:
        assert self.target.zone == Zone.CHARACTERS
        pid = self.target.pid
        player = game_state.get_player(pid)
        active_character = player.get_active_character()
        if active_character is not None and active_character.id == self.target.id:
            return game_state

        effects: list[Effect] = [
            PlayerStatusTriggererEffect(
                pid=pid,
                self_signal=TriggeringSignal.SELF_SWAP,
                other_signal=TriggeringSignal.OPPO_SWAP,
            ),
        ]
        return game_state.factory().f_player(
            pid,
            lambda p: p.factory().f_characters(
                lambda cs: cs.factory().active_character_id(cast(int, self.target.id)).build()
            ).build()
        ).f_effect_stack(
            lambda es: es.push_many_fl(effects)
        ).build()


@dataclass(frozen=True, repr=False)
class PrivateSwapCharacterEffect(SwapCharacterEffect):
    ...


@dataclass(frozen=True, repr=False)
class BackwardSwapCharacterEffect(DirectEffect):
    """
    Swap the to the next active character.

    This effect doesn't auto-add swap checker.
    """
    target_player: Pid

    def execute(self, game_state: GameState) -> GameState:
        characters = game_state.get_player(self.target_player).characters
        # oredered chars without active character
        ordered_chars = characters.get_character_in_activity_order()[:0:-1]
        from ..character.character import Character
        next_char: Optional[Character] = next(
            (
                char
                for char in ordered_chars
                if char.is_alive()
            ),
            None
        )
        if next_char is None:
            return game_state
        return game_state.factory().f_player(
            self.target_player,
            lambda p: p.factory().f_characters(
                lambda cs: cs.factory().active_character_id(
                    next_char.id  # type: ignore
                ).build()
            ).build()
        ).build()


@dataclass(frozen=True, repr=False)
class ForwardSwapCharacterEffect(DirectEffect):
    """
    Swap the to the next active character.

    This effect doesn't auto-add swap checker.
    """
    target_player: Pid

    def execute(self, game_state: GameState) -> GameState:
        characters = game_state.get_player(self.target_player).characters
        # oredered chars without active character
        ordered_chars = characters.get_character_in_activity_order()[1:]
        from ..character.character import Character
        next_char: Optional[Character] = next(
            (
                char
                for char in ordered_chars
                if char.is_alive()
            ),
            None
        )
        if next_char is None:
            return game_state
        return game_state.factory().f_player(
            self.target_player,
            lambda p: p.factory().f_characters(
                lambda cs: cs.factory().active_character_id(
                    next_char.id  # type: ignore
                ).build()
            ).build()
        ).build()


@dataclass(frozen=True, repr=False)
class ForwardSwapCharacterCheckEffect(DirectEffect):
    """
    Swap the to the next active character.

    This effect auto-adds swap checker.
    """
    target_player: Pid

    def execute(self, game_state: GameState) -> GameState:
        characters = game_state.get_player(self.target_player).characters
        ordered_chars = characters.get_character_in_activity_order()
        from ..character.character import Character
        next_char: Optional[Character] = next(
            (
                char
                for char in ordered_chars[1:]
                if char.is_alive()
            ),
            None
        )
        if next_char is None:
            return game_state
        return game_state.factory().f_player(
            self.target_player,
            lambda p: p.factory().f_characters(
                lambda cs: cs.factory().active_character_id(
                    next_char.id  # type: ignore
                ).build()
            ).build()
        ).f_effect_stack(
            lambda es: es.push_one(
                PlayerStatusTriggererEffect(
                    pid=self.target_player,
                    self_signal=TriggeringSignal.SELF_SWAP,
                    other_signal=TriggeringSignal.OPPO_SWAP,
                ),
            )
        ).build()


_DAMAGE_ELEMENTS: FrozenSet[Element] = frozenset({
    Element.PYRO,
    Element.HYDRO,
    Element.ANEMO,
    Element.ELECTRO,
    Element.DENDRO,
    Element.CRYO,
    Element.GEO,
    Element.PHYSICAL,
    Element.PIERCING,
})


@dataclass(frozen=True, kw_only=True, repr=False)
class ApplyElementalAuraEffect(DirectEffect):
    source: StaticTarget
    target: StaticTarget
    element: Element
    source_type: DamageType

    def execute(self, game_state: GameState) -> GameState:
        target_char = game_state.get_character_target(self.target)
        assert target_char is not None
        all_aura = target_char.elemental_aura
        if target_char.is_defeated() or (all_aura.aurable(self.element) and self.element in all_aura):
            return game_state
        reaction_detail = all_aura.consult_reaction(self.element)
        new_aura = all_aura
        effects: list[Effect] = []
        if reaction_detail is None:
            if new_aura.aurable(self.element):
                new_aura = new_aura.add(self.element)
        else:
            new_aura = new_aura.remove(reaction_detail.first_elem)
            if reaction_detail.reaction_type is Reaction.BLOOM:
                effects.append(
                    AddCombatStatusEffect(
                        target_pid=self.target.pid.other(),
                        status=stt.DendroCoreStatus,
                    )
                )
            elif reaction_detail.reaction_type is Reaction.BURNING:
                effects.append(
                    AddSummonEffect(
                        target_pid=self.target.pid.other(),
                        summon=sm.BurningFlameSummon,
                    )
                )
            elif reaction_detail.reaction_type is Reaction.CRYSTALLIZE:
                effects.append(
                    AddCombatStatusEffect(
                        target_pid=self.target.pid.other(),
                        status=stt.CrystallizeStatus,
                    )
                )
            elif reaction_detail.reaction_type is Reaction.FROZEN:
                effects.append(
                    AddCharacterStatusEffect(
                        target=self.target,
                        status=stt.FrozenStatus,
                    )
                )
            elif reaction_detail.reaction_type is Reaction.OVERLOADED:
                oppo_active_id = game_state \
                    .get_player(self.target.pid) \
                    .just_get_active_character() \
                    .id
                assert self.target.zone is Zone.CHARACTERS
                if self.target.id is oppo_active_id:
                    effects.append(
                        ForwardSwapCharacterEffect(self.target.pid)
                    )
            elif reaction_detail.reaction_type is Reaction.QUICKEN:
                effects.append(
                    AddCombatStatusEffect(
                        target_pid=self.target.pid.other(),
                        status=stt.CatalyzingFieldStatus,
                    )
                )
            else:
                assert reaction_detail.reaction_type in {
                    Reaction.VAPORIZE,
                    Reaction.MELT,
                    Reaction.SUPERCONDUCT,
                    Reaction.ELECTRO_CHARGED,
                    Reaction.SWIRL,
                }, f"{reaction_detail.reaction_type} is not covered"

        game_state = game_state.factory().f_player(
            self.target.pid,
            lambda p: p.factory().f_characters(
                lambda cs: cs.factory().f_character(
                    cast(int, self.target.id),
                    lambda c: c.factory().elemental_aura(new_aura).build()
                ).build()
            ).build()
        ).f_effect_stack(
            lambda efs: efs.push_many_fl(effects)
        ).build()

        if reaction_detail is not None:
            game_state = StatusProcessing.inform_all_statuses(
                game_state,
                self.source.pid,
                Informables.REACTION_TRIGGERED,
                ReactionIEvent(
                    source=self.source,
                    target=self.target,
                    source_type=self.source_type,
                    reaction=reaction_detail.reaction_type,
                ),
            )

        return game_state


@dataclass(frozen=True, kw_only=True, repr=False)
class SpecificDamageEffect(DirectEffect):
    source: StaticTarget
    target: StaticTarget
    element: Element
    damage: int
    damage_type: DamageType
    reaction: Optional[ReactionDetail] = None

    @staticmethod
    def _damage_preprocess(
            game_state: GameState, damage: SpecificDamageEffect, pp_type: Preprocessables
    ) -> tuple[GameState, SpecificDamageEffect]:
        source_id = damage.source.pid
        game_state, item = StatusProcessing.preprocess_by_all_statuses(
            game_state,
            source_id,
            pp_type,
            DmgPEvent(dmg=damage),
        )
        assert isinstance(item, DmgPEvent), item
        damage = item.dmg
        return game_state, damage

    @classmethod
    def _element_confirmation(
            cls, game_state: GameState, damage: SpecificDamageEffect
    ) -> tuple[GameState, SpecificDamageEffect]:
        """ This is the pass to check final damage element """
        return cls._damage_preprocess(game_state, damage, Preprocessables.DMG_ELEMENT)

    @classmethod
    def _reaction_confirmation(
            cls, game_state: GameState, damage: SpecificDamageEffect
    ) -> tuple[GameState, SpecificDamageEffect, Optional[ReactionDetail]]:
        """ This is the pass to check final damage reaction type """
        target_char = game_state.get_character_target(damage.target)
        assert target_char is not None

        # try to identify the reaction
        second_elem = damage.element
        all_aura = target_char.elemental_aura
        reaction_detail = all_aura.consult_reaction(second_elem)

        # generate & update new aura
        new_aura = all_aura
        if reaction_detail is not None:
            new_aura = new_aura.remove(reaction_detail.first_elem)
            damage = replace(damage, reaction=reaction_detail)
        elif new_aura.aurable(second_elem):
            new_aura = new_aura.add(second_elem)

        if new_aura != all_aura:
            game_state = game_state.factory().f_player(
                just(game_state.belongs_to(target_char)),
                lambda p: p.factory().f_characters(
                    lambda cs: cs.factory().character(
                        target_char.factory().elemental_aura(new_aura).build()  # type: ignore
                    ).build()
                ).build()
            ).build()

        game_state, damage = cls._damage_preprocess(
            game_state, damage, Preprocessables.DMG_REACTION
        )
        return game_state, damage, reaction_detail

    @classmethod
    def _damage_confirmation(
            cls, game_state: GameState, damage: SpecificDamageEffect
    ) -> tuple[GameState, SpecificDamageEffect]:
        """ This is the pass to check final damage amount """
        game_state, damage = cls._damage_preprocess(
            game_state, damage, Preprocessables.DMG_AMOUNT_PLUS)
        game_state, damage = cls._damage_preprocess(
            game_state, damage, Preprocessables.DMG_AMOUNT_MUL)
        return cls._damage_preprocess(game_state, damage, Preprocessables.DMG_AMOUNT_MINUS)

    def execute(self, game_state: GameState) -> GameState:
        # Check damage target
        target = game_state.get_character_target(self.target)
        if target is None or target.is_defeated():  # pragma: no cover
            return game_state

        # Preprocessing
        game_state, elemented_damage = self._element_confirmation(game_state, self)
        game_state, reactioned_damage, reaction = self._reaction_confirmation(
            game_state, elemented_damage
        )
        if reaction is not None:
            reactioned_damage = replace(
                reactioned_damage,
                damage=reactioned_damage.damage + reaction.reaction_type.damage_boost(),
            )
        game_state, actual_damage = self._damage_confirmation(game_state, reactioned_damage)
        # Update all statuses with this damage
        game_state = StatusProcessing.inform_all_statuses(
            game_state,
            actual_damage.source.pid,
            Informables.DMG_DEALT,
            DmgIEvent(dmg=actual_damage),
        )

        # Check damage target
        target = game_state.get_character_target(actual_damage.target)
        assert target is not None

        # Damage Calculation
        hp = target.hp
        hp = max(0, hp - actual_damage.damage)

        target_pid = self.target.pid
        effects: list[Effect] = []

        if hp != target.hp:
            target = target.factory().hp(hp).build()

        if reaction is None:
            pass

        elif reaction.reaction_type is Reaction.VAPORIZE \
                or reaction.reaction_type is Reaction.MELT:
            pass

        elif reaction.reaction_type is Reaction.OVERLOADED:
            oppo_active_id = game_state \
                .get_player(actual_damage.target.pid) \
                .just_get_active_character() \
                .id
            assert actual_damage.target.zone is Zone.CHARACTERS
            if actual_damage.target.id is oppo_active_id:
                effects.append(
                    ForwardSwapCharacterEffect(target_pid)
                )

        elif reaction.reaction_type is Reaction.SUPERCONDUCT \
                or reaction.reaction_type is Reaction.ELECTRO_CHARGED:
            effects.append(
                ReferredDamageEffect(
                    source=self.source,
                    target_ref=actual_damage.target,
                    target=DynamicCharacterTarget.OPPO_OFF_FIELD,
                    element=Element.PIERCING,
                    damage=1,
                    damage_type=replace(self.damage_type, reaction=True),
                )
            )

        elif reaction.reaction_type is Reaction.SWIRL:
            effects.append(
                ReferredDamageEffect(
                    source=self.source,
                    target_ref=actual_damage.target,
                    target=DynamicCharacterTarget.OPPO_OFF_FIELD,
                    element=reaction.first_elem,
                    damage=1,
                    damage_type=replace(self.damage_type, reaction=True),
                )
            )

        elif reaction.reaction_type is Reaction.FROZEN:
            effects.append(
                AddCharacterStatusEffect(
                    target=actual_damage.target,
                    status=stt.FrozenStatus,
                )
            )

        elif reaction.reaction_type is Reaction.QUICKEN:
            effects.append(
                AddCombatStatusEffect(
                    target_pid=actual_damage.target.pid.other(),
                    status=stt.CatalyzingFieldStatus,
                )
            )

        elif reaction.reaction_type is Reaction.BLOOM:
            effects.append(
                AddCombatStatusEffect(
                    target_pid=actual_damage.target.pid.other(),
                    status=stt.DendroCoreStatus,
                )
            )

        elif reaction.reaction_type is Reaction.CRYSTALLIZE:
            effects.append(
                AddCombatStatusEffect(
                    target_pid=actual_damage.target.pid.other(),
                    status=stt.CrystallizeStatus,
                )
            )

        elif reaction.reaction_type is Reaction.BURNING:
            effects.append(
                AddSummonEffect(
                    target_pid=actual_damage.target.pid.other(),
                    summon=sm.BurningFlameSummon,
                )
            )

        else:  # pragma: no cover
            # this exception shouldn't be reached by now, but leave it here just to be safe
            raise Exception(f"Reaction {reaction.reaction_type} not handled")

        # damaged game state
        game_state = game_state.factory().f_player(
            target_pid,
            lambda p: p.factory().f_characters(
                lambda cs: cs.factory().character(target).build()  # type: ignore
            ).build()
        ).f_effect_stack(
            lambda es: es.push_many_fl(effects)
        ).build()

        if reaction is not None:
            game_state = StatusProcessing.inform_all_statuses(
                game_state,
                self.source.pid,
                Informables.REACTION_TRIGGERED,
                ReactionIEvent(
                    source=self.source,
                    target=self.target,
                    source_type=self.damage_type,
                    reaction=reaction.reaction_type,
                ),
            )

        return game_state


@dataclass(frozen=True, repr=False)
class ReferredDamageEffect(DirectEffect):
    source: StaticTarget
    target: DynamicCharacterTarget
    element: Element
    damage: int
    damage_type: DamageType
    # this field is used as a reference if the target is OFF_FIELD
    # e.g. super-conduct caused by swirl
    target_ref: Optional[StaticTarget] = field(kw_only=True, default=None)

    def legal(self) -> bool:
        return self.element in _DAMAGE_ELEMENTS

    def execute(self, game_state: GameState) -> GameState:
        assert self.legal()
        from ..character.character import Character
        targets: list[Character] = self.target.get_target_chars(
            game_state,
            self.source.pid,
            ref_char_id=cast(int, self.target_ref.id) if self.target_ref is not None else None,
        )
        effects: list[Effect] = []
        char: Optional[Character]

        for char in targets:
            if char is None:  # pragma: no cover
                continue
            pid = game_state.belongs_to(char)
            if pid is None:  # pragma: no cover
                continue
            effects.append(
                SpecificDamageEffect(
                    source=self.source,
                    target=StaticTarget(
                        pid=pid,
                        zone=Zone.CHARACTERS,
                        id=char.id,
                    ),
                    element=self.element,
                    damage=self.damage,
                    damage_type=self.damage_type,
                    reaction=None,
                )
            )

        return game_state.factory().f_effect_stack(
            lambda es: es.push_many_fl(effects)
        ).build()


@dataclass(frozen=True, repr=False)
class EnergyRechargeEffect(DirectEffect):
    target: StaticTarget
    recharge: int

    def execute(self, game_state: GameState) -> GameState:
        character = game_state.get_target(self.target)
        from ..character.character import Character
        if not isinstance(character, Character):  # pragma: no cover
            return game_state
        energy = min(character.energy + self.recharge, character.max_energy)
        if energy == character.energy:
            return game_state
        character = character.factory().energy(energy).build()
        player = game_state.get_player(self.target.pid)
        characters = player.characters.factory().character(character).build()
        player = player.factory().characters(characters).build()
        return game_state.factory().player(
            self.target.pid,
            player
        ).build()


@dataclass(frozen=True, repr=False)
class EnergyDrainEffect(DirectEffect):
    target: StaticTarget
    drain: int

    def execute(self, game_state: GameState) -> GameState:
        character = game_state.get_target(self.target)
        from ..character.character import Character
        if not isinstance(character, Character):  # pragma: no cover
            return game_state
        energy = max(character.energy - self.drain, 0)
        if energy == character.energy:
            return game_state
        character = character.factory().energy(energy).build()
        player = game_state.get_player(self.target.pid)
        characters = player.characters.factory().character(character).build()
        player = player.factory().characters(characters).build()
        return game_state.factory().player(
            self.target.pid,
            player
        ).build()


@dataclass(frozen=True, repr=False)
class RecoverHPEffect(DirectEffect):
    target: StaticTarget
    recovery: int

    def execute(self, game_state: GameState) -> GameState:
        character = game_state.get_target(self.target)
        from ..character.character import Character
        if not isinstance(character, Character):  # pragma: no cover
            return game_state
        if character.is_defeated():
            return game_state
        hp = min(character.hp + self.recovery, character.max_hp)
        if hp == character.hp:
            return game_state
        return game_state.factory().f_player(
            self.target.pid,
            lambda p: p.factory().f_characters(
                lambda cs: cs.factory().f_character(
                    character.id,  # type: ignore
                    lambda c: c.factory().hp(hp).build()
                ).build()
            ).build()
        ).build()


@dataclass(frozen=True, repr=False)
class ReviveRecoverHPEffect(RecoverHPEffect):
    @override
    def execute(self, game_state: GameState) -> GameState:
        character = game_state.get_target(self.target)
        from ..character.character import Character
        if not isinstance(character, Character):  # pragma: no cover
            return game_state
        assert character.hp == 0, game_state
        hp = min(self.recovery, character.max_hp)
        if hp == 0:
            return game_state
        return game_state.factory().f_player(
            self.target.pid,
            lambda p: p.factory().f_characters(
                lambda cs: cs.factory().f_character(
                    character.id,  # type: ignore
                    lambda c: c.factory().alive(True).hp(hp).build()
                ).build()
            ).build()
        ).f_effect_stack(
            lambda es: es.push_one(PersonalStatusTriggererEffect(
                target=self.target,
                signal=TriggeringSignal.REVIVAL_GAME_START,
            ))
        ).build()


@dataclass(frozen=True, repr=False)
class DrawRandomCardEffect(DirectEffect):
    pid: Pid
    num: int

    def execute(self, game_state: GameState) -> GameState:
        deck_cards = game_state.get_player(self.pid).deck_cards
        left_cards, chosen_cards = deck_cards.pick_random(self.num)
        if chosen_cards.num_cards() == 0:
            return game_state
        return game_state.factory().f_player(
            self.pid,
            lambda p: p.factory().deck_cards(
                left_cards
            ).f_hand_cards(
                lambda cards: cards.extend(
                    chosen_cards,
                    limit=game_state.mode.hand_card_limit()
                )
            ).build()
        ).build()


@dataclass(frozen=True, repr=False)
class DrawRandomCardOfTypeEffect(DirectEffect):
    pid: Pid
    num: int
    card_type: type[Card]

    def execute(self, game_state: GameState) -> GameState:
        deck_cards = game_state.get_player(self.pid).deck_cards
        left_cards, chosen_cards = deck_cards.pick_random_of_type(self.num, self.card_type)
        if chosen_cards.num_cards() == 0:
            return game_state
        return game_state.factory().f_player(
            self.pid,
            lambda p: p.factory().deck_cards(
                left_cards
            ).f_hand_cards(
                lambda cards: cards.extend(
                    chosen_cards,
                    limit=game_state.mode.hand_card_limit()
                )
            ).build()
        ).build()


@dataclass(frozen=True, repr=False)
class PublicAddCardEffect(DirectEffect):
    pid: Pid
    card: type[Card]

    def execute(self, game_state: GameState) -> GameState:
        hand_card_limit = game_state.mode.hand_card_limit()
        if game_state.get_player(self.pid).hand_cards.num_cards() >= hand_card_limit:
            return game_state
        return game_state.factory().f_player(
            self.pid,
            lambda p: p.factory().f_hand_cards(
                lambda cs: cs.add(self.card)
            ).f_publicly_gained_cards(
                lambda cs: cs.add(self.card)
            ).build()
        ).build()


@dataclass(frozen=True, repr=False)
class PublicRemoveCardEffect(DirectEffect):
    pid: Pid
    card: type[Card]

    def execute(self, game_state: GameState) -> GameState:
        pid = self.pid
        card = self.card
        hand_cards = game_state.get_player(pid).hand_cards
        if not hand_cards.contains(card):  # pragma: no cover
            return game_state
        return game_state.factory().f_player(
            pid,
            lambda p: p.factory().f_hand_cards(
                lambda cs: cs.remove(card)
            ).f_publicly_used_cards(
                lambda cs: cs.add(card)
            ).build()
        ).build()


@dataclass(frozen=True, repr=False)
class PublicRemoveAllCardEffect(DirectEffect):
    pid: Pid
    card: type[Card]

    def execute(self, game_state: GameState) -> GameState:
        pid = self.pid
        card = self.card
        hand_cards = game_state.get_player(pid).hand_cards
        if not hand_cards.contains(card) or hand_cards[card] <= 0:  # pragma: no cover
            return game_state
        return game_state.factory().f_player(
            pid,
            lambda p: p.factory().f_hand_cards(
                lambda cs: cs.remove_all(card)
            ).f_publicly_used_cards(
                lambda cs: cs + {card: hand_cards[card]}
            ).build()
        ).build()


@dataclass(frozen=True, repr=False)
class PrivateAddCardEffect(DirectEffect):
    """
    Add a card to the hand cards of the player such that the opponent cannot see
    which exact card is added.
    """
    pid: Pid
    card: type[Card]

    def execute(self, game_state: GameState) -> GameState:
        hand_card_limit = game_state.mode.hand_card_limit()
        if game_state.get_player(self.pid).hand_cards.num_cards() >= hand_card_limit:
            return game_state
        return game_state.factory().f_player(
            self.pid,
            lambda p: p.factory().f_hand_cards(
                lambda cs: cs.add(self.card)
            ).build()
        ).build()


@dataclass(frozen=True, repr=False)
class AddDiceEffect(DirectEffect):
    pid: Pid
    element: Element
    num: int

    def execute(self, game_state: GameState) -> GameState:
        pid = self.pid
        curr_dice = game_state.get_player(pid).dice
        addable_num = min(self.num, game_state.mode.dice_limit() - curr_dice.num_dice())
        if addable_num <= 0:
            return game_state
        dice = ActualDice({self.element: addable_num})
        new_dice = curr_dice + dice
        return game_state.factory().f_player(
            pid,
            lambda p: p.factory().dice(new_dice).build()
        ).build()


@dataclass(frozen=True, repr=False)
class RemoveDiceEffect(DirectEffect):
    pid: Pid
    dice: ActualDice

    def execute(self, game_state: GameState) -> GameState:
        pid = self.pid
        dice = self.dice
        new_dice = game_state.get_player(pid).dice - dice
        if not new_dice.is_legal():
            raise Exception(f"Not enough dice for this effect "
                            + f"{game_state.get_player(pid).dice} - {dice}")
        return game_state.factory().f_player(
            pid,
            lambda p: p.factory().dice(new_dice).build()
        ).build()


@dataclass(frozen=True, repr=False)
class AddRerollChancesEffect(DirectEffect):
    pid: Pid
    d_chances: int

    def execute(self, game_state: GameState) -> GameState:
        return game_state.factory().f_player(
            self.pid,
            lambda p: p.factory().f_dice_reroll_chances(
                lambda n: n + self.d_chances
            ).build()
        ).build()


@dataclass(frozen=True, repr=False)
class AddCharacterStatusEffect(DirectEffect):
    """
    Inits the status with default values and adds it to the character.

    If the status is an equipment status and the character already has one,
    all other statuses will be informed about the substitution.
    """
    target: StaticTarget
    status: type[stt.PersonalStatus]

    def execute(self, game_state: GameState) -> GameState:
        character = game_state.get_target(self.target)
        from ..character.character import Character
        assert isinstance(character, Character)
        if issubclass(self.status, stt.CharacterHiddenStatus):  # pragma: no cover
            character = character.factory().f_hiddens(
                lambda ts: ts.update_status(self.status())
            ).build()
        elif issubclass(self.status, stt.EquipmentStatus):
            from ..status.statuses import Statuses
            category = next((
                ctgy
                for ctgy in Statuses._EQUIPMENT_CATEGORIES
                if issubclass(self.status, ctgy)
            ))
            substituted_status = character.character_statuses.find_type(category)
            character = character.factory().f_character_statuses(
                lambda cs: cs.update_status(self.status())
            ).build()
            if substituted_status is not None:
                assert isinstance(substituted_status, stt.EquipmentStatus)
                game_state = game_state.factory().f_player(
                    self.target.pid,
                    lambda p: p.factory().f_characters(
                        lambda cs: cs.factory().character(character).build()  # type: ignore
                    ).build()
                ).build()
                return StatusProcessing.inform_all_statuses(
                    game_state,
                    self.target.pid,
                    Informables.EQUIPMENT_DISCARDING,
                    EquipmentDiscardIEvent(
                        target=self.target,
                        status=type(substituted_status),
                    ),
                )
        elif issubclass(self.status, stt.CharacterStatus):
            character = character.factory().f_character_statuses(
                lambda cs: cs.update_status(self.status())
            ).build()
        else:
            raise NotImplementedError(self.status)
        return game_state.factory().f_player(
            self.target.pid,
            lambda p: p.factory().f_characters(
                lambda cs: cs.factory().character(character).build()  # type: ignore
            ).build()
        ).build()


@dataclass(frozen=True, repr=False)
class RemoveCharacterStatusEffect(DirectEffect):
    target: StaticTarget
    status: type[stt.PersonalStatus]

    def execute(self, game_state: GameState) -> GameState:
        character = game_state.get_character_target(self.target)
        if character is None:  # pragma: no cover
            return game_state
        new_character = character
        if issubclass(self.status, stt.CharacterHiddenStatus):  # pragma: no cover
            new_character = character.factory().f_hiddens(
                lambda ts: ts.remove(self.status)
            ).build()
        elif issubclass(self.status, stt.EquipmentStatus):
            new_character = character.factory().f_character_statuses(
                lambda es: es.remove(self.status)
            ).build()
        elif issubclass(self.status, stt.CharacterStatus):
            new_character = character.factory().f_character_statuses(
                lambda cs: cs.remove(self.status)
            ).build()
        else:
            raise NotImplementedError(self.status)
        return game_state.factory().f_player(
            self.target.pid,
            lambda p: p.factory().f_characters(
                lambda cs: cs.factory().character(new_character).build()
            ).build()
        ).build()


@dataclass(frozen=True, repr=False)
class UpdateCharacterStatusEffect(DirectEffect):
    target: StaticTarget
    status: stt.PersonalStatus

    def execute(self, game_state: GameState) -> GameState:
        character = game_state.get_target(self.target)
        from ..character.character import Character
        assert isinstance(character, Character)
        if isinstance(self.status, stt.CharacterHiddenStatus):  # pragma: no cover
            character = character.factory().f_hiddens(
                lambda ts: ts.update_status(self.status)
            ).build()
        elif isinstance(self.status, stt.EquipmentStatus):
            character = character.factory().f_character_statuses(
                lambda es: es.update_status(self.status)
            ).build()
        elif isinstance(self.status, stt.CharacterStatus):
            character = character.factory().f_character_statuses(
                lambda cs: cs.update_status(self.status)
            ).build()
        else:
            raise NotImplementedError(self.status)
        return game_state.factory().f_player(
            self.target.pid,
            lambda p: p.factory().f_characters(
                lambda cs: cs.factory().character(character).build()  # type: ignore
            ).build()
        ).build()


@dataclass(frozen=True, repr=False)
class OverrideCharacterStatusEffect(DirectEffect):
    target: StaticTarget
    status: stt.PersonalStatus

    def execute(self, game_state: GameState) -> GameState:
        character = game_state.get_target(self.target)
        from ..character.character import Character
        assert isinstance(character, Character)
        if isinstance(self.status, stt.CharacterHiddenStatus):
            character = character.factory().f_hiddens(
                lambda ts: ts.update_status(self.status, override=True)
            ).build()
        elif isinstance(self.status, stt.EquipmentStatus):
            character = character.factory().f_character_statuses(
                lambda es: es.update_status(self.status, override=True)
            ).build()
        elif isinstance(self.status, stt.CharacterStatus):
            character = character.factory().f_character_statuses(
                lambda cs: cs.update_status(self.status, override=True)
            ).build()
        else:
            raise NotImplementedError(self.status)
        return game_state.factory().f_player(
            self.target.pid,
            lambda p: p.factory().f_characters(
                lambda cs: cs.factory().character(character).build()  # type: ignore
            ).build()
        ).build()


@dataclass(frozen=True, repr=False)
class RelativeAddCharacterStatusEffect(DirectEffect):
    source_pid: Pid
    target: DynamicCharacterTarget
    status: type[stt.CharacterStatus]

    def execute(self, game_state: GameState) -> GameState:
        targets = self.target.get_targets(game_state, self.source_pid)
        for target in targets:
            game_state = AddCharacterStatusEffect(
                target=target,
                status=self.status,
            ).execute(game_state)
        return game_state


@dataclass(frozen=True, repr=False)
class AddHiddenStatusEffect(DirectEffect):
    target_pid: Pid
    status: type[stt.PlayerHiddenStatus]

    def execute(self, game_state: GameState) -> GameState:
        return game_state.factory().f_player(
            self.target_pid,
            lambda p: p.factory().f_hidden_statuses(
                lambda ss: ss.update_status(self.status())
            ).build()
        ).build()


@dataclass(frozen=True, repr=False)
class RemoveHiddenStatusEffect(DirectEffect):
    target_pid: Pid
    status: type[stt.PlayerHiddenStatus]

    def execute(self, game_state: GameState) -> GameState:
        return game_state.factory().f_player(
            self.target_pid,
            lambda p: p.factory().f_hidden_statuses(
                lambda ss: ss.remove(self.status)
            ).build()
        ).build()


@dataclass(frozen=True, repr=False)
class UpdateHiddenStatusEffect(DirectEffect):
    """
    Updates the hidden status of a player
    """
    target_pid: Pid
    status: stt.PlayerHiddenStatus

    def execute(self, game_state: GameState) -> GameState:
        return game_state.factory().f_player(
            self.target_pid,
            lambda p: p.factory().f_hidden_statuses(
                lambda ss: ss.update_status(self.status)
            ).build()
        ).build()


@dataclass(frozen=True, repr=False)
class OverrideHiddenStatusEffect(DirectEffect):
    target_pid: Pid
    status: stt.PlayerHiddenStatus

    def execute(self, game_state: GameState) -> GameState:
        return game_state.factory().f_player(
            self.target_pid,
            lambda p: p.factory().f_hidden_statuses(
                lambda ss: ss.update_status(self.status, override=True)
            ).build()
        ).build()


@dataclass(frozen=True, repr=False)
class AddCombatStatusEffect(DirectEffect):
    target_pid: Pid
    status: type[stt.CombatStatus]

    def execute(self, game_state: GameState) -> GameState:
        return game_state.factory().f_player(
            self.target_pid,
            lambda p: p.factory().f_combat_statuses(
                lambda ss: ss.update_status(self.status())
            ).build()
        ).build()


@dataclass(frozen=True, repr=False)
class RemoveCombatStatusEffect(DirectEffect):
    target_pid: Pid
    status: type[stt.CombatStatus]

    def execute(self, game_state: GameState) -> GameState:
        return game_state.factory().f_player(
            self.target_pid,
            lambda p: p.factory().f_combat_statuses(
                lambda ss: ss.remove(self.status)
            ).build()
        ).build()


@dataclass(frozen=True, repr=False)
class UpdateCombatStatusEffect(DirectEffect):
    target_pid: Pid
    status: stt.CombatStatus

    def execute(self, game_state: GameState) -> GameState:
        return game_state.factory().f_player(
            self.target_pid,
            lambda p: p.factory().f_combat_statuses(
                lambda ss: ss.update_status(self.status)
            ).build()
        ).build()


@dataclass(frozen=True, repr=False)
class OverrideCombatStatusEffect(DirectEffect):
    target_pid: Pid
    status: stt.CombatStatus

    def execute(self, game_state: GameState) -> GameState:
        return game_state.factory().f_player(
            self.target_pid,
            lambda p: p.factory().f_combat_statuses(
                lambda ss: ss.update_status(self.status, override=True)
            ).build()
        ).build()


@dataclass(frozen=True, repr=False)
class AddSummonEffect(DirectEffect):
    target_pid: Pid
    summon: type[sm.Summon]

    def execute(self, game_state: GameState) -> GameState:
        return game_state.factory().f_player(
            self.target_pid,
            lambda p: p.factory().f_summons(
                lambda ss: ss.update_summon(self.summon())
            ).build()
        ).build()


@dataclass(frozen=True, repr=False)
class RemoveSummonEffect(DirectEffect):
    target_pid: Pid
    summon: type[sm.Summon]

    def execute(self, game_state: GameState) -> GameState:
        return game_state.factory().f_player(
            self.target_pid,
            lambda p: p.factory().f_summons(
                lambda ss: ss.remove_summon(self.summon)
            ).build()
        ).build()


@dataclass(frozen=True, repr=False)
class UpdateSummonEffect(DirectEffect):
    target_pid: Pid
    summon: sm.Summon

    def execute(self, game_state: GameState) -> GameState:
        return game_state.factory().f_player(
            self.target_pid,
            lambda p: p.factory().f_summons(
                lambda ss: ss.update_summon(self.summon)
            ).build()
        ).build()


@dataclass(frozen=True, repr=False)
class OverrideSummonEffect(DirectEffect):
    target_pid: Pid
    summon: sm.Summon

    def execute(self, game_state: GameState) -> GameState:
        return game_state.factory().f_player(
            self.target_pid,
            lambda p: p.factory().f_summons(
                lambda ss: ss.update_summon(self.summon, override=True)
            ).build()
        ).build()


@dataclass(frozen=True, kw_only=True, repr=False)
class AllSummonIncreaseUsageEffect(DirectEffect):
    target_pid: Pid
    d_usages: int = 1

    def execute(self, game_state: GameState) -> GameState:
        effects: list[Effect] = []
        summons = game_state.get_player(self.target_pid).summons
        for summon in summons:
            effects.append(
                OverrideSummonEffect(
                    target_pid=self.target_pid,
                    summon=replace(summon, usages=summon.usages + self.d_usages),
                )
            )
        return game_state.factory().f_effect_stack(
            lambda es: es.push_many_fl(effects)
        ).build()


@dataclass(frozen=True, kw_only=True, repr=False)
class OneSummonIncreaseUsageEffect(DirectEffect):
    target: StaticTarget
    d_usages: int = 1

    def execute(self, game_state: GameState) -> GameState:
        effects: list[Effect] = []
        summons = game_state.get_player(self.target.pid).summons
        summon = summons.find(summon_type=cast(type[sm.Summon], self.target.id))
        if summon is None:  # pragma: no cover
            return game_state

        effects.append(
            OverrideSummonEffect(
                target_pid=self.target.pid,
                summon=replace(summon, usages=summon.usages + self.d_usages),
            )
        )
        return game_state.factory().f_effect_stack(
            lambda es: es.push_many_fl(effects)
        ).build()


@dataclass(frozen=True, kw_only=True, repr=False)
class OneSummonDecreaseUsageEffect(DirectEffect):
    target: StaticTarget
    d_usages: int = 1

    def execute(self, game_state: GameState) -> GameState:
        effects: list[Effect] = []
        summons = game_state.get_player(self.target.pid).summons
        summon = summons.find(summon_type=cast(type[sm.Summon], self.target.id))
        if summon is None:  # pragma: no cover
            return game_state

        effects.append(
            UpdateSummonEffect(
                target_pid=self.target.pid,
                summon=replace(summon, usages=-self.d_usages),
            )
        )
        return game_state.factory().f_effect_stack(
            lambda es: es.push_many_fl(effects)
        ).build()


@dataclass(frozen=True, repr=False)
class AddSupportEffect(DirectEffect):
    target_pid: Pid
    support: type[sp.Support]

    def execute(self, game_state: GameState) -> GameState:
        return game_state.factory().f_player(
            self.target_pid,
            lambda p: p.factory().f_supports(
                lambda ss: ss.update_support(self.support(sid=ss.new_sid(self.support)))
            ).build()
        ).build()


@dataclass(frozen=True, repr=False)
class RemoveSupportEffect(DirectEffect):
    target_pid: Pid
    sid: int

    def execute(self, game_state: GameState) -> GameState:
        return game_state.factory().f_player(
            self.target_pid,
            lambda p: p.factory().f_supports(
                lambda ss: ss.remove_by_sid(self.sid)
            ).build()
        ).build()


@dataclass(frozen=True, repr=False)
class UpdateSupportEffect(DirectEffect):
    target_pid: Pid
    support: sp.Support

    def execute(self, game_state: GameState) -> GameState:
        return game_state.factory().f_player(
            self.target_pid,
            lambda p: p.factory().f_supports(
                lambda ss: ss.update_support(self.support)
            ).build()
        ).build()


@dataclass(frozen=True, repr=False)
class OverrideSupportEffect(DirectEffect):
    target_pid: Pid
    support: sp.Support

    def execute(self, game_state: GameState) -> GameState:
        return game_state.factory().f_player(
            self.target_pid,
            lambda p: p.factory().f_supports(
                lambda ss: ss.update_support(self.support, override=True)
            ).build()
        ).build()


@dataclass(frozen=True, repr=False)
class CastSkillEffect(DirectEffect):
    target: StaticTarget
    skill: CharacterSkill

    def execute(self, game_state: GameState) -> GameState:
        character = game_state.get_target(self.target)
        from ..character.character import Character
        assert isinstance(character, Character)
        if not character.can_cast_skill():  # pragma: no cover
            return game_state
        effects = character.skill(game_state, self.target, self.skill)
        if not effects:  # pragma: no cover
            return game_state
        return game_state.factory().f_effect_stack(
            lambda es: es.push_many_fl(effects)
        ).build()


@dataclass(frozen=True, repr=False)
class BroadcastPostSkillInfoEffect(DirectEffect):
    source: StaticTarget
    skill: CharacterSkill

    def execute(self, game_state: GameState) -> GameState:
        char = game_state.get_character_target(self.source)
        assert char is not None
        return StatusProcessing.inform_all_statuses(
            game_state,
            self.source.pid,
            Informables.POST_SKILL_USAGE,
            SkillIEvent(
                source=self.source,
                skill_type=self.skill,
                skill_true_type=char.skill_actual_type(self.skill),
            ),
        )

@dataclass(frozen=True, repr=False)
class BroadcastPreSkillInfoEffect(DirectEffect):
    source: StaticTarget
    skill: CharacterSkill

    def execute(self, game_state: GameState) -> GameState:
        char = game_state.get_character_target(self.source)
        assert char is not None
        return StatusProcessing.inform_all_statuses(
            game_state,
            self.source.pid,
            Informables.PRE_SKILL_USAGE,
            SkillIEvent(
                source=self.source,
                skill_type=self.skill,
                skill_true_type=char.skill_actual_type(self.skill),
            ),
        )

@dataclass(frozen=True, repr=False)
class SetRedrawChancesEffect(DirectEffect):
    target_pid: Pid
    redraw_chances: int

    def execute(self, game_state: GameState) -> GameState:
        return game_state.factory().f_player(
            self.target_pid,
            lambda p: p.factory().card_redraw_chances(self.redraw_chances).build()
        ).build()


@dataclass(frozen=True, repr=False)
class SetRerollChancesEffect(DirectEffect):
    target_pid: Pid
    reroll_chances: int

    def execute(self, game_state: GameState) -> GameState:
        return game_state.factory().f_player(
            self.target_pid,
            lambda p: p.factory().dice_reroll_chances(self.reroll_chances).build()
        ).build()
