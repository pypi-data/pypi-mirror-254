from llm_party.model.session_models import LLMAgent
from llm_party.attendee.base.base_trait import AttendeeTraitBase



class RawLLMAgent(LLMAgent, AttendeeTraitBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Call the __init__ method of LLMAgent
        AttendeeTraitBase.__init__(self)  # Call the __init__ method of BaseAttendeeTrait
