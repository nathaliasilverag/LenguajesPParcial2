/* Nathalia Silvera 12-10921 
   Implementacion de Church Numeral con Swift
   Con las operaciones aritmeticas suma y multiplicacion
*/

/* Funcion para calcular los sucesores de los numeros
   Se utiliza la palabra reservada del lenguaje scaping, para "salvar"
   el valor del sucesor despues de ser aplicada la funcion, y de esta manera
   se pueda aplicar nuevamente y calcular el siguiente numero, sin necesidad de 
   usar una variable o un arreglo apra guardar dicho valor*/
/* Declaraion de la funcion tiene tres argumentos 
   genericos y un solo argumento formal como parametro de entrada */
/* El para no es etquetado */

func succ<A, B, C>(_ n: @escaping (@escaping (A) -> B) -> (C) -> A) -> (@escaping (A) -> B) -> (C) -> B {
  return {f in
    return {x in
      return f(n(f)(x))
    }
  }
}
 
/* Funcion donde se calcula el numero cero
   se definen dos argumentos genericos,
   y un argumento formal no etiquetado
   retorna el numero cero */
func zero<A, B>(_ a: A) -> (B) -> B {
  return {b in
    return b
  }
}

/* Funcion donde se calcula el numero 2,
   se definen un argumento generico,
   y un argumento formal no etiquetado
   retorna el numero 2
*/

func two<A>(_ f: @escaping (A) -> A) -> (A) -> A {
  return {x in
    return succ(succ(zero))(f)(x)
  }
}
 
/* Funcion donde se calcula el numero 3,
   se definen un argumento generico,
   y un argumento formal no etiquetado
   retorna el numero 3
*/
func three<A>(_ f: @escaping (A) -> A) -> (A) -> A {
  return {x in
    return succ(succ(succ(zero)))(f)(x)
  }
}
/* Funcion donde se calcula el numero 4,
   se definen un argumento generico,
   y un argumento formal no etiquetado
   retorna el numero 4
*/
func four<A>(_ f: @escaping (A) -> A) -> (A) -> A {
  return {x in
    return succ(succ(succ(succ(zero))))(f)(x)
  }
}
/* Funcion donde se calcula el numero 5,
   se definen un argumento generico,
   y un argumento formal no etiquetado
   retorna el numero 5
*/
func five<A>(_ f: @escaping (A) -> A) -> (A) -> A {
  return {x in
    return succ(succ(succ(succ(succ(zero)))))(f)(x)
  }
}
/* Funcion donde se calcula el numero 6,
   se definen un argumento generico,
   y un argumento formal no etiquetado
   retorna el numero 6
*/
func six<A>(_ f: @escaping (A) -> A) -> (A) -> A {
  return {x in
    return succ(succ(succ(succ(succ(succ(zero))))))(f)(x)
  }
}

/* Funcion para sumar dos Church numerals
   recibe tres argumentos genericos,
   y un solo argumento formal como entrada de la funcion
   recibe un parametro sin etiquetas, 
*/
func add<A, B, C>(_ m: @escaping (B) -> (A) -> C) -> (@escaping (B) -> (C) -> A) -> (B) -> (C) -> C {
  return {n in
    return {f in
      return {x in
        return m(f)(n(f)(x))
      }
    }
  }
}

/* Funcion para multiplicar dos Church numerals
   recibe tres argumentos genericos,
   y un solo argumento formal como entrada de la funcion
   recibe un parametro sin etiquetas, 
*/
func mult<A, B, C>(_ m: @escaping (A) -> B) -> (@escaping (C) -> A) -> (C) -> B {
  return {n in
    return {f in
      return m(n(f))
    }
  }
}
 
/* Funcion que retorna la codificacion, de church para 
   cualquier numero entero
*/
func church<A>(_ x: Int) -> (@escaping (A) -> A) -> (A) -> A {
  guard x != 0 else { return zero }
 
  return {f in
    return {a in
      return f(church(x - 1)(f)(a))
    }
  }
}

/* Funcion que retorna la resolucion entera de un
   church enconding.
   Es una funcion para retornar el numero entero que 
   resulta de las operaciones de church numerals
*/
func unchurch<A>(_ f: (@escaping (Int) -> Int) -> (Int) -> A) -> A {
  return f({i in
    return i + 1
  })(0)
}


let UNchurch = unchurch(church(8))
let a = unchurch(add(three)(four))
let b = unchurch(add(two)(six))
let c = unchurch(mult(five)(three))
let d = unchurch(mult(three)(four))

print("Operacion unchurch(church(0))), retorna ", UNchurch)
print("Suma de 3 y 4  unchurch(add(three)(four)) ", a)
print("Suma de 2 y 6 unchurch(add(two)(six))", b)
print("Multiplicacion de 5 y 3 unchurch(mult(five)(three))", c)
print("Multiplicacion de 3 y 4 unchurch(mult(three)(four))", d)