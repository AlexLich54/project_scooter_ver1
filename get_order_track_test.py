#Дипломный проект Линкевич Алексей поток 8а инженер по тестированию плюс
import sender_stand_request


def test_get_order_track():
    response = sender_stand_request.post_new_order()
    track_number = response.json()["track"]
    response = sender_stand_request.get_order_by_track(track_number)
    assert response.status_code == 200

