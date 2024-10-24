from typing import Union, Optional

import interface

class Pokemon:
    """
    Base class with all relevant information to describe a Pokemon.
    """

    def __init__(self) -> None:
        """
        Class constructor.
        """
        generation: interface.Generation
        name: interface.Name
        species: interface.Species
        types: Union[interface.TypeName, tuple[interface.TypeName]]
        weight_kg: int
        level: int

        gender: Optional[interface.GenderName]
        ability: Optional[str]
        abilityOn: Optional[bool]
        is_dynamaxed: Optional[bool]
        dynamax_level: Optional[int]
        is_salt_cure: Optional[bool]
        allies_fainted: Optional[int]
        boostedStat?: I.StatIDExceptHP | 'auto';
        item?: I.ItemName;
        teraType?: I.TypeName;

        nature: I.NatureName;
        ivs: I.StatsTable;
        evs: I.StatsTable;
        boosts: I.StatsTable;
        rawStats: I.StatsTable;
        stats: I.StatsTable;

        originalCurHP: number;
        status: I.StatusName | '';
        toxicCounter: number;

        moves: I.MoveName[];
