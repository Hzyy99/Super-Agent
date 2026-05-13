"""ORM model registration entry point.

Importing this module ensures all ORM models are registered with
``Base.metadata`` so Alembic autogenerate detects every table.

The actual ORM classes have moved to entity-specific subpackages:
- ``harness.persistence.thread_meta``
- ``harness.persistence.run``
- ``harness.persistence.feedback``
- ``harness.persistence.user``

``RunEventRow`` remains in ``harness.persistence.models.run_event`` because
its storage implementation lives in ``harness.runtime.events.store.db`` and
there is no matching entity directory.
"""

from harness.persistence.feedback.model import FeedbackRow
from harness.persistence.models.run_event import RunEventRow
from harness.persistence.run.model import RunRow
from harness.persistence.thread_meta.model import ThreadMetaRow
from harness.persistence.user.model import UserRow

__all__ = ["FeedbackRow", "RunEventRow", "RunRow", "ThreadMetaRow", "UserRow"]
