from typing import Union, Optional

import interface


class Pokemon:
    """
    Base class with all relevant information to describe a Pokemon.
    """

    generation: interface.Generation
    name: interface.Name
    species: interface.Species
    types: Union[interface.Type, tuple[interface.Type, interface.Type]]
    weight_kg: int
    level: int

    gender: Optional[interface.Gender]
    ability: Optional[interface.Ability]
    ability_on: Optional[bool]
    is_dynamaxed: Optional[bool]
    dynamax_level: Optional[int]
    is_salt_cure: Optional[bool]
    allies_fainted: Optional[int]
    boosted_stat: Optional[interface.Stat]
    item: Optional[str]
    teraType: Optional[str]

    nature: interface.Nature
    ivs: dict[interface.Stat, int]
    evs: dict[interface.Stat, int]
    boosts: dict[interface.Stat, float]
    raw_stats: dict[interface.Stat, int]
    stats: dict[interface.Stat, int]

    original_curr_hp: int
    status: Optional[interface.Status]
    toxic_counter: int

    moves: interface.Moveset

    def __init__(self) -> None:
        """
        Class constructor.
        """
        pass
