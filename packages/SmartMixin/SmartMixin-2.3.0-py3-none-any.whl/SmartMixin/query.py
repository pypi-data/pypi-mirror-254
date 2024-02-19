import re
from typing import Callable, Iterable


class FunctionApplier:
    """
    Applies a given function to each item in an iterable (in reverse order).
    """

    def __init__(self, __function_name: str, __iterable: Iterable) -> None:
        """
        Initialize the FunctionApplier with a function name and an iterable.

        Args:
            __function_name (str): The name of the function to be applied to the iterable.
            __iterable (Iterable): The iterable to which the function will be applied.
        """

        self.__function_name__ = __function_name
        self.__container__ = __iterable

    def __call__(self, **kwargs) -> None:
        """Applies the function to each item in the iterable (in reverse order).

        The function is applied by calling the function attribute of each item in the iterable.
        Any keyword arguments passed to this method will be forwarded to the function.

        Args:
            **kwargs: Arbitrary keyword arguments to be passed to the function.
        """

        for i in range(len(self.__container__) - 1, -1, -1):
            self.__container__[i].__getattribute__(
                self.__function_name__)(**kwargs)


class MultiSelector(list):
    """
    MultiSelector is a subclass of list that allows for the application of 
    functions to all elements in the list.
    """

    def __init__(self, __iterable: Iterable) -> None:
        """
        Initialize the MultiSelector with an iterable object.

        Args:
            __iterable (Iterable): An iterable object to initialize the list.
        """

        super().__init__(__iterable)

    def __getattr__(self, __name: str) -> FunctionApplier:
        """
        Overrides the default behavior of attribute access. It returns a FunctionApplier object that applies the 
        function (the attribute name) to all elements in the list.

        Args:
            __name (str): The name of the attribute or function to apply.

        Returns:
            FunctionApplier: An object that applies the function to all elements in the list.
        """

        return FunctionApplier(__name, self)


class EmptySelector:
    """
    EmptySelector is a class that represents an empty selection. 
    It has a length of 0 and any attribute access returns an empty function.
    """

    def __init__(self) -> None:
        """
        Initialize the EmptySelector. An empty function is created and stored 
        as an instance variable.
        """

        def empty_function(*args, **kwargs):
            pass

        self.empty_function = empty_function

    def __len__(self) -> int:
        """
        Returns the length of the EmptySelector, which is always 0.

        Returns:
            int: The length of the EmptySelector.
        """

        return 0

    def __getattr__(self, __object) -> Callable:
        """
        Overrides the default behavior of attribute access. It returns an empty function.

        Args:
            __object (str): The name of the attribute.

        Returns:
            Callable: An empty function that takes any arguments and does nothing.
        """

        return self.empty_function


class WrapperList(list):
    """
    WrapperList is a subclass of list that assigns a container attribute to 
    the objects it holds.
    """

    def __init__(self, __container: Iterable | None = None, __iterable: Iterable | None = None) -> None:
        """
        Initialize a new instance of WrapperList.

        Args:
            __container (Iterable): The container that holds the objects.
            __iterable (Iterable | None, optional): An iterable to initialize the list with. Defaults to None.
        """

        list.__init__([])
        if not __container == None:
            self.__container__ = __container
        if not __iterable == None:
            self.extend(__iterable)

    def append(self, __object) -> None:
        """
        Append an object to the end of the list. The object is assigned a 
        container attribute.

        Args:
            __object: The object to append to the list.
        """

        __object.__setattr__("__container__", self.__container__)
        return super().append(__object)

    def insert(self, __index: int, __object) -> None:
        """
        Insert an object at a given position in the list. The object is assigned 
        a container attribute.

        Args:
            __index (int): The position at which to insert the object.
            __object: The object to insert into the list.
        """

        __object.__setattr__("__container__", self.__container__)
        return super().insert(__index, __object)

    def extend(self, __iterable: Iterable) -> None:
        """
        Extend the list by appending all the items from the iterable. The items 
        are assigned a container attribute.

        Args:
            __iterable (Iterable): The iterable with items to append to the list.
        """

        for i in __iterable:
            i.__setattr__("__container__", self.__container__)
        return super().extend(__iterable)

    def __setitem__(self, __index: int, __value) -> None:
        """
        Set the value at a given position in the list. The value is assigned 
        a container attribute.

        Args:
            __index (int): The position at which to set the value.
            __value: The value to set at the given position in the list.
        """

        if isinstance(__index, slice):
            for i in __value:
                i.__setattr__("__container__", self.__container__)
        else:
            __value.__setattr__("__container__", self.__container__)
        super().__setitem__(__index, __value)


