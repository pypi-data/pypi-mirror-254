
import re
import csv
import logging
import mygene
from tqdm import tqdm

from cellmaps_ppidownloader.exceptions import CellMapsPPIDownloaderError

logger = logging.getLogger(__name__)


class GeneQuery(object):
    """
    Gets information about genes from mygene
    """
    def __init__(self, mygeneinfo=mygene.MyGeneInfo()):
        """
        Constructor
        """
        self._mg = mygeneinfo

    def querymany(self, queries, species=None,
                  scopes=None,
                  fields=None):

        """
        Simple wrapper that calls MyGene querymany
        returning the results

        :param queries: list of gene ids/symbols to query
        :type queries: list
        :param species:
        :type species: str
        :param scopes:
        :type scopes: str
        :param fields:
        :type fields: list
        :return: dict from MyGene usually in format of
        :rtype: list
        """
        mygene_out = self._mg.querymany(queries,
                                        scopes=scopes,
                                        fields=fields,
                                        species=species)
        return mygene_out

    def get_symbols_for_genes(self, genelist=None,
                              scopes='_id'):
        """
        Queries for genes via GeneQuery() object passed in via
        constructor

        :param genelist: genes to query for valid symbols and ensembl ids
        :type genelist: list
        :param scopes: field to query on _id for gene id, ensemble.gene
                       for ENSEMBLE IDs
        :type scopes: str
        :return: result from mygene which is a list of dict objects where
                 each dict is of format:

                 .. code-block::

                     { 'query': 'ID',
                       '_id': 'ID', '_score': #.##,
                       'ensembl': { 'gene': 'ENSEMBLEID' },
                       'symbol': 'GENESYMBOL' }
        :rtype: list
        """
        res = self.querymany(genelist,
                             species='human',
                             scopes=scopes,
                             fields=['ensembl.gene', 'symbol'])
        return res


class GeneNodeAttributeGenerator(object):
    """
    Base class for GeneNodeAttribute Generator
    """
    def __init__(self):
        """
        Constructor
        """
        pass

    @staticmethod
    def add_geneids_to_set(gene_set=None,
                           ambiguous_gene_dict=None,
                           geneid=None):
        """
        Examines **geneid** passed in and if a comma exists
        in value split by comma and assume multiple genes.
        Adds those genes into **gene_set** and add entry
        to **ambiguous_gene_dict** with key set to each gene
        name and value set to original **geneid** value

        :param gene_set: unique set of genes
        :type gene_set: set
        :param geneid: name of gene or comma delimited string of genes
        :type geneid: str
        :return: genes found in **geneid** or None if **gene_set**
                 or **geneid** is ``None``
        :rtype: list
        """
        if gene_set is None:
            return None
        if geneid is None:
            return None

        split_str = re.split('\W*,\W*', geneid)
        gene_set.update(split_str)
        if ambiguous_gene_dict is not None:
            if len(split_str) > 1:
                for entry in split_str:
                    ambiguous_gene_dict[entry] = geneid
        return split_str

    def get_gene_node_attributes(self):
        """
        Should be implemented by subclasses

        :raises NotImplementedError: Always
        """
        raise NotImplementedError('Subclasses should implement')


