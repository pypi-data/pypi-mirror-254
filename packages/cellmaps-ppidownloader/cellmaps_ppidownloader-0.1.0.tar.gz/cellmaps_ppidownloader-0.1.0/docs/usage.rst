=====
Usage
=====

This script supports the loading of AP-MS data either in Bioplex format via `--edgelist` and `--baitlist` flags,
or in CM4AI format via the `--cm4ai_table` flag.

In a project
--------------

To use cellmaps_ppidownloader in a project::

    import cellmaps_ppidownloader

On the command line
---------------------

For information invoke :code:`cellmaps_ppidownloadercmd.py -h`

**Usage**

.. code-block::

    cellmaps_ppidownloadercmd.py OUTPUT_DIRECTORY [--provenance PROVENANCE_PATH] [OPTIONS]

**Arguments**

- ``outdir``
    The directory where the output will be written to.

*Required*


- ``--provenance PROVENANCE_PATH``
    Path to file containing provenance information about input files in JSON format.

*Optional but either `edgelist` and `baitlist` parameters, or `cm4ai_table` parameter is required*

- ``--edgelist``
    APMS edgelist TSV file in the format:

    .. code-block::

        GeneID1    Symbol1    GeneID2    Symbol2
        10159      ATP6AP2    2          A2M

- ``--baitlist``
    APMS baitlist TSV file in the format:

    .. code-block::

        GeneSymbol    GeneID    # Interactors
        "ADA"         "100"     1

- ``--cm4ai_table``
    A `.tsv` file from CM4AI RO-Crate that should contain at least the following columns: Bait, Prey, logOddsScore, FoldChange.x, and BFDR.x.

*Optional*

- ``--edgelist_geneid_one_col``
    Specifies the name of the column containing the ensemble Gene ID 1 in the `--edgelist` file. Default is `GeneID1`.

- ``--edgelist_symbol_one_col``
    Specifies the name of the column containing Gene Symbol 1 in the `--edgelist` file. Default is `Symbol1`.

- ``--edgelist_geneid_two_col``
    Specifies the name of the column containing the ensemble Gene ID 2 in the `--edgelist` file. Default is `GeneID2`.

- ``--edgelist_symbol_two_col``
    Specifies the name of the column containing Gene Symbol 2 in the `--edgelist` file. Default is `Symbol2`.

- ``--baitlist_symbol_col``
    Specifies the name of the column containing the Gene Symbol in the `--baitlist` file. Default is `GeneSymbol`.

- ``--baitlist_geneid_col``
    Specifies the name of the column containing the ensemble Gene ID in the `--baitlist` file. Default is `GeneID`.

- ``--baitlist_numinteractors_col``
    Specifies the name of the column containing the number of interactors in the `--baitlist` file. Default is `# Interactors`.

- ``--logconf``
    Path to the python logging configuration file.

- ``--skip_logging``
    If set, certain log files will not be created.

- ``--verbose`` or ``-v``
    Increases the verbosity of the logger to standard error for log messages in this module. The levels are as follows:

    .. code-block::

        -v     = ERROR
        -vv    = WARNING
        -vvv   = INFO
        -vvvv  = DEBUG
        -vvvvv = NOTSET

    Default is no logging.

- ``--version``
    Displays the version of the `cellmaps_ppidownloader` program.


**Example usage**

The example file can be downloaded from `cm4ai.org <https://cm4ai.org>`. Go to Products -> Data, log in, and download file for AP-MS with the desired treatment,
then unpack the tar gz (tar -xzvf filename.tar.gz).

.. code-block::

   cellmaps_ppidownloadercmd.py ./cellmaps_ppidownloader_outdir  --cm4ai_table path/to/downloaded/unpacked/dir --provenance examples/provenance.json


Alternatively, use the files in the example directory in the repository:

1) bait list file: TSV file of baits used for AP-MS experiments
2) edge list file: TSV file of edges for protein interaction network
3) provenance: file containing provenance information about input files in JSON format (see sample provenance file in examples folder)

.. code-block::

   cellmaps_ppidownloadercmd.py ./cellmaps_ppidownloader_outdir --edgelist examples/edgelist.tsv --baitlist examples/baitlist.tsv --provenance examples/provenance.json

Via Docker
---------------

**Example usage**

.. code-block::

   Coming soon...

