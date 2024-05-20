# Lepus Videogame Info XML File Specification

## About

Lepus shall use regularly formatted XML files to encode metadata about a game over which it holds perview.  
  
This document will detail the formatting to be used within the XML files.

## What's in a Videogame?

Just as this section's title ponders about, it is important to know specifically what data needs to be saved about the game in question.

To start, let's assume that all of the following statements are true:

 - All videogames have a title
 - All (published) videogames have a release date
 - All videogames have a genre
 - All (published) videogames have a publisher
    - (one who self-publishes is still a publisher!)
 - All videogames have a target platform
 - All videogames have a developer

 So, given the info above, we can draft up some simple XML to represent it, like so:

 ```
<game>
    <title>Example: The Game</title>
    <released>2024</released>
    <genre>RPG</genre>
    <developer>Anne Exampleman</developer>
    <publisher>Exemplar Studios</publisher>
    <platform>Windows</platform>
</game>
 ```

Unfortunately, the above XML reveals some problems:
 - Some indie titles have differing release dates for Patrons vs. the Public
 - Videogames can often being described w/ **multiple** different genres
 - Videogames can (& often do) target **multiple** different platforms
    - furthermore, I think it'd more important to display info about the version(s) owned by the user over any other.
 - Videogames, unlike most other mediums, are frequently updated, & thus have multiple versions.