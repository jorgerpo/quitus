import os
from app.api.utils.tools import str2bool

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))

# PROJECT
PROJECT_TITLE = os.getenv("PROJECT_TITLE","NO TITLE")
PROJECT_DESC = os.getenv("PROJECT_DESC","NOT A PROJECT")
PROJECT_VERSION = os.getenv("PROJECT_VERSION","0")
OPENAPI_JSON = os.getenv("OPENAPI_JSON","/api/v1/cisco-api.json")

# POSTGRES
POSTGRES_HOST = os.getenv("POSTGRES_HOST","HOST")
POSTGRES_USER = os.getenv("POSTGRES_USER","USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD","PASS")
POSTGRES_DB = os.getenv("POSTGRES_DB","DB")
SQLALCHEMY_DATABASE_URI = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DB}"
)

# REDIS
# REDIS_HOST = os.getenv("REDIS_HOST")
# REDIS_PORT = os.getenv("REDIS_PORT")
# REDIS_DB = os.getenv("REDIS_DB")

# API
API_V1_STR = os.getenv("API_V1_STR")

# SECURITY APIKEY
APIKEY_HEADER_NAME=os.getenv("APIKEY_HEADER_NAME")
APIKEY_HEADER_TOKEN=os.getenv("APIKEY_HEADER_TOKEN")

# DEPLOY LOCK DIR
LOCK_DIR = os.getenv("LOCK_DIR")

# JINJA
TEMPLATES = {
    "vlan_get_one": ROOT_DIR + "/templates/vlan/get/get.j2",
    "vlan_get_multi": ROOT_DIR + "/templates/vlan/get_multi/get_multi.j2",
    "vlan_add": ROOT_DIR + "/templates/vlan/add/add.j2",
    "vlan_delete": ROOT_DIR + "/templates/vlan/delete/delete.j2",
    "interface_get_one": ROOT_DIR + "/templates/interface/get/get.j2",
    "interface_get_multi": ROOT_DIR + "/templates/interface/get_multi/get_multi.j2",
    "interface_add": ROOT_DIR + "/templates/interface/add/add.j2",
    "interface_delete": ROOT_DIR + "/templates/interface/delete/delete.j2",
    "vlan_interface_add": ROOT_DIR + "/templates/vlan_interface/add/add.j2",
    "vlan_interface_delete": ROOT_DIR + "/templates/vlan_interface/delete/delete.j2"
}

# DEFAULT DRYRUN
DRYRUN = str2bool(os.getenv("DRYRUN"))