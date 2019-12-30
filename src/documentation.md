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

**getProbabilityOfFindingPerson(G, rooms)**<br>
Esta função responde à questão número 3.
Cálcula a probabilidade de uma pessoa estar num quarto e a de uma pessoa estar num corredor, e retorna uma string com toda a informação.
Esta função recebe um grafo e um dicionário.
Tirámos proveito do facto do grafo conter, para além das ligações entre as salas, os quartos visitados.
Sendo assim para cada nodo no grafo vamos ver se este contém uma pessoa, e se é (ou não) um corredor.

**getProbabilityOfBeingOccupied(G, rooms)**<br>
Esta função responde à questão número 9.
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


## Abordagem às questões

De forma inicial as questões foram agrupadas de acordo com a sua semelhança e dependência.
Por exemplo, as questões 5 e 6 estão ambas relacionadas a caminhos não dependendo dos objetos que cada quarto contém.

### Agrupamento das questões

Tendo o que foi dito anteriormente as questões foram agrupadas da seguinte forma:

As questões 1 e 2 dizem ambas respeito conhecimento que o _ROS_ contém dos objetos de cada sala.

As questões 3 e 4 dependem da deteção de objetos, tal como as questões 1 e 2, mas o seu foco principal é o cálculo de probabilidades face ao tipo de quarto.

As questões 5 e 6 dizem apenas respeito ao conhecimento que o _ROS_ tem sobre as ligações de cada quarto.

A questão 7 depende do tempo passado.

A questão 8 depende das redes baisianas.


### Questão 1 - How many rooms are not occupied

Um quarto está ocupado se exister pelo menos uma pessoa no mesmo.

Sendo assim só temos que contar o número de quartos, dos que o agente conheçe, que não contém pessoas.

Pseudo-código:

PARA CADA quarto que o agente conhece ENTÃO
  SE este quarto não contém pessoas ENTÃO
     incrementar o número de quartos desocupados. 

Esta questão foi respondida na função **callback2** no ficheiro **agent.py**.

### Questão 2 - How many suites did you find until now?

Esta questão levantou algumas dúvidas em relação ao que considerariamos uma suíte.
Dúvidas que foram esclarecidas com o docente da unidade curricular.

Admitimos que uma suíte deve cumprir dois requisitos:

- Estar conectado a outro quarto.
- Conter pelo menos duas camas.

Para além disto, contamos ambos os quartos como uma única suíte.

Tendo estas considerações feitas falta apenas consultar os quartos visitados pelo agente, até ao momento, e contar o número de quartos que cumprem estes requisitos.

Pseudo-código:

PARA CADA quarto que o agente conhece ENTÃO
  SE este quarto está ligado a outro quarto e contém mais do que duas camas ENTÃO
     incrementar o número de suítes existentes.

Esta questão foi respondida na função **callback2** no ficheiro **agent.py**.

### Questão 3 - Is it more probable to find people in the corridors or inside the rooms?

Inicialmente decidimos calcular a probabilidade de um quarto estar ocupado e a probabilidade de um corredor estar ocupado, verificando depois qual destes era a maior.

Mas depois de discutirmos acerca desta interpretação foi decidido que isto não respondia à questão.

Sendo assim decidimos decidimos cálcular a probabilidade de uma pessoa estar num quarto e comparar com a probabilidade de uma pessoa estar num corredor,
como no nosso universo uma pessoa ou está num quarto ou num corredor só necessitamos de calcular uma das probabilidades (pois a outra será o seu complementar).

P(PessoaNumQuarto) = NúmeroDePessoasEmQuartos/NúmeroDePessoasConhecidas

~P(PessoasNumQuarto) = P(PessoasNumCorredor)

Pseudo-código:

PARA CADA quarto que o agente conhece ENTÃO
    numPessoas = numPessoas + PessoasNesteQuarto
    SE este quarto não é um corredor ENTÃO
         pessoasNumQuarto = pessoasNumQuarto + PessoasNesteQuarto

