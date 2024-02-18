import uuid


class ServiceAuthorityDeclaration:
    def __init__(self, id, authority, display_name, tier):
        self.uuid = uuid.UUID(id)
        self.authority = authority
        self.display_name = display_name
        self.tier = tier
