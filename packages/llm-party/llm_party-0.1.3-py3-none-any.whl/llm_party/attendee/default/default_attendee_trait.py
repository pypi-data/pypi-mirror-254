from typing import Final, List
from llm_party.attendee.base.base_trait import AttendeeTraitBase


class FacilitatorTrait(AttendeeTraitBase):
    # This defines the character for the facilitator.
    # The item must correspond to the keys defined in YAML files such as "default_instruction.yaml".
    character_list: Final[List[str]] = [
        "introduce_oneself",
        "can_terminate"
    ]

class CommunicatorTrait(AttendeeTraitBase):
    character_list: Final[List[str]] = [
        "is_good_at_communication"
    ]
