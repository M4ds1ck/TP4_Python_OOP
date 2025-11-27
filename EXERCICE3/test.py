import unittest
from paiements import CarteBancaire, PayPal, Crypto

class TestPaiements(unittest.TestCase):

    def test_montant_negatif_leve_erreur(self):
        print("Test montant négatif")
        with self.assertRaises(ValueError):
            CarteBancaire(-10, "1111", "000")

    def test_paiement_cb(self):
        print("Test Carte Bancaire")
        cb = CarteBancaire(100.0, "1234567812345678", "123")
        msg = cb.payer()
        print(msg)
        self.assertIn("100.00€", msg)
        self.assertIn("5678", msg)

    def test_paiement_paypal(self):
        print("Test PayPal")
        pp = PayPal(50.0, "test@test.com", "TOKEN")
        msg = pp.payer()
        print(msg)
        self.assertIn("PayPal", msg)

    def test_paiement_crypto(self):
        print("Test Crypto")
        cr = Crypto(2.5, "WALLET_ID", "BTC")
        msg = cr.payer()
        print(msg)
        self.assertIn("BTC", msg)

if __name__ == "__main__":
    unittest.main()
