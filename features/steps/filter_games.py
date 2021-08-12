from behave import *
from src.Game import *
from src.Catalogue import *

#Condiciones antes de empezar cualquier STEP
def before_scenario(context, scenario):
	context = {}

@given("a set of games")
def step_impl(context):
	game_list = []

	for row in context.table:

		elenco = []
		idiomas = []
		game = Game(row['NAME'], row['RELEASE DATE'], row['DEVELOPER'], row['RATE'])
		game_list.append(game)

	context.games = game_list

@given('the user enters the name: {name}')
def step_impl(context, name):
	context.name = name


@when("the user search games by {criteria}")
def step_impl(context, criteria):
	if(criteria == 'name'):
		result, message = get_game_name(context.games, context.name)
		print(result)
		context.result = result
		context.message = message


@then("{total} games will match")
def step_impl(context, total):
	assert len(context.result) == int(total)


@then("the names of these games are")
def step_impl(context):
	expected_games = True
	result_games = []
	for row in context.table:
		result_games.append(row['NAME'])
	for game in context.result:
		if game.name not in result_games:
			print("No game " + game.name)
			expected_games = False
	assert expected_games is True

@then("the following message is displayed: {message}")
def step_impl(context, message):
	print(message)
	print(context.message)
	assert context.message == message

################ Ratings ##################
@then("the name of all the games that correspond to these categories will be displayed")
def step_impl(context):
	expected_games = True
	result_games = []
	for row in context.table:
		result_games.append(row['NAME'])
	for game in context.result:
		if game.name not in result_games:
			print("No game " + game.name)
			expected_games = False
	assert expected_games is True

@given('the user selects one or more ratings: {ratingList}')
def step_impl(context, ratingList):
		context.ratingList = ratingList
		print(ratingList)
		print(context)

@when("choosing the search by {criteria}")
def step_impl(context, criteria):
	if (criteria == 'ratings'):
		result, message, error = get_game_rating(context.games, context.ratingList)
		context.result = result
		context.message = message


@then("the following message will be displayed: {message}")
def step_impl(context, message):
	print(message)
	print(context.message)
	assert context.message == message

################## Manufacturer ######################3

@then("the name of all the games that have been developed by said study will be displayed.")
def step_impl(context):
	expected_games = True
	result_games = []
	for row in context.table:
		result_games.append(row['NAME'])
	for game in context.result:
		if game.name not in result_games:
			print("No game " + game.name)
			expected_games = False
	assert expected_games is True

@given('the user enters a study: {study}')
def step_impl(context, study):
		context.study = study
		print(study)
		print(context)

@when("they select the search by {criteria}")
def step_impl(context, criteria):
	if (criteria == 'study'):
		result, message = get_game_developer(context.games, context.study)
		context.result = result
		context.message = message

########################## Test 2 ##########################

@given("the user enters a manufacturer: {manufacturer}")
def step_impl(context, manufacturer):
    context.manufacturer = manufacturer
    print(manufacturer)
    print(context)

@when("he selects the search by {criteria} option")
def step_impl(context, criteria):
    if criteria=="study":
        result, message = get_game_developer(context.games, context.manufacturer)
        context.result = result
        context.message = message

@then("{total} games will match")
def step_impl(context, total):
	assert len(context.result) == int(total)

@then("the following message is displayed: {message}")
def step_impl(context, message):
    print(message)
    print(context.message)
    assert context.message==message
