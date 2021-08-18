from src.factory import AbstractFactory
import random as rd
import sys

class FactoryFacade:

    def __init__(self, factory: AbstractFactory) -> None:
        self._factory = factory

    @property
    def factory(self) -> AbstractFactory:
        return self._factory

    @factory.setter
    def factory(self, factory: AbstractFactory) -> None:
        self._factory = factory

    def load_data_by_name(self, unit: int, path: str) -> any:
        """This method will create a list of an entity according to the factory.
        Although parameter unit defines the number of elements it'll also 
        depends on the number of data loaded from a file. It is expected names
        in the file.

        Args:
            unit (int): Number of entities. If no data is found no entity is created
            path (str): Path of the file that'll be loaded. The path's reference
                is from the script that involked the method.

        Returns:
            any: The return is a list of an entity defined by the factory.

        Raises:
            OSError: If not file is found an exception is raised
                and the system is closed.
        
        Notes:
            See https://docs.python.org/3/library/pathlib.html
            for more info.
        """
        try:
            with open(path) as f:
                names = rd.choices([l for l in f], k=unit)
                return self._factory.make_many(names)
        except OSError:
            print ("Could not open/read file:", path)
            sys.exit()