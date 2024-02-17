import json
import typer
import os
import sys
from prettytable import PrettyTable

from arlas.cli.settings import Configuration, Resource
from arlas.cli.service import Service
from arlas.cli.variables import variables, configuration_file

indices = typer.Typer()


@indices.command(help="List indices", name="list")
def list_indices():
    indices = Service.list_indices(variables["arlas"])
    tab = PrettyTable(indices[0], sortby="name", align="l")
    tab.add_rows(indices[1:])
    print(tab)


@indices.command(help="Describe an index")
def describe(index: str = typer.Argument(help="index's name")):
    indices = Service.describe_index(variables["arlas"], index)
    tab = PrettyTable(indices[0], sortby="field name", align="l")
    tab.add_rows(indices[1:])
    print(tab)


@indices.command(help="Display a sample of an index")
def sample(index: str = typer.Argument(help="index's name"), pretty: bool = typer.Option(default=True), size: int = typer.Option(default=10)):
    sample = Service.sample_index(variables["arlas"], index, pretty=pretty, size=size)
    print(json.dumps(sample["hits"].get("hits", []), indent=2 if pretty else None))


@indices.command(help="Create an index")
def create(
    index: str = typer.Argument(help="index's name"),
    mapping: str = typer.Option(help="Name of the mapping within your configuration, or URL or file path"),
    shards: int = typer.Option(default=1, help="Number of shards for the index")
):
    mapping_resource = Configuration.settings.mappings.get(mapping, None)
    if not mapping_resource:
        if os.path.exists(mapping):
            mapping_resource = Resource(location=mapping)
        else:
            print("Error: model {} not found".format(mapping), file=sys.stderr)
            exit(1)
    Service.create_index(
        variables["arlas"],
        index=index,
        mapping_resource=mapping_resource,
        number_of_shards=shards)
    print("Index {} created on {}".format(index, variables["arlas"]))


@indices.command(help="Index data")
def data(
    index: str = typer.Argument(help="index's name"),
    file_path: str = typer.Argument(help="Path to the file conaining the data. Format: NDJSON"),
    bulk: int = typer.Option(default=1000, help="Bulk size for indexing data")
):
    if not os.path.exists(file_path):
        print("Error: file \"{}\" not found.".format(file_path), file=sys.stderr)
        exit(1)
    Service.load_data(variables["arlas"], index=index, file_path=file_path, bulk_size=bulk)


@indices.command(help="Delete an index")
def delete(
    index: str = typer.Argument(help="index's name")
):
    if not Configuration.settings.arlas.get(variables["arlas"]).allow_delete:
        print("Error: delete on \"{}\" is not allowed. To allow delete, change your configuration file ({}).".format(variables["arlas"], configuration_file), file=sys.stderr)
        exit(1)

    if typer.confirm("You are about to delete the index '{}' on the '{}' configuration.\n".format(index, variables["arlas"]),
                     prompt_suffix="Do you want to continue (del {} on {})?".format(index, variables["arlas"]),
                     default=False, ):
        Service.delete_index(
            variables["arlas"],
            index=index)
        print("{} has been deleted on {}.".format(index, variables["arlas"]))
