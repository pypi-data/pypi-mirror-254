from langchain_core.callbacks import CallbackManagerForRetrieverRun
from langchain_core.retrievers import BaseRetriever
from langchain_core.documents.base import Document
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    ClassVar,
    Collection,
    Dict,
    Iterable,
    List,
    Optional,
    Tuple,
    Type,
    TypeVar,
)
from langchain_core.pydantic_v1 import Field, root_validator
from pydantic import model_validator
from smartq_llm_app_utils.config import settings


class SmartQLasRetriever(BaseRetriever):
    """
    以VectorStore.as_retriever(kwargs)為例, kwargs分成search_type（Optional[str]）及search_kwargs
    Optional[Dict]，search_kwargs這個dict裡可以有k, score_threshold, fetch_k, lambda_mult & filter.
    在construct SmartQLasRetriever時做為constructor parameters提供,
    ex：SmartQLasRetriever(user_email=..., search_type=..., search_kwargs={})
    """

    # TODO: similarity_search_with_score, Metadata filtering,
    user_email: str = ''
    search_type: str = "similarity"
    """Type of search to perform. Defaults to "similarity"."""
    search_kwargs: dict = Field(default_factory=dict)
    """Keyword arguments to pass to the search function."""
    ekm_doc_retrieval_api_url: str = f"http://sys-ekm/sys/sys-ekm/doc_retrieval/v1/search/{settings.APP_ID}"
    """URL of SmartQ LAS EKM doc retrieval API, ex: http://sys-ekm/sys/sys-ekm/doc_retrieval/v1/search/app01"""

    allowed_search_types: ClassVar[Collection[str]] = (
        "similarity",
        "similarity_score_threshold",
        "mmr",
    )

    @root_validator()
    def validate_search_type(cls, values: Dict) -> Dict:
        """Validate search type."""
        search_type = values["search_type"]
        if search_type not in cls.allowed_search_types:
            raise ValueError(
                f"search_type of {search_type} not allowed. Valid values are: "
                f"{cls.allowed_search_types}"
            )
        if search_type == "similarity_score_threshold":
            score_threshold = values["search_kwargs"].get("score_threshold")
            if (score_threshold is None) or (not isinstance(score_threshold, float)):
                raise ValueError(
                    "`score_threshold` is not specified with a float value(0~1) "
                    "in `search_kwargs`."
                )
        return values

    def _get_relevant_documents(self, query: str) -> List[Document]:
        import requests

        # 設定 API 的 URL 和參數
        # ex: http://127.0.0.1:8000/sys/sys-ekm/doc_retrieval/v1/search/app01?
        # user_email=ken.hu@hwacom.com&query=查詢語句&search_type=similarity&k=3
        url = settings.EKM_DOC_RETRIEVAL_API_URL.format(app_id=settings.APP_ID)
        params = {
            "user_email": self.user_email,
            "query": query,
            "search_type": self.search_type
        }
        params.update(self.search_kwargs)

        response = requests.get(url, params=params)
        if response.status_code != 200:
            raise Exception(f"call EKM API fails: {response.status_code}")
        data: list[dict] = response.json()
        docs: list[Document] = [Document(page_content=d['page_content'], metadata=d['metadata']) for d in data]
        return docs


if __name__ == '__main__':
    retriever = SmartQLasRetriever(user_email='ken.hu@hwacom.com',
                                   search_type='similarity',
                                   search_kwargs={'k':5},
                                   ekm_doc_retrieval_api_url=settings.EKM_DOC_RETRIEVAL_API_URL.format(app_id=settings.APP_ID))
    print(retriever.ekm_doc_retrieval_api_url)
    docs: list[Document] = retriever.get_relevant_documents(query='這裡說的少鏢頭叫什麼名字?')
    for d in docs:
        print(d.page_content)