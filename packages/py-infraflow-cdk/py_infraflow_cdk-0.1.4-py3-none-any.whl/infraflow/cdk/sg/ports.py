from typing import Union

from aws_cdk import IResource
from aws_cdk.aws_ec2 import Port, Protocol
from aws_cdk import aws_rds as rds
from aws_cdk import aws_elasticache as cache
from aws_cdk import aws_elasticsearch as search

postgres_port = Port.tcp(5432)
mysql_port = Port.tcp(3306)
redis_port = Port.tcp(6379)
opensearch_port = Port.tcp(9200)
https_port = Port.tcp(443)
http_port = Port.tcp(80)
http_alt_port = Port.tcp(8080)
all_tcp = Port.all_tcp()


def port_for(resource: Union[rds.DatabaseInstance, search.IDomain]):
    if isinstance(resource, rds.DatabaseInstance):
        return Port.tcp(resource.instance_endpoint.port)
    elif isinstance(resource, search.Domain):
        return opensearch_port



