from pade.behaviours.protocols import FipaSubscribeProtocol
from pade.misc.utility import display_message, call_later
from pade.acl.messages import ACLMessage, AID
from pade.core.agent import Agent
from printFilme import print_movie

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

    def send_message(self, message_text, destino):
        message = ACLMessage(ACLMessage.INFORM)
        message.add_receiver(AID(destino))
        message.set_content(message_text)
        self.send(message)
        display_message(self.aid.localname, message_text)

    def on_start(self):
        super(AgenteProjetor,self).on_start()
        display_message
        call_later(8.0, self.send_message, "Preparando para começar o filme...", "cortina")
        
    
    def react(self, message):
        super(AgenteProjetor, self).react(message)

        if self.f.filter(message):
            if f'{message.content}'.startswith("Estabelecendo"):
                display_message(self.aid.localname, "Começando o filme")
                print_movie()
                call_later(8.0, self.send_message, "Filme acabou :(", "sonorizacao")
            
            if f'{message.content}'.startswith("Abrindo"):
                display_message(self.aid.localname, "Projetor desligado.")

