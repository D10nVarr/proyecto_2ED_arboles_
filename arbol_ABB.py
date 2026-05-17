class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq=None
        self.der=None

class ArbolABB:
    def __init__(self):
        self.raiz=None

    def agregar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._agregar(valor, self.raiz)

    def _agregar(self, valor, nodo):
        if valor < nodo.valor:
            if nodo.izq is None:
                nodo.izq = Nodo(valor)
            else:
                self._agregar(valor, nodo.izq)
        else:
            if nodo.der is None:
                nodo.der = Nodo(valor)
            else:
                self._agregar(valor, nodo.der)

    def preorden(self):
        self._preorden(self.raiz)

    def _preorden(self, nodo):
        if nodo:
            print(nodo.valor, end=" ")
            self._preorden(nodo.izq)
            self._preorden(nodo.der)

    def inorden(self):
        self._inorden(self.raiz)

    def _inorden(self, nodo):
        if nodo:
            self._inorden(nodo.izq)
            print(nodo.valor, end=" ")
            self._inorden(nodo.der)

    def postorden(self):
        self._postorden(self.raiz)

    def _postorden(self, nodo):
        if nodo:
            self._postorden(nodo.izq)
            self._postorden(nodo.der)
            print(nodo.valor, end=" ")

    def eliminar(self, valor):
        self.raiz = self._eliminar(self.raiz, valor)

    def _eliminar(self, nodo, valor):
        if nodo is None:
            return nodo

        # Buscar el nodo
        if valor < nodo.valor:
            nodo.izq = self._eliminar(nodo.izq, valor)
        elif valor > nodo.valor:
            nodo.der = self._eliminar(nodo.der, valor)
        else:
            # CASO 1: sin hijos
            if nodo.izq is None and nodo.der is None:
                return None
            # CASO 2: un hijo
            elif nodo.izq is None:
                return nodo.der
            elif nodo.der is None:
                return nodo.izq
            # CASO 3: dos hijos
            else:
                sucesor = self._minimo(nodo.der)
                nodo.valor = sucesor.valor
                nodo.der = self._eliminar(nodo.der, sucesor.valor)
        return nodo

    def _minimo(self, nodo):
        while nodo.izq is not None:
            nodo = nodo.izq
        return nodo

    def buscar(self, valor):
        self._buscar(valor, self.raiz, None)

    def _buscar(self, valor, nodo, padre):
        if nodo is None:
            print(f"\n El nodo {valor} no existe en el árbol.")
            return

        if valor < nodo.valor:
            self._buscar(valor, nodo.izq, nodo)

        elif valor > nodo.valor:
            self._buscar(valor, nodo.der, nodo)

        else:
            print(f"\nEl nodo {valor} si existe en el árbol.")

            if padre is None:
                print(" - Es la raíz principal, no tiene posee raíz.")
            else:
                print(f" - Su raíz es {padre.valor}")

            altura = self._calcular_altura(nodo)
            print(f"- Altura: {altura}")

            hijos = []
            if nodo.izq is not None:
                hijos.append(f"{nodo.izq.valor} (izq)")
            if nodo.der is not None:
                hijos.append(f"{nodo.der.valor} (der)")

            if len(hijos) > 0:
                print(f"- Sus hijos son: ({', '.join(hijos)}).")
            else:
                print("- No tiene hijos.")

    def _calcular_altura(self, nodo):
        if nodo is None:
            return -1
        return 1 + max(self._calcular_altura(nodo.izq), self._calcular_altura(nodo.der))

    def editar(self, valor_viejo):
        existe = self._buscar_solo_existencia(self.raiz, valor_viejo)

        if existe:
            nuevo_valor = int(input(f"Ingrese el nuevo valor del nodo {valor_viejo}: "))
            self.eliminar(valor_viejo)
            self.agregar(nuevo_valor)
            print(f"Nodo {valor_viejo} ahora es {nuevo_valor} ")
        else:
            print(f"El nodo {valor_viejo} no se existe en el árbol.")

    def _buscar_solo_existencia(self, nodo, valor):
        if nodo is None: return False
        if valor == nodo.valor: return True
        if valor < nodo.valor: return self._buscar_solo_existencia(nodo.izq, valor)
        return self._buscar_solo_existencia(nodo.der, valor)