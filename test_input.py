import unittest

class WriteInput(): 
  def __init__(self, inputs):
     self.count = 0
     self.inputs = inputs

  def __call__(self, *args, **kwds):
    value = self.inputs[self.count]
    self.count += 1
    return value

class GetOutput():
  def __init__(self, *args, **kwds):
     self.values = list(args)

  def __call__(self, *args, **kwds):
    value = " ".join(map(str,args))
    self.values.append(args)

def run_code(inputs):
    with open("Trabalho 2 - ILP.py") as file:
        code = compile(file.read(), "Trabalho 2 - ILP.py", "exec")
        mock_print = GetOutput()
        exec(code, {"input":WriteInput(inputs), "print": mock_print})

    return mock_print.values[14:]
        
class TestSum(unittest.TestCase):
    def test_funcao1(self):
        """
        Esse teste deve verificar se a saída da função 1 está compativel com esses resultados
        """
        funcao = [1, "n"]
        result = run_code(funcao)
        self.assertEqual(result[0], ('Adson', '-', '008', '-', 4))
        self.assertEqual(result[1], ('Cassio', '-', '001', '-', 6))
        self.assertEqual(result[2], ('Fabian', '-', '004', '-', 7))
        self.assertEqual(result[3], ('Fabio', '-', '009', '-', 1))
        self.assertEqual(result[4], ('Fagner', '-', '006', '-', 7))
        self.assertEqual(result[5], ('Fausto', '-', '010', '-', 0))
        self.assertEqual(result[6], ('Gil', '-', '005', '-', 7))
        self.assertEqual(result[7], ('Renato', '-', '007', '-', 5))
        self.assertEqual(result[8], ('Roger', '-', '002', '-', 6))
        self.assertEqual(result[9], ('Yuri', '-', '003', '-', 6))

    def test_funcao2(self):
        """
        Esse teste deve verificar se a saída da função 2 está compativel com esses resultados
        """
        funcao = [2, "n"]
        result = run_code(funcao)
        self.assertEqual(result[0], ('Fausto', '-', '010' ,'-', 0))
        self.assertEqual(result[1], ('Fabio', '-', '009', '-', 1))
        self.assertEqual(result[2], ('Adson', '-', '008', '-', 4))
        self.assertEqual(result[3], ('Renato', '-', '007', '-', 5))
        self.assertEqual(result[4], ('Cassio', '-', '001', '-', 6))
        self.assertEqual(result[5], ('Roger', '-', '002', '-', 6))
        self.assertEqual(result[6], ('Yuri', '-', '003', '-', 6))
        self.assertEqual(result[7], ('Fabian', '-', '004', '-', 7))
        self.assertEqual(result[8], ('Fagner', '-', '006', '-', 7))
        self.assertEqual(result[9], ('Gil', '-', '005', '-', 7))
   
    def test_funcao3(self):
        """
        Esse teste deve verificar cada entrada da funcao 3
        """
        funcao = [3, "n"]
        result = run_code(funcao)
        self.assertEqual(result[0], ('Fabian', '-', '004', '-', 7))
        self.assertEqual(result[1], ('Fagner', '-', '006', '-', 7))
        self.assertEqual(result[2], ('Gil', '-', '005', '-', 7))

    def test_funcao4(self):
        """
        Esse teste deve verificar cada entrada da funcao 4
        """
        funcao = [4, "n"]
        result = run_code(funcao)
        self.assertEqual(result[0], ('Fausto', '-', '010' ,'-', 0))
        self.assertEqual(result[1], ('Fabio', '-', '009', '-', 1))
        self.assertEqual(result[2], ('Adson', '-', '008', '-', 4))
        self.assertEqual(result[3], ('Renato', '-', '007', '-', 5))
        self.assertEqual(result[4], ('Cassio', '-', '001', '-', 6))
        self.assertEqual(result[5], ('Roger', '-', '002', '-', 6))
        self.assertEqual(result[6], ('Yuri', '-', '003', '-', 6))

    def test_funcao5(self):
        """
        Esse teste deve verificar cada entrada da funcao 5
        """
        funcao = [5, "n"]
        result = run_code(funcao)
        self.assertEqual(result[0], ('O percentual de aprovados Ã© de: 30.0', '%.'))

    def test_funcao6(self):
        """
        Esse teste deve verificar cada entrada da funcao 6
        """
        funcao = [6, "n"]
        result = run_code(funcao)
        self.assertEqual(result[0], ('6 e 7'))

    def test_funcao7(self):
        """
        Esse teste deve verificar cada entrada da funcao 7
        """
        funcao = [7, "n"]
        result = run_code(funcao)
        self.assertEqual(result[0], ('Fabian', '-', '004', '-', 7))
        self.assertEqual(result[1], ('Fagner', '-', '006', '-', 7))
        self.assertEqual(result[2], ('Gil', '-', '005', '-', 7))

    def test_funcao8(self):
        """
        Esse teste deve verificar cada entrada da funcao 8
        """
        funcao = [8, "n"]
        result = run_code(funcao)
        self.assertEqual(result[0], ('Fausto', '-', '010' ,'-', 0))
    
    def test_funcao9(self):
        """
        Esse teste deve verificar cada entrada da funcao 9
        """
        funcao = [9, "n"]
        result = run_code(funcao)
        self.assertEqual(result[0], ('A mÃ©dia da turma Ã©: 4.9',))

    def test_funcao0(self):
        """
        Esse teste deve verificar se caso entre 0 como parametro o codigo não quebre
        """
        funcao = [0]
        result = run_code(funcao)
        self.assertEqual(result[0], ('Esse número não é válido'))  

    def test_funcaoNegativa(self):
        """
        Esse teste deve verificar se caso entre um numero negativo como parametro o codigo não quebre
        """
        funcao = [-1]
        result = run_code(funcao)
        self.assertEqual(result[0], ('Esse número não é válido'))   

    def test_funcaoLetra(self):
        """
        Esse teste deve verificar se caso entre uma letra como primeiro parametro o codigo não quebre
        """
        funcao = ["a"]
        result = run_code(funcao)
        self.assertEqual(result[0], ('Esse número não é válido',))    

if __name__ == '__main__':
    unittest.main()
