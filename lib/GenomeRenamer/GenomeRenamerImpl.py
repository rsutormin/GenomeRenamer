#BEGIN_HEADER
from biokbase.workspace.client import Workspace as workspaceService
#END_HEADER


class GenomeRenamer:
    '''
    Module Name:
    GenomeRenamer

    Module Description:
    A KBase module: GenomeRenamer
    '''

    ######## WARNING FOR GEVENT USERS #######
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    #########################################
    VERSION = "0.0.1"
    GIT_URL = ""
    GIT_COMMIT_HASH = ""
    
    #BEGIN_CLASS_HEADER
    workspaceURL = None
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.workspaceURL = config['workspace-url']
        #END_CONSTRUCTOR
        pass
    

    def rename_genome(self, ctx, params):
        # ctx is the context object
        #BEGIN rename_genome
        ws = workspaceService(self.workspaceURL, token=ctx['token'])
        objects = ws.get_objects([{'ref': params['genome_ref']}])
        data = objects[0]['data']
        info = objects[0]['info']
        print("Old genome name: " + data['scientific_name'])
        new_name = params['new_genome_name']
        if (not new_name) or str(new_name) == 0:
            raise ValueError("New name is not defined for genome object")
        data['scientific_name'] = new_name
        provenance = ctx['provenance']
        provenance[0]['input_ws_objects']=[params['genome_ref']]
        ws.save_objects({'id':info[6], 'objects':[{'type':"KBaseGenomes.Genome", 'data': data,
            'name': info[1], 'provenance': provenance}]})
        print("Genome object with new name (" + new_name + ") was stored into object [" + info[1] + "]")
        #END rename_genome
        pass

    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK", 'message': "", 'version': self.VERSION, 
                     'git_url': self.GIT_URL, 'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
