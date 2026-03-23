import pytest
from pytest_bdd import scenario, given, when, then, parsers
from fastapi.testclient import TestClient
from src.app import app
import src.app

# Test client fixture
@pytest.fixture
def client():
    return TestClient(app)

# Context fixture for sharing data between steps
@pytest.fixture
def context():
    return {}

# Reset activities fixture
@pytest.fixture(autouse=True)
def reset_activities():
    src.app.activities = {
        "Chess Club": {
            "description": "Learn strategies and compete in chess tournaments",
            "schedule": "Fridays, 3:30 PM - 5:00 PM",
            "max_participants": 12,
            "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
        },
        "Programming Class": {
            "description": "Learn programming fundamentals and build software projects",
            "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
            "max_participants": 20,
            "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
        },
        "Gym Class": {
            "description": "Physical education and sports activities",
            "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
            "max_participants": 30,
            "participants": ["john@mergington.edu", "olivia@mergington.edu"]
        },
        "Basketball Team": {
            "description": "Competitive basketball training and games",
            "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:30 PM",
            "max_participants": 15,
            "participants": ["alex@mergington.edu"]
        },
        "Tennis Club": {
            "description": "Tennis training and friendly matches",
            "schedule": "Wednesdays and Saturdays, 3:00 PM - 4:30 PM",
            "max_participants": 16,
            "participants": ["grace@mergington.edu", "jackson@mergington.edu"]
        },
        "Art Studio": {
            "description": "Painting, drawing, and visual arts exploration",
            "schedule": "Mondays and Wednesdays, 3:30 PM - 5:00 PM",
            "max_participants": 18,
            "participants": ["isabella@mergington.edu"]
        },
        "Drama Club": {
            "description": "Theater performance, acting, and script writing",
            "schedule": "Thursdays, 4:00 PM - 5:30 PM",
            "max_participants": 25,
            "participants": ["liam@mergington.edu", "ava@mergington.edu", "noah@mergington.edu"]
        },
        "Science Club": {
            "description": "Hands-on experiments and scientific research projects",
            "schedule": "Mondays, 3:30 PM - 4:30 PM",
            "max_participants": 22,
            "participants": ["lucas@mergington.edu"]
        },
        "Debate Team": {
            "description": "Competitive debate and public speaking skills",
            "schedule": "Tuesdays and Fridays, 3:30 PM - 4:30 PM",
            "max_participants": 14,
            "participants": ["mia@mergington.edu", "ethan@mergington.edu"]
        }
    }

# Scenarios
@scenario('features/activities.feature', 'View all activities')
def test_view_activities():
    pass

@scenario('features/activities.feature', 'Successful signup for an activity')
def test_successful_signup():
    pass

@scenario('features/activities.feature', 'Signup for non-existent activity')
def test_signup_nonexistent():
    pass

@scenario('features/activities.feature', 'Signup when already signed up')
def test_signup_already_signed():
    pass

@scenario('features/activities.feature', 'Successful unregister from an activity')
def test_successful_unregister():
    pass

@scenario('features/activities.feature', 'Unregister from non-existent activity')
def test_unregister_nonexistent():
    pass

@scenario('features/activities.feature', 'Unregister when not signed up')
def test_unregister_not_signed():
    pass

# Step definitions
@when('I request all activities')
def step_request_activities(client, context):
    context['response'] = client.get('/activities')

@then('I should receive a list of all activities')
def step_receive_activities(context):
    response = context['response']
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert 'Chess Club' in data

@when(parsers.parse('I sign up "{email}" for "{activity}"'))
def step_signup(client, context, email, activity):
    context['response'] = client.post(f'/activities/{activity}/signup?email={email}')

@then('the signup should be successful')
def step_signup_success(context):
    response = context['response']
    assert response.status_code == 200
    data = response.json()
    assert 'message' in data
    assert 'Signed up' in data['message']

@then(parsers.parse('"{email}" should be added to "{activity}" participants'))
def step_added_to_participants(email, activity):
    assert email in src.app.activities[activity]['participants']

@then(parsers.parse('the signup should fail with {status_code}'))
def step_signup_fail(context, status_code):
    response = context['response']
    assert response.status_code == int(status_code)

@then(parsers.parse('the error message should be "{message}"'))
def step_error_message(context, message):
    response = context['response']
    data = response.json()
    assert data['detail'] == message

@when(parsers.parse('I unregister "{email}" from "{activity}"'))
def step_unregister(client, context, email, activity):
    context['response'] = client.delete(f'/activities/{activity}/unregister?email={email}')

@then('the unregister should be successful')
def step_unregister_success(context):
    response = context['response']
    assert response.status_code == 200
    data = response.json()
    assert 'message' in data
    assert 'Unregistered' in data['message']

@then(parsers.parse('"{email}" should be removed from "{activity}" participants'))
def step_removed_from_participants(email, activity):
    assert email not in src.app.activities[activity]['participants']

@then(parsers.parse('the unregister should fail with {status_code}'))
def step_unregister_fail(context, status_code):
    response = context['response']
    assert response.status_code == int(status_code)