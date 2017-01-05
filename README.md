# GitHub Highlighter
GitHub Highlighter is a fork of GitHub Dark that introduces syntax highlighting themes for code without disrupting the overall GitHub color scheme.

## Installing

* If using Stylish:
  * Get the Stylish addon for [Firefox](https://addons.mozilla.org/en-US/firefox/addon/2108/), [Chrome](https://chrome.google.com/extensions/detail/fjnbnpbmkenffdnngjfgmeleoegfcffe), [Opera](https://addons.opera.com/en/extensions/details/stylish/), [Safari](http://sobolev.us/stylish/) and [Firefox Mobile](https://addons.mozilla.org/en-US/firefox/addon/2108/).
  * Then install this style using:
    * Install it [manually](https://raw.githubusercontent.com/dnut/GitHub-Highlighter/master/github-dark.css) into the editor.
      * Use the [grunt build process](https://github.com/StylishThemes/GitHub-Dark/wiki/Build) to customize your GitHub Dark theme.
      * Please refer to the [installation documentation](https://github.com/StylishThemes/GitHub-Dark/wiki/Install) for more details.

## Updating

If a recent change by GitHub broke the style, chances are that we already fixed it. Make sure to reinstall from [GitHub](https://raw.githubusercontent.com/StylishThemes/GitHub-Dark/master/github-dark.css) before opening an issue. Note that only Stylish for Firefox performs automatic style updates.

## Available Syntax Highlighting Themes ([Demo](https://stylishthemes.github.io/GitHub-Dark/))

| Theme                      | GitHub | CodeMirror | Jupyter  |
|----------------------------|:------:|:----------:|:--------:|
| Ambiance                   |   *    |     *      |          |
| Chaos                      |   *    |            |          |
| Clouds Midnight            |   *    |            |          |
| Cobalt                     |   *    |     *      |          |
| GitHub Dark                |   *    |            |     *    |
| Idle Fingers               |   *    |            |     *    |
| Kr Theme                   |   *    |            |          |
| Merbivore                  |   *    |            |          |
| Merbivore Soft             |   *    |            |          |
| Mono Industrial            |   *    |            |          |
| Mono Industrial Clear      |   *    |            |          |
| Monokai                    |   *    |     *      |     *    |
| Monokai Spacegray Eighties |   *    |     *      |     *    |
| Obsidian                   |   *    |            |     *    |
| Pastel on Dark             |   *    |     *      |     *    |
| Solarized Dark             |   *    |     *      |     *    |
| Terminal                   |   *    |            |          |
| Tomorrow Night             |   *    |            |          |
| Tomorrow Night Blue        |   *    |            |     *    |
| Tomorrow Night Bright      |   *    |     *      |     *    |
| Tomorrow Night Eigthies    |   *    |     *      |     *    |
| Twilight                   |   *    |     *      |     *    |
| Vibrant Ink                |   *    |     *      |          |

* Partial support for [Codemirror](https://codemirror.net/demo/theme.html) and [Jupyter notebook syntax highlighting](https://github.com/sujitpal/statlearning-notebooks/blob/master/src/chapter2.ipynb) themes.
* If the selected theme does not have an associated CodeMirror or Jupyter theme, it will fall back to a Twilight theme.
* Please provide a pull request if you have or want to create a missing theme.

## Notes

* If you're using a custom domain for GitHub Enterprise, be sure to include it though a `@-moz-document` rule (Firefox) or add it to the `Applies to` section in (Chrome).
* If you want GitHub commit messages to use a monospaced font, and have a background color indicating the width limits, check out [GitHub Commit Limit](https://github.com/StylishThemes/GitHub-Commit-Limit).

## Contributions

If you would like to contribute to this repository, please...

1. Fork
2. Make changes (please read the [contribution guidelines](./.github/CONTRIBUTING.md) and abide by them)
3. Create a pull request!

Thanks to all that have [contributed](./AUTHORS) so far!