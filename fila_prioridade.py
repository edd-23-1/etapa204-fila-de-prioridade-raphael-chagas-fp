# -*- coding:UTF-8 -*-
from no import No

class FilaPrioridade:
    """
    Implementação de Fila de Prioridade com Capacidade
    A fila de prioridade a ser implementada deverá ser em ordem crescente
    Os itens com maior prioridade devem ocupar as primeiras posições
    Itens com prioridades iguais devem ser ordenados conforme ordem de inserção
    """

    def __init__(self, capacidade=5):
        self.__inicio = None
        self.__capacidade = capacidade
        self.__qtdItens = 0
        print(f"Criada EDD Fila de Prioridade com capacidade: {capacidade}")


    # Retorna True se a fila de prioridade está vazia, False caso contrário
    def is_empty(self) -> bool:
        # implementação do método
        return self.__qtdItens == 0

    
    # retorna True se a fila de prioridade está cheia, False caso contrário
    def is_full(self) -> bool:
        # implementação do método
        return self.__qtdItens >= self.__capacidade


    # Retorna uma referência para o primeiro item da fila de prioridade
    # Caso a lista esteja vazia, retorna None
    def first(self) -> No:
        # implementação do método
        return self.__inicio


    # insere um item na fila de prioridade e retorna True, se o item for inserido
    # se a fila de prioridade estiver cheia, lança uma exceção: raise Exception("mensagem de erro")
    def add(self, valor, prioridade) -> bool:
        # implementação do método
        no = No(valor, prioridade)
        if self.is_full():
            raise Exception("Erro!")
        if self.is_empty():
            self.__inicio = no
        elif no.prioridade>self.__inicio.prioridade:
            no.prox = self.__inicio
            self.__inicio = no
        else:
            iterar = self.__inicio
            while iterar.prox is not None and no.prioridade <= iterar.prox.prioridade:
                iterar = iterar.prox
            no.prox = iterar.prox
            iterar.prox = no
        self.__qtdItens += 1
        return True
        

    
    # remove o primeiro item da fila de prioridade, caso não esteja vazia, e retorna o Nó
    # se a fila de prioridade estiver vazia, lança uma exceção: raise Exception("mensagem de erro")
    def remove(self) -> No:
        # implementação do método
        if self.is_empty():
            raise Exception("Erro!")
        else:
            iterar = self.__inicio
            self.__inicio = self.__inicio.prox
            self.__qtdItens -= 1
            return iterar


    # retorna uma lista de tuplas com os itens (valor e prioridade) da fila de prioridade 
    # imprime os itens da fila de prioridade do primeiro para o último
    # caso a fila de prioridade esteja vazia, imprime uma mensagem informando
    # que a fila de prioridade está vazia e retorna uma lista vazia
    def display(self) -> list[tuple()]:
        if self.is_empty():
            raise Exception("Erro!")
        list = []
        iterar = self.__inicio
        while iterar is not None:
            list.append((iterar.dado, iterar.prioridade))
            iterar = iterar.prox
        return list

    # retorna a quantidade de elementos na fila de prioridade
    # se a fila de prioridade estiver vazia, retorna ZERO
    def size(self) -> int:
        return self.__qtdItens
