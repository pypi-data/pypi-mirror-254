from dataclasses import dataclass

@dataclass
class NSTI:
    _n: int
    _s: int
    _t: int
    _i: int

    @property
    def n(self):
        return self._n

    @n.setter
    def n(self, value):
        if not isinstance(value, int):
            raise ValueError("Value must be an integer.")
        self._n = value

    @property
    def s(self):
        return self._s

    @s.setter
    def s(self, value):
        if not isinstance(value, int):
            raise ValueError("Value must be an integer.")
        self._s = value

    @property
    def t(self):
        return self._t

    @t.setter
    def t(self, value):
        if not isinstance(value, int):
            raise ValueError("Value must be an integer.")
        self._t = value

    @property
    def i(self):
        return self._i

    @i.setter
    def i(self, value):
        if not isinstance(value, int):
            raise ValueError("Value must be an integer.")
        self._i = value

    @property
    def n_s_t_i(self):
        return f'{self.n}_{self.s}_{self.t}_{self.i}'