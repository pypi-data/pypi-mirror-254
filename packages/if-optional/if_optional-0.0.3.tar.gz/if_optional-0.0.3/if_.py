class if_:
    def __init__(self, maybe):
        self._ = maybe

    def __next_if(self, fn):
        try:
            return if_(fn())
        except (AttributeError, LookupError, TypeError):
            return if_(None)

    def __getattr__(self, key, *a, **kw):
        return self.__next_if(lambda: getattr(self._, key, *a, **kw))

    def __getitem__(self, key):
        return self.__next_if(lambda: self._[key])

    def __call__(self, *a, **kw):
        return self.__next_if(lambda: self._(*a, **kw))

    def __repr__(self):
        return '<if_ with value %s>' % self._

    def __bool__(self):
        return bool(self._)

    def __eq__(self, other):
        return self._ == other
