#El ejercicio inicia con una clase llamada CuentaBancaria y luego se define una función llamada __init__.
#Cuando una función está dentro de una clase, esta pasa a llamarse método.
#El método __init__ es un método especial llamado constructor que se llama automáticamente cuando se crea una nueva función de una clase.
#Este método se utiliza para inicializar los atributos del objeto. Los atributos son las características o propiedades que tiene un objeto.
#En este caso, el método __init__ recibe tres parámetros: self, titular, saldo_inicial.
#El parámetro self es una referencia al objeto que se está creando y se utiliza para acceder a los atributos y métodos de la clase.


class CuentaBancaria:
    def __init__(self, titular: str, saldo_inicial: float = 0.0):
        if saldo_inicial < 0:
          raise ValueError("El saldo inicial no puede ser negativo")
        self.titular = titular
        self._saldo = float(saldo_inicial)
        self.historial: list[str] = []

#luego de iniciar el constructor __init_, se hace uso de un condicional if para verificar que el saldo inicial no sea negativo.
#Si el saldo inicial es negativo, se utiliza raise ValueError para lanzar una excepción con un mensaje de error.
#raise ValueError es una forma de indicar que ha ocurrido un error en el programa y que se debe manejar adecuadamente.
#Luego, se inicializan los atributos del objeto utilizando self. self.titular se asigna el valor titular (parametro)
#y self._saldo se asigna el valor saldo_inicial convertido a float. El _ antes del nombre del atributo _saldo indica que es 
#un encapsulamiento, es decir, que no debe ser accedido directamente desde fuera de la clase.
#Self.historial se inicializa como una lista vacía que almacenará el historial de transacciones tipo str.

    @property
    def saldo(self) -> float:
        return self._saldo

#La propiedad @property se utiliza para definir un método que se comporta como un atributo y permite acceder a los datos de manera segura.
#def saldo(self) -> float: define un método llamado saldo tipo float que devuelve el valor del atributo _saldo.
#en esta caso, _saldo esta asignado a saldo_inicial en el constructor __init__. y su valor es 0.0.

    def depositar(self, monto: float) -> None:
        if monto <= 0:
          raise ValueError("El depósito debe ser positivo")
        self._saldo += monto
        self.historial.append(f"Depósito de {monto}")

#Aqui se define un método llamado depositar que recibe un parámetro monto tipo float y no devuelve ningún valor (None).
#Siempre que se define un método, el primer parámetro debe ser self para referirse al objeto actual.
#Por obvias razones el monto debe ser mayor a 0, si no entonces da error.
#self._saldo += monto suma el monto que se deposita al saldo actual.

    def retirar(self, monto: float) -> None:
        if monto <= 0:
          raise ValueError("El retiro debe ser positivo")
        if monto > self._saldo:
          raise ValueError("Fondos insuficientes")
        self._saldo -= monto
        self.historial.append(f"Retiro de {monto}")

#Aqui es un poco de lo mismo se define un método llamado retirar que recibe un parámetro monto tipo float y no devuelve ningún valor (None).
#No puedes retirar menos de 0 y da eror.  En caso de que quieras retirar más de lo que tienes en la cuenta, también da error.
#self._saldo -= monto resta el dinero que se retira al saldo actual.
#luego se agrega una entrada al historial de transacciones indicando el retiro realizado.
#El .append() es un método de las listas en Python que se utiliza para agregar un elemento al final de la lista.
#la f en el string es para permitir varias variables dentro de un string. Otra forma de hacerlo es con el "+".

    def __repr__(self) -> str:
        return f"CuentaBancaria(titular='{self.titular}', saldo={self._saldo:.2f})"

#A diferencia del método __init__, el método __repr__ no es un constructor, sino un método especial que se utiliza para definir
#Sirve para decirle a Python cómo quieres que se muestre tu objeto cuando lo imprimes.
#luego retorna un string que representa el objeto CuentaBancaria, mostrando el titular y el saldo con dos decimales.
#Básicamente, imprime la clase CuentaBancaria con su titular y saldo.
#En este caso no se ha asignado ningún valor a nada asi que no se mostrará nada.

# Ejemplo de uso de la clase CuentaBancaria
try:
    cuenta1 = CuentaBancaria("Juan Gonzalez",500000)
    print(cuenta1)

    cuenta1.depositar(50000)
    print(cuenta1)

    cuenta1.retirar(450000)
    print(cuenta1)

    cuenta1.retirar(10000)
    print(cuenta1)

    cuenta1.depositar(50000)
    print(cuenta1)
    
# Para obetener error por retiro=   cuenta1.retirar(450000)
#   print(cuenta1)


    print("Historial de transacciones:")
    for transaccion in cuenta1.historial:
        print(transaccion)



except ValueError as e:
    print(f"Error: {e}")