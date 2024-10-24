from enum import Enum


class Data:
    """
    Base data class, from which some others inherit.
    """

    def __init__(self) -> None:
        """
        Class constructor.
        """
        pass


class Generation:
    """
    Class with all relevant info of a generation.
    """
    pass

    def __init__(self) -> None:
        """
        Class constructor.
        """
        pass


class Name(Data):
    """
    Class storing Pokemon name and ID.
    """

    def __init__(self) -> None:
        """
        Class constructor.
        """
        super.__init__()
        pass


class Species:
    """
    Class with all relevant info for all variation of a Pokemon given its name.
    """

    def __init__(self) -> None:
        """
        Class constructor.
        """
        pass


class TypeName(Enum):
    """
    Enum of all possible Pokemon types.
    """
    pass


class GenderName(Enum):
    """
    Enum of all possible Pokemon genders.
    """
    pass
