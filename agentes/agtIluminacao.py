from time import sleep
from pade.behaviours.protocols import FipaSubscribeProtocol
from pade.misc.utility import display_message, call_later
from pade.acl.messages import ACLMessage
from pade.core.agent import Agent
from pade.acl.aid import AID
from twisted.internet import reactor

class SubscriberProtocol(FipaSubscribeProtocol):
    def __init__(self, agent, message):
        super(SubscriberProtocol, self).__init__(agent, message, is_initiator=True)
    
    def handle_agree(self, message):
        display_message(self.agent.aid.localname, 'Confirmacao recebida')
    
    def handle_inform(self, message):
        self.agent.react(message.content)


class AgenteIluminacao(Agent):
    def __init__(self, aid, f):
        super(AgenteIluminacao, self).__init__(aid=aid)
        self.f = f
    
    def send_message(self, message_text):
        message = ACLMessage(ACLMessage.INFORM)
        message.add_receiver(AID('projetor'))
        message.set_content(message_text)
        self.send(message)
    
    def launch_subscriber_protocol(self):
        message = ACLMessage(ACLMessage.SUBSCRIBE)
        message.set_protocol(ACLMessage.FIPA_SUBSCRIBE_PROTOCOL)
        message.set_content(f'{self.aid.localname}')
        message.add_receiver(AID('projetor'))
        self.protocol = SubscriberProtocol(self, message)
        self.behaviours.append(self.protocol)
        self.protocol.on_start()

    def on_start(self):
        super(AgenteIluminacao, self).on_start()
        call_later(4.0, self.launch_subscriber_protocol)

    def react(self, message):
        super(AgenteIluminacao, self).react(message)

        if self.f.filter(message):
            if f'{message.content}'.startswith("Preparando"):
                display_message(self.agent.aid.localname, 'Oi')
