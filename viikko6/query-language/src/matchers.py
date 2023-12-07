class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True


class Or:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if matcher.test(player):
                return True

        return False


class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value


class All:
    def test(self, player):
        return True


class Not:
    def __init__(self, ehto):
        self.ehto = ehto

    def test(self, player):
        return not self.ehto.test(player)


class HasFewerThan:
    def __init__(self, value, attr):
        self.ehto = HasAtLeast(value, attr)

    def test(self, player):
        return Not(self.ehto).test(player)


class Matcher:
    def __init__(self):
        self.operations = []

    def add(self, query):
        self.operations.append(query)

    def clear(self):
        self.operations.clear()

    def build(self):
        return And(*self.operations)


class QueryBuilder:
    def __init__(self, operations=Matcher(), match=All()):
        self.matcher = operations
        self.matcher.add(match)

    def build(self):
        matcher = self.matcher.build()
        self.matcher.clear()
        return matcher

    def playsIn(self, team):
        return QueryBuilder(self.matcher, PlaysIn(team))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(self.matcher, HasAtLeast(value, attr))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(self.matcher, HasFewerThan(value, attr))

    def oneOf(self, m1, m2):
        return QueryBuilder(self.matcher, Or(m1, m2))