class APMSGeneNodeAttributeGenerator(GeneNodeAttributeGenerator):
    """
    Creates APMS Gene Node Attributes table
    """

    def __init__(self, apms_edgelist=None, apms_baitlist=None,
                 genequery=GeneQuery()):
        """
        Constructor

        :param apms_edgelist: list of dict elements where each
                              dict is of format:

                              .. code-block::

                                  {'GeneID1': VAL,
                                   'Symbol1': VAL,
                                   'GeneID2': VAL,
                                   'Symbol2': VAL}
        :type apms_edgelist: list
        :param apms_baitlist: list of dict elements where each dict is of
                              format:

                              .. code-block::

                                  { 'GeneSymbol': VAL,
                                    'GeneID': VAL,
                                    'NumIteractors': VAL }
        :type apms_baitlist: list
        :param genequery:
        """
        super().__init__()
        self._apms_edgelist = apms_edgelist
        self._apms_baitlist = apms_baitlist
        self._genequery = genequery

    @staticmethod
    def get_apms_edgelist_from_tsvfile(tsvfile=None,
                                       geneid_one_col='GeneID1',
                                       symbol_one_col='Symbol1',
                                       geneid_two_col='GeneID2',
                                       symbol_two_col='Symbol2'):
        """
        Generates list of dicts by parsing TSV file specified
        by **tsvfile** with the
        format header column and corresponding values:

        .. code-block::

            GeneID1\tSymbol1\tGeneID2\tSymbol2

        :param tsvfile: Path to TSV file with above format
        :type tsvfile: str
        :return: list of dicts, with each dict of format:

                 .. code-block::

                      {'GeneID1': VAL,
                       'Symbol1': VAL,
                       'GeneID2': VAL,
                       'Symbol2': VAL}
        :rtype: list
        """
        edgelist = []
        with open(tsvfile, 'r') as f:
            reader = csv.DictReader(f, delimiter='\t')
            for row in reader:
                edgelist.append({'GeneID1': row[geneid_one_col],
                                 'Symbol1': row[symbol_one_col],
                                 'GeneID2': row[geneid_two_col],
                                 'Symbol2': row[symbol_two_col]})
        return edgelist

    @staticmethod
    def get_apms_baitlist_from_tsvfile(tsvfile=None,
                                       symbol_col='GeneSymbol',
                                       geneid_col='GeneID',
                                       numinteractors_col='# Interactors'):
        """
        Generates list of dicts by parsing TSV file specified
        by **tsvfile** with the
        format header column and corresponding values:

        .. code-block::

            GeneSymbol\tGeneID\t# Interactors

        :param tsvfile: Path to TSV file with above format
        :type tsvfile: str
        :return: list of dicts, with each dict of format:

                 .. code-block::

                      { 'GeneSymbol': VAL,
                        'GeneID': VAL,
                        'NumIteractors': VAL }
        :rtype: list
        """
        edgelist = []
        if tsvfile is not None:
            with open(tsvfile, 'r') as f:
                reader = csv.DictReader(f, delimiter='\t')
                for row in reader:
                    edgelist.append({'GeneSymbol': row[symbol_col],
                                     'GeneID': row[geneid_col],
                                     'NumInteractors': row[numinteractors_col]})
        return edgelist

    def get_apms_edgelist(self):
        """
        Gets apms edgelist passed in via constructor

        :return:
        :rtype: list
        """
        return self._apms_edgelist

    def _get_unique_genelist_from_edgelist(self):
        """
        Gets unique list of genes from edge list along with a
        dict for ambiguous genes which have multiple names.
        For the ambiguous genes the dict is of format:

        ``{'GENEID': 'AMBIGUOUS ID aka x,y,z'}``

        :return: (list of genes, dict of ambiguous genes)
        :rtype: list
        """
        gene_set = set()
        ambiguous_gene_dict = {}

        for row in self._apms_edgelist:
            GeneNodeAttributeGenerator.add_geneids_to_set(gene_set=gene_set,
                                                          ambiguous_gene_dict=ambiguous_gene_dict,
                                                          geneid=row['GeneID1'])
            GeneNodeAttributeGenerator.add_geneids_to_set(gene_set=gene_set,
                                                          ambiguous_gene_dict=ambiguous_gene_dict,
                                                          geneid=row['GeneID2'])
        return list(gene_set), ambiguous_gene_dict

    def _get_apms_bait_set(self):
        """
        Gets unique set of baits

        :return:
        :rtype: set
        """
        bait_set = set()
        for entry in self._apms_baitlist:
            bait_set.add(entry['GeneID'])
        return bait_set

    def get_gene_node_attributes(self):
        """
        Gene gene node attributes which is output as a list of
        dicts in this format:

        .. code-block::

            { 'GENEID': { 'name': 'GENESYMBOL',
                          'represents': 'ensemble:ENSEMBLID1;ENSEMBLID2..',
                          'ambiguous': 'ALTERNATE GENEs' }
            }



        :return: (list of dicts containing gene node attributes,
                  list of str describing any errors encountered)
        :rtype: tuple
        """
        t = tqdm(total=2, desc='Get updated gene symbols', unit='steps')

        t.update()
        genelist, ambiguous_gene_dict = self._get_unique_genelist_from_edgelist()
        t.update()
        query_res = self._genequery.get_symbols_for_genes(genelist=genelist)
        bait_set = self._get_apms_bait_set()
        errors = []
        gene_node_attrs = {}
        for x in query_res:
            if 'symbol' not in x:
                errors.append('Skipping ' + str(x) +
                              ' no symbol in query result: ' + str(x))
                logger.error(errors[-1])
                continue

            ensemblstr = 'ensembl:'
            if 'ensembl' not in x:
                errors.append('Skipping ' + str(x) +
                              ' no ensembl in query result: ' + str(x))
                logger.error(errors[-1])
                continue
            if len(x['ensembl']) > 1:
                ensemblstr += ';'.join([g['gene'] for g in x['ensembl']])
            else:
                ensemblstr += x['ensembl']['gene']

            ambiguous_str = ''
            if x['symbol'] in ambiguous_gene_dict:
                ambiguous_str = ambiguous_gene_dict[x['symbol']]

            gene_node_attrs[x['query']] = {'name': x['symbol'],
                                           'represents': ensemblstr,
                                           'ambiguous': ambiguous_str,
                                           'bait': x['query'] in bait_set}

        return gene_node_attrs, errors


