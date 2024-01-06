## Usage

`python safecast-radiacode.py <FILENAME> <APIKEY>`

`python safecast-radiacode.py "2024-01-02 03-04-05.rctrk" abcdef_ghijklmno`

Please note, the map (https://map.safecast.org) takes some time to update

## Safecast instructions

Register for safecast here: https://api.safecast.org/en-US/users/sign_up

Once logged in, click your email at the top right, then "Profile" to see your API key

## Radiacode app instructions

Ensure that in `Map Settings`, the export format is `.rctrk`

![map-settings](https://raw.githubusercontent.com/sinaptik/safecast-radiacode/master/images/map-settings.png)

Go to map track list

![show-tracks](https://raw.githubusercontent.com/sinaptik/safecast-radiacode/master/images/show-tracks.png)

Share tracks (via email, google drive, etc) to get the `.rctrk` file

![share-track](https://raw.githubusercontent.com/sinaptik/safecast-radiacode/master/images/share-track.png)

## Dev notes

Dose rate in `.rctrk` file are to be divided by 100 to get `usv` as required by the safecast API

Time in `.rctrk` file: `2022-06-25 10:46:23` local (PST) shows as `2022-06-25 17:46:23`. So timezone in this file is UTC+00:00
