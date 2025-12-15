from abc import ABC, abstractmethod

class Veicolo(ABC):
    def __init__(self, id: str, tipo: str, horaEntrada: int):
        self.__id = id
        self.__tipo = tipo
        self.__horaEntrada = horaEntrada

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
        return f"{3:2f}"
    
class Moto(Veicolo):
    def __init__(self, id, tipo, horaEntrada):
        super().__init__(id, tipo, horaEntrada)

    def calcularValor(self, saida: int) -> float:
        valor = (saida - self.__horaEntrada) / 20
        return f"{valor:.2f}"
    
class Carro(Veicolo):
    def __init__(self, id, tipo, horaEntrada):
        super().__init__(id, tipo, horaEntrada)

    def calcularValor(self, saida: int) -> float:
        valor = (saida - self.__horaEntrada) / 10
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

    def procurar(self, id: str) -> Veicolo | None:
        for veicolo in self.__lista:
            if veicolo.__id == id:
                return veicolo
        return None
    
    def pagar(self, veicolo: Veicolo):
        entrada = veicolo.__horaEntrada
        saida = self.getHora()
        valor = veicolo.calcularValor(saida)
        return f"{veicolo.__tipo} chegou {entrada} saiu {saida}. Pagar R$ {valor}"

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
            if args[1] == "bike":
                bike = Bike(args[2],"Bike",estacionamento.getHora())
                estacionamento.estacionar(bike)
            elif args[1] == "moto":
                moto = Moto(args[2],"Moto",estacionamento.getHora())
                estacionamento.estacionar(moto)
            elif args[1] == "carro":
                carro = Carro(args[2],"Carro",estacionamento.getHora())
                estacionamento.estacionar(carro)
                
        elif args[0] == "pagar":
            id: str = args[1]
            veicolo = estacionamento.procurar(id)
            if veicolo:
                print(estacionamento.pagar(veicolo))
                estacionamento.__lista.remove(veicolo)
        else:
            print("fail: Comando nao encontrado")
main()