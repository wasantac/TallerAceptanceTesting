# language: en

Feature: Search games by Categories

  @gamesByCategories
  Scenario: Filter games that contain the ratings ["T", "E"]
      Given a set of games
     | NAME                       | RELEASE DATE | DEVELOPER            | RATE   |
     | The Witcher 3: Wild Hunt   | 2015         | CD Projekt           | M      |
     | Splatoon                   | 2016         | Nintendo             | T      |
     | Super Smash Bros. Ultimate | 2018         | Bandai Namco Studios | E      |
     | The Last of Us             | 2013         | Naughty Dog          | M      |
      Given the user selects one or more ratings: ["T", "E"]
      When choosing the search by ratings
      Then the name of all the games that correspond to these categories will be displayed
      | NAME                       |
      | Splatoon                   |
      | Super Smash Bros. Ultimate |

  @gamesByCategories
  Scenario: Filter games by rating without finding result
      Given a set of games
     | NAME                       | RELEASE DATE | DEVELOPER            | RATE   |
     | The Witcher 3: Wild Hunt   | 2015         | CD Projekt           | M      |
     | Splatoon                   | 2016         | Nintendo             | T      |
     | Super Smash Bros. Ultimate | 2018         | Bandai Namco Studios | E      |
     | The Last of Us             | 2013         | Naughty Dog          | M      |
      Given  the user selects one or more ratings: ["A"]
      When choosing the search by ratings
      Then the following message will be displayed: No game with the specified rating was found.