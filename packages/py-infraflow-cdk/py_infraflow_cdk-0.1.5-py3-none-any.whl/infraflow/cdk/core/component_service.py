from constructs import Construct

from infraflow.cdk.core.construct import HasEnv, ConstructWithEnv, HasDefaultSg


class ComponentService(Construct, HasEnv, HasDefaultSg):
    def __init__(self, parent:  ConstructWithEnv, id: str, **kwargs):
        super().__init__(parent, id, **kwargs)
        self.env = parent.env
        self.default_sg = parent.default_sg
