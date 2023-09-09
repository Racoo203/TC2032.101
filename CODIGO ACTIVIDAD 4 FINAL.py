# Imports
import math
import random
from simpleai.search import SearchProblem

# Integrantes del Equipo 4:
# 1. Ricardo Kaleb Flores Alfonso     A01198716
# 2. Sebastián Miramontes Soto        A01285296
# 3. Raúl Correa Ocañas               A01722401

x = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
y = [1.0, 1.0, 2.0, 4.0, 5.0, 4.0, 4.0, 5.0, 6.0, 5.0]

# Class definitions

class RegresionNoLineal(SearchProblem):
    def __init__(self):
        self.parametros = ['a', 'b', 'c']

        self.initial_state = {
            'a': random.randint(0, 15),
            'b': random.randint(0, 15),
            'c': random.randint(0, 15),
        }

    def actions(self, state):
        actions = []
        for parametro in self.parametros:
            actions.append(('incrementar', parametro))
            actions.append(('decrecer', parametro))
        return actions

    def result(self, state, action):
        action_type, parametro = action
        new_state = dict(state)
        if action_type == 'incrementar':
            new_state[parametro] = min(15, new_state[parametro] + 1)
        elif action_type == 'decrecer':
            new_state[parametro] = max(0, new_state[parametro] - 1)
        return new_state

    def value(self, state):
        a, b, c = state['a'], state['b'], state['c']
        error = max(abs(y_val - (math.cos(a * x_val) + b * x_val - c * x_val ** 2)) for x_val, y_val in zip(x, y))
        return error

# Simulated Annealing
step = 0
alpha = 0.99999 # Nada efectivo, sin respuesta (exceso de memoria). 
# alpha = 0.9999 # Menos efectivo, (14,11,6) consistentemente, 8.6s.
# alpha = 0.999 # Muy eficiente, (14,11,6) consistentemente, 0.3s
# alpha = 0.99 # Mejor 0.9, (14,11,6),(14,12,7), 0.1s.
# alpha = 0.9 # Nada confiable, sin respuesta concreta, <0.0, 

# t0 = 100000 # Efectivo, (14,11,6), 0.9s.
# t0 = 10000 # Nada efectivo, sin respuesta (exceso de memoria).
# t0 = 1000 # Nada efectivo, sin respuesta (exceso de memoria).
# t0 = 100 # Nada efectivo, sin respuesta (exceso de memoria).
# t0 = 10 # Nada efectivo, sin respuesta (exceso de memoria).
t0 = 1
t = t0
errores = []
best_solution = None

problem = RegresionNoLineal()
current_state = problem.initial_state

while t > 0.001:

    # Calcular temperatura
    t = t0 * math.pow(alpha, step)
    step += 1

    print("Iteration: ", step, "    Temperatura: ", t)
    print("Valores iniciales a, b, c:", current_state)
    current_error = problem.value(current_state)
    errores.append(current_error)
    print("Error máximo:", current_error)

    # Escoger un vecino al azar
    action = random.choice(problem.actions(current_state))
    neighbor_state = problem.result(current_state, action)
    neighbor_error = problem.value(neighbor_state)

    # Calcular la diferencia de error entre el vecino y el estado actual
    delta_error = neighbor_error - current_error

    # Si el vecino es mejor, moverse a él, si no, moverse a él con una probabilidad de e^(-delta_error / t)
    # Esto es para evitar quedarse atorado en un mínimo local
    if delta_error < 0 or random.random() < math.exp(-delta_error / t):
        current_state = neighbor_state
        current_error = neighbor_error
    
    if best_solution is None or current_error < best_solution['error']:
        best_solution = {
            'a': current_state['a'],
            'b': current_state['b'],
            'c': current_state['c'],
            'error': current_error
        }

print("--------------------")
min_error = min(errores)
print("")
print("Valores de a, b, c para el mínimo error:", best_solution['a'], best_solution['b'], best_solution['c'])
print("Mínimo valor de error:", min_error)
