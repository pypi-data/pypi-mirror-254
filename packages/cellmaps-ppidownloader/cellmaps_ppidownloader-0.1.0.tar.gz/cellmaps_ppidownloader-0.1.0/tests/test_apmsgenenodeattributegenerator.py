#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `APMSGeneNodeAttributeGenerator`"""

import os
import unittest
import shutil
import tempfile
import csv


from cellmaps_ppidownloader.gene import APMSGeneNodeAttributeGenerator

SKIP_REASON = 'CELLMAPS_PPIDOWNLOADER_INTEGRATION_TEST ' \
              'environment variable not set, cannot run integration ' \
              'tests'


class TestAPMSGeneNodeAttributeGenerator(unittest.TestCase):
    """Tests for `APMSGeneNodeAttributeGenerator`"""

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

    def test_get_apms_edgelist_from_tsvfile(self):
        edgelist = APMSGeneNodeAttributeGenerator.get_apms_edgelist_from_tsvfile(self.get_edgelist())
        self.assertEqual(2783, len(edgelist))
        self.assertEqual('101928739', edgelist[0]['GeneID1'])
        self.assertEqual('PIK3CA', edgelist[0]['Symbol1'])
        self.assertEqual('219541', edgelist[0]['GeneID2'])
        self.assertEqual('MED19', edgelist[0]['Symbol2'])
