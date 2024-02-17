from ou_book_theme.extensions import activity, time, where_next


def setup(app):
    """Setup all node extensions."""
    activity.setup(app)
    time.setup(app)
    where_next.setup(app)
