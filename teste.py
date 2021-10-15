from pade.misc.utility import display_message, start_loop
from pade.behaviours.protocols import FipaSubscribeProtocol
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.acl.aid import AID
from sys import argv
from agentes.agtCortina import AgenteCortina, AgenteCortinaFechada
from agentes.agtSonorizacao import AgenteSonorizacao, AgenteSonorizacaoDesligada
from pade.acl.filters import Filter
from twisted.internet import reactor

import time


class Remetente(Agent):
    def __init__(self, aid, f):
        super(Remetente, self).__init__(aid=aid, debug=False)
        self.f = f

    def on_start_open(self):
        super(Remetente, self).on_start()

        call_later(10, self.sending_message(agtCortina))
        #sending_message(agtCortina)

        #display_message(self.aid.localname, 'Enviando Mensagem')

    def on_start_close(self):
        super(Remetente, self).on_start()

        call_later(10, self.sending_message(agtCortina2))
        #sending_message(agtCortina2)

        #display_message(self.aid.localname, 'Enviando Mensagem 2')

    
    def on_start_sound(self):
        super(Remetente, self).on_start()

        call_later(10, self.sending_message(agtSound))
        #sending_message('agtSound')

    def on_start_sound_off(self):
        super(Remetente, self).on_start()

        call_later(10, self.sending_message(agtSound2))

    def sending_message(self, string):
        message = ACLMessage(ACLMessage.INFORM)
        message.set_content('Ola')
        message.add_receiver(AID(string))
        self.send(message)
        message.set_content(f'Registro: {self.aid.localname}')
        

    def react(self, message):
        pass


if __name__ == '__main__':

    f = Filter()
    f.performative = ACLMessage.INFORM
    cenario = 1
    port = int(argv[1])
    port2 = int(argv[1])
    agents = list()

    #remetente_agent = Remetente(AID(name='remetente'), f)

    cortina_agent = AgenteCortina(AID(name='agtCortina'),f)
    agente_fechar = AgenteCortinaFechada(AID(name='agtCortina2'),f)

    ligar_som = AgenteSonorizacao(AID(name='agtSound'),f)
    desligar_som = AgenteSonorizacaoDesligada(AID(name='agtSound2'),f)

    #agents.append(remetente_agent)

    numero_de_cenarios=2
    port += 1
    port2 += 100

    for i in range(numero_de_cenarios):

        if(cenario == 1):
            cortina_agent = AgenteCortina(AID(name=f'cortina_{i}@localhost:{port+i}'), f)
            ligar_som = AgenteSonorizacao(AID(name=f'som_{i}@localhost:{port2+i}'), f)
            agents.append(cortina_agent)
            agents.append(ligar_som)
            cenario = 0
        else:
            agente_fechar = AgenteCortinaFechada(AID(name=f'cortina_{i}@localhost:{port+i}'), f)
            desligar_som = AgenteSonorizacaoDesligada(AID(name=f'som_{i}@localhost:{port2+i}'), f)
            agents.append(agente_fechar)
            agents.append(desligar_som)
            cenario = 1

            #reactor.callFromThread(reactor.stop)
            break

    start_loop(agents)