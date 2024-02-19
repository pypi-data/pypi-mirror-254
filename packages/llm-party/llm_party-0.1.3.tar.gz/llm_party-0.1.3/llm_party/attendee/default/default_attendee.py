from llm_party.attendee.default.default_attendee_trait import FacilitatorTrait, CommunicatorTrait
from llm_party import RawLLMAgent


class FacilitatorAgent(RawLLMAgent):
    character_classes = [FacilitatorTrait, CommunicatorTrait]