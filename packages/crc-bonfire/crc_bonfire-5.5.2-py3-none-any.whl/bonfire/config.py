import logging
import os
import shutil
import subprocess
from pathlib import Path

from dotenv import load_dotenv
from pkg_resources import resource_filename

from bonfire.utils import FatalError, get_config_path, load_file

log = logging.getLogger(__name__)


DEFAULT_CONFIG_PATH = get_config_path().joinpath("config.yaml")
DEFAULT_ENV_PATH = get_config_path().joinpath("env")
DEFAULT_SECRETS_DIR = get_config_path().joinpath("secrets")

DEFAULT_NAMESPACE_POOL = "default"

DEFAULT_CLOWDENV_TEMPLATE = resource_filename(
    "bonfire", "resources/local-cluster-clowdenvironment.yaml"
)
EPHEMERAL_CLUSTER_CLOWDENV_TEMPLATE = resource_filename(
    "bonfire", "resources/ephemeral-cluster-clowdenvironment.yaml"
)
DEFAULT_IQE_CJI_TEMPLATE = resource_filename("bonfire", "resources/default-iqe-cji.yaml")
DEFAULT_CONFIG_DATA = resource_filename("bonfire", "resources/default_config.yaml")
DEFAULT_RESERVATION_TEMPLATE = resource_filename("bonfire", "resources/reservation-template.yaml")

DEFAULT_GRAPHQL_URL = "https://app-interface.apps.appsrep05ue1.zqxk.p1.openshiftapps.com/graphql"

DEFAULT_ELASTICSEARCH_HOST = "https://localhost:9200/search-bonfire/_doc"
DEFAULT_ENABLE_TELEMETRY = "false"

ENV_FILE = str(DEFAULT_ENV_PATH.absolute()) if DEFAULT_ENV_PATH.exists() else ""
load_dotenv(ENV_FILE)

# used in app-sre jenkins jobs
APP_INTERFACE_BASE_URL = os.getenv("APP_INTERFACE_BASE_URL")
APP_INTERFACE_USERNAME = os.getenv("APP_INTERFACE_USERNAME")
APP_INTERFACE_PASSWORD = os.getenv("APP_INTERFACE_PASSWORD")
QONTRACT_BASE_URL = os.getenv(
    "QONTRACT_BASE_URL",
    f"https://{APP_INTERFACE_BASE_URL}/graphql" if APP_INTERFACE_BASE_URL else DEFAULT_GRAPHQL_URL,
)
QONTRACT_USERNAME = os.getenv("QONTRACT_USERNAME", APP_INTERFACE_USERNAME or None)
QONTRACT_PASSWORD = os.getenv("QONTRACT_PASSWORD", APP_INTERFACE_PASSWORD or None)
QONTRACT_TOKEN = os.getenv("QONTRACT_TOKEN")

BASE_NAMESPACE_PATH = os.getenv(
    "BASE_NAMESPACE_PATH",
    "/services/insights/ephemeral/namespaces/ephemeral-base.yml",
)
EPHEMERAL_ENV_NAME = os.getenv("EPHEMERAL_ENV_NAME", "insights-ephemeral")

# can be used to set name of 'requester' on namespace reservations
BONFIRE_NS_REQUESTER = os.getenv("BONFIRE_NS_REQUESTER")
# set to true when bonfire is running via automation using a bot acct (not an end user)
BONFIRE_BOT = os.getenv("BONFIRE_BOT", "false").lower() == "true"

BONFIRE_DEFAULT_PREFER = str(os.getenv("BONFIRE_DEFAULT_PREFER", "ENV_NAME=frontends")).split(",")
BONFIRE_DEFAULT_REF_ENV = str(os.getenv("BONFIRE_DEFAULT_REF_ENV", "insights-stage"))
BONFIRE_DEFAULT_FALLBACK_REF_ENV = str(
    os.getenv("BONFIRE_DEFAULT_FALLBACK_REF_ENV", "insights-stage")
)

# list of apps we will not remove resource requests/limits for
TRUSTED_APPS = ["host-inventory"]
if os.getenv("BONFIRE_TRUSTED_APPS"):
    TRUSTED_APPS = os.getenv("BONFIRE_TRUSTED_APPS").split(",")

# list of components we will not remove requests/limits for
TRUSTED_COMPONENTS = []
if os.getenv("BONFIRE_TRUSTED_COMPONENTS"):
    TRUSTED_COMPONENTS = os.getenv("BONFIRE_TRUSTED_COMPONENTS").split(",")

ELASTICSEARCH_HOST = os.getenv("ELASTICSEARCH_HOST", DEFAULT_ELASTICSEARCH_HOST)
ELASTICSEARCH_APIKEY = os.getenv("ELASTICSEARCH_APIKEY")
if ELASTICSEARCH_APIKEY:
    ELASTICSEARCH_APIKEY = "ApiKey " + ELASTICSEARCH_APIKEY
ENABLE_TELEMETRY = os.getenv("ENABLE_TELEMETRY", DEFAULT_ENABLE_TELEMETRY).lower() == "true"

DEFAULT_FRONTEND_DEPENDENCIES = (
    "chrome-service",
    "landing-page-frontend",
    "insights-chrome",
    "insights-dashboard",
    "rbac",
    "rbac-frontend",
    "settings-frontend",
    "host-inventory",
    "host-inventory-frontend",
    "unleash-proxy",
)


def _get_auto_added_frontend_dependencies():
    env_var = os.getenv("BONFIRE_FRONTEND_DEPENDENCIES")

    if env_var is None:
        return set(DEFAULT_FRONTEND_DEPENDENCIES)
    return set([val.strip() for val in env_var.split(",") if val.strip()])


AUTO_ADDED_FRONTEND_DEPENDENCIES = _get_auto_added_frontend_dependencies()


def write_default_config(outpath=None):
    outpath = Path(outpath) if outpath else DEFAULT_CONFIG_PATH
    outpath.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    inpath = Path(DEFAULT_CONFIG_DATA)
    shutil.copy(inpath, outpath)
    outpath.chmod(0o600)
    log.info("saved config to: %s", outpath.absolute())


def edit_default_config(confpath=None):
    confpath = Path(confpath) if confpath else DEFAULT_CONFIG_PATH
    if os.getenv("EDITOR") is None:
        log.info("No $EDITOR set, exiting.")
        return

    subprocess.call([os.getenv("EDITOR"), confpath])


def load_config(config_path=None):
    if config_path:
        log.debug("user provided explicit config path: %s", config_path)
        config_path = Path(config_path)
        if not config_path.exists():
            raise FatalError(f"provided config file path '{str(config_path)}' does not exist")
    else:
        log.debug("using default config path: %s", DEFAULT_CONFIG_PATH)
        config_path = DEFAULT_CONFIG_PATH
        if not config_path.exists():
            log.info("default config not found, creating")
            write_default_config()

    log.info("reading config from: %s", str(config_path.absolute()))
    local_config_data = load_file(config_path)

    return local_config_data
