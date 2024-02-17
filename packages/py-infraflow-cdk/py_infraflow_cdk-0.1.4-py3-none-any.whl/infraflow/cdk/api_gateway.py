import aws_cdk.aws_apigateway as apigateway
from constructs import Construct


class ApiGatewayFactory:
    def __init__(self, scope: Construct, name: str):
        self.api = apigateway.RestApi(scope, name)

    def add_lambda(self, handler):
        self.api.root.add_resource()