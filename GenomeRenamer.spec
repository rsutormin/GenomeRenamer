/*
A KBase module: GenomeRenamer
*/

module GenomeRenamer {
    typedef structure {
        string genome_ref;
        string new_genome_name;
    } RenameGenomeParams;

    funcdef rename_genome(RenameGenomeParams params) returns () authentication required;
};