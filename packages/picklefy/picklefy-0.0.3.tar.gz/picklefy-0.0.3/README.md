# PickliFy
Facilitar o uso de arquivos pickle no python sem se preocupar onde estão sendo salvos e nem de qual local eles estão sendo chamados.
 
- ##### Como funciona ?
   - A lib picklify cria um diretório chamado pickle_files dentro da venv do projeto e salva todos os arquivos pickle nesse diretório;
   - Para serializar basta chamar o método serialize e passar o nome como deseja salvar e a variavel/valor que deseja serializar;
   - Ja para deserializar basta chamar o método serialize e passar apenas o nome ja salvo anteriormente.
- ##### Qual é a utilidade e porque não usar a biblioteca pickle diretamente ?
    - A utilidade é que a lib picklify facilita o uso de arquivos pickle no python, sem ficar se preocupando onde eles estão sendo salvos e nem de qual local eles estão sendo chamados.
- ##### Exemplos de uso:
    - Conseguir executar partes pequenas de código sem precisar executar o código inteiro.
    - Salvar variáveis que demoram para serem processadas e depois deserializar elas.

## Instalação
```
pip install picklify
```
## Como utilizar?
- ##### Serializando uma variavel
```
from picklefy import PickleFy

# Serializando uma variavel
variavel = 'Ola Mundo'
ok = PickleFy().serialize(file_name='var', variavel=variavel)

```
- ##### Deserializando uma variavel
```
from picklefy import PickleFy

# Deserializando uma variavel
new_var = PickleFy().serialize(file_name='var')
```

## Dependências
- pickle

## Dúvidas ou Sugestões
henriquespencer11@gmail.com
