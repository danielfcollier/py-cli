# Simple Python CLI

Built with ArgParser.

## About

A simple CLI to generate the secretary WhatsApp text scripts customized with customer and consultation data.

## Usage

```text
usage: drageisa [-h] [-m] [-p] [-c] [-i] [-d] [-t]

Informações para o atendimento via WhatsApp do consultório da Dra. Geisa.

options:
  -h, --help        show this help message and exit
  -m , --message    Número da messagem
  -p , --paciente   Nome da paciente
  -c , --consulta   Orientações da consulta
  -i , --info       Informações gerais
  -d , --dia        Dia da consulta
  -t , --hora       Hora da consulta

Utilitário da Dra. Geisa desenvolvido por Daniel Collier.
```

## Samples

```bash
drageisa -m 1 -p Ana
drageisa -m all -m Ana
drageisa -i help
drageisa -i planos
drageisa -i all
drageisa -c all
drageisa -c cadastro
drageisa -c agenda -d 19/11 -t 10h30
```

## Installation

Copy the repository and into the project folder run:

```bash
sudo make install
```

## Update

```bash
make update
```

## Remove

```bash
make clean
```
