import jax
import jax.numpy as jnp
from flax import struct

from ..core.constants import TILES_REGISTRY, Colors, Tiles
from ..core.goals import EmptyGoal, TileNearGoal
from ..core.grid import (
    equal,
    room,
    sample_coordinates,
    sample_direction,
)
from ..core.rules import EmptyRule, TileNearRule
from ..environment import Environment, EnvParams
from ..types import AgentState, EnvCarry, RuleSet, State

_empty_ruleset = RuleSet(
    goal=EmptyGoal().encode(),
    rules=EmptyRule().encode()[None, ...],
    init_tiles=jnp.array(((TILES_REGISTRY[Tiles.EMPTY, Colors.EMPTY],))),
)

def generate_room(key, height, width):
    grid = room(height, width)
    return key, grid


class XLandMiniGridEnvOptions(EnvParams):
    # experimental (can not vmap on it)
    num_rules: int = struct.field(pytree_node=False, default=1)


class XLandMiniGrid(Environment):
    def default_params(self, **kwargs) -> XLandMiniGridEnvOptions:
        default_params = XLandMiniGridEnvOptions(view_size=5)
        return default_params.replace(**kwargs)

    def time_limit(self, params: XLandMiniGridEnvOptions) -> int:
        # this is just a heuristic to prevent brute force in one episode,
        # agent need to remember what he tried in previous episodes.
        # If this is too small, change it or increase number of trials (these are not equivalent).
        return 3 * (params.height * params.width)

    def _generate_problem(self, params: XLandMiniGridEnvOptions, key: jax.Array) -> State:
        if params.num_rules == 0:
            ruleset = _empty_ruleset
        else:
            goal = TileNearGoal(
                tile_a=TILES_REGISTRY[Tiles.BALL, Colors.GREY],
                tile_b=TILES_REGISTRY[Tiles.BALL, Colors.RED]
            )
            rules = [
                TileNearRule(
                    tile_a=TILES_REGISTRY[Tiles.SQUARE, Colors.RED],
                    tile_b=TILES_REGISTRY[Tiles.BALL, Colors.GREY],
                    prod_tile=TILES_REGISTRY[Tiles.HEX, Colors.ORANGE]
                ) for _ in range(params.num_rules)
            ]
            rules = jnp.vstack([rule.encode() for rule in rules])
            if rules.ndim == 1:
                rules = rules[None, ...]

            ruleset = RuleSet(
                goal=goal.encode(),
                rules=rules,
                init_tiles=jnp.array(((
                    TILES_REGISTRY[Tiles.BALL, Colors.GREY],
                    TILES_REGISTRY[Tiles.SQUARE, Colors.RED],
                    TILES_REGISTRY[Tiles.HEX, Colors.ORANGE]
                ))),
            )

        key, grid = generate_room(key, params.height, params.width)

        num_objects = len(ruleset.init_tiles)
        objects = ruleset.init_tiles

        key, coords_key, dir_key = jax.random.split(key, num=3)
        positions = sample_coordinates(coords_key, grid, num=num_objects + 1)
        for i in range(num_objects):
            # we ignore empty tiles, as they are just paddings to the same shape
            grid = jax.lax.select(
                equal(objects[i], TILES_REGISTRY[Tiles.EMPTY, Colors.EMPTY]),
                grid,
                grid.at[positions[i][0], positions[i][1]].set(objects[i]),
            )

        agent = AgentState(position=positions[-1], direction=sample_direction(dir_key))
        state = State(
            key=key,
            step_num=jnp.asarray(0),
            grid=grid,
            agent=agent,
            goal_encoding=ruleset.goal,
            rule_encoding=ruleset.rules,
            carry=EnvCarry(),
        )
        return state
