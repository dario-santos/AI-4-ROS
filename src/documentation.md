# Documentação dos ficheiros do IA-4-ROS

## Ficheiro agent.py

O ficheiro agent.py é o ponto de partida do programa.

### Variáveis globais

room_ant       -> variável que guarda o último quarto visitado<br>
x_ant          -> variável que guarda a posição no eixo x anterior<br>
y_ant          -> variável que guarda a posição no eixo y anterior<br>
obj_ant        -> variável que guarda o último objeto detetado  <br>
G              -> Grafo, contém a informação relacionada às conecções entre cada quarto<br>
rooms          -> Dicionário que guarda víncula os objetos ao respetivo quarto, o dicinário tem o tipo <string, Room><br>
time_initial   -> variável que guarda o instante inicial<br>

### Funções

**callback(data)**<br>
Esta função é invocada sempre que o _ROS_ se move. 
É responsável pela localização do _ROS_ no mundo.
É a partir desta função que se obtém as ligações entre cada quarto, e se um quarto é uma suite.

**callback1(data)**<br>
Esta função é invocada sempre que o ros deteta um objeto.
É responsável pela deteção dos objetos.
É a partir desta função que se vão atribuindo os objetos ao seu respetivo quarto.

**callback2(data)**<br>
Esta função é invocada sempre que o utilizador coloca uma pergunta ao _ROS_.
Esta função é apenas responsável por demonstrar o conhecimento, ou parte dele, do ros ao utilizador.

**agent(data)**<br>
Esta função é a função _main_ do ros.
É responsável pela inicialização das variáveis do _ROS_ e das ligações dos eventos às respetivas funções.


## Ficheiro Room.py

Este ficheiro contém as classes Room e RoomType.

### Classe Room

Esta classe representa um quarto do mundo do _ROS_.

**init(self, objects)**<br>
Este método é o construtor da classe Room.
Este método declara dois campos _isSuit_, que diz se um quarto está conectado a outro, e _objects_, uma lista de objetos.

**SetIsSuit(self, value)**<br>
**GetIsSuit(self)**<br>
Estes dois métodos são respetivamente o set e o get da variável isSuit.
isSuit é uma variável booleana que diz se um quarto está conectado a outro quarto.

**AddObject(self, name)**<br>
Este método adiciona um objeto à lista de objetos do quarto com o nome _name_, o conteúdo da variável _name_ segue a norma imposta pelo enunciado categoria_nome, ex.: person_joe.

**RemoveObject(self, name)**<br>
Este método remove um objeto da lista de objetos do quarto a partir do seu nome.
O conteúdo da variável _name_ segue a norma imposta pelo enunciado categoria_nome, ex.: person_joe.

**GetObjectByName(self, name)**<br>
Este método retorna o objeto com o nome dado. Caso não exista um objeto com o nome dado é devolvido o valor None.
O conteúdo da variável _name_ segue a norma imposta pelo enunciado categoria_nome, ex.: person_joe.

**GetObjectsByCategory(self, category)**<br>
Este método retorna uma lista de objetos de uma dada categoria. Caso não existam objetos dessa categoria é devolvida uma lista vazia.

**IsOccupied(self)**<br>
Este método devolve o valor verdade caso existe pelo menos uma pessoa no quarto, falso caso contrário.

**GetRoomType(self)**<br>
Este método devolve o tipo de quarto a partir dos objetos contidos na sua lista de objetos.

### Classe RoomType

A classe RoomType é utilizada como um enum que contém os tipos de quarto.

### Variáveis Estáticas

size    -> Número de tipos que existem<br>
none    -> Caso não estejamos num quarto/corredor, exemplo: uma posição do mundo fora do elevador terá o valor none.<br>
single  -> Tipo de quarto single<br>
double  -> Tipo de quarto double<br>
suite   -> Tipo de quarto suite<br>
meeting -> Tipo de quarto meeting<br>
generic -> Tipo de quarto generic<br>

### Métodos Estáticos

**GetType(type_name)**<br>
Este método devolve o tipo de quarto dado o seu nome. 
Exemplo: 'single' devolve o valor Room.single.

**GetName(type_index)**<br>
Este método realiza a operação inversa ao método GetType.
Dado um tipo de quarto é devolvido o seu nome.
Exemplo: RoomType.single devolve o valor 'single'

## Ficheiro RoomObject.py

Este ficheiro contém as classes RoomObject e Category.

### Classe RoomObject

Esta classe representa um objeto do mundo do _ROS_.

**__init__(self, category, name)**<br>
Este método é o construtor da classe RoomObject.
Este método declara dois campos _name_, o nome do objeto, e _category_, a categoria do objeto.

