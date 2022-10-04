from celery import shared_task

from movies import omdb_integrations

@shared_task
def search_and_save(search):
  return omdb_integrations.search_and_save(search)

