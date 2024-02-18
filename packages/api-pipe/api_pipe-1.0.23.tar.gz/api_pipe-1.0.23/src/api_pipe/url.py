'''
    URL
'''
class Url:
    '''
        URL
    '''

    def __init__(self, value: str) -> None:
        '''
            Init
        '''
        self.value = value

    def __truediv__(self, other) -> "Url":
        '''
            Truediv
        '''
        _other = other.value if isinstance(other, Url) else other
        return Url(f"{self.value}/{_other}")

    def __str__(self):
        '''
            Str
        '''
        return self.value

    def __eq__(self, other):
       '''
           Eq
       '''
       if isinstance(other, str):
           return self.value == other
       elif isinstance(other, Url):
           return self.value == other.value
       else:
           return NotImplemented
