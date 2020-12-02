# Caliente

Esse projeto visa consultar temperatura e humidade dos POPs da Quick (com o ESP 8266 NodeMCU). Os dados são apresentados de 2 formas, como página web `'/'` e uma API com formato json `'/api'`.
Segue abaixo instruções de onde e como instalar, configurar e deployment.

## instalação
Para instalar, clone o repo.
```
git clone https://github.com/LucasRochaAbraao/caliente
```
Em seguida, instale as dependências:
```
pip install -r requirements.txt
```

OBS: Essa instalação é para o servidor web. Coloquei o código do NodeMCU no repo, mas existem documentações oficiais online de como realizar a instalação do firmware do arduino.

## Configuração

A configuração é simples. Renomeie o `config_sample.py` para `config.py` e coloque o IP do seu NodeMCU.

## Deployment

Em desenvolvimento. Quando finalizar a eu atualizo o README.
