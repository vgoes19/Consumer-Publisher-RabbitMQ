# Consumer-Publisher-RabbitMQ
Implementando o conceito pub-sub (Publisher and Subscriber), funcionalidade de desacoplar completamente a comunicação entregrando a um message broker (RabbitMQ)
utilizando Procolo AMQP (protocolo avançado de enfileiramento de mensagens)

Termos:
- Queue (filas onde as mensagens são armazenadas, basicamente o consumer)
- Exchange (responsável por pegar mensagem de publicados, analisar, processar e descobrir pra qual fila direcionar, basicamente o publisher)
  - default
  - direct (manda msg para uma fila específica)
  - fanout (binding key)
  - topic (determinar regras)
  - header (envia baseado no cabeçalho)
