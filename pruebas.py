import unittest
import numcomplejos


class OpComplejosTestCase(unittest.TestCase):

    def test_suma(self):
        result=numcomplejos.suma((5,1),(4,3))
        self.assertEqual(result,'9+4i')

    def test_resta(self):
        result=numcomplejos.resta((5,1),(4,3))
        self.assertEqual(result,'1-2i')

    def test_multiplica(self):
        result=numcomplejos.mult((5,1),(4,3))
        self.assertEqual(result,'17+19i')

    def test_division(self):
        result=numcomplejos.div((5,1),(4,3))
        self.assertEqual(result,'23-11i/25')

    def test_modulo(self):
        result=numcomplejos.modulo((5,1))
        self.assertEqual(result,5.099)

    def test_conjugado(self):
        result=numcomplejos.conj((5,1))
        self.assertEqual(result,'5-1i')

    def test_polar(self):
        result=numcomplejos.polar((5,1))
        self.assertEqual(result,(5.099,0.197))

    def test_cartesiano(self):
        result=numcomplejos.cart((5,1))
        self.assertEqual(result,'2.702+4.207i')

    def test_suma_matrices(self):
        result=numcomplejos.sumatrices([[('1', '2'), ('3', '4')], [('5', '6'), ('7', '8')]],[[('9', '10'), ('11', '12')], [('13', '14'), ('15', '16')]])
        self.assertEqual(result,[['10+12i', '14+16i'], ['18+20i', '22+24i']])

    def test_inversa_matrices(self):
        result=numcomplejos.matrinv([[('1', '2'), ('3', '4')], [('5', '6'), ('7', '8')]])
        self.assertEqual(result,[['-1-2i', '-3-4i'], ['-5-6i', '-7-8i']])

    def test_multiplica_escalar(self):
        result=numcomplejos.escalar((5,1),[[('1', '2'), ('3', '4')], [('5', '6'), ('7', '8')]])
        self.assertEqual(result,[['3+11i', '11+23i'], ['19+35i', '27+47i']])

    def test_matriz_transpuesta(self):
        result=numcomplejos.transpuesta([[('1', '2'), ('3', '4')], [('5', '6'), ('7', '8')]],(2,2))
        self.assertEqual(result,[['1+2i', '5+6i'], ['3+4i', '7+8i']])

    def test_matriz_conjugada(self):
        result=numcomplejos.matrizconj([[('1', '2'), ('3', '4')], [('5', '6'), ('7', '8')]])
        self.assertEqual(result,[['1-2i', '3-4i'], ['5-6i', '7-8i']])

    def test_matriz_adjunta(self):
        result=numcomplejos.adjmatriz([[('1', '2'), ('3', '4')], [('5', '6'), ('7', '8')]],(2,2))
        self.assertEqual(result,[['1-2i', '5-6i'], ['3-4i', '7-8i']])

    def test_2matriz_adjunta(self):
        result=numcomplejos.adjmatriz([[('9', '10'), ('11', '12')], [('13', '14'), ('15', '16')]],(2,2))
        self.assertEqual(result,[['9-10i', '13-14i'], ['11-12i', '15-16i']])

    def test_normatriz(self):
        result=numcomplejos.normatriz([[('9', '10'), ('11', '12')], [('13', '14'), ('15', '16')]],(2,2))
        self.assertEqual(result,'(-100+1288i)**(1/2)')

    def test_distancia(self):
        result=numcomplejos.dismat([[('1', '2'), ('3', '4')], [('5', '6'), ('7', '8')]],[[('9', '10'), ('11', '12')], [('13', '14'), ('15', '16')]],(2,2))
        self.assertEqual(result,'-68+480i')

    def test_unitaria(self):
        result=numcomplejos.matrizconj([[('1', '2'), ('3', '4')], [('5', '6'), ('7', '8')]])
        self.assertEqual(result,[['1-2i', '3-4i'], ['5-6i', '7-8i']])

    def test_hermitian(self):
        result=numcomplejos.hermitian([[('1', '2'), ('3', '4')], [('5', '6'), ('7', '8')]],(2,2))
        self.assertEqual(result,False)

    def test_tensor(self):
        result=numcomplejos.tensor([[('1', '2'), ('3', '4')], [('5', '6'), ('7', '8')]],[[('9', '10'), ('11', '12')], [('13', '14'), ('15', '16')]])
        self.assertEqual(result,[['-11+28i', '-13+34i', '-13+66i', '-15+80i'], ['-15+40i', '-17+46i', '-17+94i', '-19+108i'], ['-15+104i', '-17+126i', '-17+142i', '-19+172i'], ['-19+148i', '-21+170i', '-21+202i', '-23+232i']])



if __name__ == "__main__":
    unittest.main()
