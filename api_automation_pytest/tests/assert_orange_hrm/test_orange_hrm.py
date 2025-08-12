from qa_resources import reso_orange_hrm

def test_get_about_orange_hrm():
    response = reso_orange_hrm.get_about_orange_hrm()
    assert response["data"]["companyName"] == "OrangeHRM"
    assert response["data"]["productName"] == "OrangeHRM OS"
    assert response["data"]["version"] == "5.7"
    assert response["data"]["numberOfActiveEmployee"] >= 50
    assert response["data"]["numberOfPastEmployee"] == 0
    assert response["meta"] == []
    assert response["rels"] == []