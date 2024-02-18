def anndata_human_immune_cells(populate_registries=False):
    """Anndata object with semi-curated metadata."""
    import lamindb as ln

    adata = ln.dev.datasets.anndata_human_immune_cells()
    adata.obs["sex_ontology_term_id"] = "PATO:0000384"
    # create some typos in the metadata
    adata.obs["tissue"].replace({"lung": "lungg"}, inplace=True)
    # new donor ids
    adata.obs["donor"] = adata.obs["donor"].astype(str) + "-1"

    if populate_registries:
        import lnschema_bionty as lb

        verbosity = ln.settings.verbosity
        ln.settings.verbosity = "error"
        cell_types = lb.CellType.from_values(adata.obs["cell_type"])
        ln.save(cell_types)
        organism = lb.Organism.using("laminlabs/cellxgene").filter(name="human").one()
        organism.save()
        genes = lb.Gene.from_values(
            adata.var_names, field=lb.Gene.ensembl_gene_id, organism=organism
        )
        ln.save(genes[:-10])
        ln.settings.verbosity = verbosity

    return adata
