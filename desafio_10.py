# def area_rectangulo(base, altura):
#     return base * altura

# print(f"Area de rectangulo de 15 de base y 10 de altura: {area_rectangulo(15, 10)}")
#========================================================================
# import math

# def area_circulo(radio):
#     return ((math.pi) * (math.pow(radio, 2)))
    
# print(f"Area de circulo de radio = 5 es: {area_circulo(5)}")    
#========================================================================
# def relacion(x, y):
#     if x > y:
#         return 1
#     elif x < y:
#         return -1
#     elif x ==y:
#         return 0
    
# print(f"La relacion entre 5 y 10 es: {relacion(5, 10)}")
# print(f"La relacion entre 10 y 5 es: {relacion(10, 5)}")
# print(f"La relacion entre 5 y 5 es: {relacion(5, 5)}")
#========================================================================
# def intermedio(x, y):
#     return (x + y)/2

# print(f"El numero intermedio entre -12 y 24 es: {intermedio(-12, 24)}")
#========================================================================
# def recortar(x1, x2, x):
#     if x < x1:
#         return x1
#     elif x > x2:
#         return x2
#     else:
#         return x
    
# print(f"Se recortará 15 entre los limites inferior 0 y superior 10: {recortar(0, 10, 15)}")
# ========================================================================
def separar(*args):
    par = []
    impar = []
    for arg in args:
        if arg % 2 == 0:
            par.append(arg)
        else:
            impar.append(arg)
    par.sort() 
    impar.sort()            
    return f"Numeros pares: {par}\nNumeros impares: {impar}"        
            
print(separar(6,5,2,1,7))



