"""
NetForge Stateful ACL Rule Manager
Manages dynamic IP blacklist/whitelist rules.
"""

class ACLRuleManager:
    def __init__(self):
        self.rules = []

    def add_rule(self, ip_cidr: str, action: str = "ALLOW"):
        self.rules.append({"cidr": ip_cidr, "action": action})
