import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_saldo_oikein_alussa(self):
        self.assertEqual(self.maksukortti.saldo, 1000)

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(1000)

        self.assertEqual(self.maksukortti.saldo_euroina(), 20)
    
    def test_saldo_vahenee_oikein_jos_raha_on_tarpeeksi(self):
        self.maksukortti.ota_rahaa(500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 5)
    
    def test_saldo_ei_muutu_jos_rahaa_ei_ole_tarpeeksi(self):
        self.maksukortti.ota_rahaa(1500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 10)
    
    def test_true_jos_tarpeeksi_false_jos_ei_ole_tarpeeksi_rahaa(self):

        self.assertTrue(self.maksukortti.ota_rahaa(1000))
    
    def test_saldo_euroina_pyöristety(self):

        maksukortti = Maksukortti(1000)

        self.assertEqual(maksukortti.__str__(), 'Kortilla on rahaa 10.00 euroa')

