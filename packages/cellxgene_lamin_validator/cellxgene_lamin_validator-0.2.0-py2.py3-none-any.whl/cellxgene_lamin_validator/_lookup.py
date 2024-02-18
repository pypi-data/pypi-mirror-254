from functools import cached_property

import lamindb as ln
import lnschema_bionty as lb


def _orm_using(orm, *, using: str):
    if using == "current":
        return orm
    else:
        return orm.using(using)


class Lookup:
    """Lookup features and labels from the reference instance."""

    def __init__(self, using: str = "laminlabs/cellxgene") -> None:
        verbosity = ln.settings.verbosity
        ln.settings.verbosity = "error"
        self._assays = _orm_using(lb.ExperimentalFactor, using=using).lookup()
        self._cell_types = _orm_using(lb.CellType, using=using).lookup()
        self._development_stages = _orm_using(
            lb.DevelopmentalStage, using=using
        ).lookup()
        self._diseases = _orm_using(lb.Disease, using=using).lookup()
        self._ethnicities = _orm_using(lb.Ethnicity, using=using).lookup()
        self._phenotypes = _orm_using(lb.Phenotype, using=using).lookup()
        is_suspension_type = (
            _orm_using(ln.ULabel, using=using).filter(name="is_suspension_type").one()
        )
        self._suspension_types = is_suspension_type.children.lookup()
        self._tissues = _orm_using(lb.Tissue, using=using).lookup()
        is_tissue_type = (
            _orm_using(ln.ULabel, using=using).filter(name="is_tissue_type").one()
        )
        self._tissue_types = is_tissue_type.children.lookup()
        self._organisms = _orm_using(lb.Organism, using=using).lookup()
        self._features = _orm_using(ln.Feature, using=using).lookup()
        ln.settings.verbosity = verbosity

    @cached_property
    def assays(self):
        return self._assays

    @cached_property
    def cell_types(self):
        return self._cell_types

    @cached_property
    def development_stages(self):
        return self._development_stages

    @cached_property
    def diseases(self):
        return self._diseases

    @cached_property
    def ethnicities(self):
        return self._ethnicities

    @cached_property
    def phenotypes(self):
        return self._phenotypes

    @cached_property
    def suspension_types(self):
        return self._suspension_types

    @cached_property
    def tissues(self):
        return self._tissues

    @cached_property
    def tissue_types(self):
        return self._tissue_types

    @cached_property
    def organisms(self):
        return self._organisms

    @cached_property
    def features(self):
        return self._features
