#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Integration Tests for `cellmaps_ppidownloader` package."""

import os
import csv
import tempfile
import shutil
import unittest
from cellmaps_ppidownloader import cellmaps_ppidownloadercmd

SKIP_REASON = 'CELLMAPS_PPIDOWNLOADER_INTEGRATION_TEST ' \
              'environment variable not set, cannot run integration ' \
              'tests'


@unittest.skipUnless(os.getenv('CELLMAPS_PPIDOWNLOADER_INTEGRATION_TEST') is not None, SKIP_REASON)
class TestIntegrationCellmaps_downloader(unittest.TestCase):
    """Tests for `cellmaps_ppidownloader` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def get_test_data_dir(self):
        """
        get test data dir
        :return:
        """
        return os.path.join(os.path.dirname(__file__), 'data')

    def get_test_provenance(self):
        """
        Gets test provenance file path
        :return:
        """
        return os.path.join(self.get_test_data_dir(), 'test_provenance.json')

    def get_baitlist(self):
        """
        Gets baitlist file path
        :return:
        """
        return os.path.join(self.get_test_data_dir(), 'baitlist.tsv')

    def get_edgelist(self):
        """
        Gets edgelist file path
        :return:
        """
        return os.path.join(self.get_test_data_dir(), 'edgelist.tsv')

    def test_download_with_edgelist_and_baitlist(self):
        """Tests parse arguments"""
        temp_dir = tempfile.mkdtemp()
        try:
            baitlist = self.get_baitlist()
            edgelist = self.get_edgelist()
            run_dir = os.path.join(temp_dir, 'run')
            provenance = self.get_test_provenance()
            res = cellmaps_ppidownloadercmd.main(['myprog.py', run_dir,
                                                  '--edgelist', edgelist,
                                                  '--baitlist', baitlist,
                                                  '--provenance', provenance,
                                                  '--skip_logging'])
            self.assertEqual(0, res)
            ppi_edgelist = os.path.join(run_dir, 'ppi_edgelist.tsv')
            self.assertTrue(os.path.isfile(ppi_edgelist))
            entries = []
            with open(ppi_edgelist, 'r', newline='') as f:
                reader = csv.DictReader(f, delimiter='\t')
                for row in reader:
                    entries.append(row)

            self.assertEqual(2783, len(entries))
            self.assertEqual({'geneA': 'PIK3CA-DT', 'geneB': 'MED19'},
                             entries[0], 'If symbol changes this may fail')
            self.assertEqual({'geneA': 'PIK3CA-DT', 'geneB': 'IVNS1ABP'},
                             entries[2782], 'If symbol changes this may fail')

            # Todo: add more checks on the results

        finally:
                shutil.rmtree(temp_dir)

    def test_download_with_only_edgelist(self):
        """Tests parse arguments"""
        temp_dir = tempfile.mkdtemp()
        try:
            edgelist = self.get_edgelist()
            run_dir = os.path.join(temp_dir, 'run')
            provenance = self.get_test_provenance()
            res = cellmaps_ppidownloadercmd.main(['myprog.py', run_dir,
                                                  '--edgelist', edgelist,
                                                  '--provenance', provenance,
                                                  '--skip_logging'])
            self.assertEqual(0, res)
            ppi_edgelist = os.path.join(run_dir, 'ppi_edgelist.tsv')
            self.assertTrue(os.path.isfile(ppi_edgelist))
            entries = []
            with open(ppi_edgelist, 'r', newline='') as f:
                reader = csv.DictReader(f, delimiter='\t')
                for row in reader:
                    entries.append(row)
            self.assertEqual(2783, len(entries))
            self.assertEqual({'geneA': 'PIK3CA-DT', 'geneB': 'MED19'},
                             entries[0], 'If symbol changes this may fail')
            self.assertEqual({'geneA': 'PIK3CA-DT', 'geneB': 'IVNS1ABP'},
                             entries[2782], 'If symbol changes this may fail')

            # Todo: add more checks on the results

        finally:
            shutil.rmtree(temp_dir)