**SetName(self, name)**<br>
**GetName(self)**<br>
Estes dois métodos são respetivamente o set e o get da variável name.
name é uma variável do tipo string que contém o nome do objeto.

**SetCategory(self, category)**<br>
**GetCategory(self)**<br>
Estes dois métodos são respetivamente o set e o get da variável category.
category é uma variável do tipo integer que contém a categoria do objeto.

### Classe Category

A classe Category é utilizada como um enum que contém as diferentes categorias de um objeto.

### Variáveis Estáticas

door    -> Categoria de objeto door, é utilizado como um None<br>
bed     -> Categoria de objeto bed      <br>
book    -> Categoria de objeto book     <br>
chair   -> Categoria de objeto chair    <br>
computer-> Categoria de objeto computer <br>
person  -> Categoria de objeto person   <br>
table   -> Categoria de objeto table    <br>
mistery -> Categoria de objeto mistery  <br>

### Métodos Estáticos

**GetCategory(category_name)**<br>
Este método devolve a categoria de um objeto dado o nome da categoria. 
Exemplo: 'bed' devolve o valor Category.bed.

## Ficheiro room_util.py

O ficheiro room_util.py contém funções auxiliares que ajudam no tratamento dos dados obtidos pelo _ROS_.

### Variáveis globais

room_nomenclature_prefix -> assegura que é utilizado o mesmo prefixo do quarto em todo o programa.

### Funções

**getNumber(x, y)**<br>
Esta função devolve o número do quarto dado uma posição (x, y).

**getNomenclature(x, y)**<br>
Esta função devolve o nome do quarto dado uma posição (x, y).

**isHall(roomNumber, roomName)**<br>
Esta função devolve verdade caso o quarto com o número roomNumber ou o nome roomNome seja um corredar, falso caso contrário.
roomNumber e roomName são dois argumentos opcionais mas em que se deve passar sempre um para a função, caso não seja passado um dos argumentos é lançada uma excepção.

**getProbabilityOfBeingOccupied(G, rooms)**<br>
Esta função responde à questão número 3.
Cálcula a probabilidade de um quarto e de um corredor estarem ocupados e retorna uma string com toda a informação.
Esta função recebe um grafo e um dicionário.
Tirámos proveito do facto do grafo conter, para além das ligações entre as salas, os quartos visitados.
Sendo assim para cada nodo no grafo vamos ver se este contém uma pessoa, e se é (ou não) um corredor.

**getProbabilityComputer(G, rooms)**<br>
Esta função responde à questão número 4.
Cálcula a probabilidade de um computador estar em cada um dos tipos de quarto (ver a classe RoomsType) e retorna uma string com toda a informação.
Esta função recebe um grafo e um dicionário.
Tirámos proveito do facto do grafo conter, para além das ligações entre as salas, os quartos conhecidos pelo _ROS_.
Sendo assim para cada nodo no grafo vamos calcular o seu tipo de quarto e se contém um ou mais computadores, incrementando as variáveis correspondentes.

**getNumberOfBooks(rooms)**<br>
Esta função auxilia na resposta à pergunta número 7.
Conta o número de livros conhecidos pelo _ROS_.

## Ficheiro graph_util.py

O ficheiro graph_util.py contém funções auxiliares que ajudam no tratamento dos dados obtidos pelo _ROS_.
Mais especificamente, a sua localização.
Utilizámos a biblioteca networkx.

**createGraph()**<br>
Esta função cria um grafo vazio.

**addNode(G, node)**<br>
Esta função adiciona o nodo _node_ ao grafo _G_.
Esta função verifica também se o nodo é válido e se este já não existe no grafo.

**addEdge(G, node_1, node_2)**<br>
Esta função adiciona uma aresta entre os nodos *node_1* e *node_2*.
Esta função verifica também se a aresta é válida e se esta já não existe no grafo.

**shortestPath(G, currentPos, goalPos='Room 1')**<br>
Esta função responde à questão número 6.
Dado um nodo de partida e um de chegada é cálculado o caminho mais curto entre ambos.
Esta função utiliza a pesquisa informada, A*.

**closesteRoom(G, rooms, current_room)**<br>
Esta função responde à questão número 5.
Dado um nodo de partida, um dicionário de quartos e um grafo é cálculado o quarto do tipo _single_ mais próximo do _ROS_.
Esta função utiliza o algoritmo dijkstra para cálcular o caminho mais curto do quarto atual para todos os outros.
Nesta função o dicionário é apenas utilizado para se extraír a informação do tipo de quarto.
