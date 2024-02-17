import armored.enums.status as status


def test_status_failed():
    e: status.Status = status.Status.FAILED

    assert e == status.Status.FAILED
    assert e in status.Status
    assert e <= status.Status.FAILED
    assert e < status.Status.WAITING
    assert e > status.Status.SUCCESS
    assert e.value == 1
    assert not e.in_process()
