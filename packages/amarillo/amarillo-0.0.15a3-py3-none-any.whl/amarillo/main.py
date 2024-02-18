import logging.config
import importlib
import pkgutil

import uvicorn
import mimetypes
from starlette.staticfiles import StaticFiles

import amarillo.plugins
from amarillo.configuration import configure_services, configure_admin_token
from amarillo.routers import carpool, agency, agencyconf, region
from fastapi import FastAPI

# https://pydantic-docs.helpmanual.io/usage/settings/
from amarillo.views import home

logging.config.fileConfig('logging.conf', disable_existing_loggers=False)
logger = logging.getLogger("main")

logger.info("Hello Amarillo!")

app = FastAPI(title="Amarillo - The Carpooling Intermediary",
              description="This service allows carpool agencies to publish "
                          "their trip offers, so routing services may suggest "
                          "them as trip options. For carpool offers, only the "
                          "minimum required information (origin/destination, "
                          "optionally intermediate stops, departure time and a "
                          "deep link for booking/contacting the driver) needs to "
                          "be published, booking/contact exchange is to be "
                          "handled by the publishing agency.",
              version="0.0.1",
              # TODO 404
              terms_of_service="http://mfdz.de/carpool-hub-terms/",
              contact={
                  # "name": "unused",
                  # "url": "http://unused",
                  "email": "info@mfdz.de",
              },
              license_info={
                  "name": "AGPL-3.0 License",
                  "url": "https://www.gnu.org/licenses/agpl-3.0.de.html",
              },
              openapi_tags=[
                  {
                      "name": "carpool",
                      # "description": "Find out more about Amarillo - the carpooling intermediary",
                      "externalDocs": {
                          "description": "Find out more about Amarillo - the carpooling intermediary",
                          "url": "https://github.com/mfdz/amarillo",
                      },
                  }],
              servers=[
                  {
                      "description": "MobiData BW Amarillo service",
                      "url": "https://amarillo.mobidata-bw.de"
                  },
                  {
                      "description": "DABB bbnavi Amarillo service",
                      "url": "https://amarillo.bbnavi.de"
                  },
                  {
                      "description": "Demo server by MFDZ",
                      "url": "https://amarillo.mfdz.de"
                  },
                  {
                      "description": "Dev server for development",
                      "url": "https://amarillo-dev.mfdz.de"
                  },
                  {
                      "description": "Localhost for development",
                      "url": "http://localhost:8000"
                  }
              ],
              redoc_url=None
              )

app.include_router(carpool.router)
app.include_router(agency.router)
app.include_router(agencyconf.router)
app.include_router(region.router)


def iter_namespace(ns_pkg):
     # Source: https://packaging.python.org/guides/creating-and-discovering-plugins/
    return pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + ".")

def load_plugins():
    discovered_plugins = {
        name: importlib.import_module(name)
        for finder, name, ispkg
        in iter_namespace(amarillo.plugins)
    }
    print(f"Discovered plugins: {list(discovered_plugins.keys())}")

    for name, module in discovered_plugins.items():
        if hasattr(module, "setup"):
            print(f"Running setup function for {name}")
            module.setup(app)

        else: print(f"Did not find setup function for {name}")

def configure():
    configure_admin_token()
    configure_services()
    configure_routing()
    load_plugins()


def configure_routing():
    mimetypes.add_type('application/x-protobuf', '.pbf')
    app.mount('/static', StaticFiles(directory='static'), name='static')
    app.mount('/gtfs', StaticFiles(directory='data/gtfs'), name='gtfs')
    app.include_router(home.router)


if __name__ == "__main__":
    configure()
    uvicorn.run(app, host="0.0.0.0", port=8000)
else:
    configure()
