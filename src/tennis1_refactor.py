class TennisGame1:

    # Inicializador de clase.
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1points = 0
        self.p2points = 0



    # Función que suma un punto a la puntuación del ganador del punto.
    def won_point(self, player_name):
        if player_name == "player1":
            self.p1points += 1
        else:
            self.p2points += 1



    # Función que determina el marcador de un juego en un determinado momento.
    def score(self):
        game_scoreboard = ""
        temporal_game_score = 0
        
        # Caso 1: si las puntuaciones son iguales.
        if self.p1points == self.p2points:
            game_scoreboard = {
                0: "Love-All",
                1: "Fifteen-All",
                2: "Thirty-All",
            }.get(self.p1points, "Deuce") # Para cualquier valor mayor que 3 devuelve "Deuce".
        
        
        # Caso 2: victoria o ventaja.
        elif self.p1points >= 4 or self.p2points >= 4:
            minus_result = self.p1points - self.p2points
            if minus_result == 1:
                game_scoreboard = "Advantage player1"
            elif minus_result == -1:
                game_scoreboard = "Advantage player2"
            elif minus_result >= 2:
                game_scoreboard = "Win for player1"
            else:
                game_scoreboard = "Win for player2"
        
        # Caso 3: marcador dónde uno va ganando pero no tiene ventaja.
        
        else:
            for i in range(1, 3):
                if i == 1:
                    temporal_game_score = self.p1points
                else:
                    game_scoreboard += "-"
                    temporal_game_score = self.p2points
                game_scoreboard += {
                    0: "Love",
                    1: "Fifteen",
                    2: "Thirty",
                    3: "Forty",
                }[temporal_game_score]
        return game_scoreboard