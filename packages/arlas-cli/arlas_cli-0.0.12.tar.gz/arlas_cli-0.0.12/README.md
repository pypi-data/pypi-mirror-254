# ARLAS Command line for collection management

```
Usage: python -m arlas.cli.cli [OPTIONS] ARLAS_CONFIGURATION COMMAND [ARGS]...

Arguments:
  ARLAS_CONFIGURATION  Name of the ARLAS configuration to use from your
                       configuration file
                       (/Users/gaudan/.arlas/cli/configuration.yaml)
                       [required]

Options:
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.
  --help                          Show this message and exit.

Commands:
  collections
  indices
```

Actions on collections:

```
Usage: python -m arlas.cli.cli ARLAS_CONFIGURATION collections 
           [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  count     Count the number of hits within a collection (or all...
  create    Create a collection
  describe  Describe a collection
  list      List collections
  sample    Display a sample of a collection
```
