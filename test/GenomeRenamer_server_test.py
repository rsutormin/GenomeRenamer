import unittest
import os
import json
import time

from os import environ
from ConfigParser import ConfigParser
from pprint import pprint

from biokbase.workspace.client import Workspace as workspaceService
from GenomeRenamer.GenomeRenamerImpl import GenomeRenamer


class GenomeRenamerTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        token = environ.get('KB_AUTH_TOKEN', None)
        cls.ctx = {'token': token, 'provenance': [{'service': 'GenomeRenamer',
            'method': 'please_never_use_it_in_production', 'method_params': []}],
            'authenticated': 1}
        config_file = environ.get('KB_DEPLOYMENT_CONFIG', None)
        cls.cfg = {}
        config = ConfigParser()
        config.read(config_file)
        for nameval in config.items('GenomeRenamer'):
            cls.cfg[nameval[0]] = nameval[1]
        cls.wsURL = cls.cfg['workspace-url']
        cls.wsClient = workspaceService(cls.wsURL, token=token)
        cls.serviceImpl = GenomeRenamer(cls.cfg)

    @classmethod
    def tearDownClass(cls):
        if hasattr(cls, 'wsName'):
            cls.wsClient.delete_workspace({'workspace': cls.wsName})
            print('Test workspace was deleted')

    def getWsClient(self):
        return self.__class__.wsClient

    def getWsName(self):
        if hasattr(self.__class__, 'wsName'):
            return self.__class__.wsName
        suffix = int(time.time() * 1000)
        wsName = "test_GenomeRenamer_" + str(suffix)
        ret = self.getWsClient().create_workspace({'workspace': wsName})
        self.__class__.wsName = wsName
        return wsName

    def getImpl(self):
        return self.__class__.serviceImpl

    def getContext(self):
        return self.__class__.ctx

    def test_rename_genome(self):
        contig_obj_name = "contigset.1"
        contig = {'id': '1', 'length': 10, 'md5': 'md5', 'sequence': 'agcttttcat'}
        obj = {'contigs': [contig], 'id': 'id', 'md5': 'md5', 'name': 'name', 
               'source': 'source', 'source_id': 'source_id', 'type': 'type'}
        self.getWsClient().save_objects({'workspace': self.getWsName(), 'objects':
            [{'type': 'KBaseGenomes.ContigSet', 'name': contig_obj_name, 'data': obj}]})
        features = [{"id": "1", "location": [["1", 0, "+", 0]], "type": "CDS", 
            "protein_translation": "iddqdidkfa", "aliases": [], "annotations":[], 
            "function": ""}]
        genome_name = "Test genome 1"
        genome_obj_name = "genome.1"
        genome_obj = {"complete": 0, "contig_ids": ["1"], "contig_lengths": [10],
            "contigset_ref": self.getWsName() + "/" + contig_obj_name, "dna_size": 10, 
            "domain": "Bacteria", "gc_content": 0.5, "genetic_code": 11, 
            "id": genome_obj_name, "md5": "md5", "num_contigs": 1, 
            "scientific_name": genome_name, "source": "test folder", "source_id": "noid",
            "features": features}
        self.getWsClient().save_objects({'workspace': self.getWsName(), 'objects':
            [{'type': 'KBaseGenomes.Genome', 'name': genome_obj_name, 
            'data': genome_obj}]})
        new_genome_name = "Test genome 2"
        self.getImpl().rename_genome(self.getContext(), 
            {"genome_ref": self.getWsName() + "/" + genome_obj_name, 
            "new_genome_name": new_genome_name})
        new_genome_obj = self.getWsClient().get_objects(
            [{'ref': self.getWsName() + "/" + genome_obj_name}])[0]['data']
        self.assertEqual(new_genome_obj['scientific_name'], new_genome_name)
        pass
