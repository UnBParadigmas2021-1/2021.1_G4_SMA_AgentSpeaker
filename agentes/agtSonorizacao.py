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

class AgenteSonorizacao(Agent):

    def __init__(self, aid, f):
        super(AgenteSonorizacao, self).__init__(aid=aid, debug=False)
        self.f = f
    
    def react(self, message):
        super(AgenteSonorizacao, self).react(message)
        #display_message(self.aid.localname, 'Mensagem recebida from {}'.format(message.sender.name))
        display_message(self.aid.localname, 'Inicializando aparelhos de Som')
    

class AgenteSonorizacaoDesligada(Agent):

    def __init__(self, aid, f):
        super(AgenteSonorizacaoDesligada, self).__init__(aid=aid, debug=False)
        self.f = f
    
    def react(self, message):
        super(AgenteSonorizacaoDesligada, self).react(message)
        #display_message(self.aid.localname, 'Mensagem recebida from {}'.format(message.sender.name))
        display_message(self.aid.localname, 'Desligando aparelhos de Som')