class CM4AIGeneNodeAttributeGenerator(GeneNodeAttributeGenerator):
    """
    Creates APMS Gene Node Attributes table from CM4AI data
    """

    def __init__(self, apms_edgelist=None,
                 genequery=GeneQuery()):
        """
        Constructor

        :param apms_edgelist: list of dict elements where each
                              dict is of format:

                              .. code-block::

                                  {'Bait': VAL,
                                   'Prey': VAL,
                                   'logOddsScore': VAL,
                                   'FoldChange.x': VAL,
                                   'BFDR.x': VAL}
        :type apms_edgelist: list
        :param genequery:
        """
        super().__init__()
        self._raw_apms_edgelist = apms_edgelist
        self._apms_edgelist = None
        self._genequery = genequery

    @staticmethod
    def get_apms_edgelist_from_tsvfile(tsvfile=None,
                                       bait_col='Bait',
                                       prey_col='Prey',
                                       bfdr_col=None,
                                       foldchange_col=None,
                                       foldchange_cutoff=0.0,
                                       bfdr_maxcutoff=0.05):
        """
        Generates list of dicts by parsing TSV file specified
        by **tsvfile** with the
        format header column and corresponding values:

        .. code-block::

            Bait\tPrey\tBFDR.x\tFoldChange.x

        .. note::

           If BFDR.x column does not exist, no BFDR filtering will occur
           Same goes if FoldChange.x column does not exist

        :param tsvfile: Path to TSV file with above format
        :type tsvfile: str
        :param bait_col: Name of bait column
        :type bait_col: str
        :param prey_col: Name of prey column
        :type prey_col: str
        :param bfdr_col: Name of BFDR aka false discovery rate column
                         If ``None`` no BFDR filtering will occur
        :type bfdr_col: str
        :param foldchange_col: Name of FoldChange column
                               If ``None`` no FoldChange filtering will occur
        :type foldchange_col: str
        :param foldchange_cutoff: Foldchange cutoff. Only keep rows with
                                  values greater then this value.
                                  If this value is ``None`` no filtering
                                  will occur
        :type foldchange_cutoff: float
        :param bfdr_maxcutoff: BFDR cutoff. Only keep rows with BFDR
                               less then or equal to this value.
                               If this value is ``None`` no filtering will
                               occur
        :type bfdr_maxcutoff: float
        :return: list of dicts, with each dict of format:

                 .. code-block::

                      {'Bait': VAL,
                       'Prey': VAL}
        :rtype: list
        """
        edgelist = []
        with open(tsvfile, 'r') as f:
            reader = csv.DictReader(f, delimiter='\t')
            for row in reader:
                if bfdr_col is not None and bfdr_col in row\
                     and row[bfdr_col] > bfdr_maxcutoff:
                    continue
                if foldchange_col is not None and foldchange_col in row\
                     and row[foldchange_col] <= foldchange_cutoff:
                    continue
                edgelist.append({'Bait': row[bait_col],
                                 'Prey': row[prey_col]})
        return edgelist

    def _get_unique_set_from_raw_edgelist(self, colname=None):
        """
        Given a column name **colname** extract unique set of values from
        raw apms edgelist passed in via constructor

        :return:
        :rtype: set
        """
        col_set = set()
        for entry in self._raw_apms_edgelist:
            col_set.add(entry[colname])
        return col_set

    def _get_baits_to_ensemblsymbolmap(self):
        """
        Get unique set of bait names from raw apms edgelist
        and query mygene to get symbols and ensembl gene ids

        :return: original bait name to mapped to tuple
                 (id, symbol, ensembl gene id)
        :rtype: dict
        """
        bait_set = self._get_unique_set_from_raw_edgelist('Bait')
        res = self._genequery.get_symbols_for_genes(list(bait_set),
                                                    scopes='symbol')
        bait_to_id = {}
        for entry in res:

            bait_to_id[entry['query']] = (entry['_id'],
                                          entry['symbol'],
                                          entry['ensembl']['gene'])
        return bait_to_id

    def _get_prey_to_ensemblsymbolmap(self):
        """
        Get unique set of prey names from raw apms edgelist
        and query mygene to get symbols and ensembl gene ids

        :return: original bait name to mapped to tuple
                 (id, symbol, ensembl gene id)
        :rtype: dict
        """
        prey_set = self._get_unique_set_from_raw_edgelist('Prey')
        res = self._genequery.get_symbols_for_genes(list(prey_set),
                                                    scopes='uniprot')
        prey_to_id = {}
        for entry in res:
            ensemblstr = ''
            if 'ensembl' not in entry:
                logger.error(str(entry) + ' no ensembl found')
                continue
            if isinstance(entry['ensembl'], list):
                ensemblstr += ';'.join([g['gene'] for g in entry['ensembl']])
            else:
                ensemblstr = entry['ensembl']['gene']
            prey_to_id[entry['query']] = (entry['_id'],
                                          entry['symbol'],
                                          ensemblstr)
        return prey_to_id

    def get_apms_edgelist(self):
        """
        Gets apms edgelist

        :return:
        :rtype: list
        """
        if self._apms_edgelist is not None:
            return self._apms_edgelist

        # we need to generate this list
        baits_to_idmap = self._get_baits_to_ensemblsymbolmap()

        prey_set = self._get_unique_set_from_raw_edgelist('Prey')

        prey_to_idmap = self._get_prey_to_ensemblsymbolmap()
        self._apms_edgelist = []
        for row in self._raw_apms_edgelist:
            if row['Bait'] not in baits_to_idmap:
                logger.warning('Bait ' + str(row['Bait']) + ' not in map. Skipping')
                continue
            if row['Prey'] not in prey_to_idmap:
                logger.warning('Prey ' + str(row['Prey'] + ' not in map. Skipping'))
                continue
            bait_tuple = baits_to_idmap[row['Bait']]
            prey_tuple = prey_to_idmap[row['Prey']]
            self._apms_edgelist.append({'GeneID1': bait_tuple[0],
                                        'Symbol1': bait_tuple[1],
                                        'Ensembl1': bait_tuple[2],
                                        'GeneID2': prey_tuple[0],
                                        'Symbol2': prey_tuple[1],
                                        'Ensembl2': prey_tuple[2]})
        return self._apms_edgelist

    def _get_apms_bait_set(self):
        """
        Gets unique set of baits

        :return:
        :rtype: set
        """
        bait_set = set()
        for entry in self._apms_baitlist:
            bait_set.add(entry['GeneID'])
        return bait_set

    def get_gene_node_attributes(self):
        """
        Gene gene node attributes which is output as a list of
        dicts in this format:

        .. code-block::

            { 'GENEID': { 'name': 'GENESYMBOL',
                          'represents': 'ensemble:ENSEMBLID1;ENSEMBLID2..',
                          'ambiguous': 'ALTERNATE GENEs',
                          'bait': True or False}
            }



        :return: (list of dicts containing gene node attributes,
                  list of str describing any errors encountered)
        :rtype: tuple
        """
        self.get_apms_edgelist()
        errors = []
        gene_node_attrs = {}
        for i in ['1', '2']:
            if i == '1':
                bait = True
            else:
                bait = False
            for x in self._apms_edgelist:
                if x['GeneID' + i] in gene_node_attrs:
                    continue
                ensemblstr = 'ensembl:' + x['Ensembl' + i]
                gene_node_attrs[x['GeneID' + i]] = {'name': x['Symbol' + i],
                                                    'represents': ensemblstr,
                                                    'ambiguous': '',
                                                    'bait': bait}

        return gene_node_attrs, errors

