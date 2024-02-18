from typing import Literal, Optional

import lamindb as ln
import lnschema_bionty as lb
import pandas as pd
from anndata import AnnData
from lamin_utils import colors, logger
from lamindb._from_values import _print_values

ONTOLOGY_DEFAULTS_HINT = {
    "disease": ("normal", "lb.Disease.lookup()"),
    "development_stage": ("unknown", "lb.DevelopmentStage.lookup()"),
    "self_reported_ethnicity": ("unknown", "lb.Ethnicity.lookup()"),
    "suspension_type": ("cell", '"cell" or "nucleus" or "na"'),
    "donor_id": ("na", "ln.ULabel.filter(name='is_donor').one().children.lookup()"),
    "tissue_type": ("tissue", '"tissue" or "organoid" or "cell culture"'),
    "cell_type": ("native_cell", "lb.CellType.lookup()"),
}

FEATURE_MODELS = {
    "assay": lb.ExperimentalFactor,
    "cell_type": lb.CellType,
    "development_stage": lb.DevelopmentalStage,
    "disease": lb.Disease,
    "donor_id": ln.ULabel,
    "self_reported_ethnicity": lb.Ethnicity,
    "sex": lb.Phenotype,
    "suspension_type": ln.ULabel,
    "tissue": lb.Tissue,
    "tissue_type": ln.ULabel,
    "organism": lb.Organism,
}


def _inspect_obs(
    adata: AnnData,
    organism: Literal["human", "mouse", "sars-2", "synthetic construct"],
    tissue_type: Literal["tissue", "organoid", "cell culture"],
    using: Optional[str] = None,
    verbosity: str = "hint",
    **kwargs,
):
    """Inspect ontology terms in an AnnData object using LaminDB registries."""
    ln.settings.verbosity = verbosity

    features = (
        ln.Feature.lookup().dict()
        if using is None
        else ln.Feature.using(using).lookup().dict()
    )

    def inspect_ontology_terms(
        adata,
        col_name: str,
        field: Literal["ontology_id", "name"],
        using: Optional[str] = None,
    ):
        """Validate ontology terms in a pandas series using LaminDB registries."""
        values = adata.obs[col_name].unique()
        feature_name = col_name.replace("_ontology_term_id", "")
        feature = features.get(feature_name)
        orm = FEATURE_MODELS.get(feature.name)
        if orm == lb.Tissue and tissue_type == "cell culture":
            orm = lb.CellType
        orm = orm if using is None else orm.using(using)
        # inspect the values, validate and make suggestions to fix
        if (
            field == "ontology_id"
            and feature.name in adata.obs.columns
            and adata.obs[col_name].isnull().sum() > 0
        ):
            # if some ontology_ids are None, validate terms by name
            field = "name"
        inspect_result = orm.inspect(values, field=field, mute=True)
        # if all terms are validated, add ontology_term_id or name column
        n_non_validated = len(inspect_result.non_validated)
        if n_non_validated == 0:
            validated = True
            logger.success(f"all {feature_name}s are validated")
            # if the column is validated by ontology_id, adding its corresponding name column
            if field == "ontology_id":
                new_col_name = feature_name
                cols = ["ontology_id", "name"]
            # if the column is validated by name, adding its corresponding ontology_id column
            else:
                new_col_name = f"{col_name}_ontology_term_id"
                cols = ["name", "ontology_id"]
            # map name from/to ontology_id
            validated_records = orm.filter(**{f"{field}__in": values})
            try:
                mapper = (
                    pd.DataFrame(validated_records.values_list(*cols))
                    .set_index(0)
                    .to_dict()[1]
                )
            except Exception:
                return validated
            # add the ontology_term_id/name column
            adata.obs[new_col_name] = adata.obs[col_name].map(mapper)
            logger.success(
                f"added column '{new_col_name}' with validated terms from {cols[1]}"
            )
        else:
            are = "are" if n_non_validated > 1 else "is"
            print_values = _print_values(inspect_result.non_validated)
            feature_name_print = f"`.register_labels('{feature_name}')`"
            logger.warning(
                f"{colors.yellow(f'{n_non_validated} terms')} {are} not validated: {colors.yellow(print_values)}\n      → register terms via {colors.red(feature_name_print)}"
            )
            validated = False
        return validated

    # add object level metadata to obs columns
    if "organism" not in adata.obs.columns:
        logger.info(f"adding obs column '{colors.bold('organism')}'")
        adata.obs["organism"] = organism
    if "tissue_type" not in adata.obs.columns:
        logger.info(f"adding obs column '{colors.bold('tissue_type')}'")
        adata.obs["tissue_type"] = tissue_type
    for key, value in kwargs.items():
        if key in FEATURE_MODELS and key not in adata.obs.columns:
            logger.info(f"adding obs column '{colors.bold(key)}'")
            adata.obs[key] = value

    # start validation
    validated = True
    for feature_name in FEATURE_MODELS:
        # validate by ontology_id if annotated
        if f"{feature_name}_ontology_term_id" in adata.obs.columns:
            logger.indent = ""
            logger.info(f"inspecting '{colors.bold(feature_name)}' by ontology_id")
            logger.indent = "   "
            validated &= inspect_ontology_terms(
                adata,
                f"{feature_name}_ontology_term_id",
                field="ontology_id",
                using=using,
            )
            logger.indent = ""
        elif feature_name in adata.obs.columns:
            logger.indent = ""
            logger.info(f"inspecting '{colors.bold(feature_name)}' by name")
            logger.indent = "   "
            validated &= inspect_ontology_terms(
                adata, feature_name, field="name", using=using
            )
            logger.indent = ""
        else:
            logger.indent = ""
            logger.warning(f"could not find column {colors.yellow(feature_name)}")
            if feature_name in ONTOLOGY_DEFAULTS_HINT:
                feature_name_print = f"`.register_labels('{feature_name}')`"
                logger.warning(
                    "   → set to"
                    f" '{colors.red(ONTOLOGY_DEFAULTS_HINT[feature_name][0])}' by"
                    " default, or add terms via"
                    f" {colors.red(feature_name_print)}"
                )
            validated &= False

    # re-order columns
    if validated:
        validated_cols = [
            "assay",
            "assay_ontology_term_id",
            "cell_type",
            "cell_type_ontology_term_id",
            "development_stage",
            "development_stage_ontology_term_id",
            "disease",
            "disease_ontology_term_id",
            "donor_id",
            "self_reported_ethnicity",
            "self_reported_ethnicity_ontology_term_id",
            "sex",
            "sex_ontology_term_id",
            "suspension_type",
            "tissue",
            "tissue_ontology_term_id",
            "tissue_type",
            "organism",
            "organism_ontology_term_id",
        ]
        additional_cols = [i for i in adata.obs.columns if i not in validated_cols]
        adata.obs = adata.obs[validated_cols + additional_cols]

    return validated