Esta questão foi respondida na função **getProbabilityOfFindingPerson** no ficheiro **room_util.py**

### Questão 4 - If you want to find a computer, to which type of room do you go to?

A nossa abordagem a esta questão foi a de calcular a probabilidade de um tipo de quarto ter um computador e retornar a maior probabilidade.
Ou seja,

Cálculamos as probabilidades:

P(QuartoSingleterComputdor)   = QuartosSingleComComputador/QuartosSingle
P(QuartoDoubleMterComputdor)  = QuartosDoubleComComputador/QuartosDouble
P(QuartoSuiteMterComputdor)   = QuartosSuiteComComputador/QuartosSuite
P(QuartoMeetingMterComputdor) = QuartosMeetingComComputador/QuartosMeeting
P(QuartoGenericMterComputdor) = QuartosGenericComComputador/QuartosGeneric

Sabendo qual o tipo de quarto tem mais quartos com computador podemos responder à questão.

### Questão 5 - What is the number of the closest single room?

Para conseguirmos responder a esta questão precisámos, para além de armazenar os objetos, conseguir representar as suas ligações. 
Decidimos utilizar um grafo para representar as ligações entre os diferentes quartos, em que cada nodo é uma sala e  cada aresta uma ligação entre dois quartos.

Para além disto foi atribuído a cada aresta o peso 1 para que possamos realizar pesquisas informadas.

Tendo estes problemas resolvidos a nossa abordagem foi a de utilizar o algoritmo de Dijkstra para calcular os caminhos mais curtos de um nodo para os restantes e, indo do caminho mais curto para o mais longo, verificar se este era do tipo single, caso fosse retornávamos esse quarto.

Esta questão foi respondida na função **closestRoom** no ficheiro **graph_util.py** utilizando a biblioteca networkx.

### Questão 6 - How can you go from the current room to the elevator?

Aproveitando o facto de termos armazenadas as ligações entre os quartos num grafo, podémos responder a esta questão utilizando uma simples pesquisa informada.

Utilizámos a pesquisa informada A*, e a bilbioteca networkx.

Esta questão foi respondida na função **shortestPath** no ficheiro **graph_util.py** utilizando a biblioteca networkx.

### Questão 7 - How many books do you estimate to find in the next 2 minutes?

Sabendo o número de livros que o agente conhece e o tempo decorrido podemos fazer uma regra de 3 simples para cálcular o número estimado de livros para dois minutos.


NúmeroDeLivrosConhecidos --------------- TempoDecorrido
          X              --------------- 120 

X = 120 * NúmeroDeLivrosConhecidos / TempoDecorrido

Esta questão foi respondida na função **callback2** no ficheiro **agent.py**



### Questão 8 -

Não pensei nesta pergunta mas vai utilizar redes baisianas.


### Questão 9 - Is it more probable to a room be occuped or a corridor?

Como foi discutido na questão 3, esta questão adicional foi acrescentada a uma interpretação errada que considerámos uma mais valia manter como uma questão adicional.

A resposta a esta pergunta passa por cálcular as seguintes probabilidades:

- P(CorredorOcupado) = CorredoresOcupados/NumeroCorredores
- P(QuartoOcupado) = QuartosOcupados/NumeroQuartos

Esta questão foi respondida na função **getProbabilityOfBeingOccupied** no ficheiro **room_util.py**


## Abordagem ao problema

Começámos por pensar em formas de representar o conhecimento do nosso agente.

Depois de uma leitura do enunciado foram identificados dois objetos principais, quartos e objetos.
Para cada um destes objetos foi desenvolvida uma classe de forma a organizar o código que dizia respeito a cada um.

Para os quartos foi desenvolvida a classe Room, que se encontra no ficheiro Room.py, e para os objetos foi desenvolvida a classe RoomObject, que se encontra no ficheiro RoomObject.py.

Posteriormente foi adicionado um grafo de forma a se representar as ligações entra cada quarto, à qual foram desenvolvidas as funções auxiliares que se encontram no ficheiro graph_util.py.
