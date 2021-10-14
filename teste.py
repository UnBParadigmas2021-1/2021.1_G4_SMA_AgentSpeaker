from pade.misc.utility import display_message, start_loop
from pade.behaviours.protocols import FipaSubscribeProtocol
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.acl.aid import AID
from sys import argv
from agentes.agtCortina import AgenteCortina, AgenteCortinaFechada
from pade.acl.filters import Filter
#from agentes.agente_comprador import AgenteComprador


class Remetente(Agent):
    def __init__(self, aid, f):
        super(Remetente, self).__init__(aid=aid, debug=False)
        self.f = f

    def on_start(self):
        super(Remetente, self).on_start()
        '''
        message = ACLMessage(ACLMessage.INFORM)
        message.add_receiver(AID('Ola'))
        message.set_content(msg)
        self.send(message)'''

        display_message(self.aid.localname, 'Enviando Mensagem')
        message = ACLMessage(ACLMessage.INFORM)
        message.set_content('Ola')
        message.add_receiver(AID('agtCortina'))
        self.send(message)
        message.set_content(f'Registro: {self.aid.localname}')

        display_message(self.aid.localname, 'Enviando Mensagem 2')
        message2 = ACLMessage(ACLMessage.INFORM)
        message2.add_receiver(AID('agtCortina2'))
        message2.set_content('Ola')
        self.send(message2)
        message.set_content(f'Registro: {self.aid.localname}')

    def react(self, message):
        pass

'''class AgenteCortina(Agent):

    def __init__(self, aid):
        super(AgenteCortina, self).__init__(aid=aid, debug=False)
    
    def react(self, message):
        super(AgenteCortina, self).react(message)
        display_message(self.aid.localname, 'Abrindo cortina')'''


'''class Destinatario(Agent):
    def __init__(self, aid):
        super(Destinatario, self).__init__(aid=aid, debug=False)

    def react(self, message):
        display_message(self.aid.localname, 'Mensagem recebida') '''


if __name__ == '__main__':

    f = Filter()
    f.performative = ACLMessage.INFORM
    cenario = 1
    port = int(argv[1]) 

    agents = list()



    remetente_agent = Remetente(AID(name='remetente'), f)
    cortina_agent = AgenteCortina(AID(name='agtCortina'),f)
    agente_fechar = AgenteCortinaFechada(AID(name='agtCortina2'),f)

    agents.append(remetente_agent)

    numero_de_cenarios=3
    port += 1

    for i in range(numero_de_cenarios):
        if(cenario==1):
            agents.append(cortina_agent)
            cortina_agent = AgenteCortina(AID(name=f'cortina_{i}@localhost:{port+i}'), f)
            cenario = cenario + 1
        else:
            agente_fechar = AgenteCortinaFechada(AID(name=f'cortina_{i}@localhost:{port+i}'), f)
            agents.append(agente_fechar)

    start_loop(agents)