def select_all(__iterable: Iterable, reverse: bool = False, **kwargs) -> MultiSelector:
    """
    Selects elements from an iterable based on specified conditions. The conditions 
    are provided as keyword arguments where the key is the attribute name and the 
    value is the expected attribute value. If the key starts with "re_", a regular 
    expression search is performed on the attribute value.

    Args:
        __iterable (Iterable): The iterable from which to select elements.
        reverse (bool, optional): If True, elements that do not meet the conditions 
        are selected. If False, elements that meet the conditions are selected. 
        Defaults to False.

    Returns:
        MultiSelector: A MultiSelector object containing the selected elements.
    """

    result = []
    for i in __iterable:
        tmp = True
        for j in kwargs.keys():
            if j.startswith("re_"):
                if not re.search(kwargs[j], getattr(i, j[3:])):
                    tmp = False
                    break
            else:
                if not kwargs[j] == getattr(i, j):
                    tmp = False
                    break
        if tmp and not reverse:
            result.append(i)
        elif not tmp and reverse:
            result.append(i)
    return MultiSelector(result)


def select(__iterable: Iterable, reverse: bool = False, **kwargs) -> EmptySelector | object:
    """
    Selects the first element from an iterable that matches specified conditions. 
    The conditions are provided as keyword arguments where the key is the attribute 
    name and the value is the expected attribute value. If the key starts with "re_", 
    a regular expression search is performed on the attribute value.

    If no element matches the conditions, an EmptySelector is returned.

    Args:
        __iterable (Iterable): The iterable from which to select elements.
        reverse (bool, optional): If True, the first element that does not meet 
        the conditions is selected. If False, the first element that meets the 
        conditions is selected. Defaults to False.

    Returns:
        Union[EmptySelector, object]: The first element that matches the conditions 
        or an EmptySelector if no element matches the conditions.
    """

    for i in __iterable:
        tmp = True
        for j in kwargs.keys():
            if j.startswith("re_"):
                if not re.search(kwargs[j], getattr(i, j[3:])):
                    tmp = False
                    break
            else:
                if not kwargs[j] == getattr(i, j):
                    tmp = False
                    break
        if tmp and not reverse:
            return i
        elif not tmp and reverse:
            return i
    return EmptySelector()


def insert_front(li: list, __object) -> None:
    """
    Inserts an object at the beginning of a list.

    Args:
        li (list): The list where the object will be inserted.
        __object: The object to be inserted at the beginning of the list.
    """

    li.insert(0, __object)


def append_back(li: list, __object) -> None:
    """
    Appends an object to the end of a list.

    Args:
        li (list): The list where the object will be appended.
        __object: The object to be appended to the end of the list.
    """

    li.append(__object)


def extend_back(li: list, __iterable: Iterable) -> None:
    """
    Extends a list by appending all the items from an iterable at the end. 
    The iterable must be a list.

    Args:
        li (list): The list to be extended.
        __iterable (Iterable): The iterable with items to append to the list.

    Raises:
        ValueError: If the iterable is not a list.
    """

    if not isinstance(__iterable, list):
        raise ValueError("YAML List Expected")
    li.extend(__iterable)


def extend_front(li: list, __iterable: Iterable) -> None:
    """
    Extends a list by inserting all the items from an iterable at the beginning. 
    The iterable must be a list.

    Args:
        li (list): The list to be extended.
        __iterable (Iterable): The iterable with items to insert at the beginning of the list.

    Raises:
        ValueError: If the iterable is not a list.
    """

    if not isinstance(__iterable, list):
        raise ValueError("YAML List Expected")
    li[0:0] = __iterable
