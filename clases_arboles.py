class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None
        self.altura = 1


class ArbolABB:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar(valor, self.raiz)

    def _insertar(self, valor, nodo):
        if valor < nodo.valor:
            if nodo.izq is None:
                nodo.izq = Nodo(valor)
            else:
                self._insertar(valor, nodo.izq)
        elif valor > nodo.valor:  # Evita duplicados
            if nodo.der is None:
                nodo.der = Nodo(valor)
            else:
                self._insertar(valor, nodo.der)

    def eliminar(self, valor):
        self.raiz = self._eliminar(self.raiz, valor)

    def _eliminar(self, nodo, valor):
        if nodo is None:
            return nodo
        if valor < nodo.valor:
            nodo.izq = self._eliminar(nodo.izq, valor)
        elif valor > nodo.valor:
            nodo.der = self._eliminar(nodo.der, valor)
        else:
            if nodo.izq is None:
                return nodo.der
            elif nodo.der is None:
                return nodo.izq

            sucesor = self._minimo(nodo.der)
            nodo.valor = sucesor.valor
            nodo.der = self._eliminar(nodo.der, sucesor.valor)
        return nodo

    def _minimo(self, nodo):
        while nodo.izq is not None:
            nodo = nodo.izq
        return nodo


    def buscar(self, valor):
        camino = []
        encontrado = self._buscar(valor, self.raiz, camino)
        return encontrado, camino

    def _buscar(self, valor, nodo, camino):
        if nodo is None:
            return False
        camino.append(nodo.valor)
        if valor == nodo.valor:
            return True
        if valor < nodo.valor:
            return self._buscar(valor, nodo.izq, camino)
        return self._buscar(valor, nodo.der, camino)

    def preorden(self):
        resultado = []
        self._preorden(self.raiz, resultado)
        return resultado

    def _preorden(self, nodo, resultado):
        if nodo:
            resultado.append(nodo.valor)
            self._preorden(nodo.izq, resultado)
            self._preorden(nodo.der, resultado)

    def inorden(self):
        resultado = []
        self._inorden(self.raiz, resultado)
        return resultado

    def _inorden(self, nodo, resultado):
        if nodo:
            self._inorden(nodo.izq, resultado)
            resultado.append(nodo.valor)
            self._inorden(nodo.der, resultado)

    def postorden(self):
        resultado = []
        self._postorden(self.raiz, resultado)
        return resultado

    def _postorden(self, nodo, resultado):
        if nodo:
            self._postorden(nodo.izq, resultado)
            self._postorden(nodo.der, resultado)
            resultado.append(nodo.valor)


    def obtener_altura(self):
        return self._calcular_altura(self.raiz)

    def _calcular_altura(self, nodo):
        if nodo is None:
            return 0
        return 1 + max(self._calcular_altura(nodo.izq), self._calcular_altura(nodo.der))

    def contar_nodos(self):
        return self._contar(self.raiz)

    def _contar(self, nodo):
        if nodo is None:
            return 0
        return 1 + self._contar(nodo.izq) + self._contar(nodo.der)


class ArbolAVL(ArbolABB):
    def __init__(self):
        super().__init__()

    def altura_nodo(self, nodo):
        if nodo is None:
            return 0
        return nodo.altura

    def balance(self, nodo):
        if nodo is None:
            return 0
        return self.altura_nodo(nodo.izq) - self.altura_nodo(nodo.der)

    def insertar(self, valor):
        self.raiz = self._insertar_avl(self.raiz, valor)

    def _insertar_avl(self, nodo, valor):
        if nodo is None:
            return Nodo(valor)

        if valor < nodo.valor:
            nodo.izq = self._insertar_avl(nodo.izq, valor)
        elif valor > nodo.valor:
            nodo.der = self._insertar_avl(nodo.der, valor)
        else:
            return nodo

        #Actualizar altura
        nodo.altura = 1 + max(self.altura_nodo(nodo.izq), self.altura_nodo(nodo.der))

        #Numero de balance
        b = self.balance(nodo)

        #Rotaciones
        #Izquierda-Izquierda
        if b > 1 and valor < nodo.izq.valor:
            return self.rotar_derecha(nodo)
        #Derecha-Derecha
        if b < -1 and valor > nodo.der.valor:
            return self.rotar_izquierda(nodo)
        #Izquierda-Derecha
        if b > 1 and valor > nodo.izq.valor:
            nodo.izq = self.rotar_izquierda(nodo.izq)
            return self.rotar_derecha(nodo)
        # Derecha-Izquierda
        if b < -1 and valor < nodo.der.valor:
            nodo.der = self.rotar_derecha(nodo.der)
            return self.rotar_izquierda(nodo)

        return nodo

    def eliminar(self, valor):
        self.raiz = self._eliminar_avl(self.raiz, valor)

    def _eliminar_avl(self, nodo, valor):
        if nodo is None:
            return nodo

        if valor < nodo.valor:
            nodo.izq = self._eliminar_avl(nodo.izq, valor)
        elif valor > nodo.valor:
            nodo.der = self._eliminar_avl(nodo.der, valor)
        else:
            if nodo.izq is None:
                return nodo.der
            elif nodo.der is None:
                return nodo.izq
            temp = self._minimo(nodo.der)
            nodo.valor = temp.valor
            nodo.der = self._eliminar_avl(nodo.der, temp.valor)

        if nodo is None:
            return nodo

        # Balance
        nodo.altura = 1 + max(self.altura_nodo(nodo.izq), self.altura_nodo(nodo.der))
        b = self.balance(nodo)

        if b > 1 and self.balance(nodo.izq) >= 0:
            return self.rotar_derecha(nodo)
        if b > 1 and self.balance(nodo.izq) < 0:
            nodo.izq = self.rotar_izquierda(nodo.izq)
            return self.rotar_derecha(nodo)
        if b < -1 and self.balance(nodo.der) <= 0:
            return self.rotar_izquierda(nodo)
        if b < -1 and self.balance(nodo.der) > 0:
            nodo.der = self.rotar_derecha(nodo.der)
            return self.rotar_izquierda(nodo)

        return nodo

    def rotar_derecha(self, z):
        y = z.izq
        T3 = y.der

        y.der = z
        z.izq = T3

        z.altura = 1 + max(self.altura_nodo(z.izq), self.altura_nodo(z.der))
        y.altura = 1 + max(self.altura_nodo(y.izq), self.altura_nodo(y.der))
        return y

    def rotar_izquierda(self, z):
        y = z.der
        T3 = y.izq

        y.izq = z
        z.der = T3

        z.altura = 1 + max(self.altura_nodo(z.izq), self.altura_nodo(z.der))
        y.altura = 1 + max(self.altura_nodo(y.izq), self.altura_nodo(y.der))
        return y