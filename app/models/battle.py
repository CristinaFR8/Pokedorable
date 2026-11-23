class Battle:
    def __init__(self, trainer, pokemon, rival):
        self.participants = [
            {
                "trainer": trainer,
                "pokemon": pokemon
            },
            {
                "trainer": "CPU",
                "pokemon": rival
            }
        ]

        self.turns = []
        self.winner = None
