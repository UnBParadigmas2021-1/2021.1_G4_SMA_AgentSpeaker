from pade.behaviours.protocols import FipaSubscribeProtocol
from pade.misc.utility import display_message, call_later
from pade.acl.messages import ACLMessage
from pade.core.agent import Agent
from pade.acl.aid import AID
from random import randint
from twisted.internet import reactor

'''class AgenteCortina(Agent):

    def __init__(self, agent, message):
        super(SubscriberProtocol, self).__init__(agent, message, is_initiator=True)
    
    def handle_agree(self, message):
        self.agent.logger.log(self.agent.aid.name, "Abrindo cortina")

    '''

class AgenteCortina(Agent):

    def __init__(self, aid, f):
        super(AgenteCortina, self).__init__(aid=aid, debug=False)
        self.f = f
    
    def react(self, message):
        super(AgenteCortina, self).react(message)
        #display_message(self.aid.localname, 'Mensagem Recebida')
        display_message(self.aid.localname, 'Mensagem recebida from {}'.format(message.sender.name))
        #display_message(self.aid.localname, f'{message.content}')
        display_message(self.aid.localname, 'abrindo cortinas')
    
        if self.f.filter(message):
            display_message(self.aid.localname, 'chegou aki')
            if f'{message.content}'.startswith("Ola"):
                display_message(self.aid.localname, 'Ola Recebida')


class AgenteCortinaFechada(Agent):

    def __init__(self, aid, f):
        super(AgenteCortinaFechada, self).__init__(aid=aid, debug=False)
        self.f = f
    
    def react(self, message):
        super(AgenteCortinaFechada, self).react(message)
        #display_message(self.aid.localname, 'Mensagem Recebida')
        display_message(self.aid.localname, 'Mensagem recebida from {}'.format(message.sender.name))
        display_message(self.aid.localname, 'Fechando cortinas')


''' def react(self, message):
        super(AgenteComprador, self).react(message)
        if self.f.filter(message):

            # A ideia aqui é que o leiloeiro mandaria pro comprador uma mensagem com o prefixo vencedor
            # quando ele vencesse o leilao. Nesse caso o leiloeiro manda uma mensagem pra um comprador especifico
            # por isso nao usamos o SubscriberProtocol, que é pra quando a mensagem é pra todos os compradores 
            if f'{message.content}'.startswith("vencedor"):
                # Aqui provavelmente encerrariamos as atividades
                self.logger.log(self.aid.localname,
                                f'Venci o leilao!!')
                reactor.callFromThread(reactor.stop)'''