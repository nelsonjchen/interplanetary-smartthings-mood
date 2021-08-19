# Interplanetary-Gradient

*STATUS:* **tuned it to the place, that was it. it doesn't really work if you die though. oh well. that was interesting! Not really going to work actively on this anymore.**

This tool is a simple example tool to watch the log of a game of [Interplanetary: Enhanced Edition][steampage] and send commands to Samsung SmartThings to control the lights in the room.

## Example

When the game is in action phase state, the lights in the room will turn red.

When the game is not in action phase state, the lights in the room will turn blue.

## Usage

Fork and modify the code to your own needs. Stuff is hardcoded, stuff is not. You can do anything!

The code is kind of terrible though.

Poetry is the package manager used.

Tested on Python 3.9.6 on Windows.

## Prerequisites

If you want to use this tool, you need to have a [SmartThings account setup and a personal access token][samsung_pat] to pass in as an environment variable.

[steampage]: https://store.steampowered.com/app/650220/Interplanetary_Enhanced_Edition/
[samsung_pat]: https://smartthings.developer.samsung.com/docs/auth-and-permissions.html