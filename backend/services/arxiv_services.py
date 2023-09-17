from pprint import pprint
import arxiv
from arxiv import SortCriterion, SortOrder
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError


def fetch_papers_from_arxiv(
    query: str,
    max_results: int = 10,
    sort_by: SortCriterion = SortCriterion.SubmittedDate,
    sort_order: SortOrder = SortOrder.Descending,
) -> list[arxiv.Result]:
    """
    Fetch papers from arXiv based on the provided query parameters.

    Args:
        query (str): The search query for arXiv.
        max_results (int): The maximum number of results to fetch.
        sort_by (str): The field by which to sort the results.
        sort_order (str): The order in which to sort the results.

    Returns:
        list[arxiv.Result]: A list of fetched papers.
    """
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=sort_by,
        sort_order=sort_order,
    )
    results: list = list(search.results())

    pprint(results[0].published)
    return results


def main():
    fetch_papers_from_arxiv(
        "machine learning", 10, SortCriterion.SubmittedDate, SortOrder.Descending
    )
    # fetch_and_store_papers("machine learning", 10, SortCriterion.SubmittedDate, SortOrder.Descending)


if __name__ == "__main__":
    main()
