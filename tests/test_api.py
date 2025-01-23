import pytest
import allure

headers_for_unauthorized_users = {"Authorization": "false"}
positive_data_for_authorize = [{'name': 'Aladin'}, {'name': 'Patric'}, {'name': 'Alice'}]
negative_data_for_authorize = [{'name': 000}, {'name': {123: 'str'}}, {'name': ['robin', 'jack']}]
positive_data_for_create_memes = [{"info": {"colors": ["brown", "grey", "yellow"], "objects": ["picture", "text"]},
                                   "tags": ["fun", "little girl", "fire", "spider"],
                                   "text": "There was a spider. It`s gone now.",
                                   "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn"
                                          ":ANd9GcS20iBpZlg_uZLSnBh8tVZFJvh-JPlYOZe1Hw&s"},
                                  {"info": {"colors": ["green", "black"], "objects": ["picture", "text"]},
                                   "tags": ["fun", "Frog", "Pepe", "Cry"],
                                   "text": "When friends don`t now Pepe",
                                   "url": "https://i.imgflip.com/1yytwo.jpg"}
                                  ]

data_for_change_meme = {"info": {"colors": ["black", "white"], "objects": ["picture", "text", "human"]},
                        "tags": ["really situation", "Nicolas"],
                        "text": "You don`t say?",
                        "url": "https://preview.redd.it/favorite-celebrity-memes-edits-that-never-fail-to-make-you-v0"
                               "-72obmtpl7prb1.jpeg?width=894&format=pjpg&auto=webp&s"
                               "=88f9ae5932382e50c8545ef12704fa02db904209"}

data_for_unused_method = {"info": {"colors": ["brown", "gold", "black"], "objects": ["picture", "text"]},
                          "tags": ["fun", "Leonardo DiCaprio", "Django Unchained"],
                          "text": "When people ask me. Whats your favorite meme?",
                          "url": "https://static1.srcdn.com/wordpress/wp-content/uploads/2020/08/Leonardo-DiCaprio"
                                 "-Django-Unchained-drinking-meme.jpg"
                          }

negative_data_for_change_meme = [{"info": {"colors": ["brown", "gold", "black"], "objects": ["picture", "text"]},
                                  "tags": ["fun", "Leonardo DiCaprio", "Django Unchained"],
                                  "text": ['When people ask me. Whats your favorite meme?'],
                                  "url": "https://static1.srcdn.com/wordpress/wp-content/uploads/2020/08/Leonardo"
                                         "-DiCaprio-Django-Unchained-drinking-meme.jpg"},
                                 {"info": {"colors": ["brown", "gold", "black"], "objects": ["picture", "text"]},
                                  "tags": ["fun", "Leonardo DiCaprio", "Django Unchained"],
                                  "text": 'When people ask me. Whats your favorite meme?',
                                  "url": 1243124
                                  },
                                 {"info": {"colors": ["brown", "gold", "black"], "objects": ["picture", "text"]},
                                  "tags": {"fun", "Leonardo DiCaprio", "Django Unchained"},
                                  "text": 'When people ask me. Whats your favorite meme?',
                                  "url": "https://static1.srcdn.com/wordpress/wp-content/uploads/2020/08/Leonardo"
                                         "-DiCaprio-Django-Unchained-drinking-meme.jpg"
                                  },
                                 {"info": [{"colors": ["brown", "gold", "black"], "objects": ["picture", "text"]}],
                                  "tags": ["fun", "Leonardo DiCaprio", "Django Unchained"],
                                  "text": 'When people ask me. Whats your favorite meme?',
                                  "url": "https://static1.srcdn.com/wordpress/wp-content/uploads/2020/08/Leonardo"
                                         "-DiCaprio-Django-Unchained-drinking-meme.jpg"
                                  }
                                 ]


@pytest.mark.smoke
@allure.feature('Meme')
@allure.story('Manipulate with meme')
@allure.title('Authorize on the platform')
@pytest.mark.parametrize('data', positive_data_for_authorize)
def test_make_authorization(create_authorize_endpoint, data):
    create_authorize_endpoint.make_authorization(payload=data)
    create_authorize_endpoint.check_that_status_is_200()


@pytest.mark.negative
@allure.feature('Meme')
@allure.story('Manipulate with meme')
@allure.title('Checking authorization with invalid values')
@pytest.mark.parametrize('negative_data', negative_data_for_authorize)
def test_negative_authorization(create_authorize_endpoint, negative_data):
    create_authorize_endpoint.make_authorization(payload=negative_data)
    create_authorize_endpoint.check_bad_request()


