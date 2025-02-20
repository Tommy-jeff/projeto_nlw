from .eventos_repository import EventosRepository
import pytest

@pytest.mark.skip("Insert in db")
def test_insert_eventos():
    event_name = "eventoTeste2"
    
    event_repo = EventosRepository()
    event_repo.insert(event_name)

@pytest.mark.skip("Select in db")
def test_select_eventos():
    event_name = "eventoTeste2"

    event_repo = EventosRepository()
    event = event_repo.select_event(event_name)

    print(f"consulta: {event}")
    print(f"consulta nome: {event.nome}")

@pytest.mark.skip("Delete in db")
def test_delete_eventos():
    event_id = 2

    event_repo = EventosRepository()
    event_repo.delete(event_id)
