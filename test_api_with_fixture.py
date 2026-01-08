import pytest
import requests

#scope="session" pytest 전체 실행 동안 딱 1번만 만들어짐
@pytest.fixture(scope="session")
def base_url():
    return "http://localhost:4444"

#테스트용 사용자 데이터
@pytest.fixture
def sample_post_payload():
    return{
        "username": "testuser",
        "password": "testpassword"
        
    }

#게시글 생성 -> 생성된 데이터 전달 -> 테스트 끝나면 게시글 삭제(tear down)
@pytest.fixture
def created_user(base_url,sample_post_payload):
    create_url = f"{base_url}/users"
    response = requests.post(create_url,json=sample_post_payload)
    
    assert response.status_code == 201
    created_data = response.json()
    print(f"\n[Setup] Created user ID : {created_data['id']}")
    
    yield created_data
    
    #teardown
    user_id = created_data["id"]
    delete_url = f"{base_url}/users/{user_id}"
    
    
    del_response = requests.delete(delete_url)
    assert del_response.status_code in (200,204)
    print(
        f"[Teardown] Deleted user ID: {user_id}, "
        f"Status: {del_response.status_code}"
    )
    
#실습
def test_get_created_post(base_url,created_user):
    user_id = created_user["id"]
    get_url = f"{base_url}/users/{user_id}"
    response = requests.get(get_url)
    assert response.status_code == 200
    data=response.json()
    
    # ----------------------------
    # 응답 검증
    # ----------------------------

    # 타입 확인
    assert isinstance(data, dict)

    # key 존재 여부
    assert "id" in data
    assert "username" in data
    assert "password" in data

    # 값이 비어있지 않은지 확인
    assert data["username"]
    assert data["password"]    
