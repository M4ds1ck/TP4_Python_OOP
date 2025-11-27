from abc import ABC, abstractmethod

# --- Classe Abstraite ---
class Paiement(ABC):
    def __init__(self, montant):
        if montant <= 0:
            raise ValueError("Le montant doit être positif.")
        self._montant = float(montant)

    @abstractmethod
    def payer(self):
        pass

# --- Sous-classes ---
class CarteBancaire(Paiement):
    def __init__(self, montant, numero, cvv):
        super().__init__(montant)
        self._numero = numero
        self._cvv = cvv

    def payer(self):
        # Masquage simple du numéro pour l'affichage
        num_masque = self._numero[-4:]
        return f"Paiement Carte Bancaire de {self._montant:.2f}€ validé (Finissant par ****{num_masque})"

class PayPal(Paiement):
    def __init__(self, montant, email, token):
        super().__init__(montant)
        self._email = email
        self._token = token

    def payer(self):
        return f"Paiement PayPal de {self._montant:.2f}€ envoyé à {self._email}"

class Crypto(Paiement):
    def __init__(self, montant, wallet_id, reseau):
        super().__init__(montant)
        self._wallet_id = wallet_id
        self._reseau = reseau

    def payer(self):
        return f"Paiement Crypto de {self._montant:.2f} sur réseau {self._reseau} (Wallet: {self._wallet_id})"

# --- Fonction Utilitaire Polymorphe ---
def traiter_paiements(liste_paiements):
    print("--- Traitement des transactions ---")
    for p in liste_paiements:
        # Appel polymorphe : pas de if isinstance()
        try:
            print(p.payer())
        except Exception as e:
            print(f"Erreur : {e}")

# --- Programme Principal ---
if __name__ == "__main__":
    # Création de la collection hétérogène
    panier = [
        CarteBancaire(45.50, "1234567812348888", "123"),
        PayPal(12.00, "client@example.com", "TOK_123_SECURE"),
        Crypto(0.05, "0xABC123DEADBEEF", "ETH"),
        CarteBancaire(199.99, "9876543210987777", "999"),
        PayPal(5.50, "don@asso.org", "TOK_DON_456"),
        Crypto(1.2, "bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh", "BTC")
    ]

    traiter_paiements(panier)