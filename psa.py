#---------------------------------------------------------------------------------------------------------------
#    Esqueleto de PSA para el problema de ...
#---------------------------------------------------------------------------------------------------------------

from simpleai.search import SearchProblem, depth_first, breadth_first, uniform_cost, greedy, astar
from simpleai.search.viewers import BaseViewer, ConsoleViewer, WebViewer

#---------------------------------------------------------------------------------------------------------------
#   Definición del problema
#---------------------------------------------------------------------------------------------------------------

class Tour(SearchProblem):
    """ 
        Clase que es usada para definir el problema del Tour de Europa. Los estados son representados 
        con los nombres de las ciudades.
    """

    def __init__(self, args):
        """ Constructor de la clase. Inicializa el problema de acuerdo a ...
       
            arg1: ...
            arg2: ...
        """
        
        # Llama al constructor de su superclase SearchProblem (estado inicial = ciudad origen).
        SearchProblem.__init__(self, origen)

        # Define el estado meta = ciudad destino.
        self.goal_state = ...

    def actions(self, state):
        """ 
            Este método regresa una lista con las acciones posibles que pueden ser ejecutadas de 
            acuerdo con el estado especificado.
            
            state: ...
        """

        return ...

    def result(self, state, action):
        """ 
            Este método regresa el nuevo estado obtenido despues de ejecutar la acción.

            state: Una ciudad origen (la actual).
            action: Par (ciudad vecina, distancia)).
        """
        return ...

    def is_goal(self, state):
        """ 
            This method evaluates whether the specified state is the goal state.

            state: The state to be tested.
        """
        return state == self.goal_state
        
    def cost(self, state, action, state2):
        """ 
            Este método recibe dos estados y una acción, y regresa el costo de 
            aplicar la acción del primer estado al segundo.

            state: ...
            action: ...
            state2: ...
        """
        return ...
        
    def heuristic(self, state):
        """ 
            Este método regresa un estimado de la distancia desde el estado a la meta.

            state: ...
        """

        return ...

# Despliega los resultados
def display(result):
    if result is not None:
        for i, (action, state) in enumerate(result.path()):
            if action == None:
                print('Configuración inicial')
            elif i == len(result.path()) - 1:
                print(i,'- Después de moverse a', action)
                print('¡Meta lograda con costo =', result.cost,'!')
            else:
                print(i,'- Después de moverse a', action)

            print('  ', state)
    else:
        print('Mala configuración del problema')

#---------------------------------------------------------------------------------------------------------------
#   Programa      me pasas los datos plox?
#---------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------
#   Programa
#---------------------------------------------------------------------------------------------------------------

my_viewer = None
#my_viewer = BaseViewer()       # Solo estadísticas
#my_viewer = ConsoleViewer()    # Texto en la consola
#my_viewer = WebViewer()        # Abrir en un browser en la liga http://localhost:8000

# Crea un PSA y lo resuelve con la búsqueda primero en anchura
result = breadth_first(Problema(args...), graph_search=True, viewer=my_viewer)

if my_viewer != None:
    print('Stats:')
    print(my_viewer.stats)

print()
print('>> Búsqueda Primero en Anchura <<')
display(result)

result = depth_first(Problema(args...), graph_search=True)
print()
print('>> Búsqueda Primero en Profundidad <<')
display(result)

result = astar(Problema(args...), graph_search=True)
print()
print('>> Búsqueda A* <<')
display(result)


#---------------------------------------------------------------------------------------------------------------
#   Fin del archivo
#---------------------------------------------------------------------------------------------------------------