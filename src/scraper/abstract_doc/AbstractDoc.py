from scraper.abstract_doc.AbstractDocBase import AbstractDocBase
from scraper.abstract_doc.AbstractDocExtendedDataMixin import \
    AbstractDocExtendedDataMixin
from scraper.abstract_doc.AbstractDocGeneratorMixin import \
    AbstractDocGeneratorMixin
from scraper.abstract_doc.AbstractDocMetadataMixin import \
    AbstractDocMetadataMixin
from scraper.abstract_doc.hugging_face import AbstractDocHuggingFaceMixin
from scraper.abstract_doc.pipeline.AbstractDocPipelineMixin import \
    AbstractDocPipelineMixin
from scraper.abstract_doc.readme import AbstractDocReadMeMixin
from scraper.abstract_doc.readme.AbstractDocSummaryMixin import \
    AbstractDocSummaryMixin


class AbstractDoc(
    AbstractDocBase,
    AbstractDocGeneratorMixin,
    AbstractDocMetadataMixin,
    AbstractDocExtendedDataMixin,
    AbstractDocReadMeMixin,
    AbstractDocSummaryMixin,
    AbstractDocHuggingFaceMixin,
    AbstractDocPipelineMixin,
):
    pass
