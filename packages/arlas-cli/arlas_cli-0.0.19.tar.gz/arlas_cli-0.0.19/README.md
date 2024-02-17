# ARLAS Command line for collection management

```
arlas_cli arlas_cli_versions
                                                                                                                                                                             
 Usage: python -m arlas.cli.cli [OPTIONS] ARLAS_CONFIGURATION COMMAND [ARGS]...                                                                                              
                                                                                                                                                                             
╭─ Arguments ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *    arlas_configuration      TEXT  Name of the ARLAS configuration to use from your configuration file (/Users/gaudan/.arlas/cli/configuration.yaml) [default: None]     │
│                                     [required]                                                                                                                            │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.                                                                                                   │
│ --show-completion             Show completion for the current shell, to copy it or customize the installation.                                                            │
│ --help                        Show this message and exit.                                                                                                                 │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ collections                                                                                                                                                               │
│ indices                                                                                                                                                                   │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

```

Actions on collections:

```
arlas_cli arlas_cli_versions
                                                                                                                                                                             
 Usage: python -m arlas.cli.cli ARLAS_CONFIGURATION collections                                                                                                              
            [OPTIONS] COMMAND [ARGS]...                                                                                                                                      
                                                                                                                                                                             
╭─ Options ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                                                                                                               │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ count             Count the number of hits within a collection (or all collection if not provided)                                                                        │
│ create            Create a collection                                                                                                                                     │
│ describe          Describe a collection                                                                                                                                   │
│ list              List collections                                                                                                                                        │
│ sample            Display a sample of a collection                                                                                                                        │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

```
