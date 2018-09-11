# Máquina de Turing

Projeto para a matéria de Linguagens Formais, Autômatos e Computabilidade
Desenvolvido por Dennis Urtubia, Jorge Rossi e Otávio Goes

Dado uma descrição de funcionamento de uma Máquina de Turing e uma entrada para verficação, o programa escrito em Python efetua as possíveis transições entre os estados e retorna um resultado de aceitação ou um resultado na fita.

# Funcionamento do código fonte

##### A estrutura do programa foi separada em 5 classes e a main, sendo elas:

- ##### estado.py
  Armazena os estados coletados por meio do arquivo texto que contém a descrição da máquina.
- ##### execute.py
  É responsável pela execução de uma transição que corresponde ao estado e símbolo atual da fita, além da verficação de finalização da máquina e loop.
  Cada execução assenhoreia uma única fita que independe de outras execuções/fitas.
- ##### fita.py
  Gerencia os dados da fita e a posição da em que a cabeça de leitura se encontra. Também desempenha a função de mostra-la.
- ##### maquina.py
  Faz a gerencia de Estados, Transições e Execuções.
- ##### transição.py
  Possui os dados que serão usados na execução de uma transição.
- ##### main.py
  Faz a leitura dos dados a partir de um arquivo texto referenciado pela linha de comando, arquivo este que possui as especificações e configurações de uma Máquina de Turing.
  Também recebe o parâmetro de entrada para a execução e verificação da máquina.

# Execução do programa

#### Modo de execução do programa:

Primeiro passo:

```sh
$ cd pasta-do-projeto
```

Segundo passo:

```sh
$ cd src
```

Terceiro passo:

```sh
$ ./main.py descricaomaquina.txt "entrada"
```

## License

MIT
