from sqlalchemy import event
from app.models.topic import Topic
from app.models.associations import user_topics_association


# TODO: Test functionality of this event listener
@event.listens_for(user_topics_association, "after_delete")
def delete_orphan_topic(mapper, connection, target):
    """
    Deletes a topic if it becomes orphaned after a user-topic association is deleted.

    This function is triggered after a row is deleted from the `user_topics_association` table.
    It checks if the topic associated with the deleted row is still linked to any users.
    If not, the topic is deleted from the `Topic` table.

    Args:
        mapper (Mapper): The mapper that is the target of this event.
        connection (Connection): The database connection for this operation.
        target (RowProxy): The specific row that was deleted from the `user_topics_association` table.

    """
    # Fetch the topic_id from the target (association row)
    topic_id = target.c.topic_id

    # Query to check if any other users are associated with this topic
    remaining_users = connection.execute(
        user_topics_association.select().where(
            user_topics_association.c.topic_id == topic_id
        )
    ).fetchall()

    # If no other users are associated, delete the topic
    if not remaining_users:
        connection.execute(Topic.__table__.delete().where(Topic.id == topic_id))
