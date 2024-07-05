from logging import getLogger

import requests

from checker.models import Link
from core.celery import app

logger = getLogger('checker')


@app.task
def check_links() -> None:
    """Visit provided urls and set status codes."""
    links = Link.objects.all()
    for link in links:
        try:
            link.status_code = requests.get(url=link.url).status_code
        except requests.exceptions.ConnectionError:
            link.status_code = 400
    Link.objects.bulk_update(links, ['status_code'])
    logger.info('Status codes were successfully updated.')
