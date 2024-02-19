from llm_party.attendee.default.default_attendee_trait import FacilitatorTrait
from llm_party import RawLLMAgent
from llm_party import AttendeeTraitBase
from typing import Final, List

class GPTStaffTrait(AttendeeTraitBase):
    character_list: Final[List[str]] = [
        "gpt_staff"
    ]

class GPTProductOwner(RawLLMAgent):
    """
    This role is for the product owner of the GPT project.
    Because it has the FacilitatorTrait, it can terminate the session.
    """
    character_classes = [FacilitatorTrait, GPTStaffTrait]

class GPTInnovativeManager(RawLLMAgent):
    pass
