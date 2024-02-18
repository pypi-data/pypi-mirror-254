#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `CM4AIGeneNodeAttributeGenerator`"""

import os
import unittest
import shutil
import tempfile
import csv


from cellmaps_ppidownloader.gene import CM4AIGeneNodeAttributeGenerator

SKIP_REASON = 'CELLMAPS_PPIDOWNLOADER_INTEGRATION_TEST ' \
              'environment variable not set, cannot run integration ' \
              'tests'


class TestCM4AIGeneNodeAttributeGenerator(unittest.TestCase):
    """Tests for `CM4AIGeneNodeAttributeGenerator`"""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def create_tsvfile(self, tsvfile):
        with open(tsvfile, 'w', newline='') as f:
            writer = csv.DictWriter(f, delimiter='\t', fieldnames=['Bait', 'Prey',
                                                                   'BFDR.x', 'FoldChange.x'])
            writer.writeheader()
            writer.writerow({'Bait': 'DNMT3A',
                             'Prey': 'O00422',
                             'FoldChange.x': 77.5,
                             'BFDR.x': 0.0})
            writer.writerow({'Bait': 'HDAC2',
                             'Prey': 'Q9Y2K7',
                             'FoldChange.x': -0.5,
                             'BFDR.x': 10.0})
            writer.writerow({'Bait': 'HDAC2',
                             'Prey': 'P09429',
                             'FoldChange.x': None,
                             'BFDR.x': None})

    def test_get_apms_edgelist_from_tsvfile(self):
        temp_dir = tempfile.mkdtemp()
        try:
            tsvfile = os.path.join(temp_dir, 'foo.tsv')
            self.create_tsvfile(tsvfile)
            edgelist = CM4AIGeneNodeAttributeGenerator.get_apms_edgelist_from_tsvfile(tsvfile)
            self.assertEqual(3, len(edgelist))
            self.assertEqual({'Bait': 'DNMT3A',
                              'Prey': 'O00422'}, edgelist[0])
            self.assertEqual({'Bait': 'HDAC2',
                             'Prey': 'Q9Y2K7'}, edgelist[1])
            self.assertEqual({'Bait': 'HDAC2',
                             'Prey': 'P09429'}, edgelist[2])

        finally:
            shutil.rmtree(temp_dir)

    @unittest.skip('This needs to be refactored to hit mock object. skipping for now')
    def test_get_baits_to_ensemblsymbolmap(self):
        temp_dir = tempfile.mkdtemp()
        try:
            tsvfile = os.path.join(temp_dir, 'foo.tsv')
            self.create_tsvfile(tsvfile)
            edgelist = CM4AIGeneNodeAttributeGenerator.get_apms_edgelist_from_tsvfile(tsvfile)
            gen = CM4AIGeneNodeAttributeGenerator(apms_edgelist=edgelist)
            bait_to_id = gen._get_baits_to_ensemblsymbolmap()
            self.assertEqual(2, len(bait_to_id))
            self.assertEqual(('1788', 'DNMT3A', 'ENSG00000119772'), bait_to_id['DNMT3A'])
            self.assertEqual(('3066', 'HDAC2', 'ENSG00000196591'), bait_to_id['HDAC2'])

        finally:
            shutil.rmtree(temp_dir)




