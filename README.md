# Python Examples
Projeto Python usado para anotações de diversos exemplos e testes.


Exemplos com:
- Arguments
- Databases
- Excell
- Loops
- Logs
- Strings
- RabbitMQ  
Para acesso o RabbitMQ do Docker Toolbox, http://192.168.99.100:15672, é preciso habilitar o "Management Plugin" com os seguintes comandos de exemplo:  
$ docker ps  
$ docker exec -it rabbitmq bash  
$ rabbitmq-plugins enable rabbitmq_management  

## Dica de Instalação e configuração dos requirements.

Comandos no prompt:
- cd {diretorio\_raiz\_do\_projeto}
- pip install --install-option="--prefix={diretorio\_raiz\_do\_projeto}\\requirements" -r requirements.txt

Exemplos de comandos para prompt no Windows:
- cd C:/desenvolvimento/projects/python_examples
- pip install --install-option="--prefix=C:\\desenvolvimento\\projects\\python_examples\\requirements" -r requirements.txt

Utilizando o Eclipse IDE, junto com o PyDev plugin, é possível adicionar os "requirements" ao projeto da seguinte forma:
- "Projeto Properties" >> "PyDev - PYTHONPATH" >> "External Libraries" >> "Add source folder" >> "Incluir o diretório criado '{diretorio\_raiz\_do\_projeto}/requirements/Lib/site-packages'"
