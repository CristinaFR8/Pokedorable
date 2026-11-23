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

    def current_hp(self, participant: int) -> int:
        pokemon = self.participants[participant]["pokemon"]
        hp = pokemon.max_hp()

        for turn in self.turns:
            if turn["attacker"] != participant:
                hp -= turn["damage"]

        if hp < 0:
            hp = 0

        return hp

    def is_over(self) -> bool:
        return self.winner is not None
