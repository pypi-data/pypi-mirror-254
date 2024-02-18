# Readme
Dramatist is a project for parsing plays from [DraCor](https://dracor.org/) into a data structure which allows to access
the text of the play "character" perfect, that is, character start and end positions for various parts, for example, act
or scenes, can be retrieved. This also allows for functionality like getting the act and scene number for a character
position.

## Installation
~~~
pip install Dramatist
~~~

## Usage
There are to ways to use Dramatist. The recommended way is to use Dramatist in code in other projects.
The second option, from the command line, is only for illustration purposes, and rather limited.

### In code
~~~
from dramatist.Dramatist import Dramatist

dramatist = Dramatist()

# load from local file
drama = dramatist.from_file(path_to_play_xml_file)

# load from DraCor API using corpus name and play name
drama = await dramatist.from_api_by_name('ger', 'goethe-iphigenie-auf-tauris')

# load from DraCor API using play id
drama = await dramatist.from_api_by_id(play_id)

# get the text of the drama
drama_test = drama.get_text()

# get the start and end position of a scene
scene_start, scene_end = drama.get_range_for_scene(act_nr, scene_nr)
~~~

### Command line
The command line interface is very limited. Dramatist is meant to be used in code in other projects.
If the `--output-folder-path` the resulting the data structure is saved to a json file. Otherwise the drama text is
printed to the console.

#### Local file
~~~
dramatist --drama-path path-to-xml-drama-file
~~~

#### DraCor API with corpus name and play name
~~~
dramatist --corpus-name ger --play-name goethe-iphigenie-auf-tauris
~~~

#### DraCor API with play id
~~~
dramatist --play-id ger000001
~~~

## Functionality

- `get_text()`
  - Get the text of the drama.
- `get_text_with_markup()`
  - Get the text of the drama a list of markups.
- `get_text_for_scene_in_blocks(act_nr, scene_nr)`
  - TBD
- `get_text_for_scene_by_character(act_nr, scene_nr)`
  - TBD
- `get_scene_act_for_position(char_pos)`
  - Return a tuple of act and scene number for the given position.
- `get_range_for_scene(act_nr, scene_nr)`
  - Return a tuple of character start and end position for the given act and scene number.
