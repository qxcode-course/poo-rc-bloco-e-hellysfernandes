from abc import ABC, abstractmethod

class Veicolo(ABC):
    def __init__(self, id: str, tipo: str, horaEntrada: int):
        self.__id = id
        self.__tipo = tipo
        self.__horaEntrada = horaEntrada

    def getId(self) -> str:
        return self.__id
    
    def getHoraEntrada(self) -> int:
        return self.__horaEntrada
    
    def getTipo(self) -> str:
        return self.__tipo

    @abstractmethod
    def calcularValor(self, saida: int):
        pass
    
    def __str__(self) -> str:
        id = self.__id.rjust(10,"_")
        tipo = self.__tipo.rjust(10,"_")
        return f"{tipo} : {id} : {self.__horaEntrada}"

class Bike(Veicolo):
    def __init__(self, id, tipo, horaEntrada):
        super().__init__(id, tipo, horaEntrada)

    def calcularValor(self, saida: int = 0) -> float:
        return f"{3:.2f}"
    
class Moto(Veicolo):
    def __init__(self, id, tipo, horaEntrada):
        super().__init__(id, tipo, horaEntrada)

    def calcularValor(self, saida: int) -> float:
        valor = (saida - self.getHoraEntrada()) / 20
        return f"{valor:.2f}"
    
class Carro(Veicolo):
    def __init__(self, id, tipo, horaEntrada):
        super().__init__(id, tipo, horaEntrada)

    def calcularValor(self, saida: int) -> float:
        valor = (saida - self.getHoraEntrada()) / 10
        if valor > 5:
            return f"{valor:.2f}"
        else:
            return f"{5:.2f}"

class Estacionamento:
    def __init__(self):
        self.__lista: list[Veicolo] = []
        self.__horaAtual: int = 0

    def getHora(self) -> int:
        return self.__horaAtual
    
    def pasarTempo(self, tempo: int) -> None:
        self.__horaAtual += tempo
    
    def estacionar(self, veicolo: Veicolo) -> None:
        self.__lista.append(veicolo)

    def veicolos(self, tipo, id) -> str | None:
        if tipo == "bike":
            bike = Bike(id,"Bike",self.getHora())
            self.estacionar(bike)

        elif tipo == "moto":
            moto = Moto(id,"Moto",self.getHora())
            self.estacionar(moto)

        elif tipo == "carro":
            carro = Carro(id,"Carro",self.getHora())
            self.estacionar(carro)

        else:
            return "fail: veicolo incapas de estacionar"

    def procurar(self, id: str) -> Veicolo | None:
        for veicolo in self.__lista:
            if veicolo.getId() == id:
                return veicolo
        return None
    
    def remover(self, veicolo: Veicolo) -> None:
        self.__lista.remove(veicolo)
    
    def pagar(self, veicolo: Veicolo) -> str:
        entrada = veicolo.getHoraEntrada()
        saida = self.getHora()
        valor = veicolo.calcularValor(saida)
        return f"{veicolo.getTipo()} chegou {entrada} saiu {saida}. Pagar R$ {valor}"

    def __str__(self) -> str:
        lista = "\n".join([str(x) for x in self.__lista])
        if not lista:
            return f"Hora atual: {self.__horaAtual}"
        return f"{lista}\nHora atual: {self.__horaAtual}" 
    
def main():

    estacionamento = Estacionamento()

    while True:
        
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")

        if args[0] == "end":
            break

        elif args[0] == "show":
            print(estacionamento)

        elif args[0] == "tempo":
            estacionamento.pasarTempo(int(args[1]))

        elif args[0] == "estacionar":
            tipo: str = args[1]
            id: str = args[2]
            estacionamento.veicolos(tipo,id)
        
        elif args[0] == "pagar":
            id: str = args[1]
            veicolo = estacionamento.procurar(id)
            if veicolo:
                print(estacionamento.pagar(veicolo))
                estacionamento.remover(veicolo)

        else:
            print("fail: Comando nao encontrado")
main()