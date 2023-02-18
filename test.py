class Myclass():
    
    def __init__(self) -> None:
        pass
    def hi(self):
        raise ImportError(
            'Pereopredli' % (self.__class__.__name__)
        )

class Mycl(Myclass):
    pass

r1=Mycl()