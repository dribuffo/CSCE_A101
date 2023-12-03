class ChildName:
    def __init__(self, rank, name, births):
        self.rank = rank
        self.name = name
        self.births = births

    def print_info(self):
        return f'{self.name} is rank {self.rank} w/ {self.births} number of births'
