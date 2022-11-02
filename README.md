## Spotify PlayList

A project where you can create a playlist that you love and add songs to your playlist in a just a click.

With this python script you can time travel to your desired date or season that matters most to you.
For example if you want to know the top songs at a specific date or maybe a memory you want to bring back, all you need is to `input the date` and you have all the favorite songs of that time in a playlist created for you by this script in your speotify account and you enjoy it.

Follow these steps to set up the python script with your spotify account.

### ⚒️ Only Language / Tool
 <table>
	 <tbody>
  		<tr>
   			<td align="Center" width="25%"> 
 				<a href="https://developer.mozilla.org/en-US/docs/Glossary/Reactjs" target="_blank" rel="noreferrer"><img src="https://cdn.svgporn.com/logos/python.svg" width="36" height="36" alt="Python" /></a>
    	<br>Python
    </td>
	  </tr>
	</tbody>
  </table>
	
<br>

## Demo


https://user-images.githubusercontent.com/81332784/199428965-1847cfcd-dfff-4ba3-890a-0d88d5e77ccf.mov



## 🧑 Follow these guide

 1. You will need to create a spotify account if you don't have one here [Spotify](https://open.spotify.com)
 2. Have python installed in your system if you don't have it already here [Python Download](https://www.python.org/downloads/)



<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />



## Fork this repository

Fork this repository by clicking on the fork button on the top of this page.
This will create a copy of this repository in your account.

## Clone the repository

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Now clone the forked repository to your machine. Go to your GitHub account, open the forked repository, click on the code button and then click the _copy to clipboard_ icon.

Open a terminal and run the following git command:

```bash
git clone "url you just copied"
```

where "url you just copied" (without the quotation marks) is the url to this repository (your fork of this project). See the previous steps to obtain the url.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

For example:

```bash
git clone https://github.com/Kellsonphilips/Working-with-SpotifyAPI.git
```

where `this-is-you` is your GitHub username. Here you're copying the contents of the Asakatsu-Website repository on GitHub to your computer.

Next* You can drag and drop the project directory to your favorite IDEs or code editor.

If you have VS Code set up then you can open the project from your terminal directly by running this command

```bash
cd Working-with-SpotifyAPI
code .
```
## Setting up your Spotify

Let's set up your spotify so the script can work 💪
1. Firstly
 * Visit [Spotify](https://open.spotify.com) and login into your account.
 * Visit [Spotify for Developers](https://developer.spotify.com/) navigate to the Dashboard
![Screenshot 2022-10-31 at 17 37 22](https://user-images.githubusercontent.com/81332784/199429172-028df73c-45bb-4e1a-9851-9c72f3105463.png)

 * Like the image above, login with your spotify account.
2. Secondly
  * Click on Create An App to create an app for what you are building
  * Give your App a name and the description
  * Example below 👇
![Screenshot 2022-10-31 at 17 46 30](https://user-images.githubusercontent.com/81332784/199429439-188c5450-3851-4673-85f5-98e002fe24d3.png)
3. Thirdly
  * Copy the CLIENT ID and the CLIENT SECRET
  * Using the `env_template` provided for you in this project 
  * Create a `.env file` , copy all in the `env_template` and paste it in your created `.env file` then paste your `CLIENT ID and CLIET SECRET` respectively in the rightful place in your `.env file`.
![Screenshot 2022-10-31 at 17 50 15](https://user-images.githubusercontent.com/81332784/199429913-6a9d1555-1770-433f-bb94-72cb79dfc086.png)
  * Click on the Edit Settings
4. Fourth
  ```bash
  http://localhost:8080/callback/
  ```
  * Copy the link above and past it in the Redirect URIs exactly like the image below 👇
![Screenshot 2022-10-31 at 17 53 12](https://user-images.githubusercontent.com/81332784/199430069-a3022c7d-8fae-45e8-a7a3-d67bf448a4fe.png)

  * And Save
We are done with the spotify developer App

To make your environmental variables recognized or read by the script.
Inside your working directory
We need to install all the modules needed for this script
  * Cpy each of these commands and run it to install the modules
```bash
pip3 install python-dotenv
```
```bash
pip3 install bs4
```
```bash
pip3 install requests
```
```bash
pip3 install spotipy
```


We are all set to test our script!!!
After all the above the steps are completed.
Run the `main.py` file

If everything is fine, you will be prompted to input the date you want to check the top 100 songs on that date.

Date format:
```bash
YYYY-MM-DD
```
Example below:
![Screenshot 2022-10-31 at 17 26 17](https://user-images.githubusercontent.com/81332784/199430202-a141a0b7-9861-4707-b6d8-eacc1224c626.png)


If a song is not found in Spotify , the name of the song will be logged in the console like above.
Check your Spotify and you will find your playlist created and top100 songs added in the playlist.
Like below:
![Screenshot 2022-10-31 at 17 28 54](https://user-images.githubusercontent.com/81332784/199430269-cc3620b7-4586-4f86-bd55-0b4a0ad9b995.png)


The songs are 99 because 1 song wasn't found in Spotify.

Also if you try same date without Renaming the previous playlist with same Date, you can't have multiple playlists with the same name and same songs.
You will be notified in console like below:
![Screenshot 2022-10-31 at 21 42 29](https://user-images.githubusercontent.com/81332784/199430356-b86cc6fb-b23f-497d-8104-765d0c7fc586.png)




## License

Working-with-SpotifyAPI is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Contributors

If you have anything to add to this script, you are welcome to do so because there are many features we can add to this simple code and make it even more great for everyone. Do make your contributions and send a PR to feature in the contibutore as below 💪

<a href = "https://github.com/Kellsonphilips/Working-with-SpotifyAPI/graphs/contributors">
  <img src = "https://contrib.rocks/image?repo=Kellsonphilips/Working-with-SpotifyAPI"/>
</a>


## 🙏🏽 Support

This project needs a star️ from you. Don't forget to leave a star✨
You can contact me through my social media accounts if you need any help. I would be very pleased to offer my help.
Thank you
