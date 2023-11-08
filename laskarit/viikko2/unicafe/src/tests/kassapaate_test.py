import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):

    def setUp(self):
        self.kassa = Kassapaate()
    
    def test_kasassa_rahaa(self):

        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
    
    def test_myytyjen_edullisen_lounaan_alkumäärä(self):

        self.assertEqual(self.kassa.edulliset, 0)

    def test_myytyjen_maukkaan_lounaan_alkumäärä(self):

        self.assertEqual(self.kassa.maukkaat, 0)

    def test_osto_kateisella_riitavalla_maaralla(self):

        vaihtoraha = self.kassa.syo_edullisesti_kateisella(300)
        self.assertEqual(vaihtoraha, 60)  
        self.assertEqual(self.kassa.kassassa_rahaa, 100240)  
        self.assertEqual(self.kassa.edulliset, 1)  

        vaihtoraha = self.kassa.syo_maukkaasti_kateisella(500)
        self.assertEqual(vaihtoraha, 100) 
        self.assertEqual(self.kassa.kassassa_rahaa, 100640)  
        self.assertEqual(self.kassa.maukkaat, 1)  
    
    def test_osto_kateisella_ei_riitavalla_maaralla(self):

        vaihtoraha = self.kassa.syo_edullisesti_kateisella(200)
        self.assertEqual(vaihtoraha, 200)  
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)  
        self.assertEqual(self.kassa.edulliset, 0)  

        vaihtoraha = self.kassa.syo_maukkaasti_kateisella(300)
        self.assertEqual(vaihtoraha, 300) 
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)  
        self.assertEqual(self.kassa.maukkaat, 0)  
    
    def test_osto_kortilta_riittävällä_määrällä_rahaa(self):
        """
        I didn't know if the idea was to take the affordable and expensive 
        lunch price from the same card or not so in this exercise I created two 
        instances of the card because of the uncertainty and in the next exercise I 
        used the same card to show that I also know how to do it like that.
        """

        kortti1 = Maksukortti(300)

        self.assertTrue(self.kassa.syo_edullisesti_kortilla(kortti1), True)
        self.assertEqual(kortti1.saldo_euroina(), 0.60)
        self.assertEqual(self.kassa.edulliset, 1) 

        kortti2 = Maksukortti(500)

        self.assertTrue(self.kassa.syo_maukkaasti_kortilla(kortti2), True)
        self.assertEqual(kortti2.saldo_euroina(), 1.0)
        self.assertEqual(self.kassa.maukkaat, 1) 
    
    def test_osto_kortilta_ei_riittävällä_määrällä_rahaa(self):

        kortti = Maksukortti(200)

        self.assertFalse(self.kassa.syo_edullisesti_kortilla(kortti), False)
        self.assertEqual(kortti.saldo_euroina(), 2.00)
        self.assertEqual(self.kassa.edulliset, 0) 
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

        self.assertFalse(self.kassa.syo_maukkaasti_kortilla(kortti), False)
        self.assertEqual(kortti.saldo_euroina(), 2.00)
        self.assertEqual(self.kassa.maukkaat, 0) 
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
    
    def test_lataa_positiivinen_rahaa_kortille(self):

        kortti = Maksukortti(10000)

        kassan_saldo = self.kassa.lataa_rahaa_kortille(kortti, 5000)
        self.assertEqual(self.kassa.kassassa_rahaa, 105000)
    
    def test_lataa_negatiivinen_maara_rahaa_kortille(self):

        kortti = Maksukortti(10000)

        kassan_saldo = self.kassa.lataa_rahaa_kortille(kortti, -5000)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
    
    def test_kassan_rahat_euroina(self):

        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1000)




        

    
        

