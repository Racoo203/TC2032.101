#---------------------------------------------------------------------------------------------------------------
#    Esqueleto de PSA para el problema de ...
#---------------------------------------------------------------------------------------------------------------

from simpleai.search import SearchProblem, depth_first, breadth_first, uniform_cost, greedy, astar
from simpleai.search.viewers import BaseViewer, ConsoleViewer, WebViewer

#---------------------------------------------------------------------------------------------------------------
#   Definición del problema
#---------------------------------------------------------------------------------------------------------------

class TourDeEuropa(SearchProblem):
    """ 
        Clase que es usada para definir el problema. Los estados son representados 
        con .
    """

    def __init__(self, origen, destino):
        """ Constructor de la clase para el problema del Tour de Europa. 
            Inicializa el problema de acuerdo a la ciudad de origen.
       
            origen: ciudad de origen
            destino: ciudad de destino
        """
        
        # Llama al constructor de su superclase SearchProblem (estado inicial = ).
        SearchProblem.__init__(self, origen)

        # Define el estado meta = ciudad de destino.
        self.goal_state = destino

    def actions(self, state):
        """ 
            Este método regresa una lista con las acciones posibles que pueden ser ejecutadas de 
            acuerdo con el estado especificado.
            
            state: ciudad actual
        """
        if state == 'Paris':
            actions = ['Burdeos','Estrasburgo']
        elif state == 'Burdeos':
            actions = ['Paris','San Sebastian','Lyon']
        elif state == 'Estrasburgo':
            actions = ['Paris','Lyon','Ginebra']
        elif state == 'San Sebastian':
            actions = ['Burdeos','Barcelona']
        elif state == 'Lyon':
            actions = ['Burdeos','Estrasburgo','Grenoble']
        elif state == 'Ginebra':
            actions = ['Estrasburgo','Cannes']
        elif state == 'Barcelona':
            actions = ['San Sebastian','Cannes']
        elif state == 'Grenoble':
            actions = ['Lyon','Cannes']
        elif state == 'Cannes':
            actions = ['Barcelona','Grenoble','Ginebra']
        return actions

    def result(self, state, action):
        """ 
            Este método regresa el nuevo estado obtenido despues de ejecutar la acción.

            state: ciudad actual.
            action: ciudad a donde voy.
        """
        return action

    def is_goal(self, state):
        """ 
            This method evaluates whether the specified state is the goal state.

            state: La ciudad actual.
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
        if state == 'Paris':
            if action == 'Burdeos':
                return 300
            elif action == 'Estrasburgo':
                return 320
        elif state == 'Burdeos':
            if action == 'Paris':
                return 300
            elif action == 'San Sebastian':
                return 250
            elif action == 'Lyon':
                return 350
        elif state == 'Estrasburgo':
            if action == 'Paris':
                return 320
            elif action == 'Lyon':
                return 340
            elif action == 'Ginebra':
                return 510
        elif state == 'San Sebastian':
            if action == 'Burdeos':
                return 250
            elif action == 'Barcelona':
                return 430
        elif state == 'Lyon':
            if action == 'Burdeos':
                return 350
            elif action == 'Estrasburgo':
                return 340
            elif action == 'Grenoble':
                return 125
        elif state == 'Ginebra':
            if action == 'Estrasburgo':
                return 510
            elif action == 'Cannes':
                return 630
        elif state == 'Barcelona':
            if action == 'San Sebastian':
                return 430
            elif action == 'Cannes':
                return 485
        elif state == 'Grenoble':
            if action == 'Lyon':
                return 125
            elif action == 'Cannes':
                return 680
        elif state == 'Cannes':
            if action == 'Barcelona':
                return 485
            elif action == 'Grenoble':
                return 680
            elif action == 'Ginebra':
                return 630
        
    def heuristic(self, state):
        """ 
            Este método regresa un estimado de la distancia desde el estado a la meta.

            state: ciudad del nodo
        """
        if state == 'Paris':
            return 1400
        elif state == 'Burdeos':
            return 1100
        elif state == 'Estrasburgo':
            return 1120
        elif state == 'San Sebastian':
            return 900
        elif state == 'Lyon':
            return 780
        elif state == 'Ginebra':
            return 630
        elif state == 'Barcelona':
            return 480
        elif state == 'Grenoble':
            return 680
        elif state == 'Cannes':
            return 0

# Despliega los resultados
def display(result):
    if result is not None:
        for i, (action, state) in enumerate(result.path()):
            if action == None:
                print('Configuración inicial')
            elif i == len(result.path()) - 1:
                print(i,'- Después de moverse a', 'Ir a '+action)
                print('¡Meta lograda con costo = ', result.cost,'!')
            else:
                print(i,'- Después de moverse a', 'Ir a '+action)

            print('  ', state)
    else:
        print('Mala configuración del problema')

#---------------------------------------------------------------------------------------------------------------
#   Programa
#---------------------------------------------------------------------------------------------------------------

#my_viewer = None
my_viewer = BaseViewer()       # Solo estadísticas
#my_viewer = ConsoleViewer()    # Texto en la consola
#my_viewer = WebViewer()        # Abrir en un browser en la liga http://localhost:8000

# Crea un PSA y lo resuelve con la búsqueda primero en anchura
result = breadth_first(TourDeEuropa('Paris','Cannes'), graph_search=True, viewer=my_viewer)

if my_viewer != None:
    print('Stats:')
    print(my_viewer.stats)

print()
print('>> Búsqueda Primero en Anchura <<')
display(result)

result = depth_first(TourDeEuropa('Paris','Cannes'), graph_search=True)
print()
print('>> Búsqueda Primero en Profundidad <<')
display(result)

result = astar(TourDeEuropa('Paris','Cannes'), graph_search=True)
print()
print('>> Búsqueda A* <<')
display(result)


#---------------------------------------------------------------------------------------------------------------
#   Fin del archivo
#---------------------------------------------------------------------------------------------------------------