def _inspect_var(
    adata: AnnData, organism: str, using: Optional[str] = None, verbosity: str = "hint"
):
    """Inspect features in .var using LaminDB registries."""
    ln.settings.verbosity = verbosity
    logger.indent = ""
    logger.info(f"inspecting {colors.bold('Ensembl Gene IDs')}")
    logger.indent = "   "
    # inspect the values, validate and make suggestions to fix
    Gene = lb.Gene if using is None else lb.Gene.using(using)
    inspect_result = Gene.inspect(
        adata.var.index, field=lb.Gene.ensembl_gene_id, organism=organism, mute=True
    )
    n_non_validated = len(inspect_result.non_validated)
    if n_non_validated == 0:
        logger.success(f"all {organism} gene are validated")
        validated = True
    else:
        are = "are" if n_non_validated > 1 else "is"
        print_values = _print_values(inspect_result.non_validated)
        logger.warning(
            f"{colors.yellow(f'{n_non_validated} genes')} {are} not validated: {colors.yellow(print_values)}\n      → register genes via {colors.red('`.register_genes()`')}"
        )
        validated = False
    logger.indent = ""
    return validated


def validate(
    adata,
    organism: Literal["human", "mouse", "sars-2", "synthetic construct"],
    tissue_type: Literal["tissue", "organoid", "cell culture"],
    using: Optional[str] = None,
    verbosity: str = "hint",
    **kwargs,
) -> bool:
    """Inspect metadata in an AnnData object using LaminDB registries."""
    if using is not None:
        logger.important(f"validating metadata using registries of instance `{using}`")

    Organism = lb.Organism if using is None else lb.Organism.using(using)
    organisms = set(Organism.filter().values_list("name", flat=True))
    add_organism_msg = (
        "\n\nTo add an organism from cellxgene instance:\n"
        "   Validator.register_labels('organism')\n"
    )
    if len(organisms) == 0:
        logger.error(
            f"No organism found in the database, please add one first:{add_organism_msg}"
        )
        return False
    if organism not in organisms:
        logger.error(f"registered organisms are: {organisms}{add_organism_msg}")
        return False

    validated_var = _inspect_var(
        adata, organism=organism, using=using, verbosity=verbosity
    )
    validated_obs = _inspect_obs(
        adata,
        using=using,
        verbosity=verbosity,
        organism=organism,
        tissue_type=tissue_type,
        **kwargs,
    )
    return validated_var & validated_obs
