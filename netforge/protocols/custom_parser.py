"""
NetForge Custom Protocol Extension Parser
Defines user-extensible binary packet field decoders.
"""

class CustomProtocolExtension:
    def __init__(self, name: str = "CustomProto"):
        self.name = name

    def parse_header(self, raw_bytes: bytes) -> dict:
        return {"protocol": self.name, "length": len(raw_bytes), "status": "valid"}
