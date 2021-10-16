from agentes.agtProjetor import AgenteProjetor
from agentes.agtIluminacao import AgenteIluminacao
from agentes.agtCortina import AgenteCortina
from agentes.agtSonorizacao import AgenteSonorizacao
from typing import List
from pade.misc.utility import start_loop
from pade.acl.messages import ACLMessage
from pade.acl.filters import Filter
from pade.acl.aid import AID
from sys import argv

if __name__ == '__main__':
    f = Filter()
    f.performative = ACLMessage.INFORM

    agentes = list()
    port = int(argv[1])

    agente_projetor = AgenteProjetor(AID(name=f'projetor@localhost:{port}'), f)
    agentes.append(agente_projetor)
    port += 1
    agente_cortina = AgenteCortina(AID(name=f'cortina@localhost:{port}'), f)
    agentes.append(agente_cortina)
    port += 1

    agente_iluminacao = AgenteIluminacao(AID(name=f'iluminacao@localhost:{port}'), f)
    agentes.append(agente_iluminacao)
    port += 1
    
    agente_sonorizacao = AgenteSonorizacao(AID(name=f'sonorizacao@localhost:{port}'), f)
    agentes.append(agente_sonorizacao)


    start_loop(agentes)
