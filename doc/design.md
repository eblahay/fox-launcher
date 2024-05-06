# Project Lepus Design Document

## Purpose

Project Lepus is an application meant to allow to quickly & easily integrate new games/new *versions* of games into my videogame library in an organized fashion.

Additionally, I believe that given time & consistent development, this project will grow to become a general videogame launcher.

## Description

Project Lepus will be a CLI app, which will be called using the command: `lepus`.
The user will pass Lepus an archive file or directory, along with information such as "game ID", "version number", etc.
Lepus will then use this information, along with information stored in a user-specific config file to put this version of said game in the right location.

### Directory Structure

The basic directory structure for a Lepus-maintained game collection should look something like this:
```
GAME_COLLECTION_BASE_DIR/
    GAME_DIR/
        VERSION_DIR/
        ANOTHER_VERSION_DIR/
        VERSION_ARCHIVE/
        ANOTHER_VERSION_ARCHIVE_ETC/
        SYMBOLIC_LINK_TO_MOST_RECENT_VERSION_NAMED_'latest'
```

### Interface

`lepus <-f FILE> GAME_ID GAME_VERSION`

 - `FILE`
    - the file/directory which is being added to the collection
 - `GAME_ID`
    - the ID of the game in the library to which `FILE` is to be added  
        e.g. `holocure`  
        ID should be fast & simple to type; ideally lowercase, no spaces  
        IDs are *user-defined*!
 - `GAME_VERSION`
    - the semantic version of the game in question;  
        e.g. `0.9`, `1.17.2`, `9/19/2023`  
        (the last one is not a mistake; apparently that's how HoloCure versions itself!)
    - version should NOT include the game's name nor ID

### Configuration

This is where game IDs will be defined!

#### Things that Need to be defined in Configuration
 - Game Collection Base Dir(s)
 - Game IDs
 - Game Metadata
    - Title
 - Game Directory