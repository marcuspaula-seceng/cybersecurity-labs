# Laboratório SOC — Triagem de logs de autenticação

**Marcus de Paula**

Este exercício usa cinco eventos fictícios para praticar a triagem de alertas de autenticação. O script conta as falhas por IP e sinaliza um login bem-sucedido após pelo menos duas falhas da mesma conta e origem.

## O que a sala do TryHackMe pede

| Tarefa | O que fazer na sala | Como praticar neste laboratório |
|---|---|---|
| 1. Junior Security Analyst Journey | Identificar a equipe em que o analista júnior trabalha, o Security Operations Center (SOC). | Assumir o papel de analista L1 e fazer a triagem dos registros. |
| 2. Security Operations Center | Ler os papéis da equipe e avançar. O analista sênior assume casos mais complexos, a engenharia mantém as ferramentas, a gerência coordena o SOC e a resposta a incidentes atua nos casos graves. | Preparar uma nota de escalonamento para o analista sênior. |
| 3. A Day in the Life of a Security Analyst | Abrir **View Site**, identificar o IP nos alertas, registrar para quem o evento foi escalado e anotar a mensagem exibida após o bloqueio no firewall do simulador. | Correlacionar falhas e sucessos, documentar a evidência e registrar a decisão de contenção como exercício de mesa. |

O exercício abaixo usa seus próprios registros fictícios. Para completar a sala e verificar a mensagem do firewall, faça a atividade no simulador oficial. [Junior Security Analyst Intro](https://tryhackme.com/room/jrsecanalystintrouxo)

## 1. Abrir o laboratório

Coloque `analisar.py` e `auth.log` na mesma pasta. Abra o terminal nessa pasta. O exercício roda com Python 3 no Google Cloud Shell ou no computador local.

```sh
ls
```

## 2. Ler os registros

```sh
cat auth.log
```

Cada registro contém horário, conta, IP de origem e resultado. Os IPs são reservados para documentação. O script lê o arquivo na ordem das linhas e trabalha apenas com os dados locais.

## 3. Executar a triagem

```sh
python3 analisar.py
```

```text
Falhas por IP:
  192.0.2.20: 1
  198.51.100.23: 2
Sessões para investigação:
  09:04 | conta lab | IP 198.51.100.23 | sucesso após 2 falhas
```

## 4. Escalonar e documentar a decisão

1. Registre o evento de **09:04** da conta `lab` e o IP fictício `198.51.100.23`.
2. Inclua as duas falhas anteriores, às **09:02** e **09:03**, atribuídas à mesma conta e origem.
3. No exercício de mesa, encaminhe a nota ao analista sênior e peça que confirme se o login era esperado e revise as ações posteriores.
4. Se o acesso não for reconhecido, registre a contenção proposta de acordo com o procedimento do SOC. No simulador do TryHackMe, o exercício pede o bloqueio pela interface do próprio lab e a anotação da mensagem resultante. O script local apenas lê o log.

**Exemplo de nota.** Às 09:04, a conta `lab` autenticou com sucesso após duas falhas do mesmo IP. Solicito confirmar com o responsável pela conta se o acesso era esperado e revisar a atividade da sessão. Classificação inicial: login suspeito em investigação.

## Conclusão

O login da conta `lab` às 09:04 merece investigação. Num caso real, eu verificaria se o login era esperado e buscaria nos registros as ações da sessão após a autenticação. Os cinco registros do exercício permitem priorizar o alerta. Confirmar um comprometimento exigiria evidência adicional.

O exercício usa apenas Python 3 e dados fictícios. A execução no Cloud Shell dispensa uma VM separada, uma chave de API e chamadas a modelos de IA.
