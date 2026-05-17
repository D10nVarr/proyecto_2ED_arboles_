class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
        self.altura = 0


class ArbolAVL:
    def __init__(self):
        self.raiz = None

    def obtener_altura(self, nodo):
        if nodo is None:
            return -1  # hoja = 0
        return nodo.altura

    def insetar(self, valor):
        self.raiz = self._insertar(self.raiz, valor)

    def _insertar(self, nodo, valor):
        # insertar como ABB
        if nodo is None:
            return Nodo(valor)

        if valor < nodo.valor:
            nodo.izquierda = self._insertar(nodo.izquierda, valor)

        else:
            nodo.derecha = self._insertar(nodo.derecha, valor)

        # actualizar altura
        nodo.altura = 1 + max(self.obtener_altura(nodo.izquierda), self.obtener_altura(nodo.derecha))

        balance = self.obtener_altura(nodo.izquierda) - self.obtener_altura(nodo.derecha)
        print("Nodo; ", nodo.valor, "Balance: ", balance)

        if balance > 1:
            print("Desbalance hacia la izquierda en nodo", nodo.valor)
            if valor < nodo.izquierda.valor:
                print("Caso izquierda-izquierda")
                print("Rotación DERECHA")
                return self.rotar_derecha(nodo)
            else:
                print("Caso izquierda-derecha")
                print("Rotación DOBLE izquierda-derecha\n")
                nodo.izquierda = self.rotar_izquierda(nodo.izquierda)
                return self.rotar_derecha(nodo)

        elif balance < -1:
            print("Desbalance hacia la derecha en nodo", nodo.valor)
            if valor > nodo.derecha.valor:
                print("Caso derecha-derecha")
                print("Rotación derecha IZQUIERDA\n")
                return self.rotar_izquierda(nodo)

                # Caso Derecha-Izquierda
            else:
                print("Casa derecha-izquierda")
                print("Rotación DOBLE derecha-izquierda\n")
                nodo.derecha = self.rotar_derecha(nodo.derecha)
                return self.rotar_izquierda(nodo)

        else:
            print("Está balanceado\n")

        return nodo

    def eliminar(self, valor):
        self.raiz = self._eliminar(self.raiz, valor)

    def _eliminar(self, nodo, valor):
        if nodo is None:
            return nodo

        if valor < nodo.valor:
            nodo.izquierda = self._eliminar(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha = self._eliminar(nodo.derecha, valor)
        else:
            if nodo.izquierda is None:
                temporal = nodo.derecha
                nodo = None
                return temporal
            elif nodo.derecha is None:
                temporal = nodo.izquierda
                nodo = None
                return temporal

            actual = nodo.derecha
            while actual.izquierda is not None:
                actual = actual.izquierda
            temporal = actual

            nodo.valor = temporal.valor
            nodo.derecha = self._eliminar(nodo.derecha, temporal.valor)

        if nodo is None:
            return nodo

        nodo.altura = 1 + max(self.obtener_altura(nodo.izquierda), self.obtener_altura(nodo.derecha))
        balance = self.obtener_altura(nodo.izquierda) - self.obtener_altura(nodo.derecha)

        if balance > 1:
            balance_izq = self.obtener_altura(nodo.izquierda.izquierda) - self.obtener_altura(nodo.izquierda.derecha)
            if balance_izq >= 0:
                return self.rotar_derecha(nodo)
            else:
                nodo.izquierda = self.rotar_izquierda(nodo.izquierda)
                return self.rotar_derecha(nodo)

        if balance < -1:
            balance_der = self.obtener_altura(nodo.derecha.izquierda) - self.obtener_altura(nodo.derecha.derecha)
            if balance_der <= 0:
                return self.rotar_izquierda(nodo)
            else:
                nodo.derecha = self.rotar_derecha(nodo.derecha)
                return self.rotar_izquierda(nodo)

        return nodo

    def editar(self, valor_viejo, valor_nuevo):
        nodo_actual = self.raiz
        encontrado = False
        while nodo_actual is not None:
            if nodo_actual.valor == valor_viejo:
                encontrado = True
                break
            elif valor_viejo < nodo_actual.valor:
                nodo_actual = nodo_actual.izquierda
            else:
                nodo_actual = nodo_actual.derecha

        if encontrado:
            self.eliminar(valor_viejo)
            self.insetar(valor_nuevo)
        else:
            print("El valor no existe")

    def rotar_derecha(self, z):
        y = z.izquierda
        T3 = y.derecha

        y.derecha = z
        z.izquierda = T3

        z.altura = 1 + max(self.obtener_altura(z.izquierda), self.obtener_altura(z.derecha))
        y.altura = 1 + max(self.obtener_altura(y.izquierda), self.obtener_altura(y.derecha))
        return y

    def rotar_izquierda(self, z):
        y = z.derecha
        T2 = y.izquierda

        y.izquierda = z
        z.derecha = T2

        z.altura = 1 + max(self.obtener_altura(z.izquierda), self.obtener_altura(z.derecha))
        y.altura = 1 + max(self.obtener_altura(y.izquierda), self.obtener_altura(y.derecha))
        return y

    def mostrar(self, nodo, nivel=0):
        if nodo is not None:
            self.mostrar(nodo.derecha, nivel + 1)
            print("  " * nivel, str(nodo.valor))
            self.mostrar(nodo.izquierda, nivel + 1)


arbol = ArbolAVL()
arbol.insetar(6)
arbol.insetar(5)
arbol.insetar(4)

arbol.mostrar(arbol.raiz)