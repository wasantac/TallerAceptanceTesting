# language: en

Feature: Search games by Manufacturer

  @gamesByManufacturer
  Scenario: Filter games that contain the manufacturer
      Given a set of games
     | NAME                       | RELEASE DATE | DEVELOPER            | RATE   |
     | The Witcher 3: Wild Hunt   | 2015         | CD Projekt           | M      |
     | Splatoon                   | 2016         | Nintendo             | T      |
     | Super Smash Bros. Ultimate | 2018         | Bandai Namco Studios | E      |
     | The Last of Us             | 2013         | Naughty Dog          | M      |
      Given the user enters a study: 'Nintendo'
      When they select the search by study
      Then the name of all the games that have been developed by said study will be displayed.
      | NAME                       |
      | Splatoon                   |

  @gamesByManufacturer
  Scenario: Filter games by manufacturer
      Given a set of games
     | NAME                       | RELEASE DATE | DEVELOPER            | RATE   |
     | The Witcher 3: Wild Hunt   | 2015         | CD Projekt           | M      |
     | Splatoon                   | 2016         | Nintendo             | T      |
     | Super Smash Bros. Ultimate | 2018         | Bandai Namco Studios | E      |
     | The Last of Us             | 2013         | Naughty Dog          | M      |
		  Given the user enters a manufacturer: Sony
      When he selects the search by study option
			Then 0 games will match
      And the following message is displayed: No game developed by Sony found
