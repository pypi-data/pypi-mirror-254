from typing import Final, List, Dict
from llm_party.registry.instruction_registry import instruction_registry

class AttendeeTraitBase:
    """This is the base class for all attendee traits. It contains the "default" character. Refer to `llm_party/attendee/default/default_instruction.yaml` for "default" character.
    """

    # Used for class specific characters
    character_list: Final[List[str]] = []

    def __init__(self):
        # Used for storing all characters of the attendee. Notice that character_list is used for class specific characters.
        # - This is a dictionary of {character_key: None} to store ordered set of character keys
        self.characters: Dict[str, None] = {"default": None}

        for character in self.character_list:
            self.add_character(character)

        if hasattr(self, "character_classes"):
            for character_class in self.character_classes:
                for character in character_class.character_list:
                    self.add_character(character)

    @property
    def _character_keys(self):
        return self.characters.keys()

    def trait_instruction(self) -> str:
        return "\n".join([instruction_registry.get(character_key) for character_key in self._character_keys])

    def add_character(self, character: str) -> None:
        """
        Add a character to the attendee. If the character doesn't exist in the `InstructionRegistry`, raise a `ValueError`.
        """
        if character not in instruction_registry:
            raise ValueError(f"The character '{character}' does not exist in the InstructionRegistry.")
        self.characters[character] = None

    def remove_character(self, character: str) -> None:
        """
        Remove a character from the attendee. If the character is not in the `characters` dictionary, do nothing.
        """
        self.characters.pop(character, None)

    def has_character(self, character: str) -> bool:
        """
        Check if the attendee has a character.
        """
        return character in self.characters

    def list_characters(self) -> List[str]:
        """
        Return a list of all characters of the attendee.
        """
        return list(self.characters.keys())