@pytest.mark.smoke
@allure.feature('Meme')
@allure.story('Manipulate with meme')
@allure.title('Getting all the memes')
def test_get_all_memes(create_get_endpoint):
    create_get_endpoint.show_all_memes()
    create_get_endpoint.check_that_status_is_200()


@pytest.mark.smoke
@allure.feature('Meme')
@allure.story('Manipulate with meme')
@allure.title('Getting one meme')
def test_get_one_meme(create_get_endpoint):
    create_get_endpoint.show_one_meme()
    create_get_endpoint.check_that_status_is_200()
    create_get_endpoint.check_that_text_is_correct("Only just begun the meme war has")


@pytest.mark.negative
@allure.feature('Meme')
@allure.story('Manipulate with meme')
@allure.title('Getting one meme by unauthorized user')
def test_get_one_meme_by_unauthorized_user(create_get_endpoint):
    create_get_endpoint.show_one_meme(headers=headers_for_unauthorized_users)
    create_get_endpoint.check_no_authorize_request()


@pytest.mark.negative
@allure.feature('Meme')
@allure.story('Manipulate with meme')
@allure.title('Getting all memes by unauthorized user')
def test_get_all_memes_by_unauthorized_user(create_get_endpoint):
    create_get_endpoint.show_all_memes(headers=headers_for_unauthorized_users)
    create_get_endpoint.check_no_authorize_request()


@pytest.mark.smoke
@allure.feature('Meme')
@allure.story('Manipulate with meme')
@allure.title('Checking token validity')
def test_is_alife_a_token(check_authorize_endpoint, getting_a_token):
    check_authorize_endpoint.token_is_alive(token=getting_a_token)
    check_authorize_endpoint.check_that_status_is_200()


@pytest.mark.smoke
@allure.feature('Meme')
@allure.story('Manipulate with meme')
@allure.step('Create new meme')
@pytest.mark.parametrize("data", positive_data_for_create_memes)
def test_create_new_meme(create_post_endpoint, data):
    create_post_endpoint.add_new_meme(payload=data)
    create_post_endpoint.check_that_status_is_200()


@pytest.mark.negative
@allure.feature('Meme')
@allure.story('Manipulate with meme')
@allure.title('Create new meme with negative data')
@pytest.mark.parametrize("negative_data", negative_data_for_change_meme)
def test_create_new_meme_with_negative_data(create_post_endpoint, negative_data):
    create_post_endpoint.add_new_meme(payload=negative_data)
    create_post_endpoint.check_bad_request()


@pytest.mark.smoke
@allure.feature('Meme')
@allure.story('Manipulate with meme')
@allure.title('Complete modification of object data')
def test_change_meme_data(create_put_endpoint, getting_meme_id, getting_a_token):
    data_for_change_meme["id"] = getting_meme_id
    create_put_endpoint.change_all_data_meme(meme_id=getting_meme_id,
                                             payload=data_for_change_meme
                                             )
    create_put_endpoint.check_that_status_is_200()


@pytest.mark.smoke
@allure.feature('Meme')
@allure.story('Manipulate with meme')
@allure.title('Delete meme')
def test_delete_meme(create_delete_endpoint, getting_meme_id):
    create_delete_endpoint.delete_meme(meme_id=getting_meme_id)
    create_delete_endpoint.check_that_status_is_200()


@pytest.mark.smoke
@allure.feature('Meme')
@allure.story('Manipulate with meme')
@allure.title('Delete meme by unauthorized user')
def test_delete_meme_by_unauthorized_user(create_delete_endpoint, getting_meme_id):
    create_delete_endpoint.delete_meme(meme_id=getting_meme_id, headers=headers_for_unauthorized_users)
    create_delete_endpoint.check_no_authorize_request()


@pytest.mark.negative
@allure.feature('Meme')
@allure.story('Manipulate with meme')
@allure.title('Partial modification of meme data')
def test_change_meme_data_by_unused_method(create_patch_endpoint, getting_meme_id):
    data_for_unused_method['id'] = getting_meme_id
    create_patch_endpoint.change_meme_data(meme_id=getting_meme_id,
                                           payload=data_for_unused_method
                                           )
    create_patch_endpoint.check_method_not_allowed()
