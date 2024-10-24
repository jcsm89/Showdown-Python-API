from enum import Enum


class DataType(Enum):
    """
    Enum of all supported data types.
    """
    Name = 0    # TODO: This is not in the original Enum, investigate further
    Ability = 1
    Item = 2
    Move = 3
    Species = 4


class Data:
    """
    Base data class, from which some others inherit.
    """
    # TODO: Check how this two are filled
    id: str
    name: str
    type: DataType

    def __init__(self,
                 type: DataType) -> None:
        """
        Class constructor.
        """
        self.type = type


class Name(Data):
    """
    Class storing Pokemon name and ID.
    """

    def __init__(self) -> None:
        """
        Class constructor.
        """
        super.__init__(type=DataType.Name)
        pass


class Ability(Data):
    """
    Class storing an ability name and ID.
    """

    def __init__(self) -> None:
        """
        Class constructor.
        """
        super.__init__(type=DataType.Ability)
        pass


class Item(Data):
    """
    Class storing an item name and ID.
    """

    def __init__(self) -> None:
        """
        Class constructor.
        """
        super.__init__(type=DataType.Item)
        pass


class Move(Data):
    """
    Class with all relevant info for all a Pokemon move.
    """

    def __init__(self) -> None:
        """
        Class constructor.
        """
        super.__init__(type=DataType.Move)
        pass


class Species(Data):
    """
    Class with all relevant info for all variation of a Pokemon given its name.
    """

    def __init__(self) -> None:
        """
        Class constructor.
        """
        super.__init__(type=DataType.Species)
        pass


class Generation:
    """
    Class with all relevant info of a generation.
    """

    def __init__(self) -> None:
        """
        Class constructor.
        """
        pass


class Moveset:
    """
    Class with all relevant information of a Pokemon's moveset.
    """

    move_1: Move
    move_2: Move
    move_3: Move
    move_4: Move

    def __init__(self,
                 move_1: Move,
                 move_2: Move,
                 move_3: Move,
                 move_4: Move) -> None:
        """
        Class constructor.
        """
        self.move_1 = move_1
        self.move_2 = move_2
        self.move_3 = move_3
        self.move_4 = move_4


class Type(Enum):
    """
    Enum of all possible Pokemon types.
    """
    pass


class Gender(Enum):
    """
    Enum of all possible Pokemon genders.
    """
    pass


class Stat(Enum):
    """
    Enum of all possible Pokemon stats.
    """
    pass


class Nature(Enum):
    """
    Enum of all possible Pokemon natures.
    """
    pass


class Status(Enum):
    """
    Enum of all possible Pokemon status conditions.
    """
    pass
