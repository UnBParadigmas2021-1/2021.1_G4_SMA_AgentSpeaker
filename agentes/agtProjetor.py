from sys import modules
from pade.behaviours.protocols import FipaSubscribeProtocol, TimedBehaviour
from pade.misc.utility import display_message
from pade.acl.messages import ACLMessage, AID
from pade.core.agent import Agent

class PublisherProtocol(FipaSubscribeProtocol):
    def __init__(self, agent):
        super(PublisherProtocol, self).__init__(agent, message=None, is_initiator=False)

    def handle_subscribe(self, message):
        self.register(message.sender)
        response = message.create_reply()
        response.set_performative(ACLMessage.AGREE)
        response. ser_content('OK')
        self.agent.send(response)

    def handle_cancel(self, message):
        self.deregister(self,message.sender)
    
    def notify(self, message):
        super(PublisherProtocol, self).notify(message)


class AgenteProjetor(Agent):
    def __init__(self, aid, f):
        super(AgenteProjetor, self).__init__(aid=aid, debug=False)
        self.f = f
        self.protocol = PublisherProtocol(self)
        self.behaviours.append(self.protocol)
    
    def on_start(self, message):
        super(AgenteProjetor,self).on_start()
        message.set_content(f'Preparando para o filme')
        self.notify(message)
        
    
    def react(self, message):
        super(AgenteProjetor, self).react(message)

        if self.f.filter(message):
            if f'{message.content}'.startswith("OI"):
                message.set_content(f'Começando o filme')
                self.notify(message)
