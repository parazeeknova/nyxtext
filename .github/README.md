<h3 align="center">
	<img src="assets/logo/logo.png" width="300" alt="Logo"/><br/>
    <img src="assets/misc/transparent.png" height="30" width="0px"/>
    Nyxtext
	<img src="assets/misc/transparent.png" height="30" width="0px"/>
</h3>

<h6 align="center">
  <a href="https://github.com/parazeeknova/nyxtext#note-">Info</a>
  ·
  <a href="https://github.com//parazeeknova/nyxtext#-installing-nyxtext">Install</a>
  ·
  <a href="https://github.com//parazeeknova/nyxtext#-early-editor-screenshots">Showcase</a>
  ·
  <a href="https://github.com/parazeeknova/nyxtext#-contributing">Contribution</a>
  ·
  <a href="https://github.com/parazeeknova/nyxtext#-support">Support</a>

</h6>

<p align="center">
  <img src="assets/misc/macchiato.png" width="400" />
</p>

&nbsp;

<p align="center">
	<a href="https://github.com/parazeeknova/nyxtext/stargazers">
		<img alt="Stargazers" src="https://img.shields.io/github/stars/parazeeknova/nyxtext?style=for-the-badge&logo=starship&color=C9CBFF&logoColor=D9E0EE&labelColor=302D41"></a>
	<a href="https://github.com/parazeeknova/nyxtext/issues">
		<img alt="Issues" src="https://img.shields.io/github/issues/parazeeknova/nyxtext?style=for-the-badge&logo=gitbook&color=B5E8E0&logoColor=D9E0EE&labelColor=302D41"></a>
    <a href="https://github.com/parazeeknova/nyxtext/releases/latest">
    <img alt="Maintained" src="https://img.shields.io/badge/Maintained%3F-yes-green.svg?style=for-the-badge&logo=github&color=F2CDCD&logoColor=D9E0EE&labelColor=302D41"/></a>
		<img alt="Releases" src="https://img.shields.io/github/release/parazeeknova/nyxtext.svg?style=for-the-badge&logo=github&color=F2CDCD&logoColor=D9E0EE&labelColor=302D41"/></a>
</p>

<div align="center">

