import os.path
HOME=os.environ["HOME"]
DEFAULT_PATH=os.path.join(HOME, ".config", "idoc", "logging.yaml")

def generate_logging_config(path=DEFAULT_PATH):

    config="""
version: 1
disable_existing_loggers: true
formatters:
simple:
    format: '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
handlers:
console:
    class: logging.StreamHandler
    level: DEBUG
    formatter: simple
    stream: ext://sys.stdout
loggers:
idoc:
    level: WARNING 
    handlers: [console]
    propagate: no
    """

    folder=os.path.dirname(path)
    os.makedirs(folder, exist_ok=True)

    with open(path, "w") as handle:
        handle.write(config)
