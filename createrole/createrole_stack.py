from aws_cdk import (
    aws_iam as iam,
    core
)

class CreateroleStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        iam_principal = iam.ServicePrincipal('sqs.amazonaws.com')
        role = iam.Role(self,"MyCDKRole", assumed_by=iam_principal )
        
