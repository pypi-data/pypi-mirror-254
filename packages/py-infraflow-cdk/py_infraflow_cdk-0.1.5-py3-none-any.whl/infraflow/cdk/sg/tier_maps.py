from aws_cdk.aws_ecs import Cluster, FargateService, IService, ICluster
from aws_cdk.aws_lambda import Function
from aws_cdk.aws_rds import DatabaseInstance, DatabaseCluster, IDatabaseCluster, IDatabaseInstance
from aws_cdk.aws_elasticsearch import IDomain, Domain
from aws_cdk.aws_elasticache import CfnCacheCluster
from aws_cdk.aws_apigateway import RestApi, IRestApi

app_services = [
    Function,
    Cluster, FargateService, IService, ICluster
]

db_services = [
    DatabaseInstance, DatabaseCluster, IDatabaseCluster, IDatabaseInstance,
    IDomain, Domain,
    CfnCacheCluster
]

web_services = [
    RestApi, IRestApi
]