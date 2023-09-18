import pytest
from config.database import get_db
from services.services_manager import (
    # fetch_topics_from_db,
    check_if_paper_exists,
    process_papers_for_topic,
)
from app.models.topic import Topic
from app.models.paper import Paper
from app.models.summary import Summary


@pytest.mark.asyncio
async def test_process_papers_for_topic() -> None:
    # Initialize the database session using your get_db function
    db_gen = get_db()
    db = next(db_gen)

    try:
        # Fetch a topic from the database or create one if not exists
        topic = db.query(Topic).first()
        if not topic:
            # Create a new topic and add it to the database
            new_topic = Topic(name="Artificial Intelligence")
            db.add(new_topic)
            db.commit()

            # Fetch the newly created topic
            topic = db.query(Topic).filter_by(name="Artificial Intelligence").first()

        # Process papers for the fetched or created topic
        await process_papers_for_topic(db, topic)

        # Validate the data in the database
        papers = db.query(Paper).filter_by(topic_id=topic.id).all()  # type: ignore
        assert len(papers) > 0, "No papers were processed."

        for paper in papers:
            # Check if the paper exists in the database
            exists = check_if_paper_exists(db, paper.pdf_url)  # type: ignore
            assert exists, f"Paper with PDF URL {paper.pdf_url} not found."

            # Check if the summary exists
            summary = db.query(Summary).filter_by(paper_id=paper.id).first()
            assert summary, f"Summary for paper ID {paper.id} not found."

            # Cleanup: Remove the paper and summary from the database
            db.delete(summary)
            db.delete(paper)

        db.commit()

    finally:
        # Close the database session
        db.close()
