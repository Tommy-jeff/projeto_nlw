from .subscribers_repository import SubscribersRepository
import pytest

@pytest.mark.skip("Insert in db")
def test_insert_subscriber():
    subscriber_info = {
        "name" : "Teste2",
        "email" : "teste2@email.com",
        "evento_id" : 2
    }

    subs_repo = SubscribersRepository()
    subs_repo.insert(subscriber_info)

@pytest.mark.skip("Select in db")
def test_select_subscriber():
    subscriber_email = "teste2@email.com"
    evanto_id = 2

    subs_repo = SubscribersRepository()
    subs = subs_repo.select_subscriber(subscriber_email, evanto_id)

    print(f"\nconsulta: {subs}")
    print(f"\nconsulta nome: {subs.nome}")

@pytest.mark.skip("Select link ranking in db")
def test_select_ranking_subscriber():
    evento_id = 1

    subs_repo = SubscribersRepository()
    subs = subs_repo.get_ranking(evento_id)

    print()
    for elem in subs:
        print(f"link: {elem.link} - inscrições: {elem.total}")

@pytest.mark.skip("Delete in db")
def test_delete_subscriber():
    subscribe_id = 6

    subs_repo = SubscribersRepository()
    subs_repo.delete_subscriber(subscribe_id)
