import networkx as nx
import matplotlib.pyplot as plt

class Ligne():
    
    def __init__(self):
        self.G = nx.Graph()
        self.positions = {}
    
    def draw(self):
        # nx.draw(self.G, with_labels=True)
        fig, axs = plt.subplots(2, 3, sharex=True, sharey=True, layout="constrained")

        for arret, pos_gps in self.positions.items():
            # print(f"{arret}, {pos_gps}")
            pass
        
        plt.show()
        plt.savefig("graphe.png")

    def add_arret(self, latitude, longitude, valeur):
        self.G.add_node(valeur)
        self.positions[valeur] = (latitude, longitude)
        print(f'Ajout de ({latitude}, {longitude}) a {valeur}')

class LigneQuatre(Ligne):

    def __init__(self):
        super().__init__()
        la, lo = 47.658793863954216, 6.837021267749245
        self.add_arret(la, lo, "Mechelle")

