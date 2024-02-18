from pathlib import Path
from typing import Literal, Optional, Union

import anndata as ad
import lamindb as ln
import lnschema_bionty as lb
from lamin_utils import logger

from ._validate import FEATURE_MODELS, validate


def register(
    adata: Union[ad.AnnData, str, Path],
    description: str,
    organism: Literal["human", "mouse", "sars-2", "synthetic construct"],
    tissue_type: Literal["tissue", "organoid", "cell culture"],
    using: Optional[str] = None,
    **kwargs,
):
    """Registers all metadata with an AnnData Artifact."""
    adata = adata if isinstance(adata, ad.AnnData) else ad.read_h5ad(adata)

    # ensure the adata object is validated
    validated = validate(
        adata,
        organism=organism,
        tissue_type=tissue_type,
        using=using,
        verbosity="warning",
        **kwargs,
    )
    if not validated:
        logger.error(
            "cannot register non-validated AnnData object, please run `validate()`"
            " first!"
        )
        return

    verbosity = ln.settings.verbosity
    ln.settings.verbosity = "error"

    features = ln.Feature.lookup().dict()
    # query labels records for each obs column
    feature_labels = []
    for col in adata.obs.columns:
        if not col.endswith("ontology_term_id"):
            feature = features.get(col)
            if feature is not None:
                orm = FEATURE_MODELS.get(col)
                orm = orm if using is None else orm.using(using)
                unique_values = adata.obs[col].unique()
                if any(not isinstance(i, str) for i in unique_values):
                    raise ValueError(f"labels for {col} must be strings")
                labels = orm.filter(
                    name__in=unique_values
                ).all()  # this always use name field
                # save labels to the current instance
                for label in labels:
                    label.save()
                if len(labels) == 0:
                    raise ValueError(f"no labels found for {col}")
                feature_labels.append((feature, labels))

    # register artifact
    ln.settings.verbosity = "warning"
    artifact = ln.Artifact.from_anndata(
        adata, description=description, field=lb.Gene.ensembl_gene_id, organism=organism
    )
    artifact.n_observations = adata.n_obs
    artifact.save()

    # link validated obs metadata
    for feature, labels in feature_labels:
        artifact.labels.add(labels, feature)

    logger.print(
        "\n\n🎉 successfully registered artifact in LaminDB!\nview it in the hub"
        f": https://lamin.ai/{ln.setup.settings.instance.identifier}/record/core/Artifact?uid={artifact.uid}\n\n"
    )

    logger.print(
        "💡 please register a collection for this artifact:"
        "\n   → collection = ln.Collection(artifact, name=<title>,"
        " description=<doi>, reference=<GSE#>, reference_type=<GEO>)\n   →"
        " collection.save()"
    )
    ln.settings.verbosity = verbosity

    return artifact
