from services.arxiv_services import fetch_papers_from_arxiv
from services.ai_services import summarize_pdf, SummaryLength
from app.models.paper import Paper
from app.models.topic import Topic
from app.models.summary import Summary
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError


def fetch_topics_from_db(db: Session) -> list[Topic]:
    """
    Fetches all topics from the database.

    Args:
        db (Session): SQLAlchemy Session object.

    Returns:
        list: List of all Topic objects from the database.
    """
    print(f"""\n{'_'*80}\nfetch_topics_from_db called\n{'_'*80}""")
    return db.query(Topic).all()


def check_if_paper_exists(db: Session, pdf_url: str) -> Paper | None:
    """
    Checks if a paper with a given PDF URL exists in the database.

    Args:
        db (Session): SQLAlchemy Session object.
        pdf_url (str): The PDF URL to search for.

    Returns:
        Paper: Returns the Paper object if found, else None.
    """
    return db.query(Paper).filter_by(pdf_url=pdf_url).first()


def insert_paper_to_db(db: Session, paper_data: dict, topic_id: int) -> None:
    """
    Insert a new paper into the database.

    Args:
        db (Session): SQLAlchemy database session.
        paper_data (dict): Dictionary containing paper details.
        topic_id (int): ID of the topic to which the paper belongs.

    Returns:
        None
    """
    try:
        new_paper = Paper(
            pdf_url=paper_data["pdf_url"],
            title=paper_data["title"],
            authors=paper_data["authors"],
            topic_id=topic_id,  # Note this line
            publication_date=paper_data["published"].date(),
        )
        db.add(new_paper)
        db.commit()
    except IntegrityError:
        db.rollback()
        print(f"Paper with PDF URL {paper_data['pdf_url']} already exists.")


def insert_summary_to_db(db: Session, summary: dict) -> None:
    """
    Insert a new summary into the database.

    Args:
        db (Session): SQLAlchemy database session.
        summary (dict): Dictionary containing summary details.

    Returns:
        None
    """
    try:
        new_summary = Summary(
            paper_id=summary["paper_id"],
            short_summary=summary["short_summary"],
            long_summary=summary["long_summary"],
        )
        db.add(new_summary)
        db.commit()
    except IntegrityError:
        db.rollback()
        print(f"Summary for paper ID {summary['paper_id']} already exists.")


async def process_papers_for_topic(db: Session, topic: Topic) -> None:
    """
    Process and summarize papers for a given topic.

    Args:
        db (Session): SQLAlchemy database session.
        topic (Topic): Topic object for which papers are to be processed.

    Returns:
        None
    """
    print(f"""\n{'_'*80}\nprocessing_papers called\n{'_'*80}""")
    papers: list = fetch_papers_from_arxiv(query=topic.name, max_results=4)  # type: ignore

    for paper in papers:
        exists = check_if_paper_exists(db, paper.pdf_url)
        if not exists:
            try:
                # Short Summary
                short_summary_result = await summarize_pdf(
                    pdf_url=paper.pdf_url,
                    summary_length=SummaryLength.SHORT,
                    title=paper.title,
                    topic=topic.name,  # type: ignore
                )

                # Full Summary
                full_summary_result = await summarize_pdf(
                    pdf_url=paper.pdf_url,
                    summary_length=SummaryLength.FULL,
                    title=paper.title,
                    topic=topic.name,  # type: ignore
                )

                paper_data = {
                    "pdf_url": paper.pdf_url,
                    "title": paper.title,
                    "authors": ", ".join([str(author) for author in paper.authors]),
                    "published": paper.published,
                }

                insert_paper_to_db(db, paper_data, topic.id)  # type: ignore

                paper_db_entry = check_if_paper_exists(db, paper.pdf_url)

                if paper_db_entry:
                    summary_data: dict = {
                        "paper_id": paper_db_entry.id,
                        "short_summary": short_summary_result,
                        "long_summary": full_summary_result,
                    }

                    insert_summary_to_db(db, summary_data)

            except Exception as e:
                print(f"Error processing paper {paper.title}: {e}")
                continue
