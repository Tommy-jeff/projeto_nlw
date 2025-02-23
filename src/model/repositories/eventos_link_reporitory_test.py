from .eventos_link_repository import EventosLinkRepository
import pytest

# @pytest.mark.skip("Insert in db")
def test_insert_eventos_link():
    event_id = 10
    inscrito_id = 10
    
    event_link_repo = EventosLinkRepository()
    event_link_repo.insert(event_id, inscrito_id)

# @pytest.mark.skip("Select in db")
def test_select_eventos() -> int:
    event_id = 10
    inscrito_id = 10

    event_link_repo = EventosLinkRepository()
    event_link = event_link_repo.select_event_link(event_id, inscrito_id)

    print(f"consulta: {event_link}")
    print(f"consulta nome: {event_link.id}")

    return event_link.id

# @pytest.mark.skip("Delete in db")
def test_delete_link_eventos():

    event_link_repo = EventosLinkRepository()
    event_link_repo.delete(test_select_eventos())
