from behave import given, when, then
from assertpy import assert_that
from features.pages.pet_api import PetApi

@given('I have pet details to add')
def step_impl(context):
    context.pet_api = PetApi()
    context.pet_data = {
        "id": 12345,
        "category": {
            "id": 1,
            "name": "Dogs"
        },
        "name": "Buddy",
        "photoUrls": ["https://example.com/dog.jpg"],
        "tags": [
            {
                "id": 0,
                "name": "friendly"
            }
        ],
        "status": "available"
    }

@when('I send POST request to add a new pet')
def step_impl(context):
    context.response = context.pet_api.add_new_pet(context.pet_data)

@when('I send GET request to find pets by status "{status}"')
def step_impl(context, status):
    context.pet_api = PetApi()
    context.response = context.pet_api.find_pets_by_status(status)
    context.expected_status = status

@then('the response status code should be {status_code:d}')
def step_impl(context, status_code):
    assert_that(context.response.status_code).is_equal_to(status_code)

@then('the response should contain the correct pet details')
def step_impl(context):
    response_data = context.response.json()
    assert_that(response_data["name"]).is_equal_to(context.pet_data["name"])
    assert_that(response_data["status"]).is_equal_to(context.pet_data["status"])
    assert_that(response_data["category"]["name"]).is_equal_to(context.pet_data["category"]["name"])

@then('all pets in the response should have status "{status}"')
def step_impl(context, status):
    response_data = context.response.json()
    assert_that(response_data).is_not_empty()
    for pet in response_data:
        assert_that(pet["status"]).is_equal_to(status)
