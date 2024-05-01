from diagrams import Diagram

from diagrams.onprem.client import Users, User
from diagrams.onprem.vcs import Github
from diagrams.onprem.container import Docker
from diagrams.azure.compute import KubernetesServices

with Diagram(
    "Architecture",
    ".docs/diagrams/architecture",
    direction="LR",
    show=False,
    graph_attr={
        "pad": "0.3",
    },
):
 
    
    users = Users("User")
        
    image_registry = Docker("Docker HUB")
        
    container = KubernetesServices("AKS")
        
    github = Github("Actions")
    
    dev = User("Dev")

    users >> container << image_registry << github << dev