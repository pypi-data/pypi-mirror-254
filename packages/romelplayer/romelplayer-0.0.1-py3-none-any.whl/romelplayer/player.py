"""
Documentacion de Player
"""


class Player:
    """
    Clase del reproductor
    """

    def play(self, song):
        """
        Metodo para reproducir cancion dado el parametro

        Parameters:
        song (str): string de la cancion

        Returns:
        int: Devuelve 1 si reproduce con exito de lo contrario 0
        """
        print("Reproduciendo cancion")

    def stop(self):
        """
        Metodo para reproducir cancion dado en el constructor

        Parameters:
        song (str): string de la cancion

        Returns:
        int: Devuelve 1 si reproduce con exito de lo contrario 0
        """
        print("Stopping")
