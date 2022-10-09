# Sistema de calculo do desconto com os ultimos 2 anos de INSS
class Calculadora:
    def __init__(self) -> None:
        self.__ano               = 0
        self.__desconto_total    = 0
        self.__primeiro_desconto = 0
        self.__segundo_desconto  = 0
        self.__terceiro_desconto = 0
        self.__quarto_desconto   = 0
        self.__salario_bruto     = 0

    # Calculo do Desconto do INSS de 2022
    def calcularDesconto2022(self, salario):

        if (salario <= 1212):
            self.__desconto_total = salario * 0.075
            self.__primeiro_desconto = self.__desconto_total

            return self.__desconto_total

        elif (salario <= 2427.35):
            self.__desconto_total = self.calcularDesconto2022(1212) + (salario - 1212) * 0.09
            self.__segundo_desconto = self.__desconto_total - self.__primeiro_desconto

            return self.__desconto_total

        elif (salario <= 3641.03):
            self.__desconto_total = self.calcularDesconto2022(2427.35) + (salario - 2427.35) * 0.12
            self.__terceiro_desconto = self.__desconto_total - self.__primeiro_desconto - self.__segundo_desconto

            return self.__desconto_total

        elif (salario <= 7087.22):
            self.__desconto_total = self.calcularDesconto2022(3641.03) + (salario - 3641.03) * 0.14
            self.__quarto_desconto = self.__desconto_total - self.__primeiro_desconto - self.__segundo_desconto - self.__terceiro_desconto

            return self.__desconto_total

        elif (salario > 7087.22):
            self.__desconto_total = self.calcularDesconto2022(7087.22)
            return self.__desconto_total

    #Calculo do Desconto do INSS de 2021
    def calcularDesconto2021(self, salario):

        if (salario <= 1100):
            self.__desconto_total = salario * 0.075
            self.__primeiro_desconto = self.__desconto_total

            return self.__desconto_total

        elif (salario <= 2203.48):
            self.__desconto_total = self.calcularDesconto2021(1100) + (salario - 1100) * 0.09
            self.__segundo_desconto = self.__desconto_total - self.__primeiro_desconto

            return self.__desconto_total

        elif (salario <= 3305.22):
            self.__desconto_total = self.calcularDesconto2021(2203.48) + (salario - 2203.48) * 0.12
            self.__terceiro_desconto = self.__desconto_total - self.__primeiro_desconto - self.__segundo_desconto

            return self.__desconto_total

        elif (salario <= 6433.57):
            self.__desconto_total = self.calcularDesconto2021(3305.22) + (salario - 3305.22) * 0.14
            self.__quarto_desconto = self.__desconto_total - self.__primeiro_desconto - self.__segundo_desconto - self.__terceiro_desconto

            return self.__desconto_total

        elif (salario > 6433.57):
            self.__desconto_total = self.calcularDesconto2022(6433.57)

            return self.__desconto_total

    # Calculo da Aliquota Efetiva, usei como base alguns sites que calculam o desconto do INSS
    # A Aliquota efetiva é sobre o desconto final e o bruto inicial
    def getAliquotaEfetiva(self, desconto_total, salario):
        return desconto_total * 100 / salario

    # No final, inserindo um número válido, irá imprimir o seu desconto total.
    # Também irá imprimir a sua porcentagem da aliquota e as respectivas faixas de acordo com o salário

    def desctotal(self, salario):
        while (self.ano == 2021):

            if (self.salario_bruto <= 1100):
                desctotal = self.__desconto_total = self.calcularDesconto2021(salario)
                return desctotal

        while (self.ano == 2022):
            if (self.salario_bruto <= 1212):
                desctotal = self.__desconto_total = self.calcularDesconto2021(salario)
                return desctotal

    def pridesc(self):
        while (self.ano == 2021):

            if(self.salario_bruto <= 1100):
                pridesc = self.__primeiro_desconto = self.calcularDesconto2021(1100)
                return pridesc

        while (self.ano == 2022):
            if (self.salario_bruto <= 1212):
                pridesc = self.__primeiro_desconto = self.calcularDesconto2021(1212)
                return pridesc

    def segdesc(self):
        while (self.ano == 2021):

            if (self.salario_bruto <= 2203.48):
                segdesc = self.__segundo_desconto = self.calcularDesconto2021(2203.48)
                return segdesc

        while (self.ano == 2022):
            if (self.salario_bruto <= 2427.35):
                segdesc = self.__segundo_desconto = self.calcularDesconto2021(2427.35)
                return segdesc

    def tridesc(self):
        while (self.ano == 2021):

            if (self.salario_bruto <= 3305.22):
                tridesc = self.__terceiro_desconto = self.calcularDesconto2021(3305.22)
                return tridesc

        while (self.ano == 2022):
            if (self.salario_bruto <= 3641.03):
                tridesc = self.__terceiro_desconto = self.calcularDesconto2021(3641.03)
                return tridesc

    def quadesc(self):
        while (self.ano == 2021):

            if (self.salario_bruto <= 6433.57):
                quadesc = self.__quarto_desconto = self.calcularDesconto2021(6433.57)
                return quadesc

        while (self.ano == 2022):
            if (self.salario_bruto <= 7087.22):
                quadesc = self.__quarto_desconto = self.calcularDesconto2021(7087.22)
                return quadesc

    def aliq(self, salario, desctotal):
        while (self.ano == 2021):
            if (self.salario_bruto <= 6433.57):
                aliq = self.getAliquotaEfetiva(desctotal, salario)
                return aliq

        while (self.ano == 2022):
            if (self.salario_bruto <= 7087.22):
                aliq = self.getAliquotaEfetiva(desctotal, salario)
                return aliq


    # Validação de Float(impede que a pessoa coloque letras ou valores invalidos)
    def is_float(self, salario):
        try:
            salario = float(salario)
            return salario

        except ValueError:
            return 0

    # A função principal na qual irá calcular o seu seu desconto
    def calcular(self, salario, ano):

        self.salario_bruto = salario
        self.ano = ano

        if(self.ano == 2021):
            return self.calcularDesconto2021(self.salario_bruto)
            #aliquota = self.getAliquotaEfetiva(self.__desconto_total, self.salario_bruto)

            #self.imprimeResultado(aliquota)

        elif(self.ano == 2022):
            return self.calcularDesconto2022(self.salario_bruto)
            #aliquota = self.getAliquotaEfetiva(self.__desconto_total, self.salario_bruto)

            #self.imprimeResultado(aliquota)

        return 0


# if (__name__ == "__main__"):
#     calculadora = Calculadora()
#     calculadora.calcular()
