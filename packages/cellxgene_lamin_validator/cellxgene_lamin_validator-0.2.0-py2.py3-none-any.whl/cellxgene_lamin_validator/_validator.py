from pathlib import Path
from typing import Dict, Literal, Optional, Union

import anndata as ad
import lamindb as ln
import lnschema_bionty as lb
from lamin_utils import logger

from ._register import register
from ._validate import FEATURE_MODELS, validate


class Validator:
    """CELLxGENE Lamin validator.

    Args:
        adata: an AnnData object to validate
        using: the reference instance containing registries to validate against
    """

    def __init__(
        self,
        adata: Union[ad.AnnData, str, Path],
        using: str = "laminlabs/cellxgene",
        verbosity: str = "hint",
    ) -> None:
        """Validate an AnnData object."""
        if isinstance(adata, (str, Path)):
            self._adata = ad.read_h5ad(adata)
        else:
            self._adata = adata
        self._verbosity = verbosity
        self._using = using
        Feature = ln.Feature if using is None else ln.Feature.using(using)
        features = set(Feature.filter().values_list("name", flat=True))
        missing_features = set(FEATURE_MODELS.keys()).difference(features)
        if len(missing_features) > 0:
            logger.error(
                "please register the following features: Validator.register_features()"
            )
            raise SystemExit
        self._kwargs: Dict = {}

    def _assign_kwargs(self, **kwargs):
        organism = kwargs.get("organism") or self._kwargs.get("organism")
        tissue_type = kwargs.get("tissue_type") or self._kwargs.get("tissue_type")
        if organism is None:
            raise ValueError("please specify organism")
        else:
            self._kwargs["organism"] = organism
        if tissue_type is None:
            raise ValueError("please specify tissue_type")
        else:
            self._kwargs["tissue_type"] = tissue_type
        for k, v in kwargs.items():
            if k == "organism":
                self._register_organism(v)
            self._kwargs[k] = v

    def _register_organism(self, name: str) -> None:
        """Register an organism record.

        Args:
            name: name of the organism
        """
        organism = lb.Organism.filter(name=name).one_or_none()
        if organism is None:
            ncbitaxon_source = lb.PublicSource.filter(source="ncbitaxon").one()
            record = lb.Organism.from_public(name=name, public_source=ncbitaxon_source)
            if record is not None:
                record.save()

    def register_features(self) -> None:
        """Register features records."""
        for feature in ln.Feature.using(self._using).filter().all():
            feature.save()

    def register_genes(self, organism: Optional[str] = None):
        """Register gene records."""
        if self._kwargs.get("organism") is None:
            raise ValueError("please specify organism")
        organism = organism or self._kwargs["organism"]
        organism_record = lb.Organism.filter(name=organism).one_or_none()
        if organism_record is None:
            raise ValueError(
                f"organism {organism} is not registered!   → run `.register_labels('organism')` first"
            )
        values = self._adata.var_names
        inspect_result = lb.Gene.inspect(
            values, field=lb.Gene.ensembl_gene_id, organism=organism, mute=True
        )
        if len(inspect_result.non_validated) > 0:
            ln.settings.verbosity = "error"
            genes = lb.Gene.from_values(
                inspect_result.non_validated,
                field=lb.Gene.ensembl_gene_id,
                organism=organism,
            )
            ln.settings.verbosity = "warning"
            if len(genes) > 0:
                logger.important(
                    f"registering {len(genes)} new genes from public reference..."
                )
                ln.save(genes)

        inspect_result = lb.Gene.inspect(
            values, field=lb.Gene.ensembl_gene_id, organism=organism, mute=True
        )
        if len(inspect_result.non_validated) > 0:
            genes_cxg = (
                lb.Gene.using(self._using)
                .filter(ensembl_gene_id__in=inspect_result.non_validated)
                .all()
            )
            if len(genes_cxg) > 0:
                logger.important(
                    f"registering {len(genes_cxg)} new genes from laminlabs/cellxgene instance..."
                )
                # save the genes to the current instance, for loop is needed here
                for g in genes_cxg:
                    # need to set the organism_id manually
                    g.organism_id = organism_record.id
                    g.save()

        # print hints for the non-validated values
        ln.settings.verbosity = "warning"
        lb.Gene.inspect(values, field=lb.Gene.ensembl_gene_id, organism=organism)
        ln.settings.verbosity = self._verbosity

    def register_labels(self, feature: str, **kwargs):
        """Register labels records."""
        if feature not in FEATURE_MODELS:
            raise ValueError(f"feature {feature} is not part of the CELLxGENE schema.")

        if f"{feature}_ontology_term_id" in self._adata.obs.columns:
            field = "ontology_id"
            values = self._adata.obs[f"{feature}_ontology_term_id"].unique()
        elif feature in self._adata.obs.columns:
            field = "name"
            values = self._adata.obs[feature].unique()
        else:
            raise AssertionError(
                f"either {feature} or {feature}_ontology_term_id column must present in adata.obs!"
            )

        if feature in ["donor_id", "tissue_type", "suspension_type"]:
            ln.settings.verbosity = "error"
            records = [ln.ULabel(name=v) for v in values]
            ln.save(records)
            is_feature = ln.ULabel.filter(name=f"is_{feature}").one_or_none()
            if is_feature is None:
                is_feature = ln.ULabel(
                    name=f"is_{feature}", description=f"parent of {feature}s"
                )
                is_feature.save()
            is_feature.children.add(*records)
        else:
            orm = FEATURE_MODELS.get(feature)
            # use CellType registry for "cell culture" tissue_type
            if orm == lb.Tissue:
                tissue_type = kwargs.get("tissue_type") or self._kwargs.get(
                    "tissue_type"
                )
                if tissue_type is None:
                    raise ValueError("please specify tissue_type")
                elif tissue_type == "cell culture":
                    orm = lb.CellType

            inspect_result = orm.inspect(values, field=field, mute=True)
            if len(inspect_result.non_validated) > 0:
                ln.settings.verbosity = "error"
                records = orm.from_values(inspect_result.non_validated, field=field)
                if len(records) > 0:
                    ln.settings.verbosity = "warning"
                    logger.important(
                        f"registering {len(records)} new labels from public reference..."
                    )
                    ln.save(records)

            inspect_result = orm.inspect(values, field=field, mute=True)
            if len(inspect_result.non_validated) > 0:
                records = (
                    orm.using(self._using)
                    .filter(**{f"{field}__in": inspect_result.non_validated})
                    .all()
                )
                if len(records) > 0:
                    logger.important(
                        f"registering {len(records)} new labels from laminlabs/cellxgene instance..."
                    )
                    for record in records:
                        record.save()

            # print hints for the non-validated values
            ln.settings.verbosity = "warning"
            orm.inspect(values, field=field)
            ln.settings.verbosity = self._verbosity

    def validate(
        self,
        organism: Optional[
            Literal["human", "mouse", "sars-2", "synthetic construct"]
        ] = None,
        tissue_type: Optional[Literal["tissue", "organoid", "cell culture"]] = None,
        **kwargs,
    ) -> bool:
        """Validate an AnnData object.

        Args:
            organism: name of the organism
            tissue_type: one of "tissue", "organoid", "cell culture"
            **kwargs: object level metadata

        Returns:
            whether the AnnData object is validated
        """
        self._assign_kwargs(
            organism=organism or self._kwargs.get("organism"),
            tissue_type=tissue_type or self._kwargs.get("tissue_type"),
            **kwargs,
        )
        validated = validate(self._adata, **self._kwargs)
        return validated

    def register_artifact(
        self,
        description: str,
        **kwargs,
    ) -> ln.Artifact:
        """Register the validated AnnData and metadata.

        Args:
            description: description of the AnnData object
            **kwargs: object level metadata

        Returns:
            a registered artifact record
        """
        self._assign_kwargs(**kwargs)
        artifact = register(
            self._adata,
            description=description,
            **self._kwargs,
        )
        return artifact

    def register_collection(
        self,
        artifact: ln.Artifact,
        name: str,
        description: Optional[str] = None,
        reference: Optional[str] = None,
        reference_type: Optional[str] = None,
    ) -> ln.Collection:
        """Register a collection from artifact/artifacts.

        Args:
            artifact: a registered artifact or a list of registered artifacts
            name: title of the publication
            description: description of the publication
            reference: accession number (e.g. GSE#, E-MTAB#, etc.)
            reference_type: source type (e.g. GEO, ArrayExpress, SRA, etc.)
        """
        collection = ln.Collection(
            artifact,
            name=name,
            description=description,
            reference=reference,
            reference_type=reference_type,
        )
        instance_identifier = ln.setup.settings.instance.identifier
        if collection._state.adding:
            collection.save()
            logger.print(
                f"🎉 successfully registered collection in LaminDB!\nview it in the hub: https://lamin.ai/{instance_identifier}/record/core/Collection?uid={collection.uid}"
            )
        else:
            collection.save()
            logger.warning(
                f"collection already exists in LaminDB!\nview it in the hub: https://lamin.ai/{instance_identifier}/record/core/Collection?uid={collection.uid}"
            )
        return collection

    def clean_up_failed_runs(self):
        """Clean up previous failed runs that don't register any outputs."""
        if ln.run_context.transform is not None:
            ln.Run.filter(
                transform=ln.run_context.transform, output_artifacts=None
            ).exclude(uid=ln.run_context.run.uid).delete()