![Tkinter](https://img.shields.io/badge/Tkinter-GUI%20Library-D9E0EE?style=for-the-badge&logo=tkinter) 
![CustomTkinter](https://img.shields.io/badge/CustomTkinter-GUI%20Library-D9E0EE?style=for-the-badge)
</div>

&nbsp;

<p align="center">
<b>Nyxtext</b> is a text editor built using Python, with the added functionality of Custom Tkinter. It showcases the elegant <b>Catppuccin color scheme and follows glassmorphic design</b>, providing a visually pleasing experience. This project follows a modular approach, with each element of the text editor organized into separate files for improved clarity and maintainability. NyxText is not only build to be a text editor, but also a <b>AI-powered desktop application</b> that caters to the needs of creatives, developers, and students alike.
</p> 

<p align="center">
  <a href="https://github.com/parazeeknova/nyxtext">
    <picture>
      <source srcset="assets/social/macchiato_github.svg" width="64" height="64" alt="Github Logo" media="(prefers-color-scheme: dark)"/>
      <source srcset="assets/social/latte_github.svg" width="64" height="64" alt="Github Logo" media="(prefers-color-scheme: light), (prefers-color-scheme: no-preference)"/>
      <img src="assets/social/latte_github.svg" width="64" height="64" alt="Github Logo"/>
    </picture>
  </a>
  <img src="assets/misc/transparent.png" height="1" width="5"/>
  <a href="https://discord.gg/UwmqqXkV">
    <picture>
      <source srcset="assets/social/macchiato_discord.svg" width="64" height="64" alt="Discord Logo" media="(prefers-color-scheme: dark)"/>
      <source srcset="assets/social/latte_discord.svg" width="64" height="64" alt="Discord Logo" media="(prefers-color-scheme: light), (prefers-color-scheme: no-preference)"/>
      <img src="assets/social/latte_discord.svg" width="64" height="64" alt="Discord Logo"/>
    </picture>
  </a>
  <img src="assets/misc/transparent.png" height="1" width="5"/>
  <a href="https://twitter.com/hashcodes_">
    <picture>
      <source srcset="assets/social/macchiato_twitter.svg" width="64" height="64" alt="Twitter Logo" media="(prefers-color-scheme: dark)"/>
      <source srcset="assets/social/latte_twitter.svg" width="64" height="64" alt="Twitter Logo" media="(prefers-color-scheme: light), (prefers-color-scheme: no-preference)"/>
      <img src="assets/social/latte_twitter.svg" width="64" height="64" alt="Twitter Logo"/>
    </picture>
  </a>
  <img src="assets/misc/transparent.png" height="1" width="5"/>
  <a href="https://www.reddit.com/user/parazeeknova">
    <picture>
      <source srcset="assets/social/macchiato_reddit.svg" width="64" height="64" alt="Reddit Logo" media="(prefers-color-scheme: dark)"/>
      <source srcset="assets/social/latte_reddit.svg" width="64" height="64" alt="Reddit Logo" media="(prefers-color-scheme: light), (prefers-color-scheme: no-preference)"/>
      <img src="assets/social/latte_reddit.svg" width="64" height="64" alt="Reddit Logo"/>
    </picture>
  </a>
</p>

---

> [!IMPORTANT]
> Because the application is not signed by Microsoft, Windows Defender blocks it; add an exclusion in Defender to run the application. Its a false positive, the application is safe to use. or build it yourself from the source code.

> [!NOTE]
> Nyxtext is a work in progress. We appreciate any contributions, understanding that the project may have bugs, instability, and limited features during the time of active development. Please check back or join our Discord server to see our progress! 

### ✨ Installing Nyxtext

> [!TIP]
> Use Nerd Font to avoid any broken symbols : [JetbrainsMono Nerd Font](https://www.nerdfonts.com/font-downloads) 

<details>

<summary>Debian-based Linux distributions (e.g. Ubuntu, Mint)</summary>

**Open a terminal and run these commands:**

```bash
git clone --depth 1 https://github.com/parazeeknova/nyxtext.git
sudo apt update
sudo apt install python3 python3-pip
python3 -m venv nyxtext
source nyxtext/bin/activate
pip install -r requirements.txt
python editor/scripts/main.py
```
</details>

<details>
<summary>Arch Linux</summary>

**To install NyxText on Arch Linux, you can follow these steps:**

```bash
sudo pacman -Sy python tk
git clone --depth 1 https://github.com/parazeeknova/nyxtext.git
cd nyxtext
python -m venv nyxtext
source nyxtext/bin/activate
pip install -r requirements.txt
python editor/scripts/main.py
```

</details>

<details>
<summary>MacOS</summary>

I don't have a Mac. If you have a Mac, you can help me a lot by installing
Nyxtext and letting me know how well it works.

</details>

<details>
<summary>Windows</summary>

Download Nyxtext from [the releases page](https://github.com/parazeeknova/nyxtext/releases) and extract it. Then run through `Nyxtext.exe`.

</details>

### 🧠 Design Philosophy

- **Simplicity**: Keep the user interface clean and intuitive. Avoid cluttering the interface with unnecessary features or options. Focus on providing essential functionality in an easy-to-use manner.
- **Customizability**: Provide users with options to customize the editor to suit their preferences.
- **Modularity**: Design the codebase to be modular and extensible.
- **Maintainability**: Keep the codebase maintainable and readable.
- **Community Engagement**: Foster a vibrant and inclusive community around the editor. Encourage users to provide feedback, report bugs, and contribute code.
- **Feature Rich**: Have all the basic features for a text editor

&nbsp;

### 📸 Early Editor Screenshots

| Homescreen (as of α-v0.1.5 ) | Terminal (as of α-v0.1.5 ) | Gemini (as of α-v0.1.5 ) | Exit (as of α-v0.1.5 ) |
|--------------------------------------|--------------------------------------------|---------------------------------|---------------------------------|
| ![Homescreen](assets/screenshots/Homescreen.png) | ![Terminal](assets/screenshots/Terminal.png) | ![Gemini](assets/screenshots/Gemini.png) | ![Exit](assets/screenshots/Exit.png) |
| Codespace (as of α-v0.1.5 ) | Default Dark Windowed (as of α-v0.1.5 ) | Default Light Windowed (as of α-v0.1.5 ) | Workspace (as of α-v0.1.5 ) |
| ![Codespace](assets/screenshots/Codespace.png) | ![Dark mode](assets/screenshots/Default_Dark.png) | ![Light mode](assets/screenshots/Default_Light_mode.png) | ![Workspace](assets/screenshots/Workspace.png) |

&nbsp;

### 🎨 Palette

**Catppuccin** consists of 4 beautiful pastel color palettes. \
Thats not it it also has some other custom made themes like **lumber** and **H2O**. \
The number of themes is not definite, we will be adding more in the future, Also you can make your **own**.
<p align="center">
<img src="assets/misc/demo.png" alt="catppuccin infrastructure"/>
<h>Image referenced from Catppuccin (4 color palettes 🎨)</h> 
</p>

&nbsp;

### ✨Features :
- Edit Text files ~ duh.
- **Workspace** - Work on multiple text file simultaneously.
- **Syntax highlighting** - For the code space area.
- Catpuccin Color Palette themes(4) + 4 Custom made themes and counting on..
- **Dark / Light** mode.
- **Basic functions** (new,open,save,cut,copy, etc.) check **menu bar** for more..
- **FileTree** View which shows all your project's files & folders.
- **System scaling** support.
- **Responsive** design - 3 modes (windowed, middleman, fullscreen).
- **AI** assistence, shortcuts to Gemini, ChatGPT, BlackboxAI... 
- **Integrated Terminal** Supports all basic commands, highly customizable, supports multiple tabs to run simultaneously...
- **Integrated Gemini**: Includes a powerful search bar powered by the Gemini API for easy access to code and content.
- **Immersive Mode** Fullscreen mode for distraction-free writing. (hides titlebar)
- **Accent** Picks accent color for the editor (border, title) from you windows theme (windows)
- **Glassmorphic** design for the editor (windows)

***More Soon...***

&nbsp;

### 💡Future Plans : 
- [x] ~~Complete rebase to custom_tkinter~~ - Done 28/02/2024 ✅
- [x] ~~Integrated Gemini AI~~ - Done 27/04/2024 ✅
- [x] ~~Open Files~~ - Done 29/7/2024 ✅
- [ ] Auto completion, Grammer check
- [x] ~~Filetree viewer~~ - Done 02/03/2024 ✅
- [ ] Spell Check
- [x] ~~Syntax Highlighter~~ - Done 09/03/2024  ✅ ~ Used [Chlorophyll](https://github.com/rdbende/chlorophyll)
- [ ] Search & replace 
- [ ] Split file viewer, comparasion window
- [ ] Focus window
- [ ] Undo / Redo
- [ ] Working Settings page
- [x] ~~Terminal Support~~ - Done ✅ ~ Intergated [TkTerm](https://github.com/dhanoosu/TkTerm)
- [ ] Text Formatting - (Bold, Underline, Bulletpoints)
- [x] ~~Glassmorphic design for the editor~~ - Done 30/07/2024 ✅ ~ [pywinstyles](https://github.com/Akascape)
- [ ] Basic file Encryption / Decryption
- [ ] Hyperlinks, Markdown support
- [ ] Auto completion when pressing Tab for Codespace
- [ ] Git support
- [ ] Running files in a separate terminal or command prompt window
- [ ] Automatic indenting and trailing whitespace stripping when Enter is pressed
- [ ] Line length marker
- [ ] Code folding
- [ ] Multiple files can be opened at the same time like tabs in a web browser
- [ ] The tabs can be dragged out of the window to open a new window

&nbsp;

---

### 🐜 Bugs : 
- [x] ~~It's not responsive as the project is still in early development.~~ - Done 08/03/2024 ✅
- [x] ~~The editor only works in the full screen at the moment.~~ - Done 08/03/2024  ✅ - Now has 3 modes
- [ ] Filetree cannot open files
- [ ] There is no dynamic heading.
- [ ] Search bar does not work.

## ❓ FAQs:

### What's new in the latest NyxText release?

See [Releases](https://github.com/parazeeknova/nyxtext/releases).

<!-- ### Does NyxText support programming language X?
You will likely get syntax highlighting without any configuring
and autocompletions with a few lines of configuration file editing. -->

### Help! NyxtText doesn't work.

Install all the python pip packages for alpha stage.
If it still doesn't work, [let me know by creating an issue on
GitHub](http://github.com/parazeeknova/nyxtext/issues/new).

### Is NyxText written in NyxText?

Not at the moment. We are writing the very first version in `Neovim`, but will use it when we are done with basic features.

### Why is it named NyxText?

1. **Mythological Inspiration:** `NyxText` draws upon the Greek goddess `Nyx`, associated with night, creation, and beginnings. This resonates with writers and programmers who often find inspiration during the quiet hours. The name subtly reflects this theme through its potential use of darker design elements.

2. **Euphony and Distinction:** `NyxText` possesses a pleasant sound with `Nyx` adding a touch of mystique. This name stands out from common text editors, making it both memorable and unique.

3. **Symbolic Alignment:**  `Nyx` can also symbolize the blank canvas or the void before creation. This perfectly aligns with the core function of a text editor - providing a blank slate for writers and programmers to bring their ideas to life.

### I want an editor that does X, but X is not in the feature list above. Does NyxText do X?
You can run NyxText and find out,
or [create an issue on GitHub](https://github.com/parazeeknova/nyxtext/issues/new) and ask.
If you manage to make us excited about X, We might implement it.

### Why did you create a new editor?
Because I can.

### Why did you create a new editor in tkinter or X?
Because I can.

### Why not use editor X?
Because Nyxtext is better.

---

### 👐 Contributing

> [!NOTE]<br>
> Thank you for considering contributing to Nyxtext! We welcome contributions from everyone, whether you're fixing a bug, adding a feature, or improving documentation.

See [CONTRIBUTING.md](../docs/CONTRIBUTING.md)

&nbsp;

### 📜 License

NyxText is released under the MIT license:
For more convoluted language, see the [LICENSE](https://github.com/parazeeknova/nyxtext/blob/main/LICENSE).

&nbsp;

### 💖 Gratitude

Thanks for the initial development of the project, contributing this project :

- [Noviciuss](https://github.com/noviciusss) for `editor/.old/menubar` - depreciated
- [Castimonia07](https://github.com/castimonia07) `Catppuccin platte` - incomplete 

&nbsp;

<p align="center"><img src="assets/misc/catppuccin_cat.svg" /></p>
<div align="center">

![Dev](http://ForTheBadge.com/images/badges/built-by-developers.svg)
![Python](http://ForTheBadge.com/images/badges/made-with-python.svg)
![Love](http://ForTheBadge.com/images/badges/built-with-love.svg)
</div>
<p align="center">Copyright &copy; 2024-present <a href="https://github.com/parazeeknova/nyxtext" target="_blank">NyxText</a>
<p align="center"><a href="https://github.com/parazeeknova/nyxtext/blob/main/LICENSE"><img src="https://img.shields.io/static/v1.svg?style=for-the-badge&label=License&message=MIT&logoColor=d9e0ee&colorA=302d41&colorB=b7bdf8"/></a></